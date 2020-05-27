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
        self.sheet = pygame.image.load(self.scene_list[scene_number])
        self.buttons = []

    def add_button(self, position):
        """
        :param position: list, [leftupx, leftupy, rightdownx, rightdowny]
        :return:
        """
        self.buttons.append(position)
