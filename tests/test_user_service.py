import pytest
from user_service import User
import allure

class TestUserService:

    @allure.title('Проверка добавления пользователя')
    def test_add_user(self, user_service, sample_user):
        assert user_service.add_user(sample_user) == True
        assert user_service.get_user(1) == sample_user

    @allure.title('Проверка ошибки при повторном добавления пользователя')
    def test_add_user_raise(self, user_service, sample_user):
        user_service.add_user(sample_user)
        with pytest.raises(ValueError):
            user_service.add_user(sample_user)

    @allure.title('Проверка ошибки при добавлении пользователя с отрицательным возрастом')
    def test_add_user_raise_age(self, user_service):
        with pytest.raises(ValueError):
            user_service.add_user(User(1, "Alice", "alice@example.com", -1))

    @allure.title('Проверка пустого класа UserService')
    def test_service_user_default_null(self, user_service):
        assert len(user_service._users) == 0

    @allure.title('Проверка добавления двух пользователей')
    def test_service_user_add_two_users(self, user_service, sample_user):
        user_service.add_user(sample_user)
        user_service.add_user(User(2, "Max", "alice@example.com", 15))
        assert len(user_service.get_all_users()) == 2

    @allure.title('Проверка удаления пользователя из UserService')
    def test_delete_user_in_user_service(self, user_service, sample_user):
        user_service.add_user(sample_user)
        assert user_service.delete_user(sample_user.id) == True
        assert user_service.get_user(sample_user.id) == None

    @allure.title('Проверка удаления несуществующего пользователя')
    def test_delete_unknown_user(self, user_service):
        assert user_service.delete_user(5) == False

    @allure.title('Проверка обновления email пользователя')
    def test_update_user_email(self, user_service, sample_user):
        user_service.add_user(sample_user)
        assert user_service.update_user_email(sample_user.id, 'paramonov.maxim@vk.com') == True

    @allure.title('Проверка ошибки обновления пользоваля с некорректным email')
    def test_update_user_email_raise(self, user_service, sample_user):
        user_service.add_user(sample_user)
        with pytest.raises(ValueError):
            user_service.update_user_email(sample_user.id, 'paramonov.maximvk.com') == False

    @allure.title('Проверка обновления email у несуществующего пользователя')
    def test_update_user_email_raise_unknown_user(self, user_service):
        user_service.update_user_email(10, 'paramonov.maximv@k.com') == False

    @allure.title('Проверка отображения списка с совершеннолетними пользователями')
    @pytest.mark.parametrize('id,name,email,age,result', [(1, "Alice", "alice@example.com", 25, True),
                                  (2, "Max", "alice@example.com", 20, True),
                                  (3, "Kira", "alice@example.com", 17, False),
                                  (4, "Ksenia", "alice@example.com", 33, True),
                                  (5, "Alice", "alice@example.com", 15, False),
                                  (6, "Alice", "alice@example.com", 1, False)
                                  ]
                                  )
    def test_user_is_adult(self, user_service, id, name, email, age, result):
        user_service.add_user(User(id, name, email, age))
        assert bool(user_service.get_adult_users()) == result


class TestUser:

    @allure.title('Проверка читаемого класса User')
    def test_repr(self, sample_user):
        assert repr(sample_user) == f"User(id={sample_user.id}, name='{sample_user.name}')"