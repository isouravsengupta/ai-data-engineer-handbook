from collections import deque

print("=== 1. INITIALIZATION & BOUNDED CAPACITY ===")
# Creating a bounded deque with a max size of 5
stream_queue = deque([10, 20, 30], maxlen=5)
print(f"Initial deque: {stream_queue}")
print(f"Maximum allowed size (.maxlen attribute): {stream_queue.maxlen}\n")


print("=== 2. RIGHT-SIDE OPERATIONS ===")
# .append(x) - Adds to the absolute end
stream_queue.append(40)
print(f"After .append(40): {stream_queue}")

# .extend(iterable) - Adds multiple items sequentially to the end
stream_queue.extend([50, 60])
print(f"After .extend([50, 60]): {stream_queue}")
print("⚠️ Notice that 10 was automatically evicted from the left because we hit maxlen=5!")

# .pop() - Removes and returns the rightmost item
popped_right = stream_queue.pop()
print(f"Popped item from right (.pop()): {popped_right}")
print(f"Deque after pop: {stream_queue}\n")


print("=== 3. LEFT-SIDE OPERATIONS (DEQUE SUPERPOWERS) ===")
# .appendleft(x) - Adds to the absolute front (Constant time O(1))
stream_queue.appendleft(99)
print(f"After .appendleft(99): {stream_queue}")

# .extendleft(iterable) - Adds multiple items to the front (Reverses order!)
stream_queue.extendleft([1, 2])
print(f"After .extendleft([1, 2]): {stream_queue}")

# .popleft() - Removes and returns the leftmost item (Crucial for FIFO/Queues)
popped_left = stream_queue.popleft()
print(f"Popped item from left (.popleft()): {popped_left}")
print(f"Deque after popleft: {stream_queue}\n")


print("=== 4. STRUCTURAL & POSITIONAL MODIFICATIONS ===")
# Resetting data to a clean, unbounded state for clear examples
d = deque([10, 20, 30, 40, 50])
print(f"Fresh deque for structural ops: {d}")

# .rotate(n) - Shifting elements like a cyclic conveyor belt
# Positive n shifts right
d.rotate(2)
print(f"After .rotate(2) [Shift Right]: {d}")

# Negative n shifts left
d.rotate(-1)
print(f"After .rotate(-1) [Shift Left]: {d}")

# .insert(idx, val) - Inserts at a specific index position (Linear time O(n))
d.insert(2, 999)
print(f"After .insert(2, 999): {d}")

# .remove(value) - Removes the first occurrence of a value
d.remove(999)
print(f"After .remove(999): {d}\n")


print("=== 5. INSPECTION & SEARCH METHODS ===")
# .count(x) - Count occurrences of a specific item
d.append(40)  # Let's add a duplicate 40
print(f"Current state: {d}")
print(f"Count of value 40 (.count(40)): {d.count(40)}")

# .index(x) - Find the first zero-based index of a specific value
print(f"First index of value 40 (.index(40)): {d.index(40)}")

# .reverse() - Reverses the underlying links in-place
d.reverse()
print(f"After .reverse(): {d}\n")


print("=== 6. CLEAN UP ===")
# .clear() - Flushes all nodes, resetting length to 0
d.clear()
print(f"After .clear(): {d}")
print(f"Final length: {len(d)}")