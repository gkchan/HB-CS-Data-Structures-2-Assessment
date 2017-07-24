# Discussion

# Recursion

# 1. Recursion is when a function calls itself.
# 2. A base case will often be a degenerate case that needs to be treated differently. Otherwise, you can get errors.
# If you don't have a base case, the recursion won't know when to stop and a function can end up calling itself forever 
# (or at least until the program throws a Runtime error.)

# Graph
# 1. A graph is a data structure made up of nodes connected by edges. (Also see 2. below.)

# 2. Graphs are like trees, but they can contain cycles and can be directed or undirected.
# Graphs are more generalized and less restricted than trees.

# 3. Graphs can show connections on social networks.


# Performance of different data structures:


# Data Structure                  Index       Search      Add-R       Add-L       Pop-L       Pop-R
# Python List (Array)             O(1)        O(n)        O(1)        O(n)        O(n)        O(1)
# Linked List                     O(n)        O(n)    *O(1)/O(n)      O(1)        O(1)    *O(1)/O(n)            
# Doubly-Linked List              O(n)        O(n)        O(1)        O(1)        O(1)        O(1)
# Queue (as Array)                    X       X           O(1)        X           O(n)          X
# Queue (as LL or DLL)                X       X         *O(1)/O(n)    X           O(1)         X
# Stack (as Array, LL, or DLL)        X       X          **O(1)        X           X        **O(1)   
# Deque (as DLL)                      X       X           O(1)        O(1)         O(1)        O(1)  


# This comment applies to many of the answers:
#     * It depends on whether the linked list has a tail attribute. If it does, it's O(1) to alter the end. Otherwise, it's O(n) to traverse.

# ** The assessment says R is the end, so the * comment for linked lists also applies. 
# It also depends on whether you are using the correct side of an array.




# Data Structure          Get         Add         Delete      Iterate     Memory
# Dictionary (Hash Map)   O(1)        O(1)        O(1)        O(n)        medium
# Set (Hash Map)          O(1)         O(1)       O(1)        O(n)        medium (less than dictionary)
# Binary Search Tree      O(logn)     O(logn)     O(logn)      O(n)       a little
# Tree                    O(n)        O(1)        O(1)        O(n)        a little
        

# Sorting

# 1. Bubble sort goes through the list and swaps a pair of 2 values if they are in the wrong order and does this for every pair of contiguous values
# such that the highest value will bubble to the top. Then it goes through the list again until all values are sorted. 
# It could go through the list about as many times as there are items.

# 2. Merge sort can take 2 sorted lists and combine them into 1 sorted list by taking the lower of the lowest values of each list and adding it to a new list.
# It creates 2 sorted lists from recursion. It runs merge sort to get those 2 lists and so on.

# 3. Quick sort chooses a pivot and then splits the lists into whether the values are lower than, higher than, or equal to a certain pivot.
# It continues the process and will concatenate the lists.



