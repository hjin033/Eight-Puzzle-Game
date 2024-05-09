import heapq
import time

#Command Line Interface
def main():
    print("Enter the initial state of the puzzle.")
    print("Use 0 to represent empty space.")
    print("Use comma to separate the numbers.")
    row_one = input("Enter the first row: ")
    row_two = input("Enter the second row: ")
    row_three = input("Enter the third row: ")
    
    row_one = row_one.split(',')
    row_two = row_two.split(',')
    row_three = row_three.split(',')
    
    complete_puzzle = [row_one, row_two, row_three]
    
    print(complete_puzzle)
    
    print("Which search algorithm do you want to use?")
    print("1) Uniform Cost Search")
    print("2) A* with Misplaced Tile heuristic")
    print("3) A* with Manhanttan Distance heuristic")
    
    choice = input()
    
    empty_loc = find_zero(complete_puzzle)
    start= time.time()
    if choice == '1':
        uniform_cost(complete_puzzle, empty_loc)
    if choice == '2':
        misplaced(complete_puzzle, empty_loc)
    if choice == '3':
        manhattan(complete_puzzle, empty_loc)
    print("Time: " + str(time.time() - start))
    
    

def uniform_cost(initial, empty_loc):
    initial_state = puzzleState(initial, 0, 0, empty_loc)
    min_que = []
    visited = []
    heapq.heapify(min_que)
    heapq.heappush(min_que, initial_state)
    
    goal = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']]
    
    count = 0
    
    while True:
        if len(min_que) == 0:
            break
        
        current = heapq.heappop(min_que)
        temp = [row[:] for row in current.state]
        visited.append(temp)
        print("The puzzle state to be expanded:")
        print_puzzle(current.state)
        print("g(n) is " + str(current.g_n))
        print("")
        
        if current.state == goal:
            print("Goal Reached!")
            print("States expanded: " + str(count))
            print("Optimal Solution Depth: " + str(current.g_n))
            break
    
        count += 1

        #Expand the legal and non-repeating states
        if current.empty_loc[0] > 0:
            new_state = move_up(current.state, current.empty_loc)
            if not checkVisited(visited, new_state):
                heapq.heappush(min_que, puzzleState(new_state[:], current.g_n + 1, 0, move_up_empty(current.empty_loc)))
           
        if current.empty_loc[1] > 0:
            new_state = move_left(current.state, current.empty_loc)
            if not checkVisited(visited, new_state):
                heapq.heappush(min_que, puzzleState(new_state[:], current.g_n + 1, 0, move_left_empty(current.empty_loc)))
        
        if current.empty_loc[0] < len(current.state) - 1:
            new_state = move_down(current.state, current.empty_loc)
            if not checkVisited(visited, new_state):
                heapq.heappush(min_que, puzzleState(new_state[:], current.g_n + 1, 0, move_down_empty(current.empty_loc)))
            
        if current.empty_loc[1] < len(current.state[0]) - 1:
            new_state = move_right(current.state, current.empty_loc)
            if not checkVisited(visited, new_state):
                heapq.heappush(min_que, puzzleState(new_state[:], current.g_n + 1, 0, move_right_empty(current.empty_loc)))
                
    

def misplaced(initial, empty_loc):
    initial_state = puzzleState(initial, 0, misplaced_count(initial), empty_loc)
    min_que = []
    visited = []
    heapq.heapify(min_que)
    heapq.heappush(min_que, initial_state)
    
    goal = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']]
    
    count = 0
    
    while True:
        if len(min_que) == 0:
            break
        
        current = heapq.heappop(min_que)
        temp = [row[:] for row in current.state]
        visited.append(temp)
        
        print("The puzzle state to be expanded:")
        print_puzzle(current.state)
        print("g(n) is " + str(current.g_n))
        print("h(n) is " + str(current.h_n))
        print("")
        
        if current.state == goal:
            print("Goal Reached!")
            print("States expanded: " + str(count))
            print("Optimal Solution Depth: " + str(current.g_n))
            break
        
        count += 1

        #Expand the legal and non-repeating states
        if current.empty_loc[0] > 0:
            new_state = move_up(current.state, current.empty_loc)
            if not checkVisited(visited, new_state):
                heapq.heappush(min_que, puzzleState(new_state[:], current.g_n + 1, misplaced_count(new_state), move_up_empty(current.empty_loc)))
           
        if current.empty_loc[1] > 0:
            new_state = move_left(current.state, current.empty_loc)
            if not checkVisited(visited, new_state):
                heapq.heappush(min_que, puzzleState(new_state[:], current.g_n + 1, misplaced_count(new_state), move_left_empty(current.empty_loc)))
        
        if current.empty_loc[0] < len(current.state) - 1:
            new_state = move_down(current.state, current.empty_loc)
            if not checkVisited(visited, new_state):
                heapq.heappush(min_que, puzzleState(new_state[:], current.g_n + 1, misplaced_count(new_state), move_down_empty(current.empty_loc)))
            
        if current.empty_loc[1] < len(current.state[0]) - 1:
            new_state = move_right(current.state, current.empty_loc)
            if not checkVisited(visited, new_state):
                heapq.heappush(min_que, puzzleState(new_state[:], current.g_n + 1, misplaced_count(new_state), move_right_empty(current.empty_loc)))

def manhattan(initial, empty_loc):
    initial_state = puzzleState(initial, 0, manhattan_distance(initial), empty_loc)
    min_que = []
    visited = []
    heapq.heapify(min_que)
    heapq.heappush(min_que, initial_state)
    
    goal = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']]
    
    count = 0
    
    while True:
        if len(min_que) == 0:
            break
        
        current = heapq.heappop(min_que)
        temp = [row[:] for row in current.state]
        visited.append(temp)
        
        print("The puzzle state to be expanded:")
        print_puzzle(current.state)
        print("g(n) is " + str(current.g_n))
        print("h(n) is " + str(current.h_n))
        print("")
        
        if current.state == goal:
            print("Goal Reached!")
            print("States expanded: " + str(count))
            print("Optimal Solution Depth: " + str(current.g_n))
            break
        
        count += 1

        #Expand the legal and non-repeating states
        if current.empty_loc[0] > 0:
            new_state = move_up(current.state, current.empty_loc)
            if not checkVisited(visited, new_state):
                heapq.heappush(min_que, puzzleState(new_state[:], current.g_n + 1, manhattan_distance(new_state), move_up_empty(current.empty_loc)))
           
        if current.empty_loc[1] > 0:
            new_state = move_left(current.state, current.empty_loc)
            if not checkVisited(visited, new_state):
                heapq.heappush(min_que, puzzleState(new_state[:], current.g_n + 1, manhattan_distance(new_state), move_left_empty(current.empty_loc)))
        
        if current.empty_loc[0] < len(current.state) - 1:
            new_state = move_down(current.state, current.empty_loc)
            if not checkVisited(visited, new_state):
                heapq.heappush(min_que, puzzleState(new_state[:], current.g_n + 1, manhattan_distance(new_state), move_down_empty(current.empty_loc)))
            
        if current.empty_loc[1] < len(current.state[0]) - 1:
            new_state = move_right(current.state, current.empty_loc)
            if not checkVisited(visited, new_state):
                heapq.heappush(min_que, puzzleState(new_state[:], current.g_n + 1, manhattan_distance(new_state), move_right_empty(current.empty_loc)))
    
#Create a new state where empty tile switch with the tile above it
def move_up(state, empty_loc):
    temp = [row[:] for row in state]
    temp[empty_loc[0]][empty_loc[1]] = temp[empty_loc[0] - 1][empty_loc[1]]
    temp[empty_loc[0] - 1][empty_loc[1]] = '0'
            
    return temp

#Update the location of the empty tile after it moved up
def move_up_empty(empty_loc):
    new_empty = empty_loc[:]
    new_empty[0] -= 1
    return new_empty

#Create a new state where empty tile switch with the tile to its left
def move_left(state, empty_loc):
    temp = [row[:] for row in state]
    temp[empty_loc[0]][empty_loc[1]] = temp[empty_loc[0]][empty_loc[1] - 1]
    temp[empty_loc[0]][empty_loc[1] - 1] = '0'
    
    return temp

#Update the location of the empty tile after it moved left
def move_left_empty(empty_loc):
    new_empty = empty_loc[:]
    new_empty[1] -= 1
    return new_empty

#Create a new state where empty tile switch with the tile below it
def move_down(state, empty_loc):
    temp = [row[:] for row in state]
    temp[empty_loc[0]][empty_loc[1]] = temp[empty_loc[0] + 1][empty_loc[1]]
    temp[empty_loc[0] + 1][empty_loc[1]] = '0'
    
    return temp

#Update the location of the empty tile after it moved down
def move_down_empty(empty_loc):
    new_empty = empty_loc[:]
    new_empty[0] += 1
    return new_empty

#Create a new state where empty tile switch with the tile to its right
def move_right(state, empty_loc):
    temp = [row[:] for row in state]
    temp[empty_loc[0]][empty_loc[1]] = temp[empty_loc[0]][empty_loc[1] + 1]
    temp[empty_loc[0]][empty_loc[1] + 1] = '0'
    
    return temp

#Update the location of the empty tile after it moved right
def move_right_empty(empty_loc):
    new_empty = empty_loc[:]
    new_empty[1] += 1
    return new_empty

#find the location of the zero.
def find_zero(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == '0':
                empty_loc = [i, j]
    
    return empty_loc

#print the puzzle state in 2d format
def print_puzzle(puzzle):
    for i in range(len(puzzle)):
        print(puzzle[i])

#calculate the number of misplaced tiles
def misplaced_count(puzzle):
    count = 0
    goal = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']]
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] != '0':
                if puzzle[i][j]!= goal[i][j]:
                    count += 1
    
    return count

#calculate the manhattan distance
def manhattan_distance(puzzle):
    count = 0
    goal = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']]
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] != '0':
                if puzzle[i][j]!= goal[i][j]:
                    row = (int(puzzle[i][j]) - 1) // 3
                    col = (int(puzzle[i][j]) % 3) - 1
                    if col == -1:
                        col = len(puzzle[0]) - 1 
                    count += abs(row - i) + abs(col - j)
    
    return count

#check if it is visited
def checkVisited(li, puzzle):
    for i in range(len(li)):
        if puzzle == li[i]:
            return True
    return False

#Puzzle state class
#State -> store the current puzzle
#g_n -> store the total opertaion cost to this state
#h_n -> store the heuristic cost of this state
#empty_loc -> store the empty tile location
class puzzleState:
    def __init__(self, state, g_n, h_n, empty_loc):
        self.state = state
        self.g_n = g_n
        self.h_n = h_n
        self.empty_loc = empty_loc[:]
    
    #Compare the sum of g(n) and h(n) for heapq    
    def __lt__(self, other):
        return self.g_n + self.h_n < other.g_n + other.h_n


if __name__ == "__main__":
    main()