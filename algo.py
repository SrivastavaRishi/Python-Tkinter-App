from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
import math


root = Tk()
root.title('DP PROBLEMS')
root.geometry('1200x380')


# root.state('zoomed')
import sys
sys.path.append(r"c:\users\rishi\appdata\local\programs\python\python38-32\lib\site-packages")
import matplotlib.pyplot as plt
import numpy as np

def gr():
    master = Toplevel(root)
    #master.state('zoomed')
    fontt = tkFont.Font(family='arial', size=10)
    master.geometry('1000x350')
    master.config(bg='black')
    T = tk.Text(master, height=1000, width=300, bg='black', font=fontss, fg='#50c7c7')
    T.pack()
    T.insert(tk.END, 'The time complexity of algorithms given below are:\n'
                     '1) 0/1 Knapsack : The time complexity of this algorithm is O(N*W) where N'
                     ' is the number of bags and W is the maximum capacity.'
                     'Considering N and W comparitively same so, time complexity is approximately O(N*N).\n\n'
                     '2) Longest Common Subsequence : In this case the time complexity is O(A*B) , '
                     'where A is the length of first string and B is the length of second string'
                     'Considering A is comparible to B so the overall time complexity is O(A*A).\n\n'
                     '3)Matrix Chain multiplication: If we have n matrices to multiply, it will take O(n) '
                     'time to generate each of the O(n2) costs and entries in the best matrix for an'
                     ' overall complexity of O(n3) time at a cost of O(n2) space.\n\n'
                     '4)All Pair Shortest Path (Floyd–Warshall algorithm): All-Pairs Shortest Paths.'
                     ' The all pair shortest path algorithm is also known as Floyd-Warshall algorithm is used'
                     ' to find all pair shortest path problem from a given weighted graph.'
                     'The time complexity of this algorithm is O(V3), here V is the number of vertices '
                     'in the graph. Input − The cost matrix of the graph.\n\n'
                     '5)Assembly Line scheduling: Since we have to traverse the array only once.'
                     'So time complexity is linear i.e. is O(N).')
    #x = np.array(range(10))
    x = np.linspace(0, 3, 1000)
    y = x ** 2
    z = x ** 3

    # Create the plot
    plt.plot(x, y, label='0/1 Knapsack \n Longest Common Subsequence\n')
    plt.plot(x, x, label='Assembly Line Scheduling\n')
    plt.plot(x, z, label='Matrix Chain Multiplication \n All Pair Shortest Paths')


    # Add a title
    plt.title('Comparison of different dp algorithm')

    # Add X and y Label
    plt.xlabel('Value of N')
    plt.ylabel('Comparative time taken')

    # Add a grid
    plt.grid(alpha=.4, linestyle='--')

    # Add a Legend
    plt.legend()

    # Show the plot
    plt.show()


def knapsack():
    def eval():
        x = e3.get()
        y = e4.get()
        wt = [int(k) for k in x.split(' ')]
        val = [int(k) for k in y.split(' ')]
        # val = list(y.split(" "))
        n = int(e1.get())
        W = int(e2.get())
        K = [[0 for x in range(W + 1)] for x in range(n + 1)]
        for i in range(n + 1):
            for w in range(W + 1):
                if i == 0 or w == 0:
                    K[i][w] = 0
                elif wt[i - 1] <= w:
                    K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
                else:
                    K[i][w] = K[i - 1][w]

        myText.set(K[n][W])

    master = Toplevel(root)
    fontt = tkFont.Font(family='arial', size=20)
    master.geometry('700x350')
    master.config(bg='#000000')
    myText = StringVar()
    Label(master, text="Enter number of items", font=fontt, bg='#000000', fg='#50c7c7').grid(row=0, sticky=W)
    Label(master, text="Enter maximum bag capacity", font=fontt, bg='#000000', fg='#50c7c7').grid(row=1, sticky=W)
    Label(master, text="Enter weights", font=fontt, bg='#000000', fg='#50c7c7').grid(row=2, sticky=W)
    Label(master, text="Enter values", font=fontt, bg='#000000', fg='#50c7c7').grid(row=3, sticky=W)
    Label(master, text="Maximum profit earned is:", font=fontt, bg='#000000', fg='#50c7c7').grid(row=5, sticky=W)
    result = Label(master, text="", textvariable=myText).grid(row=6, column=1, columnspan=6, sticky=W)

    e1 = Entry(master, bg='white', highlightthickness=2.5)  # no of items
    e1.config(highlightbackground='red')
    e2 = Entry(master, bg='white', highlightthickness=2.5)  # max bag capacity
    e2.config(highlightbackground='red')
    e3 = Entry(master, bg='white', highlightthickness=2.5)  # weight array
    e3.config(highlightbackground='red')
    e4 = Entry(master, bg='white', highlightthickness=2.5)  # value array
    e4.config(highlightbackground='red')

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)

    b = Button(master, text="Calculate", command=eval, bg='white', highlightthickness=2.5)
    b.config(highlightbackground='red')
    b.grid(row=0, column=2, columnspan=6, rowspan=2, sticky=W + E + N + S, padx=5, pady=5)

    master.mainloop()


def lcs():
    def eval():
        X = e1.get()
        Y = e2.get()
        m = len(X)
        n = len(Y)
        L = [[None] * (n + 1) for i in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif X[i - 1] == Y[j - 1]:
                    L[i][j] = L[i - 1][j - 1] + 1
                else:
                    L[i][j] = max(L[i - 1][j], L[i][j - 1])
        myText.set(L[m][n])

    master = Toplevel(root)
    master.geometry('700x350')
    master.config(bg='#000000')
    myText = StringVar()
    fontt = tkFont.Font(family='arial', size=15)
    Label(master, text="Enter first string", font=fontt, bg='#000000', fg='#50c7c7').grid(row=0, sticky=W)
    Label(master, text="Enter second string", font=fontt, bg='#000000', fg='#50c7c7').grid(row=1, sticky=W)
    result = Label(master, text="", textvariable=myText, font=fontt, bg='#000000', fg='#50c7c7').grid(row=6, column=1, sticky=W)

    e1 = Entry(master, bg='white', highlightthickness=2.5)  # no of items
    e1.config(highlightbackground='red')
    e2 = Entry(master, bg='white', highlightthickness=2.5)  # max bag capacity
    e2.config(highlightbackground='red')
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    b = Button(master, text="Calculate", command=eval)
    b.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=W + E + N + S, padx=5, pady=5)


def mcm():
    def eval():
        arr = e.get()
        p = [int(k) for k in arr.split(' ')]
        n = len(p)

        m = [[0 for x in range(n)] for x in range(n)]
        for i in range(1, n):
            m[i][i] = 0

        for L in range(2, n):
            for i in range(1, n - L + 1):
                j = i + L - 1
                m[i][j] = 100000000
                for k in range(i, j):
                    q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                    if q < m[i][j]:
                        m[i][j] = q

        myText.set(m[1][n - 1])

    master = Toplevel(root)
    fontt = tkFont.Font(family='arial', size=20)
    master.geometry('700x350')
    master.config(bg='#000000')
    myText = StringVar()
    Label(master, text="Enter dimension   ", font=fontt, bg='#000000', fg='#50c7c7').grid(row=0, sticky=W)
    Label(master, text="Minimum operation are", font=fontt, bg='#000000', fg='#50c7c7').grid(row=1, sticky=W)

    result = Label(master, text="", textvariable=myText).grid(row=1, column=1, sticky=W)
    e = Entry(master, bg='white', highlightthickness=2.5)  # no of items
    e.config(highlightbackground='red')
    e.grid(row=0, column=1)
    b = Button(master, text="Calculate", command=eval)
    b.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=W + E + N + S, padx=5, pady=5)


def als():
    def eval():
        n = int(e1.get())
        y = e2.get()
        p = [int(k) for k in y.split(' ')]
        ind = 0

        row = 2
        col = n
        a = []

        for i in range(row):
            temp = []
            for j in range(col):
                temp.append(p[ind])
                ind += 1
            a.append(temp)

        y = e3.get()
        p = [int(k) for k in y.split(' ')]
        ind = 0

        row = 2
        col = n
        t = []

        for i in range(row):
            temp = []
            for j in range(col):
                temp.append(p[ind])
                ind += 1
            t.append(temp)

        y = e4.get()
        e = [int(k) for k in y.split(' ')]
        y = e5.get()
        x = [int(k) for k in y.split(' ')]

        # print(a)
        # print(t)
        # print(e)
        # print(x)

        NUM_STATION = len(a[0])
        T1 = [0 for i in range(NUM_STATION)]
        T2 = [0 for i in range(NUM_STATION)]
        T1[0] = e[0] + a[0][0]
        T2[0] = e[1] + a[1][0]
        for i in range(1, NUM_STATION):
            T1[i] = min(T1[i - 1] + a[0][i], T2[i - 1] + t[1][i] + a[0][i])
            T2[i] = min(T2[i - 1] + a[1][i], T1[i - 1] + t[0][i] + a[1][i])
            ans = min(T1[NUM_STATION - 1] + x[0], T2[NUM_STATION - 1] + x[1])

        myText.set(ans)

    master = Toplevel(root)
    fontt = tkFont.Font(family='arial', size=10)
    master.geometry('700x350')
    master.config(bg='#000000')
    myText = StringVar()
    Label(master, text="Enter number of stations", font=fontt, bg='#000000', fg='#50c7c7').grid(row=0, sticky=W)
    Label(master, text="Minimum time taken by the car chassis to leave station j on assembly line 1", font=fontt, bg='#000000', fg='#50c7c7').grid(row=1, sticky=W)
    Label(master, text="Minimum time taken by the car chassis to leave station j on assembly line 2", font=fontt, bg='#000000', fg='#50c7c7').grid(row=2, sticky=W)
    Label(master, text="Enter entry values", font=fontt, bg='#000000', fg='#50c7c7').grid(row=3, sticky=W)
    Label(master, text="Enter exit values", font=fontt, bg='#000000', fg='#50c7c7').grid(row=4, sticky=W)
    Label(master, text="Result:", font=fontt, bg='#000000', fg='#50c7c7').grid(row=6, sticky=W)
    result = Label(master, text="", textvariable=myText).grid(row=7, column=1, sticky=W)


    e1 = Entry(master, bg='white', highlightthickness=1.25)  # no of items
    e1.config(highlightbackground='red')
    e2 = Entry(master, bg='white', highlightthickness=1.25)# max bag capacity
    e2.config(highlightbackground='red')
    e3 = Entry(master, bg='white', highlightthickness=1.25)  # weight array
    e3.config(highlightbackground='red')
    e4 = Entry(master, bg='white', highlightthickness=1.25)  # value array
    e4.config(highlightbackground='red')
    e5 = Entry(master, bg='white', highlightthickness=1.25)
    e5.config(highlightbackground='red')
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    e5.grid(row=4, column=1)
    b = Button(master, text="Calculate", command=eval)
    b.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=W + E + N + S, padx=5, pady=5)

    master.mainloop()


def apsp():
    def eval():
        v = int(e1.get())
        mat = []
        dist = []
        inf = 99999999
        for i in range(v):
            temp = []
            for j in range(v):
                if (i == j):
                    temp.append(0)
                    continue
                temp.append(inf)
            mat.append(temp)
            dist.append(temp)

        x = e2.get()
        p = [int(k) for k in x.split(' ')]
        # print(mat)
        # edges = len(p)/3

        for i in range(0, len(p), 3):
            # print(p)
            src = p[i]
            dest = p[i + 1]
            cost = p[i + 2]
            mat[src][dest] = cost
            dist[src][dest] = cost

        # print('done')

        for k in range(v):
            for i in range(v):
                for j in range(v):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        for i in range(v):
            for j in range(v):
                if dist[i][j] == inf:
                    dist[i][j] = 'inf'
                    continue
                # print(dist[i][j], end=" ")
            print('\n')
        myText.set(dist)
        #return dist

    master = Toplevel(root)
    fontt = tkFont.Font(family='arial', size=10)
    master.geometry('700x350')
    master.config(bg='#000000')
    myText = StringVar()
    Label(master, text="Enter number of nodes", font=fontt, bg='#000000', fg='#50c7c7').grid(row=0, sticky=W)
    Label(master, text="Enter adjacency matrix ", font=fontt, bg='#000000', fg='#50c7c7').grid(row=1, sticky=W)
    result = Label(master, text="", textvariable=myText).grid(row=6, column=1, sticky=W)

    e1 = Entry(master)  # no of items
    e2 = Entry(master)  # max bag capacity
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    b = Button(master, text="Calculate", command=eval)
    b.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=W + E + N + S, padx=5, pady=5)


fontStyle = tkFont.Font(family="Lucida Grande", size=25)
fontss = tkFont.Font(family='arial', size=17)
a = Label(root, text='DYNAMIC PROGRAMMING', font=fontStyle, bg='#f2ace9')
a.pack(fill=X)
T = tk.Text(root, height=10, width=300, bg='black', bd=5, font=fontss, fg='#50c7c7')
T.pack()
T.insert(tk.END, "Dynamic programming is both a mathematical optimization method and a computer programming method. "
                 "The method was developed by Richard Bellman in the 1950s and has found applications in numerous "
                 "fields, from aerospace engineering to economics. In both contexts it refers to simplifying a "
                 "complicated problem by breaking it down into simpler sub-problems in a recursive manner. While some "
                 "decision problems cannot be taken apart this way, decisions that span several points in time do "
                 "often break apart recursively. Likewise, in computer science, if a problem can be solved optimally "
                 "by breaking it into sub-problems and then recursively finding the optimal solutions to the "
                 "sub-problems, then it is said to have optimal substructure. ")

frame = Frame(root)
frame.pack()
b6 = Button(frame, text='Graphs', width=10, bd=10, font='arial', fg='#50c7c7', bg='black', command=gr)
b6.pack(side='right')
b1 = Button(frame, text='0/1 Knapsack', command=knapsack, width=20, bd=10, font='arial', fg='#50c7c7', bg='black')
b1.pack(side='left')
b2 = Button(frame, text='Assembly-line Scheduling', command=als, width=20, bd=10, font='arial', fg='#50c7c7',
            bg='black')
b2.pack(side='right')
b3 = Button(frame, text='Longest Common Subsequence', command=lcs, width=25, bd=10, font='arial', fg='#50c7c7',
            bg='black')
b3.pack(side='right')
b4 = Button(frame, text='Matrix Chain Multiplication', command=mcm, width=20, bd=10, font='arial', fg='#50c7c7',
            bg='black')
b4.pack(side='right')
b5 = Button(frame, text='All pairs shortest paths', command=apsp, width=20, bd=10, font='arial', fg='#50c7c7',
            bg='black')
b5.pack(side='right')


root.mainloop()
