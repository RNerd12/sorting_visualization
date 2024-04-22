import pygame
import random
import time

class visualizer:
    def __init__(self, width, height) -> None:
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sort visualizer")
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.running = True
        self.array = []
        for _ in range(500):
            self.array.append(random.randint(0,self.height))
        self.array_pos = 0
        self.count_change = 0

    def run_canvas(self) -> None:
        
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    print("quitting")
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            self.screen.fill(self.BLACK)
            self.draw_array()
            self.sort_array_step()

    def draw_array(self):
        x_pos = 0
        for i in self.array:
            self.draw_line((x_pos, i),(x_pos, self.height))
            x_pos += 1

    def draw_line(self, start: tuple, end: tuple) -> None:
        pygame.draw.line(self.screen, self.WHITE, start, end, 1)
        pygame.display.flip()

    def sort_array_step(self):
        if (
            self.array_pos < len(self.array)-1 and 
            self.array[self.array_pos] > self.array[self.array_pos+1]
        ):
            self.array[self.array_pos], self.array[self.array_pos+1] = self.array[self.array_pos+1], self.array[self.array_pos]
            self.count_change += 1
        if self.array_pos == len(self.array)-1:
            if self.count_change == 0:
                self.running = False
            self.array_pos = 0
            self.count_change = 0
            print('cycle')
        self.array_pos += 1
        time.sleep(0.1)

    def __del__(self) -> None:
        pygame.quit()

if __name__ == '__main__':
    vs = visualizer(500,500)
    vs.run_canvas()
    del vs