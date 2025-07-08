def levenshtein_distance(str1, str2):       # Defining the edit distance method
    m = len(str1)
    n = len(str2)
    
    # Creating the dp table
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Base cases : Filling up the first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Filling the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,        # Deletion
                dp[i][j - 1] + 1,        # Insertion
                dp[i - 1][j - 1] + cost  # Substitution or match
            )

    print("\nEdit Distance Matrix:")
    for row in dp:
        print(row)

    return dp[m][n]


def needleman_wunsch(seq1, seq2, match=1, mismatch=-1, gap=-2):         # Defining the needleman wunsch method
    m = len(seq1)
    n = len(seq2)

    # Initializing the score matrix
    score = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m + 1):
        score[i][0] = i * gap
    for j in range(n + 1):
        score[0][j] = j * gap

    # Filling the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            diag = score[i - 1][j - 1] + (match if seq1[i - 1] == seq2[j - 1] else mismatch)
            up = score[i - 1][j] + gap
            left = score[i][j - 1] + gap
            score[i][j] = max(diag, up, left)

    # Backtracking method
    aligned1 = ""
    aligned2 = ""
    i, j = m, n
    while i > 0 and j > 0:
        current = score[i][j]
        if seq1[i - 1] == seq2[j - 1]:
            match_score = match
        else:
            match_score = mismatch

        if current == score[i - 1][j - 1] + match_score:
            aligned1 = seq1[i - 1] + aligned1
            aligned2 = seq2[j - 1] + aligned2
            i -= 1
            j -= 1
        elif current == score[i - 1][j] + gap:
            aligned1 = seq1[i - 1] + aligned1
            aligned2 = '-' + aligned2
            i -= 1
        else:
            aligned1 = '-' + aligned1
            aligned2 = seq2[j - 1] + aligned2
            j -= 1

    while i > 0:
        aligned1 = seq1[i - 1] + aligned1
        aligned2 = '-' + aligned2
        i -= 1
    while j > 0:
        aligned1 = '-' + aligned1
        aligned2 = seq2[j - 1] + aligned2
        j -= 1

    print("\nScore Matrix:")
    for row in score:
        print(row)

    return aligned1, aligned2


# Main Menu taking user input
while True:
    print("\nMENU :")
    print("1. Compute Edit Distance (Levenshtein):")
    print("2. Perform Sequence Alignment (Needleman-Wunsch):")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        str1 = input("Enter first string: ").strip()
        str2 = input("Enter second string: ").strip()
        distance = levenshtein_distance(str1, str2)
        print(f"\nEdit Distance between '{str1}' and '{str2}' is {distance}")

    elif choice == '2':
        seq1 = input("Enter Sequence A: ").strip()
        seq2 = input("Enter Sequence B: ").strip()
        aligned1, aligned2 = needleman_wunsch(seq1, seq2)
        print("\nAligned Sequences:")
        print(aligned1)
        print(aligned2)

    elif choice == '3':
        print("Exiting program !")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
