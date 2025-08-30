from collections import deque

import time

# Check if string is palindrome
def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())

    d = deque(cleaned)
    # Check if the cleaned string is a palindrome
    while len(d) > 1:
        if d.popleft() != d.pop():
            print(f"'{s}' is not a palindrome.")
            return
    
    print(f"'{s}' is a palindrome.")

strings = [
    "madam",
    "racecar",
    "hello",
    "world",
    "level",
    "notapalindrome",
    "openai",
    "python",
    "rotor",
    "civic"
]

for s in strings:
    time.sleep(1)
    is_palindrome(s)