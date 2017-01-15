# pieces.py
# -*- coding: utf-8 -*-
# @Author: Sidharth Mishra
# @Date:   2017-01-12 17:38:36
# @Last Modified by:   Sidharth Mishra
# @Last Modified time: 2017-01-14 15:00:19

__author__ = """Sidharth Mishra"""
__email__ = 'sidharth.mishra@sjsu.edu'
__version__ = '0.0.1'

# used to make the class an abstract base class in python
# Note - In python, if a class inheriting the abc.ABC doesn't have
# abstract methods, it can be instantiated, but if it has abstract methods
# it cannot be instantiated. Even the subclass cannot be instantiated if
# the concrete implementation of the abstract method is not assigned.
# abc module provides the AbstractBaseClass class and abstractmethod decorator
# implementations.

from abc import ABC, abstractmethod

'''
This module contains the implementations for all the pieces of chess. Since the \
Chess pieces have different behaviors, we cannot follow the type as object pattern \
instead we have to follow Subclass pattern. Pieces are extended by Pawn, Knight,\
Bishop, Queen, Rook and King. Since each piece moves differently and has different\
properties, they need to be subclasses instead of types as object.
'''


class Piece(object):
  '''
  The base class for all the chess pieces.
  '''
  def __init__(self, xpos, ypos, color):
    '''
    Takes the xpos and ypos of the piece as initial parameters.\
    Since the coordinate of the piece needs to be stored. Need the \
    color of the piece.
    '''

    self.__xpos = xpos
    self.__ypos = ypos
    self.__color = color

class Pawn(Piece):
  '''
  The Pawn piece class.
  '''

  def __init__(self, xpos, ypos, color):
    'Initializes a pawn on the chess board.'
    super().__init__(xpos, ypos, color)

class Knight(Piece):
  '''
  The Knight piece class.
  '''

  pass

class Bishop(Piece):
  '''
  The Bishop piece class.
  '''

  pass

class Rook(Piece):
  '''
  The Rook piece class.
  '''

  pass

class Queen(Piece):
  '''
  The Queen piece class.
  '''

  pass

class King(Piece):
  '''
  The King piece class.
  '''
  
  pass


