import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.currentPlayer="X"
        self.board=[["","",""],
                    ["","",""],
                    ["","",""]]
        self.window=tk.Tk()
        self.window.title("TicTacToe")

        self.buttons=[]
        for i in range(3):
            rows=[]
            for j in range(3):
                button=tk.Button(self.window,text='',height=5,width=10, command=lambda i=i,j=j:self.makeMove(i,j))
                button.grid(row=i,column=j)
                rows.append(button)
            self.buttons.append(rows)

    def makeMove(self,row,column):
        if self.board[row][column]=='':
            self.board[row][column]=self.currentPlayer
            self.buttons[row][column].config(text=self.currentPlayer)
            if self.checkWinner(self.currentPlayer):
                messagebox.showinfo('Game Over!','The winner is '+self.currentPlayer)
                self.window.quit()
            elif self.isDraw():
                messagebox.showinfo('Game Over!','It is a Draw')
                self.window.quit()
            else:
                self.currentPlayer="O" if self.currentPlayer == 'X' else 'X'
    def checkWinner(self,player):
        for i in range(3):
            if self.board[i][0]==self.board[i][1]==self.board[i][2]== player:
                return True
            if self.board[0][i]==self.board[1][i]==self.board[2][i]== player:
                return True
        if self.board[0][0]==self.board[1][1]==self.board[2][2]== player:
                return True
        if self.board[0][2]==self.board[1][1]==self.board[2][0]== player:
                return True
        return False

    def isDraw(self):
        for row in self.board:
            if '' in row:
                return False
        return True         

    def run(self):
        self.window.mainloop()
game=TicTacToe()
game.run()



        
