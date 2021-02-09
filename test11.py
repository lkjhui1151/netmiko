import pandas as pd

dataset = pd.read_csv('D:/Atom/net-auto/IP_Address.csv')

host = dataset['host'].values
command = dataset['command'].values


def ip_address():
    for i in host:
        print(i)
# def command():
#     for i in cmd:
#         print(i)


print(ip_address())
