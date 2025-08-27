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

while True:
    # Generate some requests
    for _ in range(5):
        time.sleep(1)
        generate_request()

    # Run requests processing
    process_request()
