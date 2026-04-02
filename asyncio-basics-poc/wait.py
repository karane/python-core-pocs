import asyncio


async def timed_task(task_id: int, duration: float):
    await asyncio.sleep(duration)
    return f"task_{task_id}"


async def demo():
    tasks = [
        asyncio.create_task(timed_task(1, 0.3), name="fast"),
        asyncio.create_task(timed_task(2, 0.6), name="medium"),
        asyncio.create_task(timed_task(3, 0.9), name="slow"),
    ]

    # FIRST_COMPLETED - returns as soon as any task finishes
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    print(f"  First completed: {[t.get_name() for t in done]}")
    print(f"  Still pending: {[t.get_name() for t in pending]}")

    # Wait for the rest
    done2, _ = await asyncio.wait(pending)
    print(f"  Remaining completed: {[t.get_name() for t in done2]}")


if __name__ == "__main__":
    asyncio.run(demo())
