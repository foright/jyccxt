import redis

OPENFAILEDTIMES = 5
CLOSEFAILEDTIMES = 5
class Risk:
    def __init__(self,oid,code):
        self.code = str(code)
        self.ooid = oid
        self.oid = self.parseOid(oid)
        self.redis_conn=redis.Redis(host="127.0.0.1",port=6379,db=0)
    
    def pairFailed(self):
        if self.redis_conn.get("openfailedtimes"):
            openfailedtimes = int(self.redis_conn.get("openfailedtimes").decode())
        else:
            openfailedtimes = 0
            
        if self.redis_conn.get("closefailedtimes"):
            closefailedtimes = int(self.redis_conn.get("closefailedtimes").decode())
        else:
            closefailedtimes = 0

        if openfailedtimes > OPENFAILEDTIMES:
            self.redis_conn.delete("openfailedtimes")
            return False
        if closefailedtimes > CLOSEFAILEDTIMES :
            self.redis_conn.delete("closefailedtimes")
            return False
    
        if self.redis_conn.exists(self.oid["pairid"]):
            self.redis_conn.delete(self.oid["pairid"])
            if self.oid["code"] != 0:
                return False
            
        else: 
            self.redis_conn.set(self.oid["pairid"],self.ooid+self.code)
            if self.oid["code"] != 0:
                if self.oid["oc"] == 0:
                    self.redis_conn.incr("openfailedtimes")
                else:
                    self.redis_conn.incr("closefailedtimes")
            else:
                
                if self.oid["oc"] == 0:
                    self.redis_conn.delete("openfailedtimes")
                else:
                    self.redis_conn.delete("closefailedtimes")
        return True
    
    def parseOid(self,oid):
        newOid = {}
        newOid['id'] = int(oid[0:3])
        newOid['uid'] = int(oid[3:9])
        newOid['type'] = oid[9:13]
        newOid['code'] = oid[13:15]
        newOid['oc'] = oid[15:16]
        newOid['pairid'] = oid[16:21]
        newOid['time'] = oid[21:32]
        return newOid
        
