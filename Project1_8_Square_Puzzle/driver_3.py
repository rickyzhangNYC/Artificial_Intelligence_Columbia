import queue
import time

class Node:
    def __init__( self, state, parent, direction, depth, cost ):
        # Contains the state of the node
        self.state = state
        # Contains the node that generated this node
        self.parent = parent
        # Contains the operation that generated this node from the parent
        self.direction = direction
        # Contains the depth of this node (parent.depth +1)
        self.depth = depth
        # Contains the path cost of this node from depth 0. Not used for depth/breadth first.
        self.cost = cost
    def __hash__(self):
        return self.state.__hash__
    def __str__(self):
        return (self.state,self.direction,self.depth,self.cost)

def createNode(state, parent, direction, depth, cost):
        return Node(state, parent, direction, depth, cost)
 
def expandNode(parentnode) :
    #Expand the current node as the parent. Create an empty list and append children into the list.
    expanded_nodes = []
    upNode = up(parentnode.state)
    downNode = down(parentnode.state)
    leftNode = left(parentnode.state)
    rightNode = right(parentnode.state)
    #If a child node is returned None from createNode() method, do not append to the expanded nodes list.
    if upNode != None:
        expanded_nodes.append(createNode(upNode, parentnode, "u", parentnode.depth + 1, parentnode.cost+1 ) )
    if downNode != None:
        expanded_nodes.append( createNode(downNode, parentnode, "d", parentnode.depth + 1, parentnode.cost+1 ) )
    if leftNode != None:
        expanded_nodes.append( createNode(leftNode, parentnode, "l", parentnode.depth + 1, parentnode.cost+1 ) )
    if rightNode != None:
        expanded_nodes.append( createNode(rightNode, parentnode, "r", parentnode.depth + 1, parentnode.cost+1 ) )
        
    return expanded_nodes

def up(state):
    new_state = state[:]
    index = new_state.index(0)
    
    if index not in [0,1,2]:
        temp = new_state[index-3]
        new_state[index-3] = new_state[index]
        new_state[index] = temp
        
        return new_state
    else:
        return None

def down(state):
    new_state = state[:]
    index = new_state.index(0)
    
    if index not in [6,7,8]:
        temp = new_state[index+3]
        new_state[index+3] = new_state[index]
        new_state[index] = temp
        
        return new_state
    else:
        return None

def left(state):
    new_state = state[:]
    index = new_state.index(0)
    
    if index not in [0,3,6]:
        temp = new_state[index-1]
        new_state[index-1] = new_state[index]
        new_state[index] = temp
        
        return new_state
    else:
        return None

def right(state):        
    new_state = state[:]
    index = new_state.index(0)
    
    if index not in [2,5,8]:
        temp = new_state[index+1]
        new_state[index+1] = new_state[index]
        new_state[index] = temp
        
        return new_state
    else:
        return None   

def printParent(nodeToExplore):
    if nodeToExplore.parent == None:
        return
    else:
        printParent(nodeToExplore.parent)
        print(nodeToExplore.direction, ' ,' , end = " ")

def checkRepeat(expandedNodeList,exploredStates,frontierStates):
    temp = []

    for x in expandedNodeList:
        temp.append(x)

    for expN in temp:
        if expN.state in exploredStates or expN.state in frontierStates:
            expandedNodeList.remove(expN)
    
    for n in expandedNodeList:
            frontierStates.append(n.state)

def goalFound(nodeToExplore,explored,end,start):
    directionList = []
    directionList.insert(0,nodeToExplore.direction)
    parentNode = nodeToExplore.parent
    print('path_to_goal : ', end = " ")
    printParent(nodeToExplore.parent)
    print(nodeToExplore.direction)
    print('cost_of_path: ', nodeToExplore.cost)
    print('nodes_expanded: ', len(explored))
    print('max_search_depth: ', nodeToExplore.depth+1)
    print('time_elapsed: ', end-start)

def BFSexplore(initialState, goalState):
    # Initialize lists, start timer
    start = time.time()
    # frontier - List of nodes in the frontier (to be explored)
    frontier = []
    # explored - List of nodes that have been explored/expanded
    explored = []
    # exploredStates - List of states that correlate to the explored list
    exploredStates = []
    # frontierStates - List of states that correlate to the frontier list
    frontierStates = []

    # Append starting node
    startingnode = (createNode(initialState, None, None, 0, 0))
    frontier.append(startingnode)
    frontierStates.append(startingnode.state)
    # Loop until frontier is empty or goalState is found
    while(len(frontier) != 0):
        # Dequeue from frontier and state list
        nodeToExplore = frontier.pop(0)
        frontierStates.pop(0)
        # Check if goal is been found
        if nodeToExplore.state == goalState:
            # Stop timer
            end = time.time()
            # goalFound method to print information/statistics
            goalFound(nodeToExplore,explored,end,start)
            return nodeToExplore
        
        else:
            # If goal not found, explore/expand the node
            explored.append(nodeToExplore)
            exploredStates.append(nodeToExplore.state)
            expandedNodeList = expandNode(nodeToExplore)
            # checkRepeat method used to check if list of expanded node states are already in the respective frontier/explored lists
            checkRepeat(expandedNodeList,exploredStates,frontierStates)
            # Add expanded nodes to the frontier
            frontier = frontier + expandedNodeList
            
    return None

def DfsExplore(initialState,goalState):
    start = time.time()
    frontier = []
    explored = []
    exploredStates = []
    frontierStates = []

    startingnode = (createNode(initialState, None, None, 0, 0))
    frontier.append(startingnode)
    frontierStates.append(startingnode.state)

    while(len(frontier) != 0):
        nodeToExplore = frontier.pop(0)
        frontierStates.pop(0)
        explored.append(nodeToExplore)
        exploredStates.append(nodeToExplore.state)

        if nodeToExplore.state == goalState:
            end = time.time()
            directionList = []
            directionList.insert(0,nodeToExplore.direction)
            parentNode = nodeToExplore.parent
            print('path_to_goal : ', end = " ")
            printParent(nodeToExplore.parent)
            print(nodeToExplore.direction)
            print('cost_of_path: ', nodeToExplore.cost)
            print('nodes_expanded: ', len(explored))
            print('max_search_depth: ', nodeToExplore.depth+1)
            print('time_elapsed: ', end-start)
            return nodeToExplore
        
        else:
            
            expandedNodeList = expandNode(nodeToExplore)
            temp = []

            for x in expandedNodeList:
                temp.append(x)

            for expN in temp:
                if expN.state in exploredStates or expN.state in frontierStates:
                    expandedNodeList.remove(expN)
            
            for n in expandedNodeList:
                frontierStates.append(n.state)

            frontier = expandedNodeList + frontier
            
    return None


def main():
    
    initialState = [6,1,8,4,0,2,7,3,5]
    goalState = [0,1,2,3,4,5,6,7,8]
    resultNode = BFSexplore(initialState,goalState)
    # resultNode2 = DfsExplore(initialState,goalState)

if __name__ == '__main__':
    main() 