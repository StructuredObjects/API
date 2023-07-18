
class Attack:
    host: str = "";
    port: int = 80;
    time: int = 0;
    method: str = "";

    def __init__(self, h: str, p: str, t: str, m: str):
        self.host = h; self.port = p; self.time = t; self.method = m;