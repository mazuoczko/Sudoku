import pygame
import rand

pygame.font.init()


def main():
    window = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Sudoku")
    on_off = True
    key = None
    board = Grid(500, 500, 9, 9, window)
    strikes = 0
    

    while on_off:
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on_off = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_KP1:
                    key = 1
                if event.key == pygame.K_KP2:
                    key = 2
                if event.key == pygame.K_KP3:
                    key = 3
                if event.key == pygame.K_KP4:
                    key = 4
                if event.key == pygame.K_KP5:
                    key = 5
                if event.key == pygame.K_KP6:
                    key = 6
                if event.key == pygame.K_KP7:
                    key = 7
                if event.key == pygame.K_KP8:
                    key = 8
                if event.key == pygame.K_KP9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    board.clear()
                    key = None

                if event.key == pygame.K_SPACE:
                    board.solve_gui()

                if event.key == pygame.K_RETURN:
                    i, j = board.selected
                    if board.cell[i][j].val != 0:
                        if board.place(board.cell[i][j].val):
                            print("Success")
                        else:
                            print("Wrong")
                            strikes += 1
                        key = None

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)

                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

                if (
                    board.width + 5 <= mouse[0] <= board.width + 95
                    and board.height - 500 <= mouse[1] <= board.height - 410
                ):
                    on_off = False

                if (
                    board.width + 5 <= mouse[0] <= board.width + 95
                    and board.height - 400 <= mouse[1] <= board.height - 310
                ):
                    board.new_board()
                    strikes = 0
                    

                if (
                    board.width + 5 <= mouse[0] <= board.width + 95
                    and board.height - 300 <= mouse[1] <= board.height - 210
                ):
                    board.solve_gui()

        if board.select and key != None:
            board.sketch(key)
        redraw_window(window, board, strikes)
        pygame.display.update()

        mouse = pygame.mouse.get_pos()


def redraw_window(window, board, strikes):
    window.fill((255, 255, 255))

    fnt = pygame.font.SysFont("arial", 25)


    text = fnt.render("X " * strikes, 1, (255, 0, 0))
    window.blit(text, (20, 560))

    board.draw()





class Grid:
    board = rand.random_element()

    def __init__(self, width, height, rows, col, window):
        self.rows = rows
        self.col = col
        self.width = width
        self.height = height
        self.window = window
        self.cell = [
            [Cell(self.board[i][j], i, j, width, height) for j in range(self.col)]
            for i in range(self.rows)
        ]
        self.update_model()
        self.selected = None

    def update_model(self):
        self.model = [
            [self.cell[j][i].grid_val for i in range(self.col)]
            for j in range(self.rows)
        ]

    def new_board(self):
        self.board = rand.random_element()
        self.cell = [
            [
                Cell(self.board[i][j], i, j, self.width, self.height)
                for j in range(self.col)
            ]
            for i in range(self.rows)
        ]
        self.update_model()

    def place(self, val_2):
        row, col = self.selected
        if self.cell[row][col].grid_val == 0:
            self.cell[row][col].set(val_2)
            self.update_model()

            if rand.valid(self.board, val_2, (row, col)):
                return True
            else:
                self.cell[row][col].set(0)
                self.cell[row][col].set_temp(0)
                self.update_model()
                return False

    def draw(self):
        fnt = pygame.font.SysFont("arial", 25)
        text_exit = fnt.render(str("Exit"), 1, (255, 255, 255))
        text_rand = fnt.render(str("Random"), 1, (255, 255, 255))
        text_solve = fnt.render(str("Solve"), 1, (255, 255, 255))

        gap = self.width / 9
        for i in range(self.rows + 1):
            if i % 3 == 0 and i != 0:
                line = 4
            else:
                line = 1

            pygame.draw.line(
                self.window, (0, 0, 0), (0, i * gap), (self.width, i * gap), line
            )
            pygame.draw.line(
                self.window, (0, 0, 0), (i * gap, 0), (i * gap, self.height), line
            )

            for i in range(self.rows):
                for j in range(self.col):
                    self.cell[i][j].draw(self.window)

        pygame.draw.rect(
            self.window, (0, 0, 0), [self.width + 5, self.height - 500, 90, 90]
        )
        pygame.draw.rect(
            self.window,
            (255, 255, 255),
            [self.width + 5, self.height - 500, 101, 101],
            3,
        )
        self.window.blit(text_exit, (self.width + 25, self.height - 475))
        pygame.draw.rect(
            self.window, (0, 0, 0), [self.width + 5, self.height - 400, 90, 90]
        )
        pygame.draw.rect(
            self.window,
            (255, 255, 255),
            [self.width + 5, self.height - 400, 101, 101],
            3,
        )
        self.window.blit(text_rand, (self.width + 10, self.height - 375))
        pygame.draw.rect(
            self.window, (0, 0, 0), [self.width + 5, self.height - 300, 90, 90]
        )
        pygame.draw.rect(
            self.window,
            (255, 255, 255),
            [self.width + 5, self.height - 300, 101, 101],
            3,
        )
        self.window.blit(text_solve, (self.width + 20, self.height - 275))

    def select(self, row, col):
        for i in range(self.rows):
            for j in range(self.col):
                self.cell[i][j].selected = False

        self.cell[row][col].selected = True
        self.selected = (row, col)

    def click(self, pos):
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / 9
            x = pos[0] // gap
            y = pos[1] // gap

            return (int(y), int(x))
        else:
            return None

    def sketch(self, val):
        row, col = self.selected
        self.cell[row][col].set_temp(val)

    def clear(self):
        row, col = self.selected
        if self.cell[row][col].grid_val == 0:
            self.cell[row][col].set_temp(0)

    def solve_gui(self):
        self.update_model()
        find = rand.find_0(self.model)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if rand.valid(self.model, i, (row, col)):
                self.model[row][col] = i
                self.cell[row][col].set(i)
                self.cell[row][col].draw_change(self.window, True)
                self.update_model()
                pygame.display.update()
                pygame.time.delay(20)

                if self.solve_gui():
                    return True

                self.model[row][col] = 0
                self.cell[row][col].set(0)
                self.update_model()
                self.cell[row][col].draw_change(self.window, False)
                pygame.display.update()
                pygame.time.delay(20)

        return False


class Cell:
    def __init__(self, grid, row, col, width, height):
        self.grid_val = grid
        self.val = 0
        self.width = width
        self.height = height
        self.col = col
        self.row = row
        self.selected = False

    def draw(self, window):
        fnt = pygame.font.SysFont("arial", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if self.val != 0 and self.grid_val == 0:
            text = fnt.render(str(self.val), 1, (128, 128, 128))
            window.blit(text, (x + 5, y + 5))
        elif not (self.grid_val == 0):
            text = fnt.render(str(self.grid_val), 1, (0, 0, 0))
            window.blit(
                text,
                (
                    x + (gap / 2 - text.get_width() / 2),
                    y + (gap / 2 - text.get_height() / 2),
                ),
            )

        if self.selected:
            pygame.draw.rect(window, (255, 0, 0), (x + 0.5, y + 0.5, gap, gap), 3)

    def draw_change(self, window, g=True):
        fnt = pygame.font.SysFont("arial", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        pygame.draw.rect(window, (255, 255, 255), (x, y, gap, gap), 0)

        text = fnt.render(str(self.grid_val), 1, (0, 255, 0))
        window.blit(
            text,
            (
                x + (gap / 2 - text.get_width() / 2),
                y + (gap / 2 - text.get_height() / 2),
            ),
        )
        if g:
            pygame.draw.rect(window, (0, 255, 0), (x, y, gap, gap), 3)
        else:
            pygame.draw.rect(window, (255, 0, 0), (x, y, gap, gap), 3)

    def set_temp(self, val):
        self.val = val

    def set(self, val):
        self.grid_val = val


if __name__ == "__main__":
    main()
pygame.quit
