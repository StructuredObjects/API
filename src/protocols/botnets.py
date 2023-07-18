import socket

from ..classes import *

class QBOT_M():
    name:           str;
    host_ip:        str;
    host_port:      str;
    username:       str;
    password:       str;
    methods:        str;
    method_usage:   dict;
    max_time:       int;

class BreezyQBOT():
    qbots:      list[QBOT_M];
    def __init__(self, qbot_m: dict = {}):
        self.__parseMethods();

    def __parseMethods(self, m: dict) -> bool:
        pass
    
    def __sendCmd(self, qb: QBOT_M, info: Attack) -> tuple[bool, str]:
        pass