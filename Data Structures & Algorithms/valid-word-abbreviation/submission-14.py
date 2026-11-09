class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        wi, ai = 0, 0

        while wi < len(word) and ai < len(abbr):
            if abbr[ai].isdigit():
                if abbr[ai] == '0':
                    return False
                i = ai
                while i < len(abbr) and abbr[i].isdigit():
                    i += 1
                num = int(abbr[ai:i])
                wi += num
                ai = i
            else:
                if word[wi] != abbr[ai]:
                    return False
                else:
                    wi += 1
                    ai += 1
        return wi == len(word) and ai == len(abbr) 
