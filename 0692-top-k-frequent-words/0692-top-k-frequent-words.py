class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_cnt=collections.Counter(words)
        words_cnt=[(word, words_cnt[word]) for word in words_cnt]
        words_cnt.sort(key=lambda i:i[0])
        import heapq
        heapq.heapify(words_cnt)
        return [i[0] for i in heapq.nlargest(k, words_cnt, key=lambda i:i[-1])]