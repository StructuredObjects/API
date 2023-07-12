import json, paramiko

class SSH_M():
    name:           str;            # "Server1"
    host_ip:        str;            # "5.5.5.5"
    host_port:      str = 22;       # 22 as default
    username:       str = "root";   # "root"
    password:       str = "root";   # "root"
    max_time:       int;            # 600
    methods:        dict;           # {"UDP": "./udp [IP] [PORT] 65533 [TIME]"}

class BreezySSH():
    ssh_methods: list[SSH_M];

    def __init__(self, ssh_m: dict = {}):
        self.__parseMethods(ssh_m);

    """
        using 'jsonfile2dict() -> dict:'
    """
    def __parseMethods(self, methods: dict) -> bool:
        try:
            for key in methods:
                new_m = SSH_M();
                # Changing.....
                self.ssh_methods.append(new_m);
        except:
            print("[ X ] Error, Something went wrong trying to parse the SSH JSON file...!");
            return False;
            
        return True;

    """
        Connect and login to verify all servers are up!
    """
    def __verifyServers(self) -> bool:
        pass

    """
        Detecting script paths to ensure all servers have the method listed in config!
    """
    def __detectFiles(self) -> bool:
        pass
