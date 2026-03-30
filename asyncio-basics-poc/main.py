import asyncio
import importlib.util
from pathlib import Path


def load_demo(filename):
    path = Path(__file__).parent / filename
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.demo


DEMOS = [
    ("1. Basic Coroutine",          "basic_coroutine.py"),
    ("2. Sequential Execution",     "sequential_execution.py"),
    ("3. Gather Concurrent",     "gather_concurrent.py"),
    ("4. Create Task",     "create_task.py"),
    ("5. Task Naming",     "task_naming.py"),
    ("6. Timeouts",     "timeouts.py"),
    ("7. Error Handling",     "error_handling.py"),
]

async def main():
    for name, filename in DEMOS:
        print(f"\n{'=' * 50}\n{name}\n{'=' * 50}")
        await load_demo(filename)()

asyncio.run(main())
