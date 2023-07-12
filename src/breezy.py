from protocols.api      import *
from protocols.ssh      import *
from protocols.botnet   import *

class Breezy():
    ssh: BreezySSH;
    api: BreezyAPI;
    qbot: BreezyQBOT;

    def __init__(self, ssh_m: dict = {}, api_m: dict = {}, qbot_m: dict = {}):
        self.ssh = BreezySSH(ssh_m);