def min_edit_distance(word1, word2):
    m = len(word1)
    n = len(word2)

    # 初始化一个 (m+1) x (n+1) 的 DP 数组
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base case: 一个空字符串转换到另一个字符串所需的操作数
    for i in range(m + 1):
        dp[i][0] = i  # 从 word1 删除所有字符
    for j in range(n + 1):
        dp[0][j] = j  # 向 word1 插入所有 word2 的字符

    # 填充 DP 数组
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                # 如果当前字符相等，不需要额外操作
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # 当前字符不相等，选择替换、删除或插入的最小操作数
                dp[i][j] = min(
                    dp[i - 1][j - 1] + 1,  # 替换操作
                    dp[i - 1][j] + 1,      # 删除操作
                    dp[i][j - 1] + 1       # 插入操作
                )

    # 返回右下角的结果，即所需的最小编辑距离
    return dp[m][n]

# 示例测试
word1 = "natural language processing"
word2 = "processing natural language"
print("最小编辑距离:", min_edit_distance(word1, word2))