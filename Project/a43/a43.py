#!/usr/bin/env python3
"""Jack Luft Seng265 Assignment 4 part 3"""
import sys
sys.path.append("..")
from a41 import a41
from a42 import a42
import random
class Art:
    """Art class 
    This class with take one argument that is a string to name the file.
    This class will call all the objects in a41 and a42 to create the SENG 265 art project.
     """
    def __init__(self,fileName: str):
        self.__fileName = fileName
        self.__width: int = random.randint(400,600)
        self.__height: int = random.randint(400,600)
        self.__art: object = a42.ArtConfig()
        self.__shapes: list = self.__art.getShapes()
        self.__createArt()
    def __createArt(self):
        a41.ProEpiloge(self.__fileName,self.__width,self.__height,self.__shapes)
def main():
    Art("Seng265")
main()
