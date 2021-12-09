import re
from pathlib import Path
from pprint import pprint
from typing import List

import numpy as np


class Hydrothermal:
    def __init__(self) -> None:
       self.coords_system = np.zeros(0)
       self.ventilation_map = np.zeros(0)

    def create_ventilation_map(self,max_x, max_y) -> None:
        self.ventilation_map = np.zeros((max_x, max_y),dtype=np.int32)

    def parse_text(self, file_text: List[str]) -> None:
        tmp_coord_system = []
        for coordinate_line in file_text:
            # pprint(coordinate_line.strip())
            tmp_coord = []
            matches = re.match(r'(\d+,\d+) -> (\d+,\d+)', coordinate_line.strip())
            if matches:
                for match in matches.groups():
                    tmp_coord.append(
                        tuple(int(x) for x in match.split(','))
                    )
                tmp_coord_system.append(tmp_coord)

        self.coords_system = np.array(tmp_coord_system)
        self.create_ventilation_map(len(self.coords_system), np.max(self.coords_system))


if __name__ == "__main__":
    file_name = 'test05.txt'
    # file_name = 'day05.txt'
    file_text = (Path(__file__).parent / file_name).read_text().splitlines()
    hydrothermal_system = Hydrothermal()
    hydrothermal_system.parse_text(file_text=file_text)
