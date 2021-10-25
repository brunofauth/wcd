import tracemalloc


_snapshots = []
tracemalloc.start()


def take_snapshot():
    _snapshots.append(tracemalloc.take_snapshot())


# https://docs.python.org/3/library/tracemalloc.html#display-the-top-10
def print_snapshots():
    for snapshot in _snapshots:
        for stat in snapshot.statistics("lineno")[:10]:
            print(stat)
        print()

