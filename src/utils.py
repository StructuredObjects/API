from .classes import Attack

def validateIPV4(ip: str) -> bool:
    arg = ip.split(".");
    if len(arg) != 4: return False;
    
    for i in arg: if not int(i) > 0 and not int(i) < 255: return False;

    return True;

def validateAttackPort(p: int) -> bool:
    if not p > 0 and not p < 65533: return False;
    return True;

def parse_usage(usage: str, atk: Attack) -> str:
    return usage.replace("[HOST]", atk.host).replace("[PORT]", atk.port).replace("[TIME]", atk.time).replace("[METHOD]", atk.method);