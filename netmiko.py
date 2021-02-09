import netmiko
from netmiko import ConnectHandler
from getpass import getpass
# from netmiko.ssh_exception import NetMikoTimeoutException
# from netmiko.ssh_exception import NetMikoAuthenticationException
# from paramiko.ssh_exception import SSHException
import pandas as pd

# dataset = pd.read_csv('D:/Atom/net-auto/IP_Address.csv')

# host = dataset['host'].values
# command = dataset['command'].values

# for i in host:
#     device = {
#         'host': i,
#         'username': 'ait',
#         'password': 'P@ssw0rd@PEA',
#         # 'secret': 'P@ssw0rd',
#         'device_type': 'arista_eos',
#         'fast_cli': True
#     }


# with ConnectHandler(**device) as net_connect:
#     output = net_connect.send_command('show interface status')
#     print(output.strip())
#     test = open("test.txt", "w")
#     for i in output:
#         test.write(i)
#     test.close()
