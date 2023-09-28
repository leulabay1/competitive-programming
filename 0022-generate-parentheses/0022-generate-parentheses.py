class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        valid: list[str] = []

        def traverse(s: str, left: int, right: int) -> None:
            if left == n and right == n:
                valid.append(s)
                return

            if left < n:
                traverse(s + "(", left + 1, right)

            if right < left:
                traverse(s + ")", left, right + 1)

        traverse("(", 1, 0)

        return valid