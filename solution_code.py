import cv2
import os
from collections import deque

N = 40
CELL = 20
MOD = 1000000007

def image_to_grid(img):

    grid = []

    for row in range(N):

        current_row = []

        for col in range(N):

            red_count = 0

            for y in range(row * CELL, (row + 1) * CELL):
                for x in range(col * CELL, (col + 1) * CELL):

                    b, g, r = img[y, x]

                    if r > 180 and g < 100 and b < 100:
                        red_count += 1

            if red_count > (CELL * CELL) // 2:
                current_row.append(1) 
            else:
                current_row.append(0)  

        grid.append(current_row)

    return grid



def shortest_path(grid):

    queue = deque()
    queue.append((0, 0))

    visited = [[False] * N for _ in range(N)]
    parent = [[None] * N for _ in range(N)]

    visited[0][0] = True

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    while queue:

        r, c = queue.popleft()

        if r == N - 1 and c == N - 1:
         break

        for dr, dc in directions:

            nr = r + dr
            nc = c + dc

            if nr < 0 or nr >= N:
                continue

            if nc < 0 or nc >= N:
                continue

            if grid[nr][nc] == 1:
                continue

            if visited[nr][nc]:
                continue

            visited[nr][nc] = True
            parent[nr][nc] = (r, c)

            queue.append((nr, nc))

    if not visited[N - 1][N - 1]:
        return []

    path = []

    r = N - 1
    c = N - 1

    while (r, c) != (0, 0):

        path.append((r, c))
        r, c = parent[r][c]

    path.append((0, 0))
    path.reverse()

    return path

def draw_solution(grid, path):

    img = 255 * \
        __import__("numpy").ones((N * CELL, N * CELL, 3), dtype="uint8")

    for r in range(N):
        for c in range(N):

            y1 = r * CELL
            y2 = (r + 1) * CELL

            x1 = c * CELL
            x2 = (c + 1) * CELL

            if grid[r][c] == 1:
                img[y1:y2, x1:x2] = (0, 0, 255)

    for r, c in path:

        y1 = r * CELL
        y2 = (r + 1) * CELL

        x1 = c * CELL
        x2 = (c + 1) * CELL

        img[y1:y2, x1:x2] = (0, 255, 0)

    return img

def draw_impossible():

    import numpy as np

    img = np.zeros((800, 800, 3), dtype="uint8")
    img[:] = (255, 0, 0)

    cv2.putText(
        img,
        "IMPOSSIBLE, LACHURE SIR TRICKED ME",
        (40, 400),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    return img

def main():

    if not os.path.exists("mazes"):
        print("mazes folder not found")
        return

    os.makedirs("answers", exist_ok=True)

    files = []

    for file in os.listdir("mazes"):

        if file.endswith(".png"):
            files.append(file)

    files.sort()

    password = 1

    valid_count = 0
    impossible_count = 0

    log = open("runlog.txt", "w")

    for file in files:

        path = os.path.join("mazes", file)

        img = cv2.imread(path)

        if img is None:
            continue

        grid = image_to_grid(img)

        shortest = shortest_path(grid)

        output_file = os.path.join("answers", file)

        if len(shortest) == 0:

            impossible_count += 1

            cv2.imwrite(
                output_file,
                draw_impossible()
            )

            message = file + " -> IMPOSSIBLE"

        else:

            valid_count += 1

            length = len(shortest)

            password = (password * length) % MOD

            solved = draw_solution(
                grid,
                shortest
            )

            cv2.imwrite(
                output_file,
                solved
            )

            message = file + " -> path length = " + str(length)

        print(message)
        log.write(message + "\n")

    log.write("\n")
    log.write("Valid mazes: " + str(valid_count) + "\n")
    log.write("Impossible mazes: " + str(impossible_count) + "\n")
    log.write("Password: " + str(password) + "\n")

    log.close()

    with open("password.txt", "w") as f:
        f.write(str(password))

    print("\nPassword =", password)


main()