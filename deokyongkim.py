import pygame


class Button:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def isClicked(self, mouseX, mouseY):
        if self.x1 <= mouseX <= self.x2 and self.y1 <= mouseY <= self.y2:
            return True
        return False


class Scene:

    def __init__(self, scene_number):
        self.scene_number = scene_number
        self.scene_list = []
        for i in range(13):
            self.scene_list.append('대지 ' + str(i))
        image_name = "./image/test_image/" + self.scene_list[scene_number] + ".png"
        self.sheet = pygame.image.load(image_name)
        self.buttons = []
        self.add_button()

    def add_button(self):
        """
        Scene 에 포함되어 있는 button을 buttons 리스트에 추가함
        :param button: 위에서 선언한 class Button
        :return:
        """
        number = '#' + str(self.scene_number)
        f = open('screen_button.txt', 'r')
        while True:
            line = f.readline()
            line = line[:-1]  # 엔터키 없앰
            if line == number:
                while True:
                    line = f.readline()
                    line = line[:-1]
                    if line == '#' + str(self.scene_number + 1) or line == "end":
                        break
                    pos = line.split(' ')
                    x1 = int(pos[0])
                    y1 = int(pos[1])
                    line = f.readline()
                    line = line[:-1]
                    pos = line.split(' ')
                    x2 = int(pos[0])
                    y2 = int(pos[1])
                    line = f.readline()

                    temporary_b = Button(x1, y1, x2, y2)
                    self.buttons.append(temporary_b)

            if line == "end":
                break
