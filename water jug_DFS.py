#capacities of two jud
CAP_A=4
CAP_B=3

#goal amount
GOAL=2

#function to print the state
def print_state(state):
    print("Jug A :",state[0],"liters")
    print("Jug B :",state[1],"liters")
    print()

#general all posible moves
def get_neighbors(state):
    neighbors=[]
    a,b=state

    if a<CAP_A:
        neighbors.append(((CAP_A,b),"fill jug A"))

    if b<CAP_B:
        neighbors.append(((a,CAP_B),"fill jug B"))

    #3. empty jug A
    if a>0:
        neighbors.append(((0,b),"empty jug A"))

    #4. empty jug B
    if b>0:
        neighbors.append(((a,0),"empty jug B"))

    #5. pour jug A->jug B
    amount=min(a,CAP_B-b)

    if amount>0:
        neighbors.append(((a-amount,b+amount),"pour jug A->jug B"))

    #6. pour jug B-> jug A
    amount=min(b,CAP_A-a)

    if amount>0:
        neighbors.append(((a+amount,b-amount),"pour jug B->jug A"))

    return neighbors

#BFS algorithm
def dfs(start):
    stack=[(start,[])]
    visited=set()

    while stack:
        state,path=stack.pop()
        if state in visited:
            continue
        visited.add(state)

        #check goal
        if state[0]==GOAL or state[1]==GOAL:
            return path+[(state,"goal reached")]

        #general neighbors
        for neighbor,action in reversed(get_neighbors(state)):
            if neighbor not in visited:
                stack.append((neighbor,path+[(neighbor,action)]))
    return None

#starting state
start=(0,0)

#run DFS
solution=dfs(start)

#print solution
if solution:
    print("solution found in ",len(solution)-1,"moves:\n")
    print("initial state:")
    print_state(start)

    for state,action in solution:
        print(action)
        print_state(state)
else:
    print("no solution found...!")
        
        
