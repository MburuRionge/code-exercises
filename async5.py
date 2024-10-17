import asyncio
import random

"""
using async comprehensions to process data received from
an async function that simulates fetching data asynchronously
"""

# Simulate an async function that fetches data
async def fetch_data():
    await asyncio.sleep(random.uniform(0.1, 1)) # simulate a network delay
    return random.randint(1, 100)

# define an async generator that calls fetch_data
async def data_stream():
    for _ in range(5):
        data = await fetch_data()
        yield data
        
# main async function that uses async comprehension
async def main():
    # Collect data using async comprehension
    fetched_data = [data async for data in data_stream()]
    print(f"Fetched Data: {fetched_data}")
    
# Run the main function
asyncio.run(main())

# fetch_data() - simulates asynchronous I/O, fetching a random number after a delay.
# data_stream() is an async generator that calls fetch data() and yiels its result
# [data async for data in data_stream()] - collects all fetched dta into a list.

# KEY POINTS
# - Async comprehensions allows me to collect result from asynchronous iterators e.g async generators

# very useful for I/O operations like reading from a file or making HTTPS requests

# they can be used with filtering conditions just like regular comprehensions