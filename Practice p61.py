# -*- coding: utf-8 -*-

string_words = """India have faced defeat in last ODI world cup. It was an excellent campaign for team India. A dream world cup campaign for any team
              yet getting the medal of runner up despite of such incredible efforts, management, performances and dominance. One to remember."""

word_lit = string_words.split()

# Create a list of word frequencies using list comprehension.
word_freq = [word_lit.count(n) for n in word_lit]

# Print the original string, the list of words, and pairs of words along with their frequencies.
print("String:\n {} \n".format(string_words))
print("List:\n {} \n".format(str(word_lit)))
print("Pairs (Words and Frequencies:\n {}".format(str(list(zip(word_lit, word_freq)))))

