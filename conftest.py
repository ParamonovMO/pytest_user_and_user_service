import pytest
from user_service import User, UserService
import allure


@pytest.fixture
def user_service():
    user_service = UserService()
    return user_service


@pytest.fixture
def sample_user():
    sample_user = User(1, "Alice", "alice@example.com", 25)
    return sample_user