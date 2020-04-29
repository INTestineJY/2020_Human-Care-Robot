def show_text(self, word, font_size, color, position_x, position_y):
    """
    show text on screen
    원하는 문장을 원하는 위치에 표시함
    :param color: str
    :param font_size: int
    :param word: any type
    :param position_x: int
    :param position_y: int
    :return:
    """
    font = pygame.font.SysFont("notosanscjkkr", font_size)
    textSurfaceObj = font.render(str(word), True, color_information.color[color])
    self.screen.blit(textSurfaceObj, (position_x, position_y))
    pygame.display.flip()



def show_box(self, board):
    """
    GUI 에 박스를 표현하는 함수
    여기서 박스는 보드 위의 판에 있는 네모 박스를 지칭한다
    :param board: list
    :return: None
    """
    for i in range(self.screen_size):
        for j in range(self.screen_size):
            c_i = color_information()
            box_color = c_i.get_color(board[i][j])
            pygame.draw.rect(self.screen, box_color, (i * 90 + 9, j * 90 + 9, 72, 72))
            if board[i][j] != 0:
                if board[i][j] < 10:
                    self.show_text(board[i][j], 36, 'WHITE', i * 90 + 36, j * 90 + 36)
                elif board[i][j] < 100:
                    self.show_text(board[i][j], 36, 'WHITE', i * 90 + 31.5, j * 90 + 36)
                else:
                    self.show_text(board[i][j], 31, 'WHITE', i * 90 + 22.5, j * 90 + 36)

def show_score(self, score):
    """
    게임 도중 scree 에 점수를 표시하는 함수
    :param score: int
    :return: None
    """
    self.show_text('Score', 50, 'BLACK', 10, self.screen_size * 90)
    self.show_text(score, 50, 'BLACK', 10, self.screen_size * 90 + 50)


def show_screen(self, board, score):
    """
    게임 화면을 보여주는 함수
    board 는 이차원 배열이어야 함
    :param board: list
    :param score: int
    :return: None
    """
    self.screen.fill(color_information.color[self.color])
    self.show_box(board)
    self.show_score(score)

    pygame.display.flip()
