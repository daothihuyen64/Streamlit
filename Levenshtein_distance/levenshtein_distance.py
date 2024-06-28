import streamlit as st

def levenshtein_distance(s1, tar):
    s1 = '#' + s1
    tar = '#' + tar

    n = len(s1)
    m = len(tar)

    dp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(m):
        dp[0][i] = i

    for i in range(n):
        dp[i][0] = i

    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1]
                           [j-1] if s1[i] == tar[j] else dp[i-1][j-1] + 1)

    return dp[n-1][m-1]


with open('./vocab.txt', 'r') as f:
    lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))

st.title("Word Correction using Levenshtein Distance")
word = st.text_input('Word:')
if st.button("Compute"):
    levenshtein = dict()
    for x in words:
        levenshtein[x] = levenshtein_distance(word, x)
    sorted_distences = dict(
        sorted(levenshtein.items(), key=lambda item: item[1]))
    correct_word = list(sorted_distences.keys())[0]
    st.write('Correct word: ', correct_word)

    col1, col2 = st.columns(2)
    col1.write('Vocabulary:')
    col2.write('Distances:')

    col1.write(words)
    col2.write(sorted_distences)
