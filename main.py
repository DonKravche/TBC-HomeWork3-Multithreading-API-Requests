import json
import threading
import time

import requests


def send_requests():
    all_product_data = []  # Creating List to save data from api
    for index in range(1, 101):
        response = requests.get(f'https://dummyjson.com/products/{index}')
        product_data = response.json()
        # print(product_data) tested if data really come from api
        if response.status_code == 200:
            all_product_data.append(product_data)  # adding data to all_product_list
            time.sleep(1)  # delay 1 second
        elif response.status_code == 404:
            print("Not Found.")

    # opening Json File and write all_product_list data

    with open('file.json', 'w') as file_json:
        json.dump(all_product_data, file_json, indent=3)


if __name__ == '__main__':
    product_data_response = threading.Thread(target=send_requests)  # targeting response to necessary target function

    product_data_response.start()
    product_data_response.join()
