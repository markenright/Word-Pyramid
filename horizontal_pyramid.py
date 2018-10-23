# -*- coding: utf-8 -*-

# prints a simple horizontal pyramid from a given string


def pyr_two_loops(msg):
    for i, l in enumerate(msg):
        print(msg[0:i])
    for i, l in enumerate(msg[::-1]):
        print(msg[0:(len(message)-i)])


message = "never better"


pyr_two_loops(message)
