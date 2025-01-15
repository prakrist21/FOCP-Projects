'''
Write and test three functions that each take two words (strings) as parameters and return sorted lists (as defined above) representing respectively:
Letters that appear in at least one of the two words.
Letters that appear in both words.
Letters that appear in either word, but not in both.
Hint: These could all be done programmatically, but consider carefully what topic we have been discussing this week! Each function can be exactly one line.
'''
def union(word1,word2):
    # This function prints the letters that appear in at least one of the two words.
    lst=list(set(word1).union(set(word2)))
    print("The letters that appear in at least one of the two words are: ",sorted(lst))

def intersection(word1,word2):
    # This function prints the letters that appear in both words.
    lst=list(set(word1).intersection(set(word2)))
    print("The letters that appear in both words are: ",sorted(lst))

def symmetric_difference(word1,word2):
    # This function prints the letters that appear in either word, but not in both
    lst=list(set(word1).symmetric_difference(set(word2)))
    print("The letters that appear in in either word, but not in both are: ",sorted(lst))

union('apple','ball')
intersection('apple','ball')
symmetric_difference('apple','ball')