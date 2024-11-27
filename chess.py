from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.
        
        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        Musí být implementováno v podtřídách.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position):
        self.__position = new_position

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        moves = []
        row, col = self.position
        direction = 1 if self.color == 'white' else -1

        # Tah vpřed
        forward_move = (row + direction, col)
        if self.is_position_on_board(forward_move):
            moves.append(forward_move)

        # Tah o dvě pole vpřed
        if (self.color == 'white' and row == 2) or (self.color == 'black' and row == 7):
            double_forward = (row + 2 * direction, col)
            if self.is_position_on_board(double_forward):
                moves.append(double_forward)

        # Diagonální braní
        for capture_col in [col - 1, col + 1]:
            capture_move = (row + direction, capture_col)
            if self.is_position_on_board(capture_move):
                moves.append(capture_move)

        return moves

    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        return [move for move in moves if self.is_position_on_board(move)]

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        row, col = self.position

        for dr, dc in directions:
            for i in range(1, 8):
                new_row, new_col = row + dr * i, col + dc * i
                if self.is_position_on_board((new_row, new_col)):
                    moves.append((new_row, new_col))
                else:
                    break

        return moves

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        row, col = self.position

        for dr, dc in directions:
            for i in range(1, 8):
                new_row, new_col = row + dr * i, col + dc * i
                if self.is_position_on_board((new_row, new_col)):
                    moves.append((new_row, new_col))
                else:
                    break

        return moves

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        moves = Bishop(self.color, self.position).possible_moves() + Rook(self.color, self.position).possible_moves()
        return moves

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'


class King(Piece):
    def possible_moves(self):
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        row, col = self.position

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if self.is_position_on_board((new_row, new_col)):
                moves.append((new_row, new_col))

        return moves

    def __str__(self):
        return f'King({self.color}) at position {self.position}'


if __name__ == "__main__":
    pieces = [
        Pawn("white", (2, 2)),
        Pawn("black", (7, 7)),
        Bishop("white", (4, 4)),
        Rook("black", (1, 1)),
        Queen("white", (3, 3)),
        King("black", (5, 5))
    ]

    for piece in pieces:
        print(piece)
        print("Possible moves:", piece.possible_moves())
