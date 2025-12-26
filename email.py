
import re

# Step 1: Open and read the input text file
with open("input.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Step 2: Define regex pattern for email addresses
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Step 3: Extract all email addresses
emails = re.findall(email_pattern, content)

# Step 4: Write extracted emails to output file
with open("emails.txt", "w", encoding="utf-8") as file:
    for email in emails:
        file.write(email + "\n")

# Step 5: Display result
print("Task completed successfully!")
print("Total email addresses found:", len(emails))
print("Extracted emails saved in emails.txt")
