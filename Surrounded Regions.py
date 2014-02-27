class Solution:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.

    def BFS(self, board, x, y):
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        height, width = len(board), len(board[0])
       
        queue1 = [x*width+y]
        board[x][y]='a'
        index = 0
        while index != len(queue1):
            cur = queue1[index]
            index = index+1
            
            for i in range(0, 4):
                cx = cur/width+dx[i]
                cy = cur%width+dy[i]
                if cx >= 0 and cx < height and cy >= 0 and cy < width:
                    if board[cx][cy] == 'O':
                        board[cx][cy] = 'a'
                        queue1.append(cx*width+cy)
        return
            

    def solve(self, board):
        if len(board) == 0 or len(board[0]) == 0:
            return
        height, width = len(board), len(board[0])
        for i in range(0, height):
            if board[i][0] == 'O':
                self.BFS(board, i, 0)
            if board[i][width-1] == 'O':
                self.BFS(board, i, width-1)
        for i in range(0, width):
            if board[0][i] == 'O':
                self.BFS(board, 0, i)
            if board[height-1][i] == 'O':
                self.BFS(board, height-1, i)
        for i in range(0, height):
            for j in range(0, width):
                board[i][j] = 'O' if board[i][j] == 'a' else 'X'
