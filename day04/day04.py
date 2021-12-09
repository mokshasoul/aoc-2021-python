import re
from pathlib import Path
from pprint import pprint
from typing import List

import numpy as np


class BingoGame:
    def __init__(self) -> None:
        self.bingo_numbers = []
        self.bingo_matrix = {}
        self.bingo_counter = 0
        self.bingo_winner_track = {}
        self.winning_idx = []

    def update_bingo_numbers(self, numbers_line: str) -> None:
        self.bingo_numbers = list(map(int, re.findall(r"\d+", numbers_line)))

    def update_bingo_matrix(self, bingo_matrix_tmp: List[List]):
        tmp_array = np.array(bingo_matrix_tmp)
        self.bingo_matrix[self.bingo_counter] = tmp_array.copy()
        self.bingo_winner_track[self.bingo_counter]  = np.ones_like(tmp_array)
        self.bingo_counter = self.bingo_counter + 1

    def parse_bingo_text(self, text: list) -> None:
        bingo_matrix_tmp = []
        for idx, line in enumerate(text):
            if idx == 0:
                self.update_bingo_numbers(line)
                continue
            if line == "":
                bingo_matrix_tmp = []
                continue
            bingo_matrix_tmp.append(list(map(int, re.findall(r"\d+", line))))
            if len(bingo_matrix_tmp) == 5:
                self.update_bingo_matrix(bingo_matrix_tmp=bingo_matrix_tmp)

    def print_bingo_map(self):
        pprint(self.bingo_matrix)
        pprint(self.bingo_winner_track)

    def play_bingo(self):
        for number in self.bingo_numbers:
            for idx, bingo_matrix in self.bingo_matrix.items():
                bingo_matrix: np.ndarray
                if number in bingo_matrix:
                    x,y = np.where(bingo_matrix == number)
                    self.bingo_winner_track[idx][x[0],y[0]] = 0
            win_idx, flag = self.is_there_winner()
            if flag:
                return win_idx, number

        return -1, -1
    
    def loose_bingo(self):
        target = 0
        for number in self.bingo_numbers:
            for idx, bingo_matrix in self.bingo_matrix.items():
                bingo_matrix: np.ndarray
                if number in bingo_matrix:
                    x,y = np.where(bingo_matrix == number)
                    self.bingo_winner_track[idx][x[0],y[0]] = 0
            win_idx, flag = self.register_winning_matrix()

            if number == 13:
                print(win_idx)
            if len(self.winning_idx)-1 == self.bingo_counter and flag:
                return number, win_idx


        return -1, -1

    def is_there_winner(self):
        idx: int
        for idx, matrix in self.bingo_winner_track.items():
            col_sum = np.sum(matrix, axis=0)
            row_sum = np.sum(matrix, axis=1)
            if 0 in col_sum or 0 in row_sum:
                return idx, True

        return -1, False

    def register_winning_matrix(self):
        idx: int
        for idx, matrix in self.bingo_winner_track.items():
            col_sum = np.sum(matrix, axis=0)
            row_sum = np.sum(matrix, axis=1)
            if 0 in col_sum or 0 in row_sum:
                if idx in self.bingo_winner_track:
                    continue
                self.winning_idx.append(idx)
                return idx, True

        return -1, False

    def calculate_matrix_sum(self, idx, number):
        print(np.sum(np.multiply(self.bingo_matrix[idx],self.bingo_winner_track[idx]))*number)


if __name__ == "__main__":
    file_name = 'day04.txt'
    # file_name = "test.txt"
    input_file = Path(__file__).parent / file_name

    bingo = BingoGame()

    bingo.parse_bingo_text(input_file.read_text().splitlines())
    # bingo.print_bingo_map()
    win_idx, number = bingo.play_bingo()
    bingo.calculate_matrix_sum(win_idx, number)
    loose_idx, numer = bingo.loose_bingo()
    bingo.calculate_matrix_sum(loose_idx, number)