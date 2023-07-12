import json, paramiko

class SSH_M():
    name:           str; # UDP
    max_time:       int; # 600
    script_path:    str; # "/root/udp.py"
    script_usage:   str; # "python3 udp.py [IP] [PORT] [TIME]"


class BreezySSH():
    ssh_methods: list[SSH_M];

    def __init__(self, ssh_m: dict = {}):
        self.__parseMethods(ssh_m);

    """
        using 'jsonfile2dict() -> dict:'
    """
    def __parseMethods(self, methods: dict) -> list[SSH_M]:
        for key in methods:
            new_m = SSH_M();
            new_m.name = key;
            new_m.name = methods[key]['name'];
            new_m.max_time = methods[key]['max_time'];
            new_m.script_path = methods[key]['script_path'];
            new_m.script_usage = methods[key]['script_usage'];
            self.ssh_methods.append(new_m);

    def __verifyServers(self) -> bool:
        pass

    def __detectFiles(self) -> bool:
        pass
