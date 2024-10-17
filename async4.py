import asyncio

""" filters out odd numbers and only collects even numbers into the list"""

# define an asynchronous generator
async def async_generator():
    for i in range(10):
        await asyncio.sleep(0.5)
        yield i
        
# main async function using async comprehension with filtering
async def main():
    # collect only even numbers from the asynchronous generator
    even_numbers = [i async for i in async_generator() if i % 2 == 0]
    print(even_numbers)
    
# run the main function
asyncio.run(main())