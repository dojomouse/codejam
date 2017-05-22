def solve (p, K):
  flipper = K**2 - 1
  flips = 0

  while p >= flipper:
    if p % 2 == 0:
      p //=2
    else:
      p ^= flipper
  
  return "Impossible" if p else flips

import fileinput
f = fileinput.input()

T = int(f.readline())
for case in range(1, T+1):
    S, K = f.readline().split()
    K = int(K)
    n = len(S)
    p = int(S.replace('+', '0').replace('-', '1'), 2)
    solution = solve(p, K)
    print "Case #{0}: {1}".format(case, solution)