class Solution:
    def topStudents(self, pos: List[str], neg: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        pos = set(pos)
        neg = set(neg)

        # d = {}
        d = {}
        for i,j in zip(report, student_id):
            temp = i.split(' ')
            score = 0

            for l in temp:
                if l in pos:
                    score += 3
                elif l in neg:
                    score -=1

            d[j] = score

        return list(sorted(sorted(student_id, reverse=True), key = lambda x: d[x]))[-k:][::-1]