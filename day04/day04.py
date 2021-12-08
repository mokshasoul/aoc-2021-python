from pathlib import Path
from pprint import pprint
import re
import os
from typing import List


class BingoGame:
    def __init__(self) -> None:
        self.bingo_numbers = []
        self.bingo_matrix = {}
        self.bingo_counter = 0
        self.bingo_winner_track = {}

    def update_bingo_numbers(self, numbers_line: str) -> None:
        self.bingo_numbers = list(map(int, re.findall(r"\d+", numbers_line)))

    def update_bingo_matrix(self, bingo_matrix_tmp: List[List]):
        self.bingo_matrix[self.bingo_counter] = bingo_matrix_tmp
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

    def play_bingo(self):
        for number in self.bingo_numbers:
            pass


if __name__ == "__main__":
    # file_name = 'test.txt'
    file_name = "test.txt"
    input_file = Path(__file__).parent / file_name

    bingo = BingoGame()

    bingo.parse_bingo_text(input_file.read_text().splitlines())
    bingo.print_bingo_map()
