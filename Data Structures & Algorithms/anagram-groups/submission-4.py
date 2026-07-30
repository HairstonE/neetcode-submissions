class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grams = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            grams[sorted_s].append(s)
            

        return [v for _,v in grams.items()]