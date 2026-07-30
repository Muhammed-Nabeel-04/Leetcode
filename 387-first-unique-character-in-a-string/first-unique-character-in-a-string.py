class Solution:
    def firstUniqChar(self, s: str) -> int:

        collection = {}
        for i in s:
            collection[i] = collection.get(i, 0) + 1
        if 1 in collection.values():
          for k,v in collection.items():
            if v == 1:
                return s.index(k)
        return -1        

      