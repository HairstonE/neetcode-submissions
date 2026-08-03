class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        substring_count = Counter(s1)
        string_count = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            string_count[s2[r]] += 1
            while (r - l + 1) > len(s1):
                string_count[s2[l]] -= 1
                l += 1
            
            if all([substring_count[c] == string_count[c] for c in substring_count]):
                return True

        return False
        