import asyncio


async def worker(name: str):
    current_task = asyncio.current_task()
    print(f"  Running task: {current_task.get_name()}")
    await asyncio.sleep(0.1)
    return f"{name} done"


async def demo():
    task1 = asyncio.create_task(worker("A"), name="worker-A")
    task2 = asyncio.create_task(worker("B"), name="worker-B")

    all_tasks = asyncio.all_tasks()
    print(f"  All active tasks: {len(all_tasks)}")
    for t in sorted(all_tasks, key=lambda x: x.get_name()):
        print(f"    - {t.get_name()} (done={t.done()})")

    await asyncio.gather(task1, task2)


if __name__ == "__main__":
    asyncio.run(demo())
