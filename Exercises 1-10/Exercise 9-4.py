fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)

lst = []
email_count = {}

for line in fh:
    if line.startswith('From '):
        email = line.split()[1]
        lst.append(email)
        
for email in lst:
    if email in email_count:
        email_count[email] += 1
    else:
        email_count[email] = 1

max_count = max(email_count.values())
max_emails = [email for email, count in email_count.items() if count == max_count]

print(max_emails)
print(', '.join(max_emails), max_count)