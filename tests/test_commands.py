import pytest

from fifth import (CMDError, cmd_push, cmd_pop, cmd_add, cmd_divide)


def test_cmd_push(stack):
    cmd_push(stack, '3 4 5')
    assert str(stack) == '[3, 4, 5]'


def test_cmd_push_raises_cmderror_when_non_int_args(stack):
    with pytest.raises(CMDError):
        cmd_push(stack, '1 2 three')


def test_cmd_pop(stack):
    cmd_push(stack, '3 4')
    cmd_pop(stack, '')
    assert str(stack) == '[3]'


def test_cmd_add(stack):
    cmd_push(stack, '3 4')
    cmd_add(stack, '')
    assert str(stack) == '[7]'


def test_cmd_divide_raises_cmderror_when_division_by_zero(stack):
    cmd_push(stack, '0 3')
    with pytest.raises(CMDError):
        cmd_divide(stack, '')
