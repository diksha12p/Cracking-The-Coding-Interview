class RobotInGrid:

    # Recursive Approach -> Top Down. Start from the Bottom Right and find the way up to the Top Left.
    # Starting from the last cell, we try to find a path to each of its adjacent cells
    # Time Complexity: O(2^(r+c))
    def get_path(self, maze):
        if not maze or not len(maze):
            return None
        path = []
        if self._is_path(maze, len(maze) - 1, len(maze[0]) - 1, path):
            return path
        return None

    def _is_path(self, maze, row, col, path):
        if row < 0 or col < 0 or not maze[row][col]:
            return False
        if (row == 0 or col == 0) or self._is_path(maze, row - 1, col, path) or self._is_path(maze, row, col - 1, path):
            path.append((row, col))
            return True
        return False

    # DP Approach
    # Time Complexity: O(rc)
    def get_path_memoization(self, maze):
        if not maze or not len(maze):
            return None
        path, roadblocks = [], []
        if self._path_exists(maze, len(maze) - 1, len(maze[0]) - 1, path, roadblocks):
            return path
        return None

    def _path_exists(self, maze, row, col, path, roadblocks):
        if row < 0 or col < 0 or not maze[row][col] or (row, col) in roadblocks:
            return False
        if (row == 0 or col == 0) or self._path_exists(maze, row - 1, col, path, roadblocks) or \
                self._path_exists(maze, row, col - 1, path, roadblocks):
            path.append((row, col))
            return True
        roadblocks.append((row, col))
        return False


if __name__ == '__main__':
    robot = RobotInGrid()
    print(robot.get_path([[True, True], [True, True]]))
    print(robot.get_path_memoization([[True, True], [False, True]]))

    print(robot.get_path([[True, False], [False, True]]))
    print(robot.get_path_memoization([[True, False], [False, True]]))
