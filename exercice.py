#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

def square_root(number: int) -> float:
    square_rooted = math.sqrt(float(number))
    return square_rooted


def square(number: int) -> int:
    squared = number
    return squared


def main() -> None:
    for i in range(25):
        print(f"Square root: {square_root(i)}, square: {square(i)}")


if __name__ == '__main__':
    main()
