import asyncio

#Define an aynchronous function
async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("Punk!")

#Define another asychronous function that calls the first one
async def main():
    await say_hello()

# Run the asynchronous function
asyncio.run(main())