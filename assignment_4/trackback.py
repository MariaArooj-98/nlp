def needleman_wunsch_alignment_with_traceback(seq1, seq2, gap_penalty):
    # Initialize matrices for scores and traceback
    score_matrix = [[0 for _ in range(len(seq2) + 1)] for _ in range(len(seq1) + 1)]
    traceback = [["" for _ in range(len(seq2) + 1)] for _ in range(len(seq1) + 1)]

    # Rest of the code (same as needleman_wunsch_alignment function)
    # ...

    # Traceback to find alignment path
    i, j = len(seq1), len(seq2)
    aligned_seq1, aligned_seq2 = [], []
    while i > 0 or j > 0:
        if traceback[i][j] == "D":
            aligned_seq1.append(seq1[i - 1])
            aligned_seq2.append("-")  # Gap in seq2
            i -= 1
        elif traceback[i][j] == "I":
            aligned_seq1.append("-")  # Gap in seq1
            aligned_seq2.append(seq2[j - 1])
            j -= 1
        else:
            aligned_seq1.append(seq1[i - 1])
            aligned_seq2.append(seq2[j - 1])
            i -= 1
            j -= 1

    aligned_seq1.reverse()
    aligned_seq2.reverse()
    return score_matrix[len(seq1)][len(seq2)], ''.join(aligned_seq1), ''.join(aligned_seq2)

# Example usage:
seq1 = "AGTACGCA"
seq2 = "TATGC"
gap_penalty = -1
alignment_score, aligned_seq1, aligned_seq2 = needleman_wunsch_alignment_with_traceback(seq1, seq2, gap_penalty)
print(f"Needleman-Wunsch Alignment Score: {alignment_score}")
print("Sequence 1 Alignment:", aligned_seq1)
print("Sequence 2 Alignment:", aligned_seq2)
