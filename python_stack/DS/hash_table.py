user = {
    "first_name":"Adel",

}
our_list ={"adel","full stack developer","computer science"}
our_list[2] #O(1)
user["first_name"]#O(1)
hash_table = [None,None,None,None,None]#O(1)
def set(key,value):
    index =hash(key)%len(hash_table)
    hash_table[index]= value
def get(key):
    index = hash(key)%len(hash_table)
    return hash_table[index]
set("first_name","Adel")
set("last_name","jrour")
get("first_name")

class HashTable:
    def __init__(self,size=12):
        self.size = size
        self.hash_table =[None,None,None,[None,None,None],None,None,None,None,None,None,None,None]

    def set(self,key,value):
        index = hash(key)%self.size
        hash_table[index]=value #O1
    def get(self,key):
        index=hash(key)%self.size
        return hash_table[index] #O1
    
