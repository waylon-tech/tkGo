#!/usr/bin/env python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-01-13 17:50:58
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-01-19 14:07:29
# @FilePath            : \src\frame\frame_button_main.py
# @Description         : 

from tkinter import Button
from tkinter import NSEW
from frame.frame import EFrame


class FrameButtonMain(EFrame):

    def __init__(self, master=None, cnf={}, **kw):
        
        super().__init__(master=master, cnf=cnf, **kw)
        
        self.button_test = Button(master=self, text="TEST")
        self.button_test.grid(row=0, column=0, sticky=NSEW)