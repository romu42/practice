# https://codechalleng.es/bites/214/

def countdown():
    """Write a generator that counts from 100 to 1"""
    for num in range(100, 0, -1):
       yield(num)


