class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def are_similar(str1, str2):
            # Helper function to check if two strings are similar
            diff_count = 0
            for c1, c2 in zip(str1, str2):
                if c1 != c2:
                    diff_count += 1
                if diff_count > 2:
                    return False
            return True

        def find(uf, x):
            # Helper function to find the representative of the group
            if uf[x] != x:
                uf[x] = find(uf, uf[x])
            return uf[x]

        uf = {str_: str_ for str_ in strs}
        
        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if are_similar(strs[i], strs[j]):
                    uf[find(uf, strs[i])] = find(uf, strs[j])

        # Count the number of unique representatives
        unique_representatives = set(find(uf, str_) for str_ in strs)
        return len(unique_representatives)
    