def count_nr_of_signs(word):
    result = {}
    for i in range(len(word)):
        if word[i] not in result:
            result[word[i]] = 1
        elif word[i] in result:
            result[word[i]] += 1
    return result


w = "google.com"
print(count_nr_of_signs(w))
