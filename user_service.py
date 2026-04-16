# user_service.py
class User:
    def __init__(self, user_id: int, name: str, email: str, age: int):
        self.id = user_id
        self.name = name
        self.email = email
        self.age = age

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}')"

class UserService:
    def __init__(self):
        # Хранилище пользователей в памяти: ключ - id, значение - объект User
        self._users = {}

    def add_user(self, user: User) -> bool:
        """Добавляет пользователя. Возвращает True, если успешно."""
        if user.id in self._users:
            raise ValueError(f"User with id {user.id} already exists")
        if user.age < 0:
            raise ValueError("Age cannot be negative")
        self._users[user.id] = user
        return True

    def get_user(self, user_id: int) -> User:
        """Возвращает пользователя по ID. Если не найден, возвращает None."""
        return self._users.get(user_id)

    def delete_user(self, user_id: int) -> bool:
        """Удаляет пользователя. Возвращает True, если был удален, иначе False."""
        if user_id in self._users:
            del self._users[user_id]
            return True
        return False

    def get_all_users(self) -> list[User]:
        """Возвращает список всех пользователей."""
        return list(self._users.values())

    def get_adult_users(self) -> list[User]:
        """Возвращает список пользователей старше 18 лет."""
        return [user for user in self._users.values() if user.age >= 18]

    def update_user_email(self, user_id: int, new_email: str) -> bool:
        """Обновляет email пользователя. Возвращает True, если пользователь найден."""
        user = self._users.get(user_id)
        if user:
            # Простейшая проверка на валидность email (просто наличие '@')
            if '@' not in new_email:
                raise ValueError("Invalid email format")
            user.email = new_email
            return True
        return False