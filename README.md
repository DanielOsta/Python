# Python


## Setup

VScode:
- autopep8 (formatting)

PyCharm:
- Community edition
- Keyboard shortcuts https://www.jetbrains.com/help/pycharm/mastering-keyboard-shortcuts.html

Python 3.10.6


### venv

```bash
# Create venv
python -m venv /path/to/new/virtual/environment

# Use / activate
source /path/to/new/virtual/environment

# install packages
pip install docker paramiko
```

## Bootcamp library
https://www.udemy.com/course/100-days-of-code/

Day 1: Just some basic knowledge

## Infos
- https://docs.python.org/3/library/functions.html


args are positional arguments
```python
def add(*args):
    print(args[0])
    sum = 0
    for n in args:
        sum += n
    return sum
```

kwargs are key word arguments
```python
def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n += kwargs["multiply"]
    print(n)
```

Download: https://replit.com/@appbrewery/day-27-end !
Tuples are immutable
Lists are mutable

Notes are in Obsidian!
