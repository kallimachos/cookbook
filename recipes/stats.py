#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Print system stats."""

import platform
import psutil
from psutil._common import bytes2human


def print_stats(stats):
    """Print system stats."""
    print()
    for key, value in stats.items():
        print(f"{key}: {value}")
    return


def system_stats():
    """Get stats."""
    while True:
        stats = {}
        stats["IP"] = psutil.net_if_addrs()["en0"][0].address
        stats["CPU"] = psutil.cpu_percent(interval=1.0)
        mem = psutil.virtual_memory()
        stats["Mem used"] = f"{bytes2human(mem.used)}/{bytes2human(mem.total)} - {mem.percent}%"
        disk = psutil.disk_usage("/")
        stats["Disk used"] = f"{bytes2human(disk.used)}/{bytes2human(disk.total)} - {disk.percent}%"
        if hasattr(psutil, "sensors_temperatures"):
            stats["Temp"] = psutil.sensors_temperatures()
        if hasattr(psutil, "sensors_fans"):
            stats["Fans"] = psutil.sensors_fans()
        stats["Battery"] = f"{psutil.sensors_battery().percent}%"
        print_stats(stats)
    return


if __name__ == "__main__":
    system_stats()
