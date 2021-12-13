def is_possible(board,row,col,rows_arr,cols_arr,squares):
    if rows_arr[col][board[row][col]-1]==1:
        return False
    if cols_arr[row][board[row][col]-1]==1:
        return False
    if squares[row//3*3+col//3][board[row][col]-1]==1:
        return False
    return True
def rec(board,row,col,rows_arr,cols_arr,squares):
    cor=False
    if col==9:
        row+=1
        col=0
    if row==9:
        return True
    if board[row][col]==0:
        for i in range(1,10):
            board[row][col]=i
            if is_possible(board,row,col,rows_arr,cols_arr,squares):
                rows_arr[col][i-1]=1
                cols_arr[row][i-1]=1
                squares[row//3*3+col//3][board[row][col]-1]=1
                cor=rec(board,row,col+1,rows_arr,cols_arr,squares)
                rows_arr[col][i-1]=0
                cols_arr[row][i-1]=0
                squares[row//3*3+col//3][board[row][col]-1]=0
            if cor==True:
                break
        if cor==False:
            board[row][col]=0
    else:
        while board[row][col]!=0:
            col+=1
            row+=col//9
            col%=9
            if row==9:
                break
        cor=rec(board,row,col,rows_arr,cols_arr,squares)
    return cor
def solve(board):
    rows=[]
    cols=[]
    squares=[]
    for i in range(9):
        arr=[0]*9
        arr2=[0]*9
        arr3=[0]*9
        for r in range(9):
            if board[i][r]!=0:
                arr[board[i][r]-1]=1
            if board[r][i]!=0:
                arr2[board[r][i]-1]=1
        cols.append(arr.copy())
        rows.append(arr2.copy())
    i=0
    r=0
    j=2
    k=2
    while j<=8:
        k=2
        while k<=8:
            i=j-2
            arr3=[0]*9
            while i<=j:
                r=k-2
                while r<=k:
                    if board[i][r]!=0:
                        arr3[board[i][r]-1]=1
                    r+=1
                i+=1
            squares.append(arr3.copy())
            k+=3
        j+=3
    rec(board,0,0,rows,cols,squares)
    return board
def run():
    board=[]
    print("Enter sudoku table put 0 for empty cells")
    for i in range(9):
        print("Row ",i+1)
        arr=[0]*9
        line=input("")
        for i in range(len(line)):
            arr[i]=int(line[i])
        board.append(arr)
    for i in board:
        print(i)
    print("")
    solve(board)
    print("Solution")
    for i in board:
        print(i)
run()