#!/usr/bin/env python2
import socket, json, subprocess


def ask_convert(id):
    data = json.dumps({'id': id})
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 40234))
    client.send(data)
    client.close()

if __name__ == "__main__":
    for i in range(1, 8):
        ask_convert(str(i))