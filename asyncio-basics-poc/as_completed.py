import asyncio


async def download(url: str, duration: float) -> str:
    await asyncio.sleep(duration)
    return f"content_from_{url}"


async def demo():
    tasks = [
        download("site-c.com", 0.5),
        download("site-a.com", 0.1),
        download("site-b.com", 0.3),
    ]

    print("  Results arrive in completion order:")
    for coro in asyncio.as_completed(tasks):
        result = await coro
        print(f"    Got: {result}")


if __name__ == "__main__":
    asyncio.run(demo())
