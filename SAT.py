from __future__ import annotations
from typing import List, Dict, Optional, Set

CONJUNCTION = ['not', 'and', 'or']


class SatTree:
    """
    This class represents a 3-SAT problem
    === Instance Attribute ===
    root: The variable or the conjunction of the problem
    children: A list represents clause of this problem
    === Representation Invariant ===
    1) root can be either None or str
    2) children will be empty  if root is None
    3) if root is a str then it will be either an operator from conjunction or
    an alpha numerical variable represents a unknown in the problem
    4) if root is an operator then there must have at least one children
    5) if root is not then it can only has
    """
    _root: Optional[str]
    _children: List[SatTree]

    def __init__(self, root: Optional[str], children: List[SatTree]) -> None:
        """
        Initialize a SAT problem with providing parameters
        """
        self._root = root
        self._children = children

    def is_empty(self) -> bool:
        """
        Return True only if the root is None
        """
        return self._root is None

    def eval(self, env: Dict[str:bool]) -> bool:
        """
        Evaluate all the variables with given environment
        Pre-condition: env contains all the variable for this problem
        """
        # TODO
        pass

    def get_domain(self) -> Set[str]:
        """
        Return all the variables in this problem
        """
        # TODO
        pass

    def __str__(self) -> str:
        """Return a string representation of this problem in a pre-fix style
        >>> a = SatTree('x1', [])
        >>> str(a) == 'x1'
        True
        >>> b = SatTree('and', [SatTree('x1', []), SatTree('x2', []), SatTree('x3', [])])
        >>> str(b) == '(and x1 x2 x3)'
        True
        >>> c = SatTree('not', [b])
        >>> str(c) == '(not (and x1 x2 x3))'
        True
        """
        # TODO
        pass


class SatPuzzle:
    """
    This is a class represents a State of a SAT problem
    === Instance Attribute ===
    _problem: The SAT problem of the puzzle
    _mapping: Current assignment of the variables
    """
    _problem: SatTree
    _mapping: Dict[str, bool]

    def __init__(self, sat: SatTree) -> None:
        """
        Initialize a state with providing SAT Problem
        """
        self._problem = sat
        self._mapping = {}

    def copy_state(self) -> SatPuzzle:
        """
        Return a copy of the current state
        """
        temp = SatPuzzle(self._problem)
        temp._mapping = self._mapping.copy()
        return temp

    def verify_sol(self) -> bool:
        """
        Return whether the current mapping can lead to a valid solution of the
        problem.
        A solution is considered to be valid iff all the variables are assigned
        and the problem can be evaluated to True
        """
        # TODO
        pass

    def __str__(self) -> str:
        """
        Return a string representation of the current state
        The string representation must contain a sorted mapping in the increasing
        order of variable
        """
        acc = []
        for k in sorted(self._mapping):
            acc.append(f'{k}:{self._mapping[k]}')
        return ' '.join(acc)

    def next_states(self) -> List[SatPuzzle]:
        """
        Return a list of possible states that can be reached from current state
        by assigning one unassigned variable
        """
        # TODO
        pass

    def solve(self, visit: Set[str]) -> Optional[SatSolution]:
        """
        This method return a solution to the problem if exists one.
        The returning solution must not appear in visit.
        """
        # TODO
        pass


class SatSolution(SatPuzzle):
    """
    This class represents a solution of a puzzle.  The solution is a special
    child class of a puzzle which is the a possible final state of a puzzle
    === Representation Invariant ===
    self must be a solved state
    Every domain in the problem in assigned with either True or False
    """

    def __init__(self, sat: SatTree, sol_map: Dict[str, bool]):
        SatPuzzle.__init__(self, sat)
        self._mapping = sol_map


class SatSolver:
    """
    This is a solver of the SAT Problem
    === Instance Attribute ===
    puzzle: The Problem to be solved
    _sol: All the solution of the problem
    _curr: The current index of solution
    _called: Whether have I called the solution
    """
    puzzle: SatPuzzle
    _sol: List[SatSolution]
    _curr: int
    _called: bool

    def __init__(self, sat):
        self.puzzle = SatPuzzle(sat)
        self._sol = []
        self._curr = 0
        self._called = False

    def sol(self) -> None:
        """
        Fill in all the solutions into the proper attribute
        """
        # TODO
        pass

    """
    Methods below are used to iterate solutions for this problem, those are
    already implemented for you
    """

    def next_sol(self):
        if not self._called:
            self.sol()
            self._called = True
        if self._curr >= len(self._sol):
            return None
        else:
            temp = self._sol[self._curr]
            self._curr += 1
            return temp

    def solve(self):
        temp = self.next_sol()
        while temp:
            print(f'{str(temp)}\n')
            temp = self.next_sol()


if __name__ == '__main__':
    problem = SatTree('and', [SatTree('or',
                                      [SatTree('x1', []), SatTree('x2', []),
                                       SatTree('x3', [])]), SatTree('or', [
        SatTree('x4', []), SatTree('x5', []), SatTree('x6', [])])])
    solver = SatSolver(problem)
    solver.solve()
