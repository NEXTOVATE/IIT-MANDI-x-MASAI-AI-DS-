# Given a long paragraph, manually
# compute (no regex) the most frequent two-word phrase. Ignore punctuation.
# Matching must be consecutive words. Input: "Data science is fun. Data science is
# powerful." Output: "data science".


text = input("Enter the paragrap :")

# Step 1: lowercase
text = text.lower()

# Step 2: remove punctuation (manual)
clean_text = ""
for ch in text:
    if ch.isalnum() or ch == " ":
        clean_text += ch

# Step 3: split into words
words = clean_text.split()

# Step 4: count consecutive two-word phrases
freq = {}

for i in range(len(words) - 1):
    phrase = words[i] + " " + words[i + 1]
    if phrase in freq:
        freq[phrase] += 1
    else:
        freq[phrase] = 1

# Step 5: find most frequent phrase
max_phrase = ""
max_count = 0

for phrase in freq:
    if freq[phrase] > max_count:
        max_count = freq[phrase]
        max_phrase = phrase

# Output
print(max_phrase) 
