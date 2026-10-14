sentence = input("Enter a long sentence: ")

sentence = sentence.replace(" ", "")
unique_characters = set(sentence)

print("Unique Characters:", unique_characters)
print("Total Unique Characters:", len(unique_characters))