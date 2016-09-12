import solver


def init_state():
    return 4


def primitive(state):
    return solver.UNDECIDED if state else solver.LOSS


def gen_moves(state):
    return [move for move in [-1, -2] if state + move >= 0]


def do_move(state, move):
    return state + move


print(solver.solver(init_state, primitive, gen_moves, do_move))
