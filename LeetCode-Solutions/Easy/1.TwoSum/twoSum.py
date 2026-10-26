# Eğer ki array sıralıysa
# givenArray = [2, 7, 11, 15]
# target = int(input("Enter target: "))

# i = 0
# j = len(givenArray) - 1
# indexes = []
# step = 1
# while i < j:
#     s = givenArray[i] + givenArray[j]

#     print(f"Adım {step} => i: {i}, j: {j}, Sonuç: {s}")    
#     step += 1
#     if s == target:
#         indexes = [i + 1, j + 1]
#         break
#     elif s > target:
#         j -= 1
#     else:
#         i += 1

# if indexes:
#     print(indexes)
# else:
#     print("Bu toplamı veren bir çift yok.")


# Array sıralı değil ve hashmap ile yapacaksak:



def twoSum(nums: list[int], target: int):
        seen = {}  # sayı -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []


givenArray = [2 , 15 , 7 , 11 , 12]
target = 19
resultArray = twoSum(givenArray , target)
print(resultArray)
