import asyncio


async def risky_operation(task_id: int):
    await asyncio.sleep(0.1)
    if task_id == 2:
        raise ValueError(f"Task {task_id} failed!")
    return f"task_{task_id}_ok"


async def demo():
    # gather with return_exceptions=True collects errors instead of raising
    results = await asyncio.gather(
        risky_operation(1),
        risky_operation(2),
        risky_operation(3),
        return_exceptions=True,
    )

    for i, result in enumerate(results, 1):
        if isinstance(result, Exception):
            print(f"  Task {i}: ERROR - {result}")
        else:
            print(f"  Task {i}: {result}")


if __name__ == "__main__":
    asyncio.run(demo())
