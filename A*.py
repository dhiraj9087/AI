g=0

def show_board(arr):
    for i in range(9):
        if i%3==0:
            print()
        if arr[i]==-1:
            print("_",end=" ")
        else:
            print(arr[i],end=" ")
    print()

def solvebale(start):
    inv=0
    for i in range(9):
        if start[i]==-1:
            continue
        for j in range(i+1,9):
            if start[j]==-1:
                continue
            if start[i]>start[j]:
                inv+=1
    return inv%2==0

def heuristic(start,goal):
    h=0
    global g
    for i in range(9):
        if start[i]!=-1:
            h+=abs(goal.index(start[i])-i)
    return h+g


def moveleft(start,ind):
    start[ind],start[ind-1]=start[ind-1],start[ind]
def moveright(start,ind):
    start[ind],start[ind+1]=start[ind+1],start[ind]
def moveup(start,ind):
    start[ind],start[ind-3]=start[ind-3],start[ind]
def movedown(start,ind):
    start[ind],start[ind+3]=start[ind+3],start[ind]



# def movetile(start,goal):
#     ind=start.index(-1)
#     row=ind//3
#     col=ind%3
#     t1=t2=t3=t4=start[:]
#     f1=f2=f3=f4=float('inf')
#     if col-1>=0:
#         moveleft(t1,ind)
#         f1=heuristic(t1,goal)
#     if col+1<3:
#         moveright(t2,ind)
#         f2=heuristic(t2,goal)
#     if row-1>=0:
#         moveup(t4,ind)
#         f4=heuristic(t4,goal)
#     if row+1<3:
#         movedown(t3,ind)
#         f3=heuristic(t3,goal)

#     mini = min(f1,f2,f3,f4)
#     if mini==f1:
#         moveleft(start,ind)
#     elif mini==f2:
#         moveright(start,ind)
#     elif mini==f4:
#         moveup(start,ind)
#     elif mini==f3:
#         movedown(start,ind)
    
def movetile(start, goal):
    emptyat = start.index(-1)
    row = emptyat // 3
    col = emptyat % 3
    t1, t2, t3, t4 = start[:], start[:], start[:], start[:]
    f1, f2, f3, f4 = float('inf'), float('inf'), float('inf'), float('inf')

    if col - 1 >= 0:
        moveleft(t1, emptyat)
        f1 = heuristic(t1, goal)
    if col + 1 < 3:
        moveright(t2, emptyat)
        f2 = heuristic(t2, goal)
    if row + 1 < 3:
        movedown(t3, emptyat)
        f3 = heuristic(t3, goal)
    if row - 1 >= 0:
        moveup(t4, emptyat)
        f4 = heuristic(t4, goal)

    min_heuristic = min(f1, f2, f3, f4)

    if f1 == min_heuristic:
        moveleft(start, emptyat)
    elif f2 == min_heuristic:
        moveright(start, emptyat)
    elif f3 == min_heuristic:
        movedown(start, emptyat)
    elif f4 == min_heuristic:
        moveup(start, emptyat)

def solveEight(start,goal):
    global g
    g+=1
    movetile(start,goal)
    show_board(start)
    f=heuristic(start,goal)
    if f==g:
        print("done")
        return
    solveEight(start,goal)


def main():
    global g
    start=[]
    goal=[]
    for i in range(9):
        start.append(int(input()))
    for i in range(9):
        goal.append(int(input()))
    show_board(start)

    if solvebale(start):
        solveEight(start,goal)
        print("YES")
    else:
        print("not possible")
main()