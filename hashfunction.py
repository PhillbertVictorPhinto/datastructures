class HashTable:
    def __init__(self):
        self.bucket = 16
        self.hashmaps =[[] for x in range(self.bucket)]

    def _hash(self,key):
        return len(key) % self.bucket

    def set(self,key,value):

        hashvalue = self._hash(key)

        reference = self.hashmaps[hashvalue]
        for i in range(len(reference)):
            if reference[i][0] == key:
                reference[i][1] = value
                return None
        reference.append([key,value])
        return None

    def get(self,key):
        hashvalue =self._hash(key)
        reference = self.hashmaps[hashvalue]
        for i in range(len(reference)):
            if reference[i][0]==key:
                return reference[i][1]
        return -1

    def keys(self):
        keys=[]
        for x in range(len(self.hashmaps)):
            try:

                keys.append(self.hashmaps[x][0][0])
            except:
                pass
        return keys


info =HashTable()
info.set('banana',50)
info.set('oranges',30)
info.set('apple',30)
v=info.keys()
print(v)
