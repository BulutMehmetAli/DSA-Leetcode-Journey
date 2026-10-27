# words = ["flower" , "fligt" , "flow"]

# longest = max(words, key=len)

# words = ["elma", "karpuz", "kivi", "portakal"]

# longest = words[0]
# for word in words:
#     if len(word) > len(longest):
#         longest = word

def logest(wordList):
    res = ""
    for i in range(len(wordList[0])):
        for s in wordList:
            if i == len(s) or s[i] != wordList[0][i]:
                return res
        res += wordList[0][i]

# Better Situation
def longestCommonPrefix(self, strs: list[str]) -> str:
        for i, ch in enumerate(strs[0]):
            for s in strs[1:]:
                if i == len(s) or s[i] != ch:
                    return s[:i]
        return strs[0]