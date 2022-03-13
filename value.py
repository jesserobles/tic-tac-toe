from constants import max_agent, min_agent
from max_value import max_value
from min_value import min_value
from terminal import terminal
from utility import utility


def value(state, agent_making_move):
    print(*state, sep='\n')
    if terminal(state):
        return utility(state)
    elif agent_making_move == max_agent:
        return max_value(state)
    elif agent_making_move == min_agent:
        return min_value(state)
