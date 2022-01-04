index = -1
reversed_string = []
def split(word):
    return [char for char in word]
word = input('Enter anything(a word): ')
split_word = split(word)
for item in split_word:
    reversed_string.append(split_word[index])
    index=index-1
print(word)
reversed_word = ''
print(reversed_word.join(reversed_string))