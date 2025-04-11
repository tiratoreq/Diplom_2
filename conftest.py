import allure
import pytest
import requests
from handlers.user_handlers import UserHandlers


@pytest.fixture
@allure.step('Удаление пользователя')
def user_delete(access_token):
    yield UserHandlers.user_creation
    requests.delete('https://stellarburgers.nomoreparties.site/api/auth/user',
                    headers={'Authorization': access_token})