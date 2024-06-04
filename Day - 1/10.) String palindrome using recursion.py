def is_palindrome(s):
    s = s.lower()
    s = ''.join(e for e in s if e.isalnum())
    
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

input_string = "malayalam"
if is_palindrome(input_string):
    print(f"{input_string} is a palindrome.")
else:
    print(f"{input_string} is not a palindrome.")