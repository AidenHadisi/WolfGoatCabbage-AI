

#Author: Aiden Hadisi
from search import *
class WolfGoatCabbage(Problem):
    #[Farmer, Goat, Wolf, Cabbage]
    def __init__(self, initial=(False, False, False, False), goal=(True, True, True, True)):
        super().__init__(initial, goal)
    def goal_test(self, state):
        return state == self.goal
    
    def result(self, state, action):
        #Simply flip to the opposite
        state = list(state)
        if('F' in action):
            state[0] = not state[0]
        if('G' in action):
            state[1] = not state[1]
        if('W' in action):
            state[2] = not state[2]
        if('C' in action):
            state[3] = not state[3]
        return tuple(state)
    
    def validState(self, state):
        #state not valid if goat and cabbage or goat and wolf are on one side and farmer is on the other side
        if(state[0] != state[1] and state[0] != state[2]):
            return False
        
        if(state[0] != state[1] and state[0] != state[3]):
            return False
        return True
        
        
    def actions(self, state): 
        possible_actions = []
        state = list(state)
        new_state = [not state[0]] + state[1:]
        
        #Farmer crosses alone
        if(self.validState(new_state)):
            possible_actions.append({'F'})
        
        #farmer and goat cross if valid
        if(state[0] == state[1]):
            new_state = [not state[0]] + [not state[1]] + state[2:]
            if(self.validState(new_state)):
                possible_actions.append({'F', 'G'})
        
        #farmer and wolf cross if valid
        if(state[0] == state[2]):
            new_state = [not state[0]] + state[1:2] + [not state[2]] + state[3:]
            if(self.validState(new_state)):
                possible_actions.append({'F', 'W'})
   
        #farmer and cabbage cross if valid
        if(state[0] == state[3]):
            new_state = [not state[0]] + state[1:3] + [not state[3]] 
            if(self.validState(new_state)):
                possible_actions.append({'F', 'C'})
   
       
        return possible_actions

def fancyPrint(solution):
    crossed = set()
    for action in solution:
        if action == {'F'}:
            if action.issubset(crossed):
                print('Farmer crosses back')
                crossed = crossed - action
            else:
                print('Farmer crosses')
                crossed = crossed.union(set(action))
        elif action == {'F', 'G'}:
            if action.issubset(crossed):
                print('Farmer and Goat cross back')
                crossed = crossed - action
            else:
                print('Farmer and Goat cross')
                crossed = crossed.union(set(action))
        elif action == {'F', 'W'}:
            if action.issubset(crossed):
                print('Farmer and Wolf cross back')
                crossed = crossed - action
            else:
                print('Farmer and Wolf cross')
                crossed = crossed.union(set(action))
        elif action == {'F', 'C'}:
            if action.issubset(crossed):
                print('Farmer and Cabbage cross back')
                crossed = crossed - action
            else:
                print('Farmer and Cabbage cross')
                crossed = crossed.union(set(action))
            
if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print("DEPTH FIRST:")
    fancyPrint(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print("\n")
    print("BREADTH FIRST:")
    fancyPrint(solution)
        
    
 
        
    
    
    
    