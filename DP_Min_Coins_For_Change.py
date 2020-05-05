#We know that if the amount is 0, there is no way we can make change, so in the array of minChange, initialise position 0 to be 0
#This is the base case. The rest of the elements can be initialised to max value so that we can do min() check for the initial iteration

def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    minCoins = [float("inf") for i in range(n + 1)]
    minCoins[0] = 0
    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                minCoins[amount] = min(minCoins[amount], minCoins[amount - denom] + 1)
    return -1 if minCoins[n] == float("inf") else minCoins[n]
