import pygame
import time
from collections import deque
from os.path import  join
pygame.display.set_caption("Platform")
pygame.init()
GRAPH = []
WIDTH, HEIGHT = 960, 720
FPS = 60
PLAYER_VEL = 5
TILE = []

visited = set()
path = []
window = pygame.display.set_mode((WIDTH, HEIGHT))
def dfs(graph, start, target):
    rows = len(graph)
    cols = len(graph[0])
    visited = set()
    stack = [(start[0], start[1], [])]
    visited.add((start[0], start[1]))
    
    while stack:
        row, col, path = stack.pop()
        if graph[row][col] == target:
            return path + [(col * 48, row * 48)]

        for dc, dr in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_col = col + dc
            new_row = row + dr
            
            if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited:
                if graph[new_row][new_col] != "1":
                    stack.append((new_row, new_col, path + [(col * 48, row * 48)]))
                    visited.add((new_row, new_col))
    return None

def bfs(graph, start, target):
    rows = len(graph)
    cols = len(graph[0])
    visited = set()
    queue = deque([(start[0], start[1], [])])
    visited.add((start[0], start[1]))
     
    while queue:
        row, col, path = queue.popleft()
        if graph[row][col] == target:
            return path + [(col*48, row*48)]

        for dc, dr in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_col =col + dc
            new_row = row + dr
            
            if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited:
                if graph[new_row][new_col] != "1":
                    queue.append((new_row, new_col, path + [(col*48, row*48)]))
                    visited.add((new_row, new_col))
    return None

def loadMap(text):
    with open(text, "r") as file:
        file_contents = file.read()
    lines = file_contents.split('\n')
    colY = 0
    rowX = 0
    for line in lines:
        l = line.split(" ")
        GRAPH.append(l)
        for item in l:
            if colY * 48 <= WIDTH:
                if item == "0":
                    drawTile("Background",'earth.png',(colY * 48 , rowX * 48))
                if item == "1":
                    drawTile("Background",'wall.png',(colY * 48 , rowX * 48))
                if item == "3":
                    drawTile("Background",'chest.png',(colY * 48 , rowX * 48))
                colY = colY + 1
            if colY * 48 == WIDTH:
                rowX = rowX + 1
                colY = 0


def draw_player():
    drawTile('charactors','boy_down_2.png',(0,0))
    

def drawTile(folder,name,tile):
    image = pygame.image.load(join("assets", folder, name))
    image = pygame.transform.scale(image, (48, 48))
    window.blit(image, tile)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    loadMap("./assets/map/map01.txt")
    draw_player()

    start_t = time.time() 
    path = bfs(GRAPH, (0,0), "3")
    print(path)
    if path:
        for step in path:
            print(step)
            drawTile("Background",'chest.png',step)
    end_t = time.time()
    elapsed_t = end_t - start_t
    print("Thời gian chạy của bfs: ", elapsed_t, "giây")

    startdfs_t = time.time()
    pathDFS = dfs(GRAPH,(0,0), "3")
    print(pathDFS)
    if pathDFS:
        for step in pathDFS:
            print(step)
            drawTile("Background",'chest.png',step)

    enddfs_t = time.time()
    eldfs_t = enddfs_t - startdfs_t
    print("Thời gian chạy của dfs: ", eldfs_t, " giây")

    if eldfs_t > elapsed_t:
        print("Thời gian chạy của thuật toán tìm kiếm theo chiều rộng nhanh hơn")
    else :
        print("Thời gian chạy của thuật toán tìm kiếm theo chiều sâu nhanh hơn")

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()
    

