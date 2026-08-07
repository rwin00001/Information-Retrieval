import os
from similarity_metrics import (
    levenshtein, damerau_levenshtein, hamming, lcsseq, lcsubstring,
    dice_coefficient, bag_distance, editex, jaro, jaro_winkler, q_grams_similarity
)

def run_evaluation():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_dir = os.path.join(base_dir, 'data')
    results_dir = os.path.join(base_dir, 'results')
    os.makedirs(results_dir, exist_ok=True)

    tokens_file = os.path.join(data_dir, 'tokens.txt')
    top10_file = os.path.join(data_dir, 'top10.txt')
    output_file = os.path.join(results_dir, 'similar_tokens.txt')

    # بارگذاری کلمات
    with open(tokens_file, 'r', encoding='utf-8') as f:
        tokens = list(set(f.read().splitlines()))

    with open(top10_file, 'r', encoding='utf-8') as f:
        top10 = [line.split(":")[0] for line in f.read().splitlines() if line]

    algorithms = {
        "Levenshtein": levenshtein,
        "Damerau-Levenshtein": damerau_levenshtein,
        "Hamming": hamming,
        "LCS": lcsseq,
        "LCSubstring": lcsubstring,
        "Dice": dice_coefficient,
        "Bag": bag_distance,
        "Editex": editex,
        "Jaro": jaro,
        "Jaro-Winkler": jaro_winkler,
        "Q-Grams": q_grams_similarity,
    }

    with open(output_file, 'w', encoding='utf-8') as out:
        for top_word in top10:
            out.write(f"Top Word: {top_word}\n")
            out.write("=" * 45 + "\n")

            for algo_name, algo_func in algorithms.items():
                best_match = None
                best_score = -1.0

                for token in tokens:
                    if token == top_word:
                        continue  # صرف‌نظر از خودِ کلمه

                    score = algo_func(top_word, token)
                    if score > best_score:
                        best_score = score
                        best_match = token

                out.write(f"  {algo_name:<20}: {best_match} (Score: {best_score:.4f})\n")
            out.write("\n")

    print(f"Similarity evaluation complete. Results saved to {output_file}")

if __name__ == "__main__":
    run_evaluation()
