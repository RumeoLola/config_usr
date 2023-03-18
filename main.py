# imports
import socket
import re, uuid


def usr_information():
    # get hostname
    hostname = socket.gethostname()
    # get ip address
    ip_address = socket.gethostbyname(hostname)
    # printing the value of unique MAC
    # address using uuid and getnode() function
    mac_address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    print(hostname, ip_address, mac_address)


usr_information()
