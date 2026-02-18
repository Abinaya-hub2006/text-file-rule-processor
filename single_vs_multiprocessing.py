"""
Single Processing vs Multiprocessing in Python
Author: Abinaya
"""

import time
from multiprocessing import Process


# ------------------------------
# Example Task Function
# ------------------------------
def task(name):
    print(f"Task {name} starting...")
    time.sleep(2)
    print(f"Task {name} finished.")


# ------------------------------
# Single Processing Example
# ------------------------------
def single_processing():
    print("\n--- Single Processing ---")
    start = time.time()

    task("A")
    task("B")

    end = time.time()
    print(f"Time Taken (Single Processing): {end - start:.2f} seconds")


# ------------------------------
# Multiprocessing Example
# ------------------------------
def multi_processing():
    print("\n--- Multiprocessing ---")
    start = time.time()

    p1 = Process(target=task, args=("A",))
    p2 = Process(target=task, args=("B",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()
    print(f"Time Taken (Multiprocessing): {end - start:.2f} seconds")


# ------------------------------
# Main
# ------------------------------
if __name__ == "__main__":
    single_processing()
    multi_processing()
