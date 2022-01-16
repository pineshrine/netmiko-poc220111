import os
import netmiko
import json
import threading

def login(device):
    print(f'Connect to {device["host"]}')
    connection = netmiko.ConnectHandler(**device)

    connection.enable()
    print(connection.send_command('show version'))

    print(f'Exit from {device["host"]}')

if __name__ == "__main__":
    with open(r"devlist.json", "r") as f:
        device_info_list = json.load(f)
    threads = list()

    for info in device_info_list:

        device = {
                'host': info["host"],
                'port': "22",
                'username': info["username"],
                'password': info["password"],
                'device_type': info["device_type"],
                'secret': info["password"],
                'verbose': "True"
        }

        thread = threading.Thread(target=login, args=(device,))
        threads.append(thread)

        for th in threads:
            th.start()

        for th in threads:
            th.join()
