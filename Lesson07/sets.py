nums = {2, 10, 40, 13, 70, 5, 10}
nums2 = set((45, 20, 1, 5)) # creating set using constructor

print(nums)
print(nums2)
print(type(nums))
print(type(nums2))
print(len(nums))

# set doesn't allow duplicates
nums3 = {1, 2, 2, 2, 3}
print(nums3)
print(len(nums3))

# True is a dupe of 1, and False is a dupe of zero
nums4 = {1, True, False, 4, 5, 0}
print(nums4)

print(2 in nums4)
print(4 in nums4)

# Merge sets to create a new set
one = {1, 2, 3, 4}
two = {4, 5, 6, 1}
three = one.union(two)
print(three)

# Keep only the duplicates
one = {1, 2, 3, 4}
two = {4, 5, 6, 1}
one.intersection_update(two)
print(one)

# Keep everything except duplicates
one = {1, 2, 3, 4}
two = {4, 5, 6, 1}
one.symmetric_difference_update(two)
print(one)

