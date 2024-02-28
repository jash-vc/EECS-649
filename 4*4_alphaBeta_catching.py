# Author - Jash Miteshkumar Patel
# Date - February 28, 2024
# Title - 4*4 Tic tac toe using Memoziation
from time import time

BLANK = ' '
PRINT = 2000000

states_examined = 0
seen_set = set()
seen_list = []
terminals_found = 0
start_time = time()

# Memoization cache
memoization_cache = {}

def init_globals():
    global states_examined, seen_set, seen_list, terminals_found, start_time
    states_examined = 0
    seen_set = set()
    seen_list = []
    terminals_found = 0
    start_time = time()

def print_globals():
    global states_examined, seen_set, seen_list, terminals_found
    print("states / terminals / unique states / time elapsed (s)", states_examined, terminals_found, len(seen_set), time()-start_time)
    print("\n")

def is_terminal(state):
    blanks = state.count(BLANK)
    # Adjust the condition for a win in 4x4
    if blanks > 8: return False
    if blanks == 0: return True
    # Check for 4 in a row
    if state[0:4] == 'XXXX' or state[0:4] == 'OOOO': return True
    if state[4:8] == 'XXXX' or state[4:8] == 'OOOO': return True
    if state[8:12] == 'XXXX' or state[8:12] == 'OOOO': return True
    if state[12:16] == 'XXXX' or state[12:16] == 'OOOO': return True
    # Check for 4 in a column
    if state[0]+state[4]+state[8]+state[12] == 'XXXX' or state[0]+state[4]+state[8]+state[12] == 'OOOO': return True
    if state[1]+state[5]+state[9]+state[13] == 'XXXX' or state[1]+state[5]+state[9]+state[13] == 'OOOO': return True
    if state[2]+state[6]+state[10]+state[14] == 'XXXX' or state[2]+state[6]+state[10]+state[14] == 'OOOO': return True
    if state[3]+state[7]+state[11]+state[15] == 'XXXX' or state[3]+state[7]+state[11]+state[15] == 'OOOO': return True
    # Check for 4 in a diagonal
    if state[0]+state[5]+state[10]+state[15] == 'XXXX' or state[0]+state[5]+state[10]+state[15] == 'OOOO': return True
    if state[3]+state[6]+state[9]+state[12] == 'XXXX' or state[3]+state[6]+state[9]+state[12] == 'OOOO': return True
    return False

def utility(state):
    umap = {True: 1, False: -1}
    # Check for 4 in a row
    if state[0:4] == 'XXXX' or state[0:4] == 'OOOO': return umap[state[0] == 'X']
    if state[4:8] == 'XXXX' or state[4:8] == 'OOOO': return umap[state[4] == 'X']
    if state[8:12] == 'XXXX' or state[8:12] == 'OOOO': return umap[state[8] == 'X']
    if state[12:16] == 'XXXX' or state[12:16] == 'OOOO': return umap[state[12] == 'X']
    # Check for 4 in a column
    if state[0]+state[4]+state[8]+state[12] == 'XXXX' or state[0]+state[4]+state[8]+state[12] == 'OOOO': return umap[state[0] == 'X']
    if state[1]+state[5]+state[9]+state[13] == 'XXXX' or state[1]+state[5]+state[9]+state[13] == 'OOOO': return umap[state[1] == 'X']
    if state[2]+state[6]+state[10]+state[14] == 'XXXX' or state[2]+state[6]+state[10]+state[14] == 'OOOO': return umap[state[2] == 'X']
    if state[3]+state[7]+state[11]+state[15] == 'XXXX' or state[3]+state[7]+state[11]+state[15] == 'OOOO': return umap[state[3] == 'X']
    # Check for 4 in a diagonal
    if state[0]+state[5]+state[10]+state[15] == 'XXXX' or state[0]+state[5]+state[10]+state[15] == 'OOOO': return umap[state[0] == 'X']
    if state[3]+state[6]+state[9]+state[12] == 'XXXX' or state[3]+state[6]+state[9]+state[12] == 'OOOO': return umap[state[3] == 'X']
    return 0

def new_node(state):
    global states_examined, seen_set, seen_list
    states_examined += 1
    seen_set.add(state)
    # Uncomment to save memory
    # seen_list.append(state)
    if states_examined % PRINT == 0:
        print("... states examined =", states_examined, ", terminals found =", terminals_found, ", unique stored =", len(seen_set), ", time elapsed (s) =", time()-start_time)

def next_state(state, move):
    assert state[move] == BLANK
    if state.count(BLANK) % 2 == 1:
        turn = 'X'
    else:
        turn = 'O'
    new_state = state[:move] + turn + state[move+1:]
    return new_state

def get_available_moves(state):
    return [i for i in range(len(state)) if state[i] == BLANK]

def alpha_beta_search(state, alpha=float('-inf'), beta=float('inf')):
    global terminals_found
    if state in memoization_cache:
        return memoization_cache[state]

    if is_terminal(state):
        terminals_found += 1
        value = utility(state)
        memoization_cache[state] = value
        return value

    moves = get_available_moves(state)
    best_score = float('-inf')

    for move in moves:
        new_state = next_state(state, move)
        new_node(new_state)
        score = min_value_alpha_beta(new_state, alpha, beta)
        if score > best_score:
            best_moves = [move]
            best_score = score
        elif score == best_score:
            best_moves.append(move)

        alpha = max(alpha, best_score)
        if best_score >= beta:
            break

    result = (best_score, best_moves)
    memoization_cache[state] = result
    return result

def min_value_alpha_beta(state, alpha, beta):
    global terminals_found
    if state in memoization_cache:
        return memoization_cache[state]

    if is_terminal(state):
        terminals_found += 1
        value = utility(state)
        memoization_cache[state] = value
        return value

    value = float('inf')
    moves = get_available_moves(state)

    for move in moves:
        new_state = next_state(state, move)
        new_node(new_state)
        score = max_value_alpha_beta(new_state, alpha, beta)
        value = min(value, score)

        beta = min(beta, value)
        if value <= alpha:
            break

    memoization_cache[state] = value
    return value

def max_value_alpha_beta(state, alpha, beta):
    global terminals_found
    if state in memoization_cache:
        return memoization_cache[state]

    if is_terminal(state):
        terminals_found += 1
        value = utility(state)
        memoization_cache[state] = value
        return value

    value = float('-inf')
    moves = get_available_moves(state)

    for move in moves:
        new_state = next_state(state, move)
        new_node(new_state)
        score = min_value_alpha_beta(new_state, alpha, beta)
        value = max(value, score)

        alpha = max(alpha, value)
        if value >= beta:
            break

    memoization_cache[state] = value
    return value

def print_out(state):
    for r in range(4):
        for c in range(4):
            if c < 3:
                endchar = '|'
            else:
                endchar = '\n'
            print(' ' + state[r*4+c] + ' ', end=endchar)
        if r < 3:
            print(('-'*3+'+')*3 + '-'*3)

test_boards_4x4 = [BLANK*4+'OXXO'+'OXXO'+BLANK*4, 'X'+BLANK*15]

for init in test_boards_4x4:
    init_globals()
    print_out(init)
    print("value of game, move =", alpha_beta_search(init))
    print_globals()
