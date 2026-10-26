import time

class TimerContext:
    def __init__(self, description: str):
        self.description = description

    def __enter__(self):
        print(f"[Setup] Starting timer for: {self.description}")
        self.start_time = time.time()
        return self  # Becomes the 'as' variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        elapsed = self.end_time - self.start_time
        print(f"[Teardown] Finished in {elapsed:.4f} seconds.")
        
        if exc_type:
            print(f"[Alert] An error occurred: {exc_val}")
            # Return True to swallow the error, or False to let it raise
            return False 

# Usage
with TimerContext("Database Query Simulation") as timer:
    print("Executing block tasks...")
    time.sleep(0.5)
