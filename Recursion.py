import time


# Function to simulate connecting to the internet
def connect_to_internet(signal: bool, delay: int) -> None:
    # Base case: If delay is greater than 5, assume connection is successful
    if delay > 5:
        signal = True

    # If signal is True, connection is successful
    if signal:
        print("Connected !!!!")
    else:
        # If signal is False, attempt to retry after a delay
        print(f"Connection Failed ... trying again in {delay}s.....")
        time.sleep(delay)  # Wait for the specified delay
        connect_to_internet(signal, delay + 2)  # Recursive call with incremented delay


# Initial call to the function
connect_to_internet(False, 0)

def factorial(n: int) -> int:
    # Base case: factorial of 0 or 1 is 1
    if n <= 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)

# Example usage
print(factorial(5))  # Output: 120
