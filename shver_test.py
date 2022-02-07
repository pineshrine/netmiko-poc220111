import os
import json
from netmiko.ssh_autodetect import SSHDetect
from netmiko.ssh_dispatcher import ConnectHandler
import logging

def login(device):

    if device['device_type'] == "autodetect":
        guesser = SSHDetect(**device)
        best_match = guesser.autodetect()
   
        if not best_match:
            print(f'Connect to {device["host"]},' + device['device_type'])
        else:
            print(f'Connect to {device["host"]},' + best_match )
            device['device_type'] = best_match
    else:
        print(f'Connect to {device["host"]},' + device['device_type'])

    connection = ConnectHandler(**device)

    connection.enable()
    if device['device_type'].startswith('cisco'):
        #print(connection.send_command('show version'))
        connection.send_command('show version')
    elif device['device_type'].startswith('huawei'):
        #print(connection.send_command('disp ver'))
        connection.send_command('disp ver')
    else:
        #print(connection.send_command('show version'))
        connection.send_command('show version')

if __name__ == "__main__":
    with open(r"/root/netmiko-poc220111/devlist.json", "r") as f:
        device_info_list = json.load(f)

    logging.basicConfig(filename='netmiko_global.log', level=logging.DEBUG)
    logger = logging.getLogger("netmiko")

    for info in device_info_list:
        device = {
                'host': info["host"],
                'port': "22",
                'username': info["username"],
                'password': info["password"],
                'device_type': info["device_type"],
                'secret': info["password"],
                'verbose': "True",
        }

        login(device)
