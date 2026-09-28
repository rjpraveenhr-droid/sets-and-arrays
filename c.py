# Create snack boxes using sets
box1 = {"Chips", "Juice", "Biscuits", "Chocolate"}
box2 = {"Juice", "Biscuits", "Cake", "Candy"}

print("Box 1:", box1)
print("Box 2:", box2)

# Add a new snack
box1.add("Popcorn")
print("Box 1 after adding Popcorn:", box1)

# Find shared snacks
shared_snacks = box1.intersection(box2)
print("Shared snacks:", shared_snacks)

# Create an array (list) of snack counts
snack_counts = [10, 15, 20, 15, 10]

# Add values to the array
snack_counts.append(25)
snack_counts.append(15)

print("Snack counts:", snack_counts)

# Count how many times 15 appears
print("Number of times 15 appears:", snack_counts.count(15))

# Reverse the array
snack_counts.reverse()

print("Reversed snack counts:", snack_counts)
print("Total number of snacks:", len(snack_counts))