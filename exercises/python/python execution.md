Python Language & Execution Blueprint

This document represents the absolute core of the Python programming language required to pass Google's technical rounds (Software Engineer, AI Systems Engineer, and Research Engineer).

In Google interviews, you are evaluated not just on "getting the code to work," but on your understanding of how the Python interpreter (CPython) manages memory, reference pointers, namespaces, and execution complexities.

🏛️ Module 1: Python From Scratch — Absolute Foundations

To solve complex algorithms, you must first master the native syntax, declaration rules, and logical control gates of Python from scratch.

1. Variables and Primitive Data Types

Variables are references to values. Unlike languages like $\text{C++}$ or $\text{Java}$, Python is dynamically typed—you do not need to declare a variable's type when you write it.

Integers & Floats: Numbers without and with decimals. Python dynamically allocates memory for integers, meaning they can grow arbitrarily large without overflowing.

Booleans: True or False states (True, False). Note the capital letters.

Strings: Sequential characters enclosed in quotes ("hello" or 'world').

None Type: Represents the absence of a value (None). Essential for representing empty or null pointers in linked lists and binary trees.

# Absolute scratch declarations
age = 31               # Integer
learning_rate = 0.001  # Float
is_gpu_available = True # Boolean
user_name = "systems"  # String
next_node = None       # NoneType (Null pointer)


2. Basic Arithmetic & Logical Operators

Floor Division (//): Divides and rounds down to the nearest integer. Extremely important for finding array midpoints in binary search without producing a float index.

Modulo (%): Returns the remainder of a division. Used for cyclic array traversals.

Logical Gates: and, or, and not.

# Sizing calculations
midpoint = (10 + 20) // 2  # Returns 15 (integer), not 15.0 (float)
is_even = (10 % 2 == 0)    # Returns True (remainder is 0)
is_valid = True and not False # Evaluation gates


3. Indentation & Conditional Control Gates

In Python, indentation is semantic. There are no curly braces {} to define blocks; indentation (strictly 4 spaces) defines the execution scope.

threshold = 50
score = 75

if score > threshold:
    # Everything indented here is inside this true condition
    print("Threshold surpassed!")
elif score == threshold:
    print("Exact boundary match.")
else:
    # Triggers if all above conditions evaluate to False
    print("Threshold unmet.")


4. Basic Loops (while and for)

while Loops: Execute repeatedly as long as a boolean condition remains True. Perfect for pointer manipulation.

for Loops: Iterate over a predefined range of numbers or collection items.

# Using a while loop to move two pointers inward
left, right = 0, 10
while left < right:
    left += 1
    right -= 1

# Using a for loop to iterate over indices
# range(start, stop, step) -> range(0, 5) generates: 0, 1, 2, 3, 4
for i in range(0, 5):
    print(f"Current index: {i}")


🛠️ Module 2: Functions, Arguments, and Variable Scoping

Functions allow you to package blocks of reusable logic. Google interview solutions are written inside a class method function.

1. Defining Functions & Return Contracts

Use the def keyword to define functions, declare arguments, and return values using the return keyword.

# Defining a simple sum function
def add_numbers(num1, num2):
    total = num1 + num2
    return total # Exit function and return the computed state

# Invoking the function
result = add_numbers(5, 10) # result becomes 15


2. Default and Keyword Arguments

You can assign fallback default values to arguments in the function definition.

# threshold defaults to 50 if the caller does not provide it
def validate_score(score, threshold=50):
    return score >= threshold

print(validate_score(45))               # Evaluates to False (uses default 50)
print(validate_score(45, threshold=40))  # Evaluates to True (overrides default to 40)


3. Namespace Scoping: The LEGB Rule

Python resolves variable names by searching scopes in a strict hierarchical order:

Local: Variables declared inside the current active function.

Enclosing: Variables declared inside nested parent functions.

Global: Variables declared at the module/file level.

Built-in: Python's reserved functions (len, range, print).

4. Nested Functions & The nonlocal Keyword

In complex algorithms, you will often write a helper function inside your main function to perform recursion (like Depth-First Search). To update a variable tracking state (like a running maximum) inside the helper, you must declare it nonlocal.

def find_maximum_value(numbers):
    current_max = -float('inf') # Enclosing scope variable initialized to -infinity
    
    def dfs(index):
        nonlocal current_max # Direct access to modify parent namespace variable
        if index == len(numbers):
            return
        
        if numbers[index] > current_max:
            current_max = numbers[index] # Update the outer variable
            
        dfs(index + 1) # Recursive step
        
    dfs(0) # Invoke helper
    return current_max


📦 Module 3: Core Collections & Slicing Mechanics

Now that you understand variable scopes and function logic, you must master the structural collections that store data in memory.

1. Lists (Dynamic Arrays)

An ordered, mutable sequence of elements.

Declaration: nums = [10, 20, 30]

$O(1)$ Operations: .append(val) (add to end), .pop() (remove from end), accessing elements by index (nums[0]).

$O(N)$ Operations: .insert(index, val) (forces shifting elements), .pop(0) or .pop(index) (forces shifting elements).

Slicing (list[start:stop:step]):

arr = [1, 2, 3, 4, 5]
sub = arr[1:4]   # Returns [2, 3, 4] (indexes 1, 2, 3)
rev = arr[::-1]  # Inverts the list, returning [5, 4, 3, 2, 1] in O(N)


2. Dictionaries (Hash Maps)

An unordered collection of key-value pairs. Keys must be unique and immutable (integers, strings, tuples).

Declaration: freq = {"token": 4, "id": 109}

Operations:

Updating/Writing: freq["token"] = 5

Safe Querying: If a key is missing, querying directly with freq["missing"] throws a KeyError. Use .get(key, default) to safely fallback:

count = freq.get("missing", 0) # Returns 0 instead of crashing


Membership Testing: if "token" in freq: runs in average-case $O(1)$ time.

3. Sets (Hash Sets)

An unordered collection of unique elements, highly optimized for membership testing.

Declaration: visited = set()

Operations: visited.add(101). Checking 101 in visited is average-case $O(1)$ complexity (compared to $O(N)$ for a standard list).

4. Tuples

An immutable sequence of elements.

Coordinate Packing: Tuples like (row, col) are commonly used as keys in sets or dicts to track traversed grid coordinates because, unlike lists, tuples are hashable.

Variable Unpacking:

left, right = 0, 10 # Unpack values in one line
left, right = right, left # Swap variables in-place without temporary variables


🌳 Module 4: Object-Oriented Programming & Reference Semantics

Object-Oriented Programming (OOP) allows you to define custom data types. In interviews, custom nodes representing elements in trees or lists are built using OOP.

1. Classes, Attributes, and Methods

A class is a blueprint, and an object is an active instance of that blueprint.

Methods: Functions defined inside a class that operate on an instance.

The self Parameter: Represents the active instance itself. Used to access and modify the instance's unique attributes.

class MLModel:
    def __init__(self, name):
        self.name = name # Attribute unique to each instance
        
    def describe(self):
        # A class method accessing instance attributes
        return f"This is a {self.name} model."


2. The Constructor (__init__)

The __init__ method is the constructor. It runs automatically when you instantiate an object.

# Instantiating objects
model_a = MLModel("Transformer")
model_b = MLModel("Linear Regression")

print(model_a.describe()) # "This is a Transformer model."


3. Understanding Reference Semantics (Pointers)

This is a critical area where many engineers fail. In Python, assigning an object to a new variable does not copy its data. It copies the memory pointer (reference).

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Create node 1
node1 = Node(10)
# Reference copy
node2 = node1 

node2.val = 99 # Modifying node2 modifies node1 because they point to the same memory!
print(node1.val) # Prints 99


4. Custom Node Blueprints (Mandatory for Google Interviews)

You must be able to write these custom node templates quickly from scratch:

Tree Node Template:

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


Trie (Prefix Tree) Node Template:

class TrieNode:
    def __init__(self):
        self.children = {} # Maps characters to child TrieNodes
        self.is_end_of_word = False


🧠 Module 5: CPython Under the Hood & Memory Models

Now we bridge basic syntax to how the Python interpreter (CPython) physically processes memory.

1. Variables as Pointer Labels

Variables are simply reference labels pointing to memory locations on the heap.

id(obj): Retrieves the actual physical memory address of an object.

is vs ==: == checks if values are equal. is checks if the physical memory addresses are identical (id(a) == id(b)).

2. Mutability vs Immutability

Immutable Types: int, float, str, tuple, frozenset. Modifications create a new object in memory.

Mutable Types: list, dict, set. Modifications occur in-place.

DSA Impact: Strings are immutable. Concatenating strings in a loop (s += char) runs in $O(N^2)$ time because Python copies the string in memory on every iteration. You must collect characters in a mutable list and join them at the end: ''.join(chars) which runs in $O(N)$ time.

3. Shallow vs Deep Copying

Shallow Copy (list.copy() or path[:]): Copies the outer container, but elements inside still point to their original memory references.

Deep Copy (copy.deepcopy()): Clones the entire nested hierarchy recursively.

DSA Impact: When saving a path state in backtracking:

results.append(path[:]) # Correct: Saves a snapshot of the current list
results.append(path)    # Incorrect: Saves a pointer. results will update dynamically as path changes.


⚡ Module 6: Collection Complexities & CPython Nuances

To guarantee $O(1)$ operations during live whiteboard rounds, you must know exactly when Python collections fall back to linear $O(N)$ sweeps under the hood.

1. Lists (Dynamic Arrays) Under the Hood

The Architecture: CPython implements lists as contiguous arrays of object references.

$O(1)$ Operations: .append(), .pop() (from the end), and indexing (arr[i]).

$O(N)$ Operations: .insert(0, val) (shifting all elements), .pop(0) (shifting all elements), .remove(val), and val in arr (linear scan).

DSA Impact: Never use a Python list as a Queue. Adding or removing elements from the left of a list is an $O(N)$ operation and will ruin your BFS (Breadth-First Search) complexity.

2. Dictionaries & Sets Under the Hood

The Architecture: Both collections utilize a sparse array of hash buckets to achieve $O(1)$ average-case insertion, retrieval, and deletion.

Key Methods:

dict.setdefault(key, default): Retrieve value if key is in dict; otherwise, write and return the default.

DSA Impact: Ensure your custom classes used as dict keys implement __hash__ and __eq__ so the interpreter can index them correctly.

⚡ Module 7: The Google-Critical Standard Libraries

Google coding rounds do not allow external libraries (no NumPy/Pandas). You must utilize high-performance, pre-compiled C-extensions built directly into Python's standard library.

1. collections.deque (Doubly-Ended Queue)

Why use it: Standard Python lists are slow ($O(N)$) when popping or inserting from index 0. deque executes these operations in $O(1)$ time.

Google Usage: Mandatory for BFS Traversal, Sliding Windows, and Monotonic Queues.

from collections import deque
queue = deque()
queue.append(10)      # Push right in O(1)
first = queue.popleft() # Pop left in O(1)


2. heapq (Binary Heaps)

Why use it: Dynamically keeps collections sorted, allowing you to push and pop elements in $O(\log N)$ time.

Google Usage: Essential for Top K Elements, Two Heaps, and K-Way Merges.

The Max-Heap Negation Trick: Python’s heapq is strictly a min-heap. To implement a max-heap, multiply values by -1 before pushing them, and negate them again upon popping:

import heapq
max_heap = []
heapq.heappush(max_heap, -value) # Negate value to reverse priority
largest = -heapq.heappop(max_heap) # Negate again upon popping


3. bisect (Built-in Binary Search)

Why use it: Bypasses having to write raw binary search loops from scratch, preventing off-by-one errors.

Key Functions:

bisect.bisect_left(arr, target): Finds the leftmost index where target can be inserted to keep arr sorted.

bisect.bisect_right(arr, target): Finds the rightmost index.

4. collections.defaultdict & collections.Counter

defaultdict: Automatically initializes missing keys, eliminating nested if key not in dict checks when building graph adjacency maps:

from collections import defaultdict
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v) # Automatically creates an empty list if key is missing


Counter: Easily counts element frequencies in $O(N)$ time.

🔁 Module 8: Recursion Call Stack Limits & Caching

Most advanced DP, tree, and graph algorithms are solved recursively.

1. Base Cases

Every recursive function must have an explicit base case boundary check to stop execution and prevent a RecursionError (Stack Overflow).

2. Overriding the Call Stack Limit

CPython caps maximum recursion depth at $1000$ calls. For large graph DFS runs on LeetCode Hard, you must manually expand recursion limits in your opening lines:

import sys
sys.setrecursionlimit(200000) # Safeguards deep graph DFS runs from crashing


3. Top-Down DP with @functools.lru_cache

Speeds up Top-Down Dynamic Programming by automatically caching recursive inputs:

from functools import lru_cache

@lru_cache(None) # Memoizes solved subproblems automatically
def solve_dp(index, state):
    if index == len(nums): return 0
    # ... transition calculations ...
    return result


🔢 Module 9: Bitwise State Optimizations

Useful for advanced DP state-space compressions (Bitmasking).

AND (&): Checks if specific bits are active (e.g., state & (1 << i)).

OR (|): Sets bits to active (e.g., state | (1 << i)).

XOR (^): Flips bit states.

Left-Shift (<<): Multiplies states by powers of two (e.g., 1 << N represents a complete bitmask set containing $2^N$ elements).
