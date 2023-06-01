import configuration
import requests
import data

# Задание 1:
# def post_new_user(body):
    #return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                       # json={ "firstName": "Анатолий", "phone": "+79995553322", "address": "г. Москва, ул. Пушкина, д. 10"},  # тут тело
                        # headers={"Content-Type": "application/json"})  # а здесь заголовки

# response = post_new_user(data.user_body);
# print(response.status_code)
# print(response.json())

# Задание 2:

def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, json=products_ids,
                             headers=data.headers)

    response = post_products_kits(data.product_ids);
    print(response.status_code)
    print(response.json())