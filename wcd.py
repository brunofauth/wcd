import asyncio as aio
import os

from pathlib import Path

from event import ConnectionMode, DaemonEvent, fire_event
from funcs import wp_cycler
from cfg import get_cfg, save_cfg


async def _read_int(r: aio.StreamReader) -> int:
    return int.from_bytes(await r.readexactly(4), byteorder="big")


async def _handle_client(r: aio.StreamReader, w: aio.StreamWriter) -> None:

    conn_mode = await _read_int(r)

    if conn_mode == ConnectionMode.ONE_SHOT:
        await fire_event(await _read_int(r), r, w)
        return

    if conn_mode == ConnectionMode.KEEP_CONNECTED:
        # If the client disconnects, this errors out and quits.
        while True: 
            # No need to await here, we can listen for commands
            # while these event handlers are running as bg tasks
            fire_event(await _read_int(r), r, w)


async def on_client_connected(r: aio.StreamReader, w: aio.StreamWriter) -> None:
    print("Client connected.")

    try:
        await _handle_client(r, w)
    except (aio.IncompleteReadError, IndexError):
        pass

    w.close()
    await w.wait_closed()
    print("Client disconnected.")


async def main():

    if "TMPDIR" not in os.environ:
        os.environ["TMPDIR"] = "/tmp"

    path = Path(os.path.expandvars(get_cfg()["socket_path"]))
    os.makedirs(path.parent, exist_ok=True)

    server = await aio.start_unix_server(on_client_connected, path=path)
    aio.create_task(wp_cycler())

    async with server:
        await server.serve_forever()



if __name__ == "__main__":
    aio.run(main())

