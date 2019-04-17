def is_even(x):
    return x & 1 == 0


if __name__ == '__main__':
    assert is_even(0)
    assert is_even(4)
    assert is_even(-20)
    assert not is_even(1)
    assert not is_even(-5)
    assert not is_even(-99)

"""
Explanation: This is actually not in the book but I wanted to do this anyway. How can we quickly determine if a number 
is even without using the modulo operator (%)? Simple we just use the bit-wise operator AND (&) and check it with 1. 
What do all odd numbers have in common in binary? They all end in 1: 

1: 01
3: 11
7: 111
11: 1011
etc. 

Thus by checking if x & 1 == 0 we can determine if the number is even or odd. If the number is even, then it will have
a 0 at its least significant bit; on the other hand, if the number is odd, then it will have a 1 at its least 
significant bit. More importantly 0 & 1 = 0 (even) while 1 & 1 = 1 (odd) allowing us to distinguish between the two. 
"""
