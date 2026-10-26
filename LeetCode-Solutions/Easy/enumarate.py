"""
enumerate() function adds a counter to each item in a list or any other iterable, 
and returns a list of tuples containing the index position and the element for each element of the iterable.

We can use enumerate() with a dictionary to get both the index and its key-value pair:

"""

a = ["Geeks", "for", "Geeks"]

# Iterating list using enumerate to get both index and element
for i, name in enumerate(a , start=0):
    print(f"Index {i}: {name}")
# Converting to a list of tuples
print(list(enumerate(a)))

print("***************************")

d = {"a": 10, "b": 20, "c": 30}

# Enumerating through dictionary items
for index, (key, value) in enumerate(d.items()):
    print(index, "-", key, ":", value)

s = "python"
for i, ch in enumerate(s):
    print(f"Index {i}: {ch}")

"""
Enumerate is a built-in Python function. It enables you to keep track of iterations, write more efficient loops, 
and access the index and values of an iterable object
You can use enumerate with any iterable object in Python. Examples of iterable objects include lists, strings, tuples, 
and dictionaries.

By default, the syntax of Python enumerate is as follows:
enumerate(iterable, start=0)

enumerate() işlevine bir yinelenebilir nesne aktarıldığında, for döngüsüyle yinelenebilen veya list() yöntemi kullanılarak 
tuple listesine dönüştürülebilen bir numaralandırılmış nesne döndürülür.This function may be helpful anytime you want to keep count of or access iterable items.

"""