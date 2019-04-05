from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import yes_no_dialog

from core.stack import FifthStack


class CMDError(Exception):
    pass


def cmd_push(stack: FifthStack, args_str: str) -> None:
    """ Pushes the arguments to the top of the stack  """
    try:
        args = [int(arg.strip()) for arg in args_str.split()]
    except ValueError:
        raise CMDError
    for arg in args:
        stack.push(arg)
    return None


def cmd_pop(stack: FifthStack, args_str: str) -> None:
    """ Removes the top element of the stack """
    stack.pop()
    return None


def cmd_swap(stack: FifthStack, args_str: str) -> None:
    """ Swaps the top two elements of the stack """
    a, b = stack.pop2()
    stack.push(a)
    stack.push(b)
    return None


def cmd_dup(stack: FifthStack, args_str: str) -> None:
    """ Duplicats the top element of the stack """
    a = stack.pop()
    stack.push(a)
    stack.push(a)
    return None


def cmd_add(stack: FifthStack, args_str: str) -> None:
    """
    Adds the top two elements of the stack and pushes the
    result to the top.
    """
    a, b = stack.pop2()
    stack.push(a + b)
    return None


def cmd_substract(stack: FifthStack, args_str: str) -> None:
    """
    Substracts the second element from the top element and
    pushes the result to the top.
    """
    a, b = stack.pop2()
    stack.push(a - b)
    return None


def cmd_multiply(stack: FifthStack, args_str: str) -> None:
    """
    Multiplies the top two elements of the stack and pushes
    the result to the top.
    """
    a, b = stack.pop2()
    stack.push(a * b)
    return None


def cmd_divide(stack: FifthStack, args_str: str) -> None:
    """
    Divies the top element by the next element, rounding down, and
    pushes the result to the top of the stack.
    """
    a, b = stack.pop2()
    try:
        stack.push(int(a / b))
    except ZeroDivisionError:
        raise CMDError
    return None


class CLI:
    def __init__(self):
        self.stack = FifthStack()
        self.commands = {
            'PUSH': cmd_push,
            'POP': cmd_pop,
            'SWAP': cmd_swap,
            'DUP': cmd_dup,
            '+': cmd_add,
            '-': cmd_substract,
            '*': cmd_multiply,
            '/': cmd_divide,
        }

    def prompt(self) -> str:
        print('stack is: {}'.format(self.stack))
        return prompt('> ')

    def eval(self) -> str:
        answer = self.prompt().upper().strip()
        cmd, _, args = answer.partition(' ')
        if cmd in self.commands:
            self.stack.save_snapshot()
            try:
                self.commands[cmd](self.stack, args)
            except (IndexError, CMDError):
                self.stack.rollback()
                print('ERROR')
        return answer

    def repl(self) -> None:
        while True:
            answer = self.eval()
            if answer == 'QUIT' and yes_no_dialog(
                title="Confirm exit",
                text="Are you sure you want to quit?",
            ):
                break


if __name__ == '__main__':
    cli = CLI()
    cli.repl()
