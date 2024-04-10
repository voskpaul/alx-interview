#!/usr/bin/python3
"""
N queens puzzle solution
"""
import sys

def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens(board, col, N):
    """
    Solve N queens problem recursively
    """
    if col >= N:
        print_solution(board, N)
        return True
    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_nqueens(board, col + 1, N) or res
            board[i][col] = 0
    return res

def print_solution(board, N):
    """
    Print the solution
    """
    sol = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                sol.append([i, j])
    print(sol)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    board = [[0 for j in range(N)] for i in range(N)]
    solve_nqueens(board, 0, N)

