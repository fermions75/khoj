import json
import requests

# URL = "http://127.0.0.1:8000/API/get_cluster/"
#
#
#
# def get_data(user_name=None):
#     data = {}
#     if user_name is not None:
#         data = {'user_name' : user_name}
#     json_data = json.dumps(data)
#     headers = {'content-Type' : 'application/json'}
#     r = requests.get(url=URL, headers=headers, data=json_data)
#     data = r.json()
#     print(data)
#
# get_data("OmiFarhan")


a_list = []


a_dictionary = {"name" : "John", "age" : 20}
# dictionary_copy = a_dictionary.copy()
a_list.append(a_dictionary)

b_dictionary = {"name" : "sakib", "age" : 30}
# dictionary_copy = b_dictionary.copy()
a_list.append(b_dictionary)

# print(a_list)




print(a_list)