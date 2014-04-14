class Solution:
    # @param strs, a list of strings
    # @return a list of strings
       def anagrams(self, strs):
        if not strs:
            return None
        d={}
        for word in strs:
            newword=''.join(sorted(word))
            if newword not in d:
                d[newword]=[word]
            else:
                d[newword].append(word)
        alllist=[]
        for i in d:
            if len(d[i])>1:
                alllist=alllist+d[i]
        return alllist
