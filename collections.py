# List (like ArrayList)
nums = [1, 2, 3, 4]

# Tuple (immutable list)
t = (1, 2, 3)

# Dictionary (like Map)
user = {"name": "Mayank", "age": 25}


#we can access direct user["name"] but it cancause error if name not exist so safe way to use .get() to avoid crashes



print(user.get("name"))

print(user.get("City")) #safe handle

print(t.index(1))




# ================================
# TUPLE IN PYTHON - COMPLETE GUIDE
# ================================

# 1. What is a Tuple?
# A tuple is an ordered, immutable collection of elements
# Immutable = cannot change after creation

t = (10, 20, 30)

# --------------------------------
# 2. Accessing Tuple Elements
# --------------------------------

# By index (0-based)
print(t[0])   # 10
print(t[1])   # 20

# Negative indexing (from end)
print(t[-1])  # 30 (last element)

# --------------------------------
# 3. Looping through Tuple
# --------------------------------

for item in t:
    print(item)

# --------------------------------
# 4. Tuple is Immutable
# --------------------------------

# ❌ This will give error
# t[0] = 100

# --------------------------------
# 5. Tuple with Different Data Types
# --------------------------------

mixed = (1, "Mayank", 25.5, True)
print(mixed)

# --------------------------------
# 6. Single Element Tuple
# IMPORTANT: Must use comma
# --------------------------------

single = (10,)   # सही
not_tuple = (10) # ❌ This is int, not tuple

# --------------------------------
# 7. Tuple Packing & Unpacking
# --------------------------------

# Packing
person = ("Mayank", 25, "Pune")

# Unpacking
name, age, city = person

print(name)
print(age)
print(city)

# --------------------------------
# 8. Returning Multiple Values from Function
# --------------------------------

def get_user():
    return ("Mayank", 25)

name, age = get_user()
print(name, age)

# --------------------------------
# 9. Tuple as Dictionary Key
# (Because tuple is immutable)
# --------------------------------

locations = {
    (18.52, 73.85): "Pune",
    (28.61, 77.20): "Delhi"
}

print(locations[(18.52, 73.85)])

# --------------------------------
# 10. Useful Tuple Methods
# --------------------------------

nums = (1, 2, 3, 2, 4, 2)

print(nums.count(2))   # Count occurrences → 3
print(nums.index(3))   # Index of value → 2

# --------------------------------
# 11. Tuple vs List
# --------------------------------

# List → mutable
lst = [1, 2, 3]
lst[0] = 100   # allowed

# Tuple → immutable
tpl = (1, 2, 3)
# tpl[0] = 100 ❌ not allowed

# --------------------------------
# 12. Real-World Use Cases
# --------------------------------

# Fixed data (coordinates)
coordinate = (18.5204, 73.8567)

# RGB color
color = (255, 0, 0)

# Database-like record
user = (101, "Mayank", "Pune")

# --------------------------------
# 13. Nested Tuple
# --------------------------------

nested = ((1, 2), (3, 4), (5, 6))
print(nested[0])      # (1, 2)
print(nested[0][1])   # 2

# --------------------------------
# 14. Convert Tuple ↔ List
# --------------------------------

# Tuple to List
t = (1, 2, 3)
lst = list(t)

# Modify list
lst[0] = 100

# Convert back to tuple
t = tuple(lst)
print(t)

# --------------------------------
# 15. Slicing Tuple
# --------------------------------

t = (10, 20, 30, 40, 50)

print(t[1:4])   # (20, 30, 40)
print(t[:3])    # (10, 20, 30)
print(t[::2])   # (10, 30, 50)

# ================================
# END OF TUPLE GUIDE
# ================================







#list

listd=["mayank",5]
tupled=(1,"Mayank",1)
dictonryd={"Name":"punit"}



print("\n")
print("\n")
print("\n")




print(listd.index("mayank"))

print(tupled[0])


print(dictonryd.get("Name"))

setd={tupled}


print(setd)
