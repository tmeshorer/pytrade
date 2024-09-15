# Dyanamic programming overview

## Optimial substructure
- Sove a probelm based on a solution to sub problem.
- Easily solved recursivly
```yaml
fib(5) = fib(4) + fib(3)
```

## Overlapping subproblem
- When you split your problem to subproblem, get the same subproblem multiple times
- Save solution of subproblem in memory.

## Memoization
- Write a function that remembers the results of pervious computations.
- Use HashMap to store the result

## Top Down
- Start with the final result and recursivly break it into sub problem.
- First find top down and than convert it to buttom up.

## FAST
- First solution
  - First possible solution
  - Recursive call must be self contained
  - Solution must compute the result for each sub problem and combine them
  - Do not pass unnecceray variable.
- Analyze the solution
  - Does it have optimal substructure
  - Are the subproblem overlapping
- Identify the sub problem
  - Make the solution dynamic by caching the problem
- Turn the solution around
    - Make the top downsolution buttom up.

# Fib
## First solution
```yaml
fib(n) = fib(n-1) + fib(n-2)
```
## Analyze
- optimal substructure
- Overlapping subproblem
