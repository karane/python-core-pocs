import asyncio
import time


async def fetch_data(source: str, delay: float) -> str:
    """Simulates an I/O operation with asyncio.sleep"""
    print(f"  Fetching from {source}...")
    await asyncio.sleep(delay)
    print(f"  Got data from {source}")
    return f"data_from_{source}"


async def demo():
    """gather() runs coroutines concurrently"""
    start = time.perf_counter()

    # All three run at the same time
    results = await asyncio.gather(
        fetch_data("database", 0.5),
        fetch_data("api", 0.3),
        fetch_data("cache", 0.1),
    )

    elapsed = time.perf_counter() - start
    print(f"  Results: {results}")
    print(f"  Concurrent time: {elapsed:.2f}s (only the longest delay)")


if __name__ == "__main__":
    asyncio.run(demo())
