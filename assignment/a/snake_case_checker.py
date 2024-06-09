# snake_case_checker.py

from pylint.checkers import BaseChecker, utils
from pylint.interfaces import IAstroidChecker
import re

class SnakeCaseChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = 'snake_case_checker'
    priority = -1
    msgs = {
        'C9001': (
            'Function name "%s" does not follow snake_case naming style',
            'snake-case',
            'All function names should follow the snake_case naming convention',
        ),
    }

    def __init__(self, linter=None):
        super().__init__(linter)
        self.snake_case_regex = re.compile(r'^[a-z_][a-z0-9_]*$')

    @utils.check_messages('snake-case')
    def visit_functiondef(self, node):
        function_name = node.name
        if not self.snake_case_regex.match(function_name):
            self.add_message('snake-case', node=node, args=(function_name,))

def register(linter):
    linter.register_checker(SnakeCaseChecker(linter))
