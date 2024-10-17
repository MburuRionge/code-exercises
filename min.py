def min_operations(n, memo={}):
    if n == 1:
        return 0
    if n in memo:
        return memo[n]
    
    operations = 1 + min_operations(n - 1) # Subtract 1 operation
    
    if n % 2 == 0:
        operations = min(operations, 1 + min_operations(n // 2))
    if n % 3 == 0:
        operations = min(operations, 1 + min_operations(n // 3))
        
    memo[n] = operations
    return operations

n = 10
print(min_operations(n))