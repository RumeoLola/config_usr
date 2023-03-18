# imports
import socket
import re, uuid


# get hostname
hostname = socket.gethostname()


# get ip address
ip_address = socket.gethostbyname(hostname)


print(hostname)
print(ip_address)


# printing the value of unique MAC
# address using uuid and getnode() function
mac_address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
print(mac_address)
