def needleman_wunsch_alignment(seq1, seq2, gap_penalty):
    # Initialize the score matrix
    score_matrix = [[0 for _ in range(len(seq2) + 1)] for _ in range(len(seq1) + 1)]

    # Initialize the first row and column with gap penalties
    for i in range(1, len(seq1) + 1):
        score_matrix[i][0] = i * gap_penalty
    for j in range(1, len(seq2) + 1):
        score_matrix[0][j] = j * gap_penalty

    # Fill the score matrix using dynamic programming
    for i in range(1, len(seq1) + 1):
        for j in range(1, len(seq2) + 1):
            match_score = 1 if seq1[i - 1] == seq2[j - 1] else -1
            diagonal_score = score_matrix[i - 1][j - 1] + match_score
            horizontal_score = score_matrix[i][j - 1] + gap_penalty
            vertical_score = score_matrix[i - 1][j] + gap_penalty
            score_matrix[i][j] = max(diagonal_score, horizontal_score, vertical_score)

    # Optimal alignment score is at score_matrix[len(seq1)][len(seq2)]
    return score_matrix[len(seq1)][len(seq2)]

# Example usage:
seq1 = "AGTACGCA"
seq2 = "TATGC"
gap_penalty = -1
alignment_score = needleman_wunsch_alignment(seq1, seq2, gap_penalty)
print(f"Needleman-Wunsch Alignment Score: {alignment_score}")
