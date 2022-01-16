This is the group Assignment 2 from the U of T course *CSC148 - Introduction to Computer Science*, which demonstrates the process of puzzle-solving by programming two puzzle solvers accoding to **Depth-First Search** and **Breadth-First Search**.

## Introduction

This assignment investigates a class of puzzles that have the following features in common:

- full information: all information about the puzzle state at any given point is visible to the solver; there are no hidden or random aspects
- well-defined extensions: a definition of legal "extensions" from a given puzzle state to new states is given 
- well-defined solution: a definition of what it means for the puzzle to be in a solved state is given 

These features are common to a very large class of puzzles: crosswords, sudoku, peg solitaire, verbal arithmetic, and so on. The general puzzle solvers built are designed to work for all puzzles of this sort.

## 3 Main Puzzles
### Sudoku 
This puzzle commonly appears in print media and online. They are presented with an n × n grid with some symbols, for example digits or letters, filled in. The symbols must be from a set of n symbols. The goal is to fill in the remaining symbols in such a way that each row, column, and subsquare, contains each symbol exactly once. In order for all of that to make sense, n must be a square integer such as 4, 9, 16, or 25.

### Word Ladder 
This puzzle involves transforming one word into a target word by changing one letter at a time. Each word must belong to a specified set of valid words. Here’s an example where we assume that the set of valid words is a rather large set of common English words, and the goal is to get from the word ‘cost’ to the word ‘save’:

cost → cast → case → cave → save

### Expression Tree Puzzle 
This puzzle consists of an algebraic equation containing one or more variables, and a target value. The puzzle is solved when the variables are assigned values such that the expression evaluates to the target value.

## The Solvers
Solving a puzzle can be done by systematically searching for a solution, starting from its current state. To make this daunting task even possible, we have to be sure that we have a systematic way of exploring all possible puzzle states - without needlessly re-visiting the same state twice. We implemented two search techniques: **depth-first search**, **breadth-first search**.

## Module Description
**Try running any of the following modules to play with different puzzles with solvers.**
- *play_sudoku.py* contains a simple GUI to let you try playing the sudoku puzzle. It makes use of the solvers in two ways: (1) to create a random SudokuPuzzle of a selected difficulty level and (2) to provide you with hints as you try solving the puzzle.
- *play_word_ladder.py* contains a simple text UI to let you try playing the word ladder puzzle It makes use of the solvers in two ways: (1) to create a random WordLadderPuzzle of a selected difficulty level and (2) to provide you with hints if you get stuck solving the puzzle.
- *play_expression_tree.py* contains a simple GUI to let you try playing the expression tree puzzle. It makes use of the solvers to provide you with hints.
- *experiment.py* runs a small experiment and produces output that you can review how the solvers perform on different puzzles.
