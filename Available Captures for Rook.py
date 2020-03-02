class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        #  r_pos = [r,c]
        for i in range(len(board)):
            if board[i].count("R")==1:
                r_pos=[i,board[i].index("R")]
                break

        c=0

        for i in range(len(board[r_pos[0]][:r_pos[1]])):
            if board[r_pos[0]][:r_pos[1]][::-1][i]=="B":
                break
            else:
                if board[r_pos[0]][:r_pos[1]][::-1][i]=="p":
                    c+=1
                    break

        for i in range(len(board[r_pos[0]][r_pos[1]:])):
            if board[r_pos[0]][r_pos[1]:][i]=="B":
                break
            else:
                if board[r_pos[0]][r_pos[1]:][i]=="p":
                    c+=1
                    break


        col_arr=[]

        for i in range(len(board[i])):
            col_arr.append(board[i][r_pos[1]])



        for i in range(len(col_arr[:r_pos[1]])):
            if col_arr[:r_pos[1]][::-1][i]=="B":
                break
            else:
                if col_arr[:r_pos[1]][::-1][i]=="p":
                    c+=1
                    break

        for i in range(len(col_arr[r_pos[1]:])):
            if col_arr[r_pos[1]:][i]=="B":
                break
            else:
                if col_arr[r_pos[1]:][i]=="p":
                    c+=1
                    break
        return c