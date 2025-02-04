import asyncio

from .bot import start


async def main() -> None:
    await start()


if __name__ == "__main__":
    asyncio.run(main())
