import requests
import allure
import json

from constants import Constants

class OrderHandlers:


    @allure.step('Создание заказа')
    def order_creation(self, access_token = ''):
        response = requests.post(Constants.OrderUrl,
                                 headers={'Authorization': access_token},
                                 data={"ingredients": ["61c0c5a71d1f82001bdaaa6d"]})
        return response

    @allure.step('Создание заказа без ингридиентов')
    def empty_order_creation(self, access_token=''):
        response = requests.post(Constants.OrderUrl,
                                 headers={'Authorization': access_token},
                                 data={"ingredients": ''})
        return response

    @allure.step('Создание заказа с неверным хешем ингредиентов')
    def wrong_order_creation(self, access_token=''):
        response = requests.post(Constants.OrderUrl,
                                 headers={'Authorization': access_token},
                                 data={"ingredients": 'wrong_data'})
        return response


    @allure.step('Вызываем список заказов')
    def order_list_get(self):
        response = requests.get(Constants.AllOrdersUrl)
        return response

    @allure.step('Вызываем список заказов пользователя')
    def order_list_get_user(self, access_token):
        response = requests.get(Constants.OrderUrl,
                                 headers={'Authorization': access_token})
        return response