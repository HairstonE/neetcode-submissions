class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grams = defaultdict()

        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in grams:
                grams[sorted_s].append(s)
            else:
                grams[sorted_s] = [s]

        return [v for _,v in grams.items()]