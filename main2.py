fruits = {"apple","banana","cherry"}
fruits.add("orange")
print("After adding 'orange':", fruits)
fruits.remove("banana")
print("After removing 'banana':", fruits)
tropical = {"mango","papaya","apple"}
union_set = fruits.union(tropical)
print("union with tropical fruits:", union_set)
intersection_set = fruits.intersection(tropical)
print("Intersection with tropical fruits:", intersection_set)
difference_set = fruits.difference(tropical)
print("Difference with tropical fruits:", difference_set)
print("Number of elements in fruits set:", len(fruits))