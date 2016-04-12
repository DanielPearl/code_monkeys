# Your company delivers breakfast via autonomous quadcopter drones. And something mysterious has happened.
# Each breakfast delivery is assigned a unique ID, a positive integer. When one of the company's 100 drones takes off with a delivery, the delivery's ID is added to a list, delivery_id_confirmations. When the drone comes back and lands, the ID is again added to the same list.
#
# After breakfast this morning there were only 99 drones on the tarmac. One of the drones never made it back from a delivery. We suspect a secret agent from Amazon placed an order and stole one of our patented drones. To track them down, we need to find their delivery ID.
#
# Given the list of IDs, which contains many duplicate integers and one unique integer, find the unique integer.
#
# The IDs are not guaranteed to be sorted or sequential. Orders aren't always fulfilled in the order they were received, and some deliveries get cancelled before takeoff.

import random


def drone_id():
    """
    Returns unique integers given txt file of duplicate integers
    :return: int
    """
    unique_ids = {}
    drone_ids = open("droneIDs.txt", "r").read()

    drone_list = drone_ids.split()
    for i in drone_list:
        if i not in unique_ids:
            unique_ids[i] = None
        else:
            del unique_ids[i]
    for key in unique_ids:
        return key

print(drone_id())
