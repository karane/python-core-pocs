import asyncio


async def background_work(task_id: int, duration: float):
    print(f"  Task {task_id}: started")
    await asyncio.sleep(duration)
    print(f"  Task {task_id}: completed")
    return f"result_{task_id}"


async def demo():
    # Tasks start running immediately when created
    task1 = asyncio.create_task(background_work(1, 0.3))
    task2 = asyncio.create_task(background_work(2, 0.2))
    task3 = asyncio.create_task(background_work(3, 0.1))

    print("  All tasks created, doing other work...")
    await asyncio.sleep(0.05)
    print("  Other work done, waiting for tasks...")

    # Await tasks to get results
    result1 = await task1
    result2 = await task2
    result3 = await task3
    print(f"  Results: {result1}, {result2}, {result3}")


if __name__ == "__main__":
    asyncio.run(demo())
