import asyncio

# Define an asynchronous generator that yields values after some delay
async def async_generator():
    for i in range(5):
        await asyncio.sleep(1)
        yield i
        
# Main async function to use async comprehension
async def main():
    # use an async comprehension to collect results
    results = [i async for i in async_generator()]
    print(results)
    
# Run the main function
asyncio.run(main())

# async_generator() - an asynchronous generator that yields a value every second
# async comprehension [i async for i in async_generator] - gathers all values produced by the generator into a list