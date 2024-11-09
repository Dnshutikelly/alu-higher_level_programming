#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

# Check instantiation
my_list = MyList()  # Should create an empty MyList

# Check append()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)

print(my_list)          # Expected: [1, 4, 2, 3, 5]
my_list.print_sorted()  # Expected: [1, 2, 3, 4, 5]
print(my_list)          # Expected: [1, 4, 2, 3, 5] (unchanged)

# Test with negative numbers
my_list.append(-10)
my_list.append(-5)
my_list.print_sorted()  # Expected: [-10, -5, 1, 2, 3, 4, 5]
