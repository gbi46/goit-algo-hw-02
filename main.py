from collections import deque
from queue import Queue

import hashlib
import time

# Initialize a queue
q = Queue()

# Requests counter
request_counter = 0

# Generate request
def generate_request():
    global request_counter
    request_counter += 1
    request = {
        "uuid": hashlib.sha256(f"Request {request_counter}".encode()).hexdigest(),
        "data": f"Request data {request_counter}"
    }
    q.put(request)
    print(f"Generated request {request_counter}: {request}")

# Process the requests
def process_request():
    if not q.empty():
        while not q.empty():
            request = q.get()
            print(f"Processing {request['uuid']}: {request['data']}")
            time.sleep(1)   
    else:
        print("No requests to process.")

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

def main():
    all_strings_tested = False
    while True:
        # Test strings for palindrome
        if not all_strings_tested:
            for s in strings:
                time.sleep(1)
                is_palindrome(s)
        all_strings_tested = True
        # Generate some requests
        for _ in range(5):
            time.sleep(1)
            generate_request()

        # Run requests processing
        process_request()

if __name__ == "__main__":
    main()
