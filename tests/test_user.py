import pytest
import allure

from constants import Constants
from handlers.user_handlers import UserHandlers



class TestsUser:

    @allure.title('пользователя можно создать')
    def test_user_create(self):
        user = UserHandlers()
        response = user.user_creation()
        with allure.step(f"Проверка, что '{response.status_code}' равен '403'"):
            assert response.status_code == 403, f"Ответ сервера '{response.status_code}' не совпадает с ожидаемым '403'"


    @allure.title('создание пользователя, который уже зарегистрирован')
    def test_same_user_create(self):
        user = UserHandlers()
        response = user.same_user_creation()
        json_data = response.json()
        message = json_data.get("message")
        with allure.step(f"Проверка, что '{response.status_code}' равен '403'"):
            assert response.status_code == 403, f"Ответ сервера '{response.status_code}' не совпадает с ожидаемым '403'"
            assert message == Constants.UserExist

    @allure.title('пользователя можно создать')
    def test_user_create_without_field(self):
        user = UserHandlers()
        response = user.user_creation()
        json_data = response.json()
        message = json_data.get("message")
        with allure.step(f"Проверка, что '{response.status_code}' равен '403'"):
            assert response.status_code == 403, f"Ответ сервера '{response.status_code}' не совпадает с ожидаемым '403'"
            assert message == Constants.ReqFields

    @allure.title('логин пользователя')
    def test_user_login(self):
        user = UserHandlers()
        response = user.user_login()
        with allure.step(f"Проверка, что '{response.status_code}' равен '200'"):
            assert response.status_code == 200, f"Ответ сервера '{response.status_code}' не совпадает с ожидаемым '200'"

    @allure.title('логин пользователя с неверным паролем')
    def test_user_create_wrong_password(self):
        user = UserHandlers()
        response = user.user_login_wrong_password()
        json_data = response.json()
        message = json_data.get("message")
        with allure.step(f"Проверка, что '{response.status_code}' равен '401'"):
            assert response.status_code == 401, f"Ответ сервера '{response.status_code}' не совпадает с ожидаемым '401'"
            assert message == Constants.WrongData

    @allure.title('Изменение данных пользователя с авторизацией')
    def test_user_change_data(self):
        user = UserHandlers()
        response = user.user_login()
        json_data = response.json()
        access_token = json_data.get("accessToken")
        response = user.user_data_change(access_token)
        json_data = response.json()
        message = json_data.get("success")
        with allure.step(f"Проверка, что поле '{message}' присутствует при корректном ответе"):
            assert response.status_code == 200, f"Ответ сервера '{response.status_code}' не совпадает с ожидаемым '401'"
            assert message == True


    @allure.title('Изменение данных пользователя без авторизации')
    def test_user_change_data_without_login(self):
        user = UserHandlers()
        response = user.user_data_change(access_token = "faketoken")
        json_data = response.json()
        message = json_data.get("success")
        with allure.step(f"Проверка, что '{response.status_code}' равен '401'"):
            assert response.status_code == 401, f"Ответ сервера '{response.status_code}' не совпадает с ожидаемым '401'"
            assert message == False