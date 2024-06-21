from collections import defaultdict

def is_edit_distance_one(word1, word2):
    if len(word1) != len(word2):
        return False
    count_diff = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count_diff += 1
            if count_diff > 1:
                return False
    return count_diff == 1

def is_edit_distance_two(word1, word2):
    if len(word1) != len(word2):
        return False
    count_diff = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count_diff += 1
            if count_diff > 2:
                return False
    return count_diff == 2

def find_matching_words(queries, dictionary):
    word_dict = defaultdict(list)
    for word in dictionary:
        word_dict[len(word)].append(word)
    
    result = []
    for query in queries:
        if query in dictionary:
            result.append(query)
        else:
            for word_length in word_dict:
                if len(query) - 2 <= word_length <= len(query) + 2:
                    for word in word_dict[word_length]:
                        if is_edit_distance_one(query, word) or is_edit_distance_two(query, word):
                            result.append(query)
                            break
    return result

# Example 1
queries = ["word", "note", "ants", "wood"]
dictionary = ["wood", "joke", "moat"]
output1 = find_matching_words(queries, dictionary)
print(output1)

# Example 2
queries = ["yes"]
dictionary = ["not"]
output2 = find_matching_words(queries, dictionary)
print(output2)
