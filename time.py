import time

interval = 3
start_time = time.time()

while True:
    current_time = time.time()
    if current_time - start_time >= interval:
        print("yes")
        start_time = current_time