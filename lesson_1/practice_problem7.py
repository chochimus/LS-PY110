words = ['ant', 'bear', 'cat']
selected_words = []
for word in words:
    if len(word) > 3:
        selected_words.append(word)

print(selected_words)

# The following code should output a list with all the words from the words list that are
# are longer than 3 characters, bear in this case is the only one.