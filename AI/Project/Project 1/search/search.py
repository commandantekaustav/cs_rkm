# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

#    print("Start:", problem.getStartState())
 #   print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
  #  print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    explored = []
    node = [problem.getStartState(),[]]
    stack = util.Stack()
    stack.push(node)

    while(True):        #as described in the book
        if(stack.isEmpty()):
            return -1
        else:
            #currentState,path = stack.top()
            top = stack.pop()
            stack.push(top)
            if (top[0] in explored):
                pass
            else:
                explored.append(top[0])
                if(problem.isGoalState(top[0])):
                    return top[1]
                else:
                    stack.pop()
                    for successors in problem.getSuccessors(top[0]):
                        if successors[0] not in explored:
                            stack.push([successors[0],top[1]+[successors[1]]])

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    explored = []
    node = [problem.getStartState(),[]]
    frontier = util.Queue()
    frontier.push(node)

    while(True):
        if(frontier.isEmpty()):
            return -1
        else:
            top = frontier.pop()
            if (top[0] in explored):
                pass
            else:
                explored.append(top[0])
                if(problem.isGoalState(top[0])):
                    return top[1]
                for successors in problem.getSuccessors(top[0]):
                    frontier.push([successors[0],top[1]+[successors[1]]])

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    explored = []
    node = [problem.getStartState(),[]]
    frontier = util.PriorityQueue()
    frontier.push(node,problem.getCostOfActions([]))

    while(True):
        if(frontier.isEmpty()):
            return -1
        else:
            top = frontier.pop()
            if (top[0] in explored):
                pass
            else:
                explored.append(top[0])
                if(problem.isGoalState(top[0])):
                    return top[1]
                for successors in problem.getSuccessors(top[0]):
                    frontier.update([successors[0],top[1]+[successors[1]]],problem.getCostOfActions(top[1]+[successors[1]]))

"""
    explored = []
    node = (problem.getStartState(),[])
    frontier =util.PriorityQueue()
    frontier.push(node,0)

    while (True):
        if(frontier.isEmpty()):
    util.raiseNotDefined()
            return -1
        else:
            top = frontier.pop()
            if(top[0] not in explored):
                explored.append(top[0])
                if(problem.isGoalState(top[0])):
                    return top[1]
                for successors in problem.getSuccessors(top[0]):
                    frontier.update((successors[0],[successors[1]]),problem.getCostOfActions(successors[2]))
"""

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=None):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    explored = []
    node = [problem.getStartState(),[]]
#newedit
    frontier = util.PriorityQueue()
    frontier.push(node,problem.getCostOfActions([])+heuristic(problem.getStartState(),problem))

    while(True):
        if(frontier.isEmpty()):
            return -1
        else:
            top = frontier.pop()
            if (top[0] in explored):
                pass
            else:
                explored.append(top[0])
                if(problem.isGoalState(top[0])):
                    return top[1]
                for successors in problem.getSuccessors(top[0]):
                    frontier.update([successors[0],top[1]+[successors[1]]],problem.getCostOfActions(top[1]+[successors[1]])+heuristic(successors[0],problem))

    util.raiseNotDefined()


#extra content
def greedySearch(problem, heuristic=None):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    explored = []
    node = [problem.getStartState(),[]]
#newedit
    frontier = util.PriorityQueue()
    frontier.push(node,heuristic(problem.getStartState(),problem))

    while(True):
        if(frontier.isEmpty()):
            return -1
        else:
            top = frontier.pop()
            if (top[0] in explored):
                pass
            else:
                explored.append(top[0])
                if(problem.isGoalState(top[0])):
                    return top[1]
                for successors in problem.getSuccessors(top[0]):
                    frontier.update([successors[0],top[1]+[successors[1]]],heuristic(successors[0],problem))

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
greedy = greedySearch