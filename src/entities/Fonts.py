import pygame as pyg
from pygame.locals import *
from ..constants.constants import (UP, DOWN, TYPE_ERROR_MESSAGE, 
                                   CONTENT_TYPE_ERROR_MESSAGE, 
                                   VALUE_ERROR_MESSAGE, SRC_DIR,
                                   FREE_SANS_BOLD_FONT, PIXELED_FONT)

import os
dir_name = os.path.join(os.path.dirname(__file__))

class Fonts:

    def __init__(self,
                 text: str,
                 style: str,
                 size: int,
                 position: tuple,
                 color: tuple = (255,255,255)):
        self.text = text
        self.style = style
        self.size = size
        self.color = color

        self._set_font_type()
        self._set_font_render()
        self._set_font_area()
        self.set_font_location_by_mid(mid=position[0], top=position[1])

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        if isinstance(text, str):
            self.__text = text
        else:
            raise TypeError(TYPE_ERROR_MESSAGE.format(param='text', tp=str,
                                                      inst=type(text)))
        
    @property
    def style(self):
        return self.__style
    
    @style.setter
    def style(self, style: str):
        if isinstance(style, str):
            style = style.lower()

            if style in (FREE_SANS_BOLD_FONT, PIXELED_FONT):
                self.__style = style
            else:
                raise ValueError(
                    VALUE_ERROR_MESSAGE.format(
                        param='style', restr=("'style' must be equal to " +
                                              "'{0}' or '{1}'")
                                             .format(FREE_SANS_BOLD_FONT,
                                                     PIXELED_FONT)
                    )
                )
        else:
            raise TypeError(TYPE_ERROR_MESSAGE.format(param='style', tp=str,
                                                      inst=type(style)))
    
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, size: int):
        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError(TYPE_ERROR_MESSAGE.format(param='size', tp=str,
                                                      inst=type(size)))
    
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: tuple): 
        if isinstance(color, tuple):
            if all(isinstance(elem, int) for elem in color):
                if all(elem <= 255 and elem >= 0 for elem in color):
                    self.__color = color
                else:
                  raise ValueError(VALUE_ERROR_MESSAGE.format(param='color', 
                                                              restr='elem <= 255 and elem >= 0'))  
            else:
                raise TypeError(CONTENT_TYPE_ERROR_MESSAGE.format(param='color',
                                                                  tp=int))
        else:
            raise TypeError(TYPE_ERROR_MESSAGE.format(param='color', tp=str,
                                                      inst=type(color)))

    @property
    def font_type(self):
        return self.__font_type

    def _set_font_type(self):
        self.__font_type = pyg.font.Font(
            os.path.join(SRC_DIR, 'resources', 'game_fonts', self.__style),
            self.__size
        )
    
    def _set_font_render(self, antialias: bool=True):
        self.__font_render = self.__font_type.render(self.__text, antialias,
                                                     self.__color)
    
    def _set_font_area(self):
        self.__font_area = self.__font_render.get_rect()

    def set_font_location_by_mid(self, 
                                  mid: int,
                                  top: int=None,
                                  left: int=None,
                                  bottom: int=None,
                                  right: int=None):
        if top:
            self.__font_area.midtop = (mid, top)
        elif left:
            self.__font_area.midleft = (mid, left)
        elif bottom:
            self.__font_area.midbottom = (mid, bottom)
        elif right:
            self.__font_area.midright = (mid, right)
        else:
            raise TypeError("Excpected an <class 'int'> instance for one of the " +
                            "params (top, left, bottom, right), got "+
                            "<class 'NoneType'> or all of them")

    def print_font(self, screen: pyg.Surface):
        if isinstance(screen, pyg.Surface):
            screen.blit(self.__font_render, self.__font_area)
        else:
            raise TypeError(TYPE_ERROR_MESSAGE.format(param='screen', tp=pyg.Surface,
                                                      inst=type(screen)))

    def alter_font_color(self, color: tuple):
        self.color = color
        self._set_font_render()    
