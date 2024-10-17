def minOperations(n):
    if n < 2: #can't perform any operation to achieve 1 or 0
        return 0
    factor_list  = [] # used to store factors of n
    i = 1 # i will beused to check factors of n
    while n != 1: #the loop wi;; continue unti; n becomes 1
        i += 1 #increases each time i is a factor of n
        if n % i == 0: # if no remainder i is a factor of n
            while n % i == 0: # loop continues until n is no longer divisible by i
                n /= i # as long as i remains a factor of n it keeps on dividing
                factor_list.append(i) # each time n is divided by i, i is added to the factor_list
    return sum(factor_list) # program returns sum of  all factor_list

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))