import asyncio
import time


async def fetch_data(source: str, delay: float) -> str:
    """Simulates an I/O operation with asyncio.sleep"""
    print(f"  Fetching from {source}...")
    await asyncio.sleep(delay)  # Non-blocking sleep
    print(f"  Got data from {source}")
    return f"data_from_{source}"


async def demo():
    """Awaiting coroutines one by one runs them sequentially"""
    start = time.perf_counter()

    result1 = await fetch_data("database", 0.5)
    result2 = await fetch_data("api", 0.3)
    result3 = await fetch_data("cache", 0.1)

    elapsed = time.perf_counter() - start
    print(f"  Results: {result1}, {result2}, {result3}")
    print(f"  Sequential time: {elapsed:.2f}s (sum of all delays)")


if __name__ == "__main__":
    asyncio.run(demo())
