def array_left_rotation(a, n, k):
    alist = list(a)
    b = alist[k:]+alist[:k]
    return b

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
