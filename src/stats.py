#!/usr/bin/env python3
"""Print system stats."""

import platform

import psutil
from psutil._common import bytes2human


def print_stats(stats) -> None:
    """Print system stats."""
    for _key, _value in stats.items():
        pass


def system_stats() -> None:
    """Get stats."""
    while True:
        stats = {}
        if platform.system() == "Darwin":
            stats["IP"] = psutil.net_if_addrs()["en0"][0].address
            stats["Battery"] = f"{psutil.sensors_battery().percent}%"
        else:
            stats["IP"] = psutil.net_if_addrs()["eth0"][0].address
            stats["Temp"] = f"{psutil.sensors_temperatures()['cpu-thermal'][0].current} C"
        stats["CPU"] = f"{psutil.cpu_percent(interval=1.0)}%"
        mem = psutil.virtual_memory()
        stats["Mem used"] = f"{bytes2human(mem.used)}/{bytes2human(mem.total)} - {mem.percent}%"
        disk = psutil.disk_usage("/")
        stats["Disk used"] = (
            f"{bytes2human(disk.used)}/{bytes2human(disk.total)} - {disk.percent}%"
        )
        print_stats(stats)


if __name__ == "__main__":
    system_stats()
