import nose
import fourtozero
import solver
ORIGINAL_DWULT = solver.WIN, solver.LOSS, solver.TIE, solver.DRAW, \
                 solver.UNDECIDED


def losing_state():
    return 0


def test_init_pos():
    assert solver.solver(losing_state, fourtozero.primitive,
                         fourtozero.gen_moves,
                         fourtozero.do_move) == solver.LOSS


def change_dwult():
    solver.WIN = 9
    solver.LOSS = 8
    solver.TIE = 7
    solver.DRAW = 6


def restore_dwult():
    solver.WIN = ORIGINAL_DWULT[0]
    solver.LOSS = ORIGINAL_DWULT[1]
    solver.TIE = ORIGINAL_DWULT[2]
    solver.DRAW = ORIGINAL_DWULT[3]


@nose.with_setup(change_dwult, restore_dwult)
def test_dwult_abstraction():
    assert solver.solver(fourtozero.init_state, fourtozero.primitive,
                         fourtozero.gen_moves,
                         fourtozero.do_move) == solver.WIN
