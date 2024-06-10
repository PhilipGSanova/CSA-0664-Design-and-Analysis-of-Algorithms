def isMatch(s: str, p: str) -> bool:
    if not p:
        return not s

    first_match = bool(s) and p[0] in {s[0], '.'}

    if len(p) >= 2 and p[1] == '*':
        return (isMatch(s, p[2:]) or
                first_match and isMatch(s[1:], p))
    else:
        return first_match and isMatch(s[1:], p[1:])

if __name__ == "__main__":
    s1, p1 = "aa", "a"
    print(isMatch(s1, p1))

    s2, p2 = "aa", "a*"
    print(isMatch(s2, p2))

    s3, p3 = "ab", ".*"
    print(isMatch(s3, p3))
