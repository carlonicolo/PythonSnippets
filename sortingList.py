'''
Difference between sort() and sorted() function
'''

# Using sort() the list will be modified
years = [2024, 1977, 2001, 2023]
print("Original list: ", years)
print("Using sort()")
years.sort()
print("List sorted with sort() ", years)
print("Original list after applying sort()", years)
print("####################")
print("")


# Using sorted the list will no tbe modified
years = [2024, 1977, 2001, 2023]
print("Original list: ", years)
print("Using sorted()")
years_sorted = sorted(years)
print("List sorted with sorted() ", years_sorted)
print("Original list after applying sort()", years)
print("####################")
