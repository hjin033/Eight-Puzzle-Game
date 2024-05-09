import heapq
import time

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
    '''
    if choice == '2':
        misplaced(complete_puzzle, empty_loc)
    if choice == '3':
        manhattan(complete_puzzle, empty_loc)
    '''
    print("Time: " + str(time.time() - start))
    
    
    
def uniform_cost(initial, empty_loc):
    initial_state = puzzleState(initial, None, 0, 0, empty_loc)
    min_que = []
    heapq.heapify(min_que)
    heapq.heappush(min_que, initial_state)
    
    goal = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']]
    
    count = 0
    
    while True:
        if len(min_que) == 0:
            break
        
        current = heapq.heappop(min_que)
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
    
        if current.empty_loc[0] > 0 and (current.parent == None or current.empty_loc[0] - 1 != current.parent.empty_loc[0]):
            heapq.heappush(min_que, puzzleState(move_up(current.state, current.empty_loc), current, current.g_n + 1, 0, move_up_empty(current.empty_loc)))
           
        if current.empty_loc[1] > 0 and (current.parent == None or current.empty_loc[1] - 1 != current.parent.empty_loc[1]):
            heapq.heappush(min_que, puzzleState(move_left(current.state, current.empty_loc), current, current.g_n + 1, 0, move_left_empty(current.empty_loc)))
        
        if current.empty_loc[0] < len(current.state) - 1 and (current.parent == None or current.empty_loc[0] + 1 != current.parent.empty_loc[0]):
            heapq.heappush(min_que, puzzleState(move_down(current.state, current.empty_loc), current, current.g_n + 1, 0, move_down_empty(current.empty_loc)))
            
        if current.empty_loc[1] < len(current.state[0]) - 1 and (current.parent == None or current.empty_loc[1] + 1 != current.parent.empty_loc[1]):
            heapq.heappush(min_que, puzzleState(move_right(current.state, current.empty_loc), current, current.g_n + 1, 0, move_right_empty(current.empty_loc)))
    


    
def move_up(state, empty_loc):
    temp = [row[:] for row in state]
    temp[empty_loc[0]][empty_loc[1]] = temp[empty_loc[0] - 1][empty_loc[1]]
    temp[empty_loc[0] - 1][empty_loc[1]] = '0'
            
    return temp

def move_up_empty(empty_loc):
    new_empty = empty_loc[:]
    new_empty[0] -= 1
    return new_empty

def move_left(state, empty_loc):
    temp = [row[:] for row in state]
    temp[empty_loc[0]][empty_loc[1]] = temp[empty_loc[0]][empty_loc[1] - 1]
    temp[empty_loc[0]][empty_loc[1] - 1] = '0'
    
    return temp

def move_left_empty(empty_loc):
    new_empty = empty_loc[:]
    new_empty[1] -= 1
    return new_empty

def move_down(state, empty_loc):
    temp = [row[:] for row in state]
    temp[empty_loc[0]][empty_loc[1]] = temp[empty_loc[0] + 1][empty_loc[1]]
    temp[empty_loc[0] + 1][empty_loc[1]] = '0'
    
    return temp

def move_down_empty(empty_loc):
    new_empty = empty_loc[:]
    new_empty[0] += 1
    return new_empty

def move_right(state, empty_loc):
    temp = state[:]
    temp[empty_loc[0]][empty_loc[1]] = temp[empty_loc[0]][empty_loc[1] + 1]
    temp[empty_loc[0]][empty_loc[1] + 1] = '0'
    
    return temp

def move_right_empty(empty_loc):
    new_empty = empty_loc[:]
    new_empty[1] += 1
    return new_empty

def find_zero(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == '0':
                empty_loc = [i, j]
    
    return empty_loc

def print_puzzle(puzzle):
    for i in range(len(puzzle)):
        print(puzzle[i])

class puzzleState:
    def __init__(self, state, parent, g_n, h_n, empty_loc):
        self.state = state
        self.parent = parent
        self.g_n = g_n
        self.h_n = h_n
        self.empty_loc = empty_loc[:]
        
    def __lt__(self, other):
        return self.g_n + self.h_n < other.g_n + other.h_n


if __name__ == "__main__":
    main()