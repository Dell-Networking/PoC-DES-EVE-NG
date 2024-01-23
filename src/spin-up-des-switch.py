import requests
import json

ip_address = '192.168.30.13'
login_url = f'http://{ip_address}/api/auth/login'
login_creds = '{"username":"admin","password":"eve","html5":"-1"}'
headers = {'Accept': 'application/json'}

login = requests.post(url=login_url, data=login_creds)
cookies = login.cookies
print(cookies)


sonic_data = {"template": "SONiC", "type": "qemu", "count": "1", "image": "SONiC-4.1.1", "name": "SONiC",
               "icon": "Switch L3.png", "uuid": "", "cpulimit": "undefined", "cpu": "2", "ram": "4096",
               "ethernet": "16", "qemu_version": "", "qemu_arch": "", "qemu_nic": "",
               "qemu_options": "-machine type: pc,accel=kvm -vga std -usbdevice tablet -boot order=dc",
               "ro_qemu_options": "-machine type=pc,accel=kvm -vga std -usbdevice tablet -boot order=dc", "config": "0",
               "delay": "0", "console": "telnet", "left": "607", "top": "239", "postfix": 0}

sonic_data = json.dumps(sonic_data)
create_url = f'http://{ip_address}/api/labs/SONiC%20Test%20Lab.unl/nodes'

create_api = requests.post(url=create_url, data=sonic_data, cookies=cookies, headers=headers)
response = create_api.json()
print(response)

#  TODO - API call in try catch and function

requests.exceptions