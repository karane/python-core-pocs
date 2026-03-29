import asyncio


async def slow_operation():
    await asyncio.sleep(5.0)
    return "completed"


async def demo():
    # asyncio.wait_for with timeout
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=0.5)
        print(f"  Result: {result}")
    except asyncio.TimeoutError:
        print("  wait_for: Operation timed out after 0.5s")

    # asyncio.timeout context manager (Python 3.11+)
    try:
        async with asyncio.timeout(0.3):
            await slow_operation()
    except asyncio.TimeoutError:
        print("  asyncio.timeout: Operation timed out after 0.3s")


if __name__ == "__main__":
    asyncio.run(demo())
