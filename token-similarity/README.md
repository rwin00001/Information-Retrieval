# Token Similarity & String Distance Metrics Engine

An Information Retrieval benchmark evaluating 11 string similarity and edit-distance algorithms on tokens extracted from StackExchange XML dumps.

## Implemented Metrics
1. Levenshtein Distance
2. Damerau-Levenshtein Distance
3. Hamming Distance
4. Longest Common Subsequence (LCS)
5. Longest Common Substring (LCSubstring)
6. Sørensen–Dice Coefficient
7. Bag Distance
8. Editex Phonetic Distance
9. Jaro Similarity
10. Jaro-Winkler Distance
11. Q-Grams Similarity

## Execution Pipeline

1. **Extract Tokens**:
   ```bash
   python src/xml_parser.py
   ```
2. **Run Evaluation Engine**:
   ```bash
    python src/evaluate_matches.py
   ```
