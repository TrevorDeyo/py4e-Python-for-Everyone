# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
count2 = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    number_str = line[19:].strip()
    number = float(number_str)
    count2 = count2 + number
avg = count2 / count
print("Average spam confidence:", avg)