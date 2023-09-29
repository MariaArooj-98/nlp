def min_edit_distance_with_traceback(str1, str2):
    # Initialize matrices for edit distances and traceback
    dp = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
    traceback = [["" for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

    # Initialize the first row and column with incremental values
    for i in range(len(str1) + 1):
        dp[i][0] = i
        traceback[i][0] = "D"  # Deletion
    for j in range(len(str2) + 1):
        dp[0][j] = j
        traceback[0][j] = "I"  # Insertion

    # Fill the matrices using dynamic programming
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            delete_cost = dp[i - 1][j] + 1
            insert_cost = dp[i][j - 1] + 1
            substitute_cost = dp[i - 1][j - 1] + cost

            # Determine the minimum cost operation
            if delete_cost <= insert_cost and delete_cost <= substitute_cost:
                dp[i][j] = delete_cost
                traceback[i][j] = "D"  # Deletion
            elif insert_cost <= delete_cost and insert_cost <= substitute_cost:
                dp[i][j] = insert_cost
                traceback[i][j] = "I"  # Insertion
            else:
                dp[i][j] = substitute_cost
                traceback[i][j] = "S"  # Substitution

    # Traceback to find edit operations
    i, j = len(str1), len(str2)
    operations = []
    while i > 0 or j > 0:
        if traceback[i][j] == "D":
            operations.append(f"Delete '{str1[i - 1]}' at position {i - 1}")
            i -= 1
        elif traceback[i][j] == "I":
            operations.append(f"Insert '{str2[j - 1]}' at position {i}")
            j -= 1
        else:
            if dp[i][j] != dp[i - 1][j - 1]:
                operations.append(f"Replace '{str1[i - 1]}' at position {i - 1} with '{str2[j - 1]}'")
            i -= 1
            j -= 1

    operations.reverse()
    return dp[len(str1)][len(str2)], operations

# Example usage:
str1 = "kitten"
str2 = "sitting"
distance, operations = min_edit_distance_with_traceback(str1, str2)
print(f"Minimum Edit Distance between '{str1}' and '{str2}': {distance}")
print("Edit Operations:")
for op in operations:
    print(op)
