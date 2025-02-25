import allure
from handlers.order_handlers import OrderHandlers
from handlers.user_handlers import UserHandlers
import pytest


class TestsOrder:

    @allure.title('Создание заказа с авторизацией')
    def test_create_order_with_authorisation(self):
        user = UserHandlers()
        order = OrderHandlers()
        response = user.user_login()
        json_data = response.json()
        access_token = json_data.get("accessToken")
        user.user_data_change(access_token)
        response = order.order_creation(access_token)
        json_data = response.json()
        message = json_data.get("name")
        with allure.step(f"Проверка, что поле '{message}' присутствует при корректном ответе"):
            assert message == "Флюоресцентный бургер"

    @allure.title('Создание заказа без авторизации')
    def test_create_order_without_authorisation(self):
        order = OrderHandlers()
        response = order.order_creation()
        json_data = response.json()
        message = json_data.get("name")
        with allure.step(f"Проверка, что поле '{message}' присутствует при корректном ответе"):
            assert message == "Флюоресцентный бургер"

    @allure.title('Создание заказа с ингредиентами')
    def test_create_order_with_ingredients(self):
        order = OrderHandlers()
        response = order.order_creation()
        json_data = response.json()
        message = json_data.get("name")
        with allure.step(f"Проверка, что поле '{message}' присутствует при корректном ответе"):
            assert message == "Флюоресцентный бургер"

    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_create_order_with_wrong_ingredients(self):
        order = OrderHandlers()
        response = order.wrong_order_creation()
        with allure.step(f"Проверка, что '{response.status_code}' равен '500'"):
            assert response.status_code == 500, f"Ответ сервера '{response.status_code}' не совпадает с ожидаемым '500'"

    @allure.title('Вызываем список заказов авторизованного пользователя')
    def test_create_order_with_authorized_user(self):
        user = UserHandlers()
        order = OrderHandlers()
        response = user.user_login()
        json_data = response.json()
        access_token = json_data.get("accessToken")
        user.user_data_change(access_token)
        response = order.order_list_get_user(access_token)
        json_data = response.json()
        message = json_data.get("success")
        with allure.step(f"Проверка, что поле '{message}' присутствует при корректном ответе"):
            assert message == True

    @allure.title('Вызываем список заказов неавторизованного пользователя')
    def test_create_order_with_not_authorized_user(self):
        order = OrderHandlers()
        response = order.order_list_get()
        json_data = response.json()
        message = json_data.get("success")
        with allure.step(f"Проверка, что поле '{message}' присутствует при корректном ответе"):
            assert message == True

