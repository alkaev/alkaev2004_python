import typing as tp


def _get_new_cell_state(cell: int, neighbors: list[int]) -> int:
    if cell == 0:
        fish_count = neighbors.count(2)
        shrimp_count = neighbors.count(3)
        if fish_count == 3:
            return 2
        elif shrimp_count == 3:
            return 3
    elif cell == 1:
        return 1
    elif cell == 2:
        fish_count = neighbors.count(2)
        if fish_count < 2 or fish_count >= 4:
            return 0
    elif cell == 3:
        shrimp_count = neighbors.count(3)
        if shrimp_count < 2 or shrimp_count >= 4:
            return 0
    return cell


class LifeGame(object):
    """
    Class for Game life
    """

    def __init__(self: tp.Any, ocean: tp.Any) -> None:
        self.ocean = ocean
        self.rows = len(ocean)
        self.cols = len(ocean[0])

    def get_next_generation(self: tp.Any) -> tp.Any:
        new_ocean = [[0] * self.cols for i in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                cell = self.ocean[i][j]
                neighbors = self._get_neighbors(i, j)
                new_ocean[i][j] = _get_new_cell_state(cell, neighbors)
        self.ocean = new_ocean
        return self.ocean

    def _get_neighbors(self, i: int, j: int) -> tp.Any:
        neighbors = []
        for k in range(-1, 2):
            for l in range(-1, 2):
                if k == 0 and l == 0:
                    continue
                ni, nj = i + k, j + l
                if 0 <= ni < self.rows and 0 <= nj < self.cols:
                    neighbors.append(self.ocean[ni][nj])
        return neighbors
