import asyncio

# Define an async function that simulates a task with a delay
async def task(name, delay):
    print(f"Task {name} starting...")
    await asyncio.sleep(delay)
    print(f"Task {name} is finished!")
    
# Define the main function that runs multiple tasks
async def main():
    # Schedule multiple tasks to run concurrently
    task1 = asyncio.create_task(task("A", 2))
    task2 = asyncio.create_task(task("B", 1))

    print("Both tasks started.")
    
    # Wait for both tasks to finidh
    await task1
    await task2

# run the main function  
asyncio.run(main())