# https://www.hackerrank.com/challenges/jim-and-the-skyscrapers/problem

def solve(a):
    stack = []
    count = 0
    for i in range(len(a)):
        if len(stack) == 0 or a[i] < a[stack[-1][0]]:
            stack.append((i, 1))
        else:
            c = 0
            while len(stack) != 0 and a[i] >= a[stack[-1][0]]:
                if a[stack[-1][0]] == a[i]:
                    c += stack[-1][1]
                stack.pop()
            count += c
            stack.append((i, c+1))
        print(a[i], stack, count)

    count *= 2 # bidirectional
    print(count)
    return count


# def solve2(a):
#     stack = []
#     count = 0
#     # a.append(math.inf)
#     for i in range(len(a)):
#         print(a[i], stack, count)
#         if len(stack) == 0:
#             stack.append(a[i])
#         elif stack[-1] > a[i]:
#             stack.append(a[i])
#         elif stack[-1] < a[i]:
#             while (len(stack) != 0 and stack[-1] < a[i]):
#                 sameS, cnt = 0, 0
#                 first_pass = True
#                 while first_pass or (len(stack) != 0 and stack[-1] < sameS):
#                     first_pass = False
#                     sameS = stack.pop()
#                     cnt += 1
#                 if cnt >= 2:
#                     count += ((cnt-1)*cnt)
#             stack.append(a[i])
#         elif stack[-1] == a[i]:
#             stack.append(a[i])
#         print(a[i], stack, count)
#
#     count *= 2 # bidirectional
#     print(count)
#     return count
#
#
# def solve1(a):
#     d = defaultdict(list)
#     for i in range(len(a)):
#         d[a[i]].append(i)
#     # print(d.items())
#     count = 0
#     for k, v in d.items():
#         # print(k, v)
#         if len(v) > 1:
#             for c in combinations(v, 2):
#                 if is_valid(a, c[0], c[1], d):
#                     # print('is_valid', c)
#                     count += 1
#     count *= 2 # bidirectional
#     print(count)
#     return count
#
# def is_valid(heights, start, end, d):
#     for i in range(start + 1, end+1):
#         if heights[i] > heights[start]:
#             return False
#     return True

# solve([3, 2, 1, 2, 3, 3])
assert solve([3, 2, 1, 2, 3, 3]) == 8
assert solve([1, 1000, 1]) == 0
assert solve([1, 1, 1, 1]) == 12
