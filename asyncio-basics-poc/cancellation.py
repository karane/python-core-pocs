import asyncio


async def long_running_task():
    try:
        print("  Long task: started")
        await asyncio.sleep(10.0)
        print("  Long task: completed")
    except asyncio.CancelledError:
        print("  Long task: was cancelled, cleaning up...")
        raise  # Re-raise to propagate cancellation


async def demo():
    task = asyncio.create_task(long_running_task())

    await asyncio.sleep(0.2)
    print(f"  Task done? {task.done()}")

    # Cancel the task
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print(f"  Task cancelled? {task.cancelled()}")


if __name__ == "__main__":
    asyncio.run(demo())
