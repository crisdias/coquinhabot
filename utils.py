import json
import os
from datetime import datetime, timedelta

def pp(data):
    print(json.dumps(data, indent=4))

def array_from_file(path):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    else:
        return []

def file_too_old(path, days=30):
    if not os.path.exists(path):
        return 1
    else:
        # Get the modification time of the file
        mod_time = os.path.getmtime(path)

        # Convert the modification time to a datetime object
        mod_time = datetime.fromtimestamp(mod_time)

        # Get the current time
        now = datetime.now()

        # Calculate the difference between the current time and the modification time
        time_diff = now - mod_time

        # Check if the difference is more than one month
        if time_diff > timedelta(days=days):
            return 1
        else:
            return 0

def reverse_name(name):
    parts = name.split(", ")
    return " ".join(parts[::-1])