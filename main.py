my_tuple = ("apple","banana","cherry","apple","orange")
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])
print("Slice from index 1 to 3:", my_tuple[1:4])
new_tuple = my_tuple + ("grape", "melon")
print("After concentration:", new_tuple)
repeated_tuple = my_tuple * 2
print("Repeated tuple:", repeated_tuple)
print("Length of tuple:", len(my_tuple))
if "banana" in my_tuple:
    print("Yes, 'banana' is in the tuple.")
print("Count of 'apple':", my_tuple.count("apple"))
print("index of 'cherry':", my_tuple.index("cherry"))