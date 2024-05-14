import threading
import time


def task1():
    """Simulates a slow task that prints numbers"""
    for i in range(5):
        print(f"Task 1: Printing number {i}")
        time.sleep(1)  # Simulate some processing time


def task2():
    """Simulates a quick task that prints a message"""
    for j in range(5, 10):
        print("Task 2: This is a quick message!")
        time.sleep(2)


# Create two threads with target functions
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish (optional)
thread1.join()
thread2.join()

print("All tasks completed!")
