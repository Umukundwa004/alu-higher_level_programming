#!/usr/bin/python3


def element_at(my_list: list, idx: int) -> int:
    
    if 0 > idx >= len(my_list):
        return None

    for i, data in enumerate(my_list):
        if i == idx:
            return data

    return None  # element not found
