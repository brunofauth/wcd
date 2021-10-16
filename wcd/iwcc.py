import asyncio as aio
import sys

from .event import ConnectionMode


async def print_recvd_msgs(r: aio.StreamReader) -> None:
    while (line := await r.readline()):
        sys.stdout.write(line.decode("utf-8"))


async def ainput(prompt: str) -> str:
    await aio.get_event_loop().run_in_executor(None, sys.stdout.write, prompt)
    return await aio.get_event_loop().run_in_executor(None, sys.stdin.readline)


async def main():
    r, w = await aio.open_unix_connection(sys.argv[1])
    aio.create_task(print_recvd_msgs(r))

    w.write(ConnectionMode.KEEP_CONNECTED.to_bytes(4, byteorder="big"))
    await w.drain()

    while (line := (await ainput("Send: ")).strip()) != "quit":
        if line.isdigit():
            w.write(int(line).to_bytes(4, "big"))
            await w.drain()


if __name__ == "__main__":
    print("THIS IS NOT SUPPOSED TO BE USED (its a dbg script)")
    aio.run(main())

