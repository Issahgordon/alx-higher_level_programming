#!/usr/bin/python3
# 0-add.py

if __name__ == "__main__":
    """print the sum of 1 and 2."""
 #   from add_0 import add
    def add(a,b):
      y = int(a+b)
      return(y)
    a = 1
    b = 2
    print("{} + {} = {}".format(a,b, add(a,b)))
