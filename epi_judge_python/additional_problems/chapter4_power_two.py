def power_two(x):
    if x < 1:
        return False
    else:
        return x & (x - 1) == 0


if __name__ == '__main__':
    assert power_two(1)
    assert power_two(2)
    assert power_two(16777216)
    assert not power_two(0)
    assert not power_two(3)
    assert not power_two(17)

"""
Explanation: What is a power of two in binary? A power of two in binary consists of one 1 in the entire binary 
representation of the number. You can see that here by looking at a few examples: 

1: 01
2: 10
4: 100
8: 1000
etc. 

As a result, we can detect a power of two by determining that there is a single 1 in the entire number. How do we do 
that in O(1) time. Well as the book states, you can remove the lowest set bit (e.g lowest 1) by using `x & (x - 1)`. 
What happens if we try doing that with a power of two? Well since there is only one 1, doing so should result in zero!
Hence we can simply use the check `x & (x - 1) == 0` to determine if a number is a power of two. 
"""
