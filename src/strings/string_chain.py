# https://blog.cancobanoglu.net/2016/09/18/interview-questions-string-chain/
# https://careercup.com/question?id=5647083983863808
# Two Sigma Test

# def longestChain(words):
#     l = []
#     n = len(words)
#     for word in words:
#         l.append((len(word), word))
#     sorted(l, key=lambda x:x[0])
#     dp = [0] * (n + 1)
#     dp[0] = 1
#     max_len = dp[0]
#     word_map = {}
#     word_map[l[0][1]] = 0
#     for i in range(1, n):
#         dp[i] = 1
#         size, word = l[i]
#         for j in range(size):
#             tmp = word[:j]
#             if tmp in word_map:
#                 dp[i] = max(dp[i], dp[word_map[tmp]]+1)
#         max_len = max(max_len, dp[i])
#         word_map[word] = i
#     return max_len

def longestChain(words):
    """
        Build a dp table bottom-up with number of edits of string chain
    :param words: list of words
    :return: max len of string chain
    """
    print(words)
    word_pairs = []
    n = len(words)
    for word in words:
        word_pairs.append((len(word), word))
    word_pairs = sorted(word_pairs, key=lambda x: x[0])
    print(word_pairs)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n):
        local_max = 1
        for j in range(i - 1, -1, -1):
            print(word_pairs[i][1], word_pairs[j][1])
            if word_pairs[i][0] - word_pairs[j][0] > 0:
                if word_pairs[i][0] - word_pairs[j][0] == 1:
                    word = word_pairs[i][1]
                    print(word)
                    for k in range(len(word)):
                        remind = word[:k] + word[k + 1:]
                        print('\t', remind)
                        if remind == word_pairs[j][1]:
                            if dp[j] + 1 > local_max:
                                local_max = dp[j] + 1
                else:
                    break
        dp[i] = local_max
    global_max = max(dp)
    return global_max

# def longestChain(data1, max_chain):
#     global Prev_chains
#     if (data1):
#         for i in range(len(data1)):
#             w = str(data1[:i] + data1[i + 1:])
#             if (w):
#                 if w in words:
#                     if Prev_chains < max_chain:
#                         max_chain += 1
#                         find_max_chain(w, max_chain)
#         if Prev_chains < max_chain:
#             Prev_chains = max_chain
#         max_chain = 1
#
#     return


"""
n = int(input("enter the number of element in list"))
data = []
for i in range(0,n):
    data.append(input("enetr the element"))
print (data)
"""
max_chain = 1
Prev_chains = 0
data = "bdca"
li = []
# words = ["a", "b", "ba", "bca", "bda", "bdca"]
words = ['a', 'zxb', 'ba', 'bca', 'bda', 'bdca', 'zxbe', 'azxbe', 'azxpbe']
# for data in words:
#     max_chain = 1
#     Prev_chains = 0
#     longestChain(data, max_chain)
#     li.append(Prev_chains)
# print(li)
# print("max chain length = ", max(li))

max_len = longestChain(words)
print("max chain length = ", max_len)
