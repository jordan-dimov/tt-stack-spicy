
def test_stack_push(stack):
    stack.push(3)
    assert str(stack) == "[3]"


def test_stack_pop(stack):
    stack.push(1)
    stack.push(3)
    stack.pop()
    assert str(stack) == "[1]"


def test_stack_pop2(stack):
    stack.push(1)
    stack.push(3)
    stack.pop2()
    assert str(stack) == "[]"


def test_rollback(stack):
    stack.push(1)
    stack.save_snapshot()
    stack.push(2)
    stack.rollback()
    assert str(stack) == "[1]"
