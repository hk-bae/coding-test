

# a_k = n ( n(n-1)/2 < k <= n(n+1)/2 )

def binary_search(start, end, target):
    mid = (start + end) // 2
    lower = get_lower_bound(mid)
    upper = get_upper_bound(mid)

    if lower <= target <= upper:
        return (mid, upper, lower)
    elif target < lower:
        return binary_search(start, mid - 1, target)
    else:  # target > upper
        return binary_search(mid + 1, end, target)


def get_lower_bound(n):
    return n * (n - 1) // 2 + 1


def get_upper_bound(n):
    return n * (n + 1) // 2


a,b = map(int, input().split())

# 1~1000 은 n이 1~45 사이인 숫자들만 포함되어 있다
n_for_a, upper_for_a, _ = binary_search(1, 45, a)
n_for_b, _, lower_for_b = binary_search(1, 45, b)

result = n_for_a * (upper_for_a - a + 1) + n_for_b * (b - lower_for_b + 1)
print(n_for_a,upper_for_a,n_for_b,lower_for_b)
# 범위 내의 숫자 합
for i in range(n_for_a + 1, n_for_b):
    result += (i * i)

print(result)


