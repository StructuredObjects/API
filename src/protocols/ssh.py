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

{
      “Server1”: {
            “host_ip”: “5.5.5.5”,
            “host_port”: 22,
            “username”: “root”,
            “password”: “root”,
            “methods”: {
                  “tcp”: “python3 tcp.py [IP] [PORT] [TIME]”
              }
      }
}
    """
    def __parseMethods(self, methods: dict) -> bool:
        try:
            for key in methods:
                new_m = SSH_M();
                new_m.name = key;
                new_m.host_ip = methods[key]['host_ip'];
                new_m.password = methods[key]['password'];
                new_m.max_time = methods[key]['max_time'];

                for method in methods['methods']: new_m.methods[method] = methods['methods'][method];
                self.ssh_methods.append(new_m);
        except:
            print("[ X ] Error, Something went wrong trying to parse the SSH JSON file...!");
            return False;
            
        return True;

    """
        Connect and login to verify all servers are up!
    """
    def __verifyServers(self) -> bool:
        for ssh_server in self.ssh_methods:
            ssh_check, ssh_stdin = self.sendCmd(ssh_server, "whoami");
            if not ssh_check:
                print(f"[ X ] Error, Unable to connect to {ssh_server.host_ip}");
                return False;
                
        return True;

    """
        Detecting script paths to ensure all servers have the method listed in config!

        NOT DONE 57/14/23 9PM EST 
    """
    def __detectFiles(self) -> bool:
        for ssh in self.methods:
            ssh_check, ssh_stdin = self.sendCmd(ssh, "/root/methods/"); 

    def sendCmd(self, ssh: SSH_M, cmd: str) -> tuple[bool, str]:
        try:
            server = paramiko.client.SSHClient();
            server.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            server.connect(host=ssh.host_ip, username=ssh.host_port, password=ssh.password);
            _stdin, stdout, _strerr = server.exec_command(cmd);
            server.close();
            return True, _stdin;
        except:
            print(f"[ X ] Error, Unable to connect to {ssh_server.host_ip}....!");
            return False, "";
