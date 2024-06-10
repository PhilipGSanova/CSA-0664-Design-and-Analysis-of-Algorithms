def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    strs.sort()
    prefix = ""
    
    for i in range(len(strs[0])):
        if strs[0][i] == strs[-1][i]:
            prefix += strs[0][i]
        else:
            break
    
    return prefix

strs1 = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs1)) 

strs2 = ["dog", "racecar", "car"]
print(longestCommonPrefix(strs2))  