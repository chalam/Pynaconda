# invariant s[i, i+1..j-1,j] is palindrome,
# if substrinng s[i+1..j-1] is a palindrome
# diag(dp) = True since single letter is  palind
# dp[i][j] = True if s[i+1][j-1] is True and s[i] == s[j]
# upper dp is filled for each substr length