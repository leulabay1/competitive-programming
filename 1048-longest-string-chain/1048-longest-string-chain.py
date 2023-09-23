class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        mem = {}
        ws = collections.defaultdict(set)
        for w in words:
            ws[len(w)].add(w)
        l = list(ws.keys())
        l.sort()
        ret = 1
        for ll in l:
            if ll-1 not in ws:
                for w in ws[ll]:
                    mem[w] = 1
            else:
                for w in ws[ll]:
                    m = 0
                    for i in range(ll):
                        ww = w[:i] + w[i+1:]
                        if ww in mem:
                            m = max(m, mem[ww])
                    mem[w] = m+1
                    ret = max(ret, m+1)
        return ret