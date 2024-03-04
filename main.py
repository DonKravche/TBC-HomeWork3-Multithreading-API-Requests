import json
import threading
import time

import requests


def send_request(index, api_list):
    response = requests.get(f'https://dummyjson.com/products/{index}')
    api_data = response.json()
    if response.status_code == 200:
        api_list.append(api_data)  # adding data to all_product_list
        print(api_list)
        # time.sleep(1)  # delay 1 second
    elif response.status_code == 404:
        print("Not Found.")


def main_function():
    start_time = time.time()  # Capture start time

    threads = []
    api_list = []

    for index in range(0, 101):  # Creating Threads for each request or 'index'
        thread = threading.Thread(target=send_request, args=(index, api_list))
        threads.append(thread)
        thread.start()

    for thread in threads:  # Waiting and checking to all threads to complete
        thread.join()

    with open('file.json', 'w') as file_json:  # opening json file
        json.dump(api_list, file_json, indent=3)

        elapsed_time = time.time() - start_time  # Calculate elapsed time
        print(f"Execution time: {elapsed_time} seconds")


if __name__ == '__main__':
    main_function()


# Old Code


# def send_requests():
#     start = time.perf_counter()
#     all_product_data = []  # Creating List to save data from api
#     for index in range(1, 101):
#         response = requests.get(f'https://dummyjson.com/products/{index}')
#         product_data = response.json()
#         print(product_data)  # tested if data really come from api
#         if response.status_code == 200:
#             all_product_data.append(product_data)  # adding data to all_product_list
#             # time.sleep(1)  # delay 1 second
#         elif response.status_code == 404:
#             print("Not Found.")
#
#     # opening Json File and write all_product_list data
#
#     with open('file.json', 'w') as file_json:
#         json.dump(all_product_data, file_json, indent=3)
#
#     finish = time.perf_counter()
#     print('time: ', finish - start)
#
#
# if __name__ == '__main__':
#     product_data_response = threading.Thread(target=send_requests)  # targeting response to necessary target function
#
#     product_data_response.start()
#     product_data_response.join()
