import requests
import allure
from constants import Constants
from faker import Faker



class UserHandlers:

    @allure.step('создать уникального пользователя')
    def user_creation(self):
        fake = Faker()
        email = fake.email()
        user_name = fake.user_name()
        response = requests.post(Constants.URL + Constants.UserCreateUrl,
                                 data={"email": email,
                                       "password": "password",
                                       "name": user_name})
        return response

    @allure.title('создать пользователя, который уже зарегистрирован')
    def same_user_creation(self):
        fake = Faker()
        email = fake.email()
        user_name = fake.user_name()
        requests.post(Constants.URL + Constants.UserCreateUrl,
                                 data={"email": email,
                                       "password": "password",
                                       "name": user_name})
        response = requests.post(Constants.URL + Constants.UserCreateUrl,
                                 data={"email": email,
                                       "password": "password",
                                       "name": user_name})
        return response

    @allure.step('создать пользователя и не заполнить одно из обязательных полей')
    def user_creation(self):
        fake = Faker()
        email = fake.email()
        user_name = fake.user_name()
        response = requests.post(Constants.URL + Constants.UserCreateUrl,
                                 data={"email": email,
                                       "password": '',
                                       "name": user_name})
        return response

    @allure.step('логин под существующим пользователем')
    def user_login(self):
        fake = Faker()
        email = fake.email()
        user_name = fake.user_name()
        requests.post(Constants.URL + Constants.UserCreateUrl,
                                 data={"email": email,
                                       "password": 'password',
                                       "name": user_name})
        response = requests.post(Constants.URL + Constants.UserLogin,
                                 {
                                     "email": email,
                                     "password": 'password'
                                 }
                                 )
        return response

    @allure.step('логин с неверным логином и паролем')
    def user_login_wrong_password(self):
        fake = Faker()
        email = fake.email()
        user_name = fake.user_name()
        requests.post(Constants.URL + Constants.UserCreateUrl,
                      data={"email": email,
                            "password": 'password',
                            "name": user_name})
        response = requests.post(Constants.URL + Constants.UserLogin,
                                 {
                                     "email": email,
                                     "password": 'password1'
                                 }
                                 )
        return response

    @allure.step('Изменение данных пользователя')
    def user_data_change(self, access_token):
        response = requests.patch('https://stellarburgers.nomoreparties.site/api/auth/user',
                                  headers={'Authorization': access_token},
                                  data={"user": {"name": "name_example"}})
        return response