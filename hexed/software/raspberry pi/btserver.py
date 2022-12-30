
import socket
from threading import Thread
import json

import os,sys


class BluetoothServer(Thread):
    ERROR = -1
    LISTEN = 1
    CONNECTED = 2
    STOP = 3

    SIG_NORMAL = 0
    SIG_STOP = 1
    SIG_DISCONNECT = 2

    def __init__(self, out_cmd_queue):
        Thread.__init__(self)

        self.cmd_queue = out_cmd_queue

        with open(os.path.join(sys.path[0],'config.json'),'r' ) as read_file:
            self.config = json.load(read_file)

        stream = os.popen('hciconfig hci0')
        output = stream.read()
        device_id = "hci0"
        bt_mac = output.split("{}:".format(device_id))[1].split(
            "BD Address: ")[1].split(" ")[0].strip()

        self.mac = bt_mac
        self.port = 10
        self.bt_socket = socket.socket(
            socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

        self.signal = self.SIG_NORMAL

    def run(self):
        try:
            self.bt_socket.bind((self.mac, self.port))
            self.bt_socket.listen(1)
            print('TCP listening')
        except OSError as err:
            # print('emit tcp server error')
            # self.status.emit(self.STOP, '')
            pass
        else:
            while True:
                self.cmd_queue.put('standby:')
                # Wait for a connection
                # print('wait for a connection')
                # self.status.emit(self.LISTEN, '')
                try:
                    self.connection, addr = self.bt_socket.accept()
                    # self.connection.setblocking(False)
                    # self.connection.settimeout(1)
                    print('New connection')
                except socket.timeout as t_out:
                    pass
                else:
                    while True:
                        # print('waiting for data')
                        # if self.signal == self.SIG_NORMAL:
                        try:
                            data = self.connection.recv(4096)
                        except socket.error as e:
                            print(e)
                            break
                        else:
                            if data:
                                print(data.decode())
                                self.cmd_queue.put(data.decode())
                            else:
                                break

        finally:
            self.bt_socket.close()
            self.cmd_queue.put('standby:')
            print('exit')
