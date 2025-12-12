import numpy as np
import zlib

robots = defaultdict(tuple)
for i, line in enumerate(data):
    px, py, vx, vy = map(int, re.findall(r"-?\d+", line))
    robots[i] = (px, py, vx, vy)

rows = 103
cols = 101
board_size = rows*cols
compression_ratio = 1

for t in range(board_size):
    board = np.zeros((cols, rows), dtype=bool)
    for i in robots:
        px, py, vx, vy = robots[i]
        board[(px + vx * t) % cols, (py + vy * t) % rows] = 1

    # Compress using zlib after having converted binary board to bytes
    compressed_board = zlib.compress(np.packbits(board))
    new_ratio = len(compressed_board) / board_size
    if new_ratio < compression_ratio:
        compression_ratio = new_ratio
        bestt = t