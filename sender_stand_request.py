import configuration
import requests

# Задание 1:
# def get_docs():
# return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)
# response = get_docs()
# print(response.status_code)

# Задание 2:
# def get_logs():
   # return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,
                       # params={"count":20})

# response = get_logs()
# print(response.status_code)
# print(response.headers)

# Задание 3:
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

response = get_users_table()
print(response.status_code)