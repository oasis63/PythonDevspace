from contextlib import contextmanager
import time

@contextmanager
def timer_context(description: str):
    # Setup phase
    print(f"[Setup] Starting timer for: {description}")
    start_time = time.time()
    
    try:
        yield  # The context pauses here while the 'with' block executes
    except Exception as e:
        print(f"[Alert] An error occurred: {e}")
        raise  # Re-raise the exception if you don't want to suppress it
    finally:
        # Cleanup phase (always runs)
        end_time = time.time()
        elapsed = end_time - start_time
        print(f"[Teardown] Finished in {elapsed:.4f} seconds.")

# Usage
with timer_context("API Call Simulation"):
    print("Executing block tasks...")
    time.sleep(0.5)





"""

with open("file.txt", encoding="utf-8") as file:
    content = file.read()


# here open is built-in context manager


"""