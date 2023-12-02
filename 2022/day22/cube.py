import numpy as np


def move(number_of_steps, location, direction_idx, directions, open_tiles, wall_tiles, face_size):
    for _ in range(number_of_steps):
        direction = directions[direction_idx]
        next_location = tuple(np.array(location) + np.array(direction))
        if (next_location not in wall_tiles) and (next_location not in open_tiles):
            # print(f"Attempted to move from {location} to {next_location}, which is not on the board")

            if 0*face_size <= location[0] < 1*face_size and 1*face_size <= location[1] < 2*face_size:  # Face 1
                if tuple(direction) == (1, 0):
                    raise
                elif tuple(direction) == (-1, 0):  # Moving up off face 1 up the left of face 6
                    next_location = np.array(((location[1] + 2*face_size, 0)))
                    assert 3*face_size <= next_location[0] < 4*face_size and 0 <= next_location[1] < face_size
                    direction_idx = 0
                elif tuple(direction) == (0, 1):
                    raise
                elif tuple(direction) == (0, -1):  # Moving left off face 1 up the left of face 5
                    next_location = np.array((3*face_size - 1 - location[0], 0))
                    assert 2*face_size <= next_location[0] < 3*face_size and 0 <= next_location[1] < face_size
                    direction_idx = 0
                else:
                    raise
            elif 0*face_size <= location[0] < 1*face_size and 2*face_size <= location[1] < 3*face_size:  # Face 2
                if tuple(direction) == (1, 0):  # Moving down off face 2 up the right of face 3
                    next_location = np.array((location[1] - face_size, 2*face_size - 1))
                    assert face_size <= next_location[0] < 2*face_size and face_size <= next_location[1] < 2*face_size
                    direction_idx = 2
                elif tuple(direction) == (-1, 0):  # Moving up off face 2 up the bottom of face 6
                    next_location = np.array((4*face_size - 1, location[1] - 2*face_size))
                    assert 3*face_size <= next_location[0] < 4*face_size and 0 <= next_location[1] < face_size
                    direction_idx = 3
                elif tuple(direction) == (0, 1):  # Moving right off face 2 up the right of face 4
                    next_location = np.array((3*face_size - 1 - location[0], 2*face_size - 1))
                    assert 2*face_size <= next_location[0] < 3*face_size and face_size <= next_location[1] < 2*face_size
                    direction_idx = 2
                elif tuple(direction) == (0, -1):
                    raise
                else:
                    raise
            elif face_size <= location[0] < 2*face_size and face_size <= location[1] < 2*face_size:  # Face 3
                if tuple(direction) == (1, 0):
                    raise
                elif tuple(direction) == (-1, 0):
                    raise
                elif tuple(direction) == (0, 1):  # Moving right off face 3 up the bottom of face 2
                    next_location = np.array((face_size - 1, face_size + location[0]))
                    assert 0*face_size <= next_location[0] < 1*face_size and 2*face_size <= next_location[1] < 3*face_size
                    direction_idx = 3
                elif tuple(direction) == (0, -1):  # Moving left off face 3 down the top of face 5
                    next_location = np.array((2*face_size, location[0] - face_size))
                    assert 2*face_size <= next_location[0] < 3*face_size and 0 <= next_location[1] < face_size
                    direction_idx = 1
                else:
                    raise
            elif 2*face_size <= location[0] < 3*face_size and face_size <= location[1] < 2*face_size:  # Face 4
                if tuple(direction) == (-1, 0):
                    raise
                elif tuple(direction) == (1, 0):  # Moving down off face 4 up the right of face 6
                    next_location = np.array((location[1] + 2*face_size, face_size - 1))
                    assert 3*face_size <= next_location[0] < 4*face_size and 0 <= next_location[1] < face_size
                    direction_idx = 2
                elif tuple(direction) == (0, 1):  # Move right off face 4 up the right of face 2
                    next_location = np.array((3*face_size - 1 - location[0], 3*face_size - 1))
                    assert 0*face_size <= next_location[0] < 1*face_size and 2*face_size <= next_location[1] < 3*face_size
                    direction_idx = 2
                elif tuple(direction) == (0, -1):
                    raise
                else:
                    raise
            elif 2*face_size <= location[0] < 3*face_size and 0 <= location[1] < face_size:  # Face 5
                if tuple(direction) == (1, 0):
                    raise
                elif tuple(direction) == (-1, 0):  # Moving up off face 5 up the left of face 3
                    next_location = np.array((face_size + location[1], face_size))
                    assert face_size <= next_location[0] < 2*face_size and face_size <= next_location[1] < 2*face_size
                    direction_idx = 0
                elif tuple(direction) == (0, 1):
                    raise
                elif tuple(direction) == (0, -1):  # Moving left off face 5 up the left of face 1
                    next_location = np.array((3*face_size - 1 - location[0], face_size))
                    assert 0*face_size <= next_location[0] < 1*face_size and 1*face_size <= next_location[1] < 2*face_size
                    direction_idx = 0
                else:
                    raise
            elif 3*face_size <= location[0] < 4*face_size and 0 <= location[1] < face_size:  # Face 6
                if tuple(direction) == (1, 0):  # Moving down off face 6 down the top of face 2
                    next_location = np.array((0, 2*face_size + location[1]))
                    assert 0*face_size <= next_location[0] < 1*face_size and 2*face_size <= next_location[1] < 3*face_size
                    direction_idx = 1
                elif tuple(direction) == (-1, 0):
                    raise
                elif tuple(direction) == (0, 1):  # Moving right off face 6 up the bottom of face 4
                    next_location = np.array((3*face_size - 1, location[0] - 2*face_size))
                    assert 2*face_size <= next_location[0] < 3*face_size and face_size <= next_location[1] < 2*face_size
                    direction_idx = 3
                elif tuple(direction) == (0, -1):  # Moving left off face 6 down the top of face 1
                    next_location = np.array((0, location[0] - 2*face_size))
                    assert 0*face_size <= next_location[0] < 1*face_size and 1*face_size <= next_location[1] < 2*face_size
                    direction_idx = 1
                else:
                    raise
            else:
                raise

            assert tuple(next_location) in wall_tiles + open_tiles, next_location

            # print(f"Next target location becomes {next_location} instead")
            # print(f"Direction changed to {directions[direction_idx]}")

        if tuple(next_location) in wall_tiles:
            # print(f"Target location {next_location} is a wall tile - stopping and moving on to changing direction")
            break
        elif tuple(next_location) in open_tiles:
            # print(f"Target location {next_location} is an open tile - moving there")
            location = next_location
        else:
            raise

    return location, direction_idx
