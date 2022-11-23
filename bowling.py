 # N кеглей выставили в один ряд, занумеровав их слева направо числами от 1 до N. Затем по этому ряду бросили K шаров, при этом i-й шар сбил все кегли с номерами от li до ri включительно. Определите, какие кегли остались стоять на месте.
# Программа получает на вход количество кеглей N и количество бросков K. Далее идет K пар чисел li, ri, при этом 1≤ li≤ ri≤ N.

# Программа должна вывести последовательность из N символов, где j-й символ есть “I”, если j-я кегля осталась стоять, или “.”, если j-я кегля была сбита.



FirstArgs = input().split()
N = int(FirstArgs[0])
K = int(FirstArgs[1])
throws = []
counter = 0
args = []
while counter < K:
    args = [int(s) for s in input().split()]
    throws.append(args[0])
    throws.append(args[1])
    counter += 1

pins = ['I'] * N

for i in range(0, len(throws) - 1, 2):
    j = i + 1
    pins[throws[i] - 1:throws[j]] = ['.'] * (throws[j] - throws[i] + 1)
print(''.join(pins))