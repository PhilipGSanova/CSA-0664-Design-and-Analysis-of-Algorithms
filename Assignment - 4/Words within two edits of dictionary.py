def findMatchingWords(queries, dictionary):
    def isMatch(word1, word2):
        return sum(c1 != c2 for c1, c2 in zip(word1, word2)) <= 2

    return [query for query in queries if any(isMatch(query, word) for word in dictionary)]

# Example 1
queries1 = ["word", "note", "ants", "wood"]
dictionary1 = ["wood", "joke", "moat"]
output1 = findMatchingWords(queries1, dictionary1)
print(output1)  # Output: ["word", "note", "wood"]

# Example 2
queries2 = ["yes"]
dictionary2 = ["not"]
output2 = findMatchingWords(queries2, dictionary2)
print(output2)  # Output: []
