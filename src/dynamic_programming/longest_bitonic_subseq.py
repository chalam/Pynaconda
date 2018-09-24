# bitonic = increasing and decreasing
# longest bitonic subseq = longest incr subseq LIS + longest decr subseq LDS
# combine the two for solution
# LIS
# j = o to i: compare ai > aj update dp if it grows
# /* Compute optimized LIS values in bottom up manner */
#     for (i = 1; i < n; i++ )
#         for (j = 0; j < i; j++ )
#             if ( arr[i] > arr[j] && lis[i] < lis[j] + 1)
#                 lis[i] = lis[j] + 1;
# LDS
# j = n to i: compare ai > aj, update dp if it is less
# for (i = 1; i < n; i++)
#     for (j = 0; j < i; j++)
#         if (arr[i] < arr[j] & & lds[i] < lds[j] + 1)
#             lds[i] = lds[j] + 1;