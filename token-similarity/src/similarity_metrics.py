import collections

def levenshtein(s1: str, s2: str) -> float:
    """محاسبه فاصله لونشتاین (نرمال‌شده به نمره تشابه بین 0 و 1)."""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1): dp[i][0] = i
    for j in range(n + 1): dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s1[i-1] == s2[j-1] else 1
            dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + cost)
            
    dist = dp[m][n]
    max_len = max(m, n)
    return 1.0 - (dist / max_len) if max_len > 0 else 1.0

def damerau_levenshtein(s1: str, s2: str) -> float:
    """محاسبه فاصله دامراو-لونشتاین (شامل عملیات جابه‌جایی دو حرف مجاور)."""
    m, n = len(s1), len(s2)
    d = {}
    for i in range(-1, m + 1): d[(i, -1)] = i + 1
    for j in range(-1, n + 1): d[(-1, j)] = j + 1

    for i in range(m):
        for j in range(n):
            cost = 0 if s1[i] == s2[j] else 1
            d[(i, j)] = min(
                d[(i - 1, j)] + 1,
                d[(i, j - 1)] + 1,
                d[(i - 1, j - 1)] + cost
            )
            if i > 0 and j > 0 and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
                d[(i, j)] = min(d[(i, j)], d[(i - 2, j - 2)] + cost)

    dist = d[(m - 1, n - 1)]
    max_len = max(m, n)
    return 1.0 - (dist / max_len) if max_len > 0 else 1.0

def hamming(s1: str, s2: str) -> float:
    """محاسبه تشابه همینگ (برای رشته‌های با طول نامساوی پدینگ صفر انجام می‌شود)."""
    if len(s1) != len(s2):
        max_len = max(len(s1), len(s2))
        s1 = s1.ljust(max_len)
        s2 = s2.ljust(max_len)
    matches = sum(1 for a, b in zip(s1, s2) if a == b)
    return matches / len(s1) if len(s1) > 0 else 1.0

def lcsseq(s1: str, s2: str) -> float:
    """بلندترین زیردنباله مشترک (Longest Common Subsequence)."""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    lcs_len = dp[m][n]
    max_len = max(m, n)
    return lcs_len / max_len if max_len > 0 else 1.0

def lcsubstring(s1: str, s2: str) -> float:
    """بلندترین زیررشته مشترک پیوسته (Longest Common Substring)."""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    longest = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                longest = max(longest, dp[i][j])
    max_len = max(m, n)
    return longest / max_len if max_len > 0 else 1.0

def dice_coefficient(s1: str, s2: str) -> float:
    """ضریب تشابه دایس بر پایه بیگرام‌ها (Sørensen–Dice coefficient)."""
    if not s1 or not s2: return 0.0
    s1_bigrams = [s1[i:i+2] for i in range(len(s1)-1)]
    s2_bigrams = [s2[i:i+2] for i in range(len(s2)-1)]
    if not s1_bigrams or not s2_bigrams: return 1.0 if s1 == s2 else 0.0
    
    intersection = len(list((collections.Counter(s1_bigrams) & collections.Counter(s2_bigrams)).elements()))
    return (2.0 * intersection) / (len(s1_bigrams) + len(s2_bigrams))

def bag_distance(s1: str, s2: str) -> float:
    """محاسبه تشابه بر پایه فاصله چندمجموعه‌ای (Bag Distance)."""
    c1, c2 = collections.Counter(s1), collections.Counter(s2)
    dist = max(sum((c1 - c2).values()), sum((c2 - c1).values()))
    max_len = max(len(s1), len(s2))
    return 1.0 - (dist / max_len) if max_len > 0 else 1.0

def editex(s1: str, s2: str) -> float:
    """پیاده‌سازی الگوریتم Editex جهت مقایسه تشابه آوایی-ساختاری."""
    # گروه‌های صوتی ساده‌شده برای حروف انگلیسی
    groups = [{'a','e','i','o','u','y'}, {'b','p'}, {'c','k','q'}, {'d','t'}, {'l','r'}, {'m','n'}]
    def d_cost(a, b):
        if a == b: return 0
        for g in groups:
            if a in g and b in g: return 1
        return 2

    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1): dp[i][0] = dp[i-1][0] + 2
    for j in range(1, n + 1): dp[0][j] = dp[0][j-1] + 2

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = d_cost(s1[i-1], s2[j-1])
            dp[i][j] = min(dp[i-1][j] + 2, dp[i][j-1] + 2, dp[i-1][j-1] + cost)

    max_dist = 2 * max(m, n)
    return 1.0 - (dp[m][n] / max_dist) if max_dist > 0 else 1.0

def jaro(s1: str, s2: str) -> float:
    """محاسبه الگوریتم تشابه Jaro."""
    if s1 == s2: return 1.0
    len1, len2 = len(s1), len(s2)
    max_dist = max(len1, len2) // 2 - 1
    match1, match2 = [False]*len1, [False]*len2
    matches = 0
    
    for i in range(len1):
        start = max(0, i - max_dist)
        end = min(i + max_dist + 1, len2)
        for j in range(start, end):
            if match2[j] or s1[i] != s2[j]: continue
            match1[i] = match2[j] = True
            matches += 1
            break
            
    if matches == 0: return 0.0
    t = 0
    k = 0
    for i in range(len1):
        if not match1[i]: continue
        while not match2[k]: k += 1
        if s1[i] != s2[k]: t += 1
        k += 1
    t /= 2.0
    return (matches/len1 + matches/len2 + (matches - t)/matches) / 3.0

def jaro_winkler(s1: str, s2: str, p: float = 0.1) -> float:
    """محاسبه الگوریتم Jaro-Winkler با در نظر گرفتن پیشوند یکسان."""
    j_score = jaro(s1, s2)
    prefix = 0
    for a, b in zip(s1, s2):
        if a == b: prefix += 1
        else: break
        if prefix == 4: break
    return j_score + (prefix * p * (1 - j_score))

def q_grams_similarity(s1: str, s2: str, q: int = 2) -> float:
    """تشابه بر پایه Q-Grams (پیش‌فرض q=2 یا Bigram)."""
    q1 = [s1[i:i+q] for i in range(len(s1)-q+1)]
    q2 = [s2[i:i+q] for i in range(len(s2)-q+1)]
    if not q1 or not q2: return 1.0 if s1 == s2 else 0.0
    c1, c2 = collections.Counter(q1), collections.Counter(q2)
    intersection = sum((c1 & c2).values())
    total = sum((c1 | c2).values())
    return intersection / total if total > 0 else 0.0
