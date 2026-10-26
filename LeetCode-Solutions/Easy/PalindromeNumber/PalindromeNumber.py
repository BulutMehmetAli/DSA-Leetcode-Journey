def isPalindrome(x: int) -> bool:
    x = str(x)
    i = 0
    j = len(x) - 1
    while i < j:
        if x[i] != x[j]:
            return False
        i += 1
        j -= 1
    return True

number = "1234565432661"

print(number[::-1] == number)
