import os

class Blacklist:
    @staticmethod
    def readIPBlacklisted(filename: str) -> list[str]:
        if not os.path.isfile(filename): return []; 
        """ TRY/EXCEPT TO AVOID DETECTING MULTIPLE EXCEPTIONS """
        try: 
            file = open(filename, "r");
            data = file.read().split("\n");
            file.close();
        except:
            return [];
        return data;

    @staticmethod
    def addBlacklistIP(ip: str) -> bool:
        pass