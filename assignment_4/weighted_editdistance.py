def weighted_edit_distance(str1, str2, insertion_cost, deletion_cost, substitution_cost):
    # Initialize a matrix to store edit distances
    dp = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

    # Initialize the first row and column with incremental values
    for i in range(len(str1) + 1):
        dp[i][0] = i * deletion_cost
    for j in range(len(str2) + 1):
        dp[0][j] = j * insertion_cost

    # Fill the matrix using dynamic programming
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            cost = 0 if str1[i - 1] == str2[j - 1] else substitution_cost
            dp[i][j] = min(
                dp[i - 1][j] + deletion_cost,  # Deletion
                dp[i][j - 1] + insertion_cost,  # Insertion
                dp[i - 1][j - 1] + cost  # Substitution
            )

    # Minimum weighted edit distance is at dp[len(str1)][len(str2)]
    return dp[len(str1)][len(str2)]

# Example usage:
str1 = "kitten"
str2 = "sitting"
insertion_cost = 2
deletion_cost = 1
substitution_cost = 3
distance = weighted_edit_distance(str1, str2, insertion_cost, deletion_cost, substitution_cost)
print(f"Weighted Edit Distance between '{str1}' and '{str2}': {distance}")
