#create a ways array where we know that for n = 0, there is 1 way i.e by using no coins 
#and using this as a base for the amount n = denom, we can calculate the ways for the rest of the amounts


def waysToMakeChange(n, denoms):
    ways = [0 for i in range(n + 1)]
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
    return ways[n]
