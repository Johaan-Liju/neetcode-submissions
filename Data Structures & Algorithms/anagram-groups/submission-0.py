class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag={}
        for i in strs:
            x="".join(sorted(i))
            anag.setdefault(x,[]).append(i)
        return list(anag.values())