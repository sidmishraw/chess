# gameplay.py
# -*- coding: utf-8 -*-
# @Author: Sidharth Mishra
# @Date:   2017-01-12 17:57:48
# @Last Modified by:   Sidharth Mishra
# @Last Modified time: 2017-01-14 16:42:02


__author__ = """Sidharth Mishra"""
__email__ = 'sidharth.mishra@sjsu.edu'
__version__ = '0.0.1'


# The board consists of 8 x 8 squares (of white/black colors alternating
# between them). Each square has a x-coordinate and y-coordinate.
# The square can be considered as a room on the map. Now it can hold only
# one piece at a time. If another piece comes into the same room, it will 
# capture the existing piece.

# There are 2 players, White and Black. Each initially has a specific nbr of
# pieces which start on specific squares.

class ChessBoard(object):
  '''The chess board itself.'''

  def __init__(self):
    '''
    The board will initialize with 8 x 8 squares. The colors will alternate
    between black and white. The board will have 2 players, 1 black 
    and 1 white color.
    '''

    # A list of squares.
    self.__squares = []

    prev_color = None
    allow_promotion = False

    for i in range(0, 8, 1):

      if i ==0 or i == 7:
        allow_promotion = True

      for j in range(0, 8, 1):

        if prev_color == None:
          prev_color = 'WHITE'
        elif prev_color == 'WHITE':
          prev_color = 'BLACK'
        elif prev_color = 'BLACK':
          prev_color = 'WHITE'

        # if the square is on the end row of the player's side
        self.__squares.append(Square(i, j, prev_color, allow_promotion))

    # white player
    self.__player_white = Player()

    # black player
    self.__player_black = Player()


class Square(object):
  '''The square on the chess board.'''
  
  def __init__(self, xpos, ypos, piece = None, color, allow_promotion = False):
    '''Takes the xposition and yposition. This is the coordinate defining the 
    square on the chess board. Then it takes a piece that is currently present
    in the square. Initially no pieces are present in the squares. It also
    requires the color parameter to initialize the square to be of a particular
    color. By default the squares donot allow promotions, but the final row,
    squares allow promotion to a pawn if it enters that square.'''

    self.__xpos = xpos
    self.__ypos = ypos
    self.__piece = piece
    self.__color = color
    self.__allow_promotion = allow_promotion

  @property
  def xpos(self):
    '''The x-coordinate of the square. Generally follows the A, B, C convention.'''

    return self.__xpos

  @property
  def ypos(self):
    '''The y-coordinate of the square. Generally follows the 1, 2, 3 convention.'''

    return self.__ypos
  
  @property
  def color(self):
    '''The color of the square.'''

    return self.__color

  @property
  def allow_promotion(self):
    '''If the square is the square on the end rows of the board. i.e. if \
    the pawn is eligible to ascend into a higher ranked piece if it reaches the \
    square.'''

    return self.allow_promotion

  @property
  def piece(self):
    '''The piece currently present in the square.'''

    return self.__piece


  def __str__(self):
    '''
    The string representation (for display).
    '''

    xpos = None
    ypos = self.__ypos + 1

    if self.__xpos == 0:
      xpos =  'A'
    elif self.__xpos == 1:
      xpos =  'B'
    elif self.__xpos == 2:
      xpos =  'C'
    elif self.__xpos == 3:
      xpos =  'D'
    elif self.__xpos == 4:
      xpos =  'E'
    elif self.__xpos == 5:
      xpos =  'F'
    elif self.__xpos == 6:
      xpos =  'G'
    elif self.__xpos == 7:
      xpos =  'H'

    return '{}-{}'.format(xpos, ypos)

  @piece.setter
  def piece(self, new_piece):
    '''The new piece that moves into the square. It will capture the existing piece.\
    So, the existing piece in the square needs to modify it\'s status to captured,\
    and move out of play. If the new piece is a pawn, need to check if it can\
    receive a promotion if it reaches the last row square.'''

    pass
