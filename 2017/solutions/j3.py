def exactly_electrical(a, b, c, d, t):
    # get absolute differences
    # negatives dont matter because it's a grid
    x = abs(c-a)
    y = abs(d-b)
    # total difference
    distance = x+y

    if (distance > t): # not enough energy to reach
        return 'N'

    # both must match (odd or even)
    # ie:
    # if we need to move 3 steps, with 5 energy
    # we can backtrack, but with 4 we cannot
    if ((distance % 2 != 0 and t % 2 != 0) or (distance % 2 == 0 and t % 2 == 0)):
        return 'Y'
    # probably can be done better with
    # bitwise-operators but overkill for this level

    return 'N'

a, b = [int(i) for i in input().split(' ')]
c, d = [int(i) for i in input().split(' ')]
t = int(input())
print(exactly_electrical(a, b, c, d, t))