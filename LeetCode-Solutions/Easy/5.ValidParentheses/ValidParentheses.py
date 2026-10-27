characters = {'(' : ')' , '{' : '}' , '[': ']'}

enterenceValue = "()[]{[[[}{{(())}}]]]}"

sizeOfEnterence = len(enterenceValue)
checkArray = []
boolValue = True
i = 0
valid = True

for i in enterenceValue:
    if i in characters.keys():
        checkArray.append(i)
    elif checkArray and characters[checkArray[-1]] == i:
        # if checkArray: ifadesi if len(checkArray) > 0: Bu kontrolü and’in soluna koymamızın bir sebebi var.
        #  and önce sol tarafa bakar ve sol taraf False ise sağ tarafı hiç çalıştırmaz. Buna kısa devre (short-circuit) deniyor.
        checkArray.pop()
    else:
        valid = False
        break

if valid and not checkArray:
    print("Valid Parenthesis")
else:
    print("Invalid Parenthesis")


class Solution:
    def isValid(self, s: str) -> bool:
        characters = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if c in characters:  # kapanış parantezi
                if not stack or stack[-1] != characters[c]:
                    return False
                stack.pop()
            else:  # açılış parantezi
                stack.append(c)
        return not stack