#!/usr/bin/python3


def best_score(a_dictionary: dict) -> str:
    
    return (

        sorted(a_dictionary.items(), key=lambda *items: items[0][1])[-1][0]
         if a_dictionary is not None and len(a_dictionary) >= 1
                else None
    )
