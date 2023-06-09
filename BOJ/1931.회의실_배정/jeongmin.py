import sys
input = sys.stdin.readline

N = int(input())
time = sorted([tuple(map(int, input().split())) for _ in range(N)])
cnt = 0
available = 0

for start, end in time:
    if available <= start:
        cnt += 1
        available = end
    elif end < available:
        available = end

print(cnt)
