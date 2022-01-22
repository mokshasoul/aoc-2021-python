import re
from pathlib import Path
from pprint import pprint
from typing import List
from itertools import product

import numpy as np
from numpy.lib.utils import source


class Hydrothermal:
    def __init__(self) -> None:
        self.coords_system = np.zeros(0)
        self.ventilation_map = np.zeros(0)

    def create_ventilation_map(self, max_tiles: int) -> None:
        self.ventilation_map = np.zeros((max_tiles + 1, max_tiles + 1), dtype=np.int32)

    def calculate_overlapping_lines(self):
        return np.count_nonzero(self.ventilation_map >= 2)

    def populate_map(self):
        coord_pair: np.ndarray
        for coord_pair in self.coords_system:
            source_coord, dest_coord = coord_pair
            source_coord: np.ndarray
            dest_coord: np.ndarray
            x1, y1 = source_coord
            x2, y2 = dest_coord
            if x1 == x2:
                vector_y_start = y1 if y1 < y2 else y2
                vector_y_end = y1 if y1 > y2 else y2
                for vector_y in range(vector_y_start, vector_y_end + 1):
                    self.ventilation_map[vector_y, x1] = (
                        self.ventilation_map[vector_y, x1] + 1
                    )
            if y1 == y2:
                vector_x_start = x1 if x1 < x2 else x2
                vector_x_end = x1 if x1 > x2 else x2
                for vector_x in range(vector_x_start, vector_x_end + 1):
                    self.ventilation_map[y1, vector_x] = (
                        self.ventilation_map[y1, vector_x] + 1
                    )

    def populate_map_diagonal(self):
        coord_pair: np.ndarray
        for coord_pair in self.coords_system:
            source_coord, dest_coord = coord_pair
            source_coord: np.ndarray
            dest_coord: np.ndarray
            """
                Idea is that we iterate through increments of both at the same time except if 
                x1 == x2 or y1 == y2
            """
            x1, y1 = source_coord
            x2, y2 = dest_coord
            x1_ge, y1_ge = np.greater_equal(source_coord, dest_coord)
            x_iterator = x1 
            y_iterator = y1 
            x_val = -1 if x1_ge else 1
            y_val = -1 if y1_ge else 1
            while True:
                if(
                    x1 == x2 or
                    y1 == y2
                ):
                    break
                self.ventilation_map[y_iterator, x_iterator] = (
                    self.ventilation_map[y_iterator, x_iterator] + 1
                )
                if (
                    x_iterator != x2 and
                    y_iterator != y2
                ):
                    x_iterator = x_iterator + x_val
                    y_iterator = y_iterator + y_val
                else:
                    break


    def parse_text(self, file_text: List[str]) -> None:
        tmp_coord_system = []
        for coordinate_line in file_text:
            # pprint(coordinate_line.strip())
            tmp_coord = []
            matches = re.match(r"(\d+,\d+) -> (\d+,\d+)", coordinate_line.strip())
            if matches:
                for match in matches.groups():
                    tmp_coord.append(tuple(int(x) for x in match.split(",")))
                tmp_coord_system.append(tmp_coord)

        self.coords_system = np.array(tmp_coord_system)
        self.create_ventilation_map(np.max(self.coords_system))


if __name__ == "__main__":
    # file_name = "test05.txt"
    # file_name = "test05_dup.txt"
    file_name = "day05.txt"
    file_text = (Path(__file__).parent / file_name).read_text().splitlines()
    hydrothermal_system = Hydrothermal()
    hydrothermal_system.parse_text(file_text=file_text)
    hydrothermal_system.populate_map()
    hydrothermal_system.populate_map_diagonal()
    print(hydrothermal_system.ventilation_map)
    print(hydrothermal_system.calculate_overlapping_lines())
