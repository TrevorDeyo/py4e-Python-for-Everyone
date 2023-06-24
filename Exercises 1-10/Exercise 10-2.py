# Prompt user for file name. If none is entered, use default file name "mbox-short.txt"
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

# Open the file
handle = open(name)

# Initialize an empty dictionary to count the number of occurrences of each hour
counts = dict()

# Loop through each line in the file
for line in handle:
    # Skip lines that don't start with 'From '
    if not line.startswith('From '): continue

    # Extract the hour from the timestamp on the line
    time = line.split()[5]
    hour = time.split(':')[0]

    # Increment the count for this hour in the dictionary
    counts[hour] = counts.get(hour, 0) + 1

# Sort the dictionary by keys
sorted_counts = dict(sorted(counts.items()))

# Loop through the sorted dictionary and print the counts for each hour
for (k,v) in sorted_counts.items():
    print(k, v)