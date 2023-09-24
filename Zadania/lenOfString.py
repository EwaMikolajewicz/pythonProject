def word_len(word):
    counter = 0
    for i in word:
        counter += 1
    return counter


word = "CodeBrainers"
print(f"{word} has {word_len(word)} letters.")
