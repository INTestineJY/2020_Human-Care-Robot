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
        self.scene_list = ['대지 1', '대지 2', '대지 3', '대지 4', '대지 5']
        image_name = "./image/test_image/"+self.scene_list[scene_number]+".png"
        self.sheet = pygame.image.load(image_name)
        self.buttons = []

    def add_button(self, button):
        """
        Scene 에 포함되어 있는 button을 buttons 리스트에 추가함
        :param button: 위에서 선언한 class Button
        :return:
        """
        self.buttons.append(button)
