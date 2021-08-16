"""Brief concept of strategy pattern without using complicated classes for easier digestion"""

import random
from typing import List


def reverse_strategy(input_: List[int]) -> List[int]:
    input_.reverse()
    return input_


def random_strategy(input_: List[int]) -> List[int]:
    random.shuffle(input_)
    return input_


def add_one_to_each(input_: List[int]) -> List[int]:
    return [item + 1 for item in input_]


def get_output(list_: List[int], strategy) -> List[int]:
    return strategy(input_=list_)


if __name__ == '__main__':
    prompt = input("Please choose available strategy: reverse, random, add_one:\n")
    strategies = {"reverse": reverse_strategy, "random": random_strategy, "add_one": add_one_to_each}
    print(f"{get_output(list_=[1,2,3,4,5,6,7,8,9], strategy=strategies[prompt])}")
