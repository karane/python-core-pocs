import asyncio


async def say_hello(name: str) -> str:
    print(f"  Hello, {name}!")
    return f"Greeted {name}"


async def demo():
    result = await say_hello("Alice")
    print(f"  Return value: {result}")

    # A coroutine object is NOT the result - you must await it
    coro = say_hello("Bob")
    print(f"  Coroutine object (not awaited yet): {coro}")
    result = await coro
    print(f"  Now awaited: {result}")


if __name__ == "__main__":
    asyncio.run(demo())
