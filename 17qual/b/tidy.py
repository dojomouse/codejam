def isDirty(N):
  N = list(N)
  for i in range(0, len(N)-1):
    if N[i] > N[i+1]:
      return True
  return False

def solve(N):
    N = list(N)[:-1]
    while isDirty(''.join(N)):
      for i in range(1,len(N)):
        if N[i] < N[i-1]:
          N[i-1] = str(int(N[i-1])-1)
          for j in range(i, len(N)):
            N[j] = str(9)
    return str(int(''.join(N)))

import fileinput
f = fileinput.input()

T = int(f.readline())
for case in range(1, T+1):
    N = f.readline()
    solution = solve(str(N))
    print(f"Case #{case}: {solution}")