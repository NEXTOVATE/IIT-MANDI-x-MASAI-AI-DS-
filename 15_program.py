# Q6 (3 Marks): Write Python code to count the frequency of each word in a sentence using a dictionary.
sentence = input("Enter a sentence: ")
word_list = sentence.split()
word_frequency = {}
for word in word_list:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1
print("Word Frequency:")
for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")

    