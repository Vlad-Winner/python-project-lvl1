#!/usr/bin/env python
from brain_games.games import brain_gcd as gcd
from brain_games import engine


def main():
    engine.run(gcd)


if __name__ == '__main__':
    main()
