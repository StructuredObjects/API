import enum

from .utils import *

class InputResponse(enum.Enum):
    RCE_VULN            = -1;
    VALID_INPUTS        = 0;
    BLACKLISTED_HOST    = 2;
    INVALID_HOST        = 3;
    INVALID_PORT        = 4;
    INVALID_TIME        = 5;

class Attack:
    host: str = "";
    port: int = 80;
    time: int = 0;
    method: str = "";

    def __init__(self, h: str, p: str, t: str, m: str):
        self.host = h; self.port = p; self.time = t; self.method = m;

    def validateHost(self) -> InputResponse:
        if not (validateIPV4(self.host) or validateURL(self.host)):
            return InputResponse.INVALID_HOST;

        if validateAttackPort(self.port): return InputResponse.INVALID_PORT;

        if int(self.time) < 1: return InputResponse.INVALID_TIME;

        return InputResponse.VALID_INPUTS;

    def sanitizeInputs(self) -> InputResponse:
        """ RCE CHECK """
        possibilities = [";", "|", "\\", "curl", "wget", "echo", "nc", "netcat", "ncat"];
        for i in possibilities:
            if i in self.host:
                return InputResponse.RCE_VULN;

        