class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) <= 0:
            return False

        self.ans = False
        n = len(board)
        m = len(board[0])

        def dfs(i, j, target: str, visited: set[tuple[int]]) -> None:
            if len(target) == 1 and board[i][j] == target:
                self.ans = True
                return
            elif board[i][j] != target[0]:
                return

            visited.add((i, j))

            if i > 0 and (i - 1, j) not in visited:
                dfs(i-1, j, target[1:], visited)
            if i < n - 1 and (i + 1, j) not in visited:
                dfs(i+1, j, target[1:], visited)
            if j > 0 and (i, j - 1) not in visited:
                dfs(i, j-1, target[1:], visited)
            if j < m - 1 and (i, j + 1) not in visited:
                dfs(i, j+1, target[1:], visited)

            visited.remove((i, j))

            return

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    dfs(i, j, word, set([]))
                    if self.ans:
                        return True

        return False


            

        