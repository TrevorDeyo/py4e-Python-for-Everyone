# Prompt user for file name, use default if none given
fname = input("Enter file name: ")
if len(fname) < 1: fname = "mbox-short.txt"

# Open the file for reading
fh = open(fname)

# Create an empty dictionary to hold email counts
counts = dict()

# Loop through each line in the file
for line in fh:
    # Check if line starts with "From "
    if not line.startswith('From '): continue
    
    # Split line into words
    words = line.split()
    
    # Get email address from second word
    email = words[1]
    
    # Increment count for this email address in dictionary
    counts[email] = counts.get(email, 0) + 1

# Close the file
fh.close()

# Initialize variables to hold most prolific sender's email and count
maxcount = None
maxemail = None

# Loop through each email address in the dictionary
for email, count in counts.items():
    # Check if this count is the highest so far
    if maxcount is None or count > maxcount:
        # If so, update the max email and count
        maxemail = email
        maxcount = count

# Print out the email address and count for the most prolific sender
print(maxemail, maxcount)