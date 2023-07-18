from .classes import Attack, InputResponse

def validateIPV4(ip: str) -> bool:
    arg = ip.split(".");
    if len(arg) != 4: return False;
    
    for i in arg: 
        if not int(i) > 0 and not int(i) < 255: return False;

    return True;

def validateURL(url: str) -> bool:
    pass

def validateAttackPort(p: int) -> bool:
    if not p > 0 and not p < 65533: return False;
    return True;

def validateTime(t: str, user_max_time: int = 0) -> InputResponse:
    if int(t) < 1: return InputResponse.INVALID_TIME;

    if user_max_time > 0:
        if int(t) > user_max_time: return InputResponse.INVALID_TIME;

    return InputResponse.VALID_INPUTS;

def parse_usage(usage: str, atk: Attack) -> str:
    return usage.replace("[HOST]", atk.host).replace("[PORT]", atk.port).replace("[TIME]", atk.time).replace("[METHOD]", atk.method);