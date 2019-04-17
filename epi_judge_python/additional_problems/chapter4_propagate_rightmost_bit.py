def propagate_rightmost_bit(x):
    num = x
    counter = 1

    while num:
        if num & 1 == 1:
            break
        else:
            x ^= counter
            counter <<= 1
            num >>= 1

    return x


def propagate_rightmost_bit_slightly_better(x):
    counter = 1

    if x > 0:
        while (x & counter) ^ counter != 0:
            x ^= counter
            counter <<= 1

    return x


def propagate_rightmost_bit_more_efficient(x):
    if x == 0:
        return 0
    else:
        return x | (x - 1)


def test_propagate_rightmost_bit_more_efficient(func):
    assert func(1) == 1
    assert func(0) == 0
    assert func(2) == 3
    assert func(8) == 15
    print(f'function |{func.__name__}| passed all tests!')


if __name__ == '__main__':

    test_propagate_rightmost_bit_more_efficient(propagate_rightmost_bit)
    test_propagate_rightmost_bit_more_efficient(propagate_rightmost_bit_slightly_better)
    test_propagate_rightmost_bit_more_efficient(propagate_rightmost_bit_more_efficient)

'''
Explanation. Since there are two solutions, let's take each one in turn, starting with the naive solution. 

The naive solution attempts to mimic what you actually might do when trying to calculate the problem by hand. 
Specifically starting from the right, check if the bit is 1. If it is, stop because you've found the rightmost 
bit. If it's not, change that bit to 1 and then move to the next (left) bit. Repeat this process until you find the
rightmost 1 bit. 

To achieve this we have to do several things. First we have to have a mechanism to propagate our bit to the left. We
achieve this with counter and counter <<= 1. Next we have to update our number to switch a 0 to a 1. The easiest way
to do this is to do x ^ (XOR) counter. Because counter has only one 1, and we are toggling 0 bits, the bit that counter 
is at will change from 0 to 1. Finally, we need to have a mechanism to know we've reached a 1. In the first 
implementation, I decided to create a second dummy variable called num that starts of as x and then slowly gets smaller
by shifting to the right num >>= 1. By doing this, we can check num with & 1 to see if we've reached a 1. If the result
is a 1, then we're all set. 

In other words, to solve this problem we have x, counter, and num. The reason this process is so convoluted, however, 
is because I couldn't think of a way to identify a specific bit at a location (e.g. third position). But this is silly
because doing that is easy: you just do x & (1 << bit_number), where the least significant bit is bit_number 0 or the
zeroth bit or the bit at position 0. 

Here's an example showing you this is correct. Say we want bit at position 2 of 13. Well 13 is represented as 1101 while 
1 << 2 is 0100. Doing 13 & (1 << 2) gives you: 

1101
0100 
----
0100 which is the bit at position 2 of 13. Why is this important? Because we can use it to simplify our naive solution!
Rather than having three variables, we can move counter to the left, extract the bit at that position and then XOR (^)
with counter. If it returns 0 we know that was a 1 and we are done. `propagate_rightmost_bit_slightly_better` shows
how to do just that

**A potential gotcha**: You might be tempted--as I was--to have the check be:

while (x & counter) ^ counter == 1:
    ...do stuff..
    
While this works in the first check, this fails in the subsequent ones. To see this see what happens when we try to 
propagate the rightmost bits for 8 (1000)

Pass 1: 
x: 1000
counter: 00001

x & counter
1000
0001
----
0000

(x & counter) ^ counter

0000
0001
----
0001

So far so good.

Pass 2: 
x: 1001
counter: 0010

x & counter
1000
0010
----
0000

(x & counter) ^ counter
0000
0010
----
0010 (OOPS!)

As you can see the new update is now 2 instead of 1. Thus, it is better to check that it is not 0 rather than checking
_for_ a specific value. 

One thing to note about this process: we have to check if x is less than 1 because, if we don't, we'll end up with an 
infinite loop as 0 & counter will always return 0 so (x & counter) ^ counter will always be nonzero! 

Both solutions are O(n) but can we do better than that? 

The answer is yes. To do this we need a bit of insight, specifically to remember what x - 1 does. What does x - 1 do? 
Well, as always, jot down some examples to get a feel: 

1 - 1 =  0  => 0001 - 0001 = 0000
2 - 1 =  1  => 0010 - 0001 = 0001
8 - 1 =  7  => 1000 - 0001 = 0111
12 - 1 = 11 => 1100 - 0001 = 1011
In other words, it takes the right most 1, converts it to zero and then switches everything to the right to 1's. This
is so close to the actual solution, except we want the right most 1 to STILL STAY a 1. How do we do that? Simple we just
OR (|) the original value with the value minus 1. To see why this is the case, let's divide x into three parts: 
everything to the left of the rightmost 1 bit, the rightmost 1 bit, and everything to the right of the rightmost 1 bit. 

In the case of everything to the left of the rightmost 1 bit, (x - 1) produces no changes in the value. As a result 
x | (x - 1) has no impact as a | a = a. In the case of everything to the right of the rightmost 1 bit, x only has zeros
(by problem definition) and (x - 1) has all 1's. As a result, x | (x - 1) will produce all 1's as 0 | 1 = 1, which is 
exactly what we want. Finally, what about the rightmost 1 bit itself. Well by definition the value of that bit in x is 
1. Additionally, as we have shown above, (x - 1) makes that bit into 0. Given that 0 | 1 = 1, the rightmost 1 bit 
in x while still remain a 1 after doing x | (x - 1). Therefore this solves the problem! 

Like the previous answer, however, we have to check for x == 0 because x | ( x - 1) produces -1 (all 1's) which is not
what we want. This solution is O(1).

Source: https://catonmat.net/low-level-bit-hacks (BitHack #8)
'''