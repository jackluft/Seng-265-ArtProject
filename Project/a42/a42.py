#!/usr/bin/env python3
"""Jack Luft seng265 Assignment 4, part 2"""
from typing import IO
import sys 
sys.path.append("..")
from a41 import a41
import random
class GenRandom:
    """class GenRandom"""
    cnt:int = 0
    Xbounds: int = 600
    Ybounds: int = 600
    def __init__(self):
        self.__cnt: int = GenRandom.cnt 
        self.__sha: int = random.randint(0,2)
        self.__x: int = random.randint(0,GenRandom.Xbounds)
        self.__y: int = random.randint(0,GenRandom.Ybounds)
        self.__rad: int = random.randint(0,100)
        self.__rx: int = random.randint(10,30)
        self.__ry: int = random.randint(10,30)
        self.__w: int = random.randint(10,100)
        self.__h: int = random.randint(10,100)
        self.__r: int = random.randint(0,255)
        self.__g: int = random.randint(0,255)
        self.__b: int = random.randint(0,255)
        self.__op: float = random.uniform(0.0,1.0)
        GenRandom.cnt = GenRandom.cnt +1
    def printData(self)-> None:
        print(f"{self.__cnt}  {self.__sha}  {self.__x}  {self.__y}  {self.__rad}  {self.__rx}  {self.__ry}  {self.__w}  {self.__h}  {self.__r}  {self.__b}  {round(self.__op,2)}\n")
    def getSHA(self)->int:
        """This method will return the SHA value, which tells you the type of shape """
        return self.__sha
    def getX(self)-> int:
        """retrun random x value """
        return self.__x
    def getY(self)-> int:
        """return random y value """
        return self.__y
    def getRad(self)-> int:
        """return random rad value"""
        return self.__rad
    def getRx(self)-> int:
        """return random rx value """
        return self.__rx
    def getRy(self)-> int:
        """return random ry value """
        return self.__ry
    def getW(self)-> int:
        """return random width value"""
        return self.__w
    def getH(self)->int:
        """return random height value """
        return self.__h
    def getR(self)->int:
        """return random red value"""
        return self.__r
    def getG(self)->int:
        """return random green value"""
        return self.__g
    def getB(self):
        """return random blue value """
        return self.__b
    def getOp(self)->float:
        """return random op value """
        return self.__op
    def __str__(self):
        return f"{self.__cnt}  {self.__sha}  {self.__x}  {self.__y}  {self.__rad}  {self.__rx}  {self.__ry}  {self.__w}  {self.__h}  {self.__r}  {self.__g}  {self.__b}  {round(self.__op,2)}"
class ArtConfig:
    """class ArtConfig"""
    numOfObjects: int = 10000
    def __init__(self):
        self.__num: int = random.randint(0,ArtConfig.numOfObjects)
        self.__data:list = []
        data: tuple = self.__genRand()
        self.__circleList: list = data[0]
        self.__rectangleList: list = data[1]
        self.__ellipseList: list = data[2]
    def __genRand(self):
        """This method will add a circle, rectangle or ellipse to a list based off the  GenRandom SHA value """
        circl = []
        rec = []
        ell = []
        i: int = 0
        while(i < self.__num):
            g = GenRandom()
            if(g.getSHA() == 0):
                #shape is a circle
                cir: tuple = (g.getX(),g.getY(),g.getRad())
                col: tuple = (g.getR(),g.getG(),g.getB(),g.getOp())
                c = a41.Circle(cir,col)
                circl.append(c)
            elif(g.getSHA() == 1):
                #shape is rectangle
                cir: tuple = (g.getX(),g.getY(),g.getW(),g.getH())
                col: tuple = (g.getR(),g.getG(),g.getB(),g.getOp())
                r = a41.Rectanlge(cir,col)
                rec.append(r)
            elif(g.getSHA() == 2):
                #shape is ellipse
                cir: tuple = (g.getX(),g.getY(),g.getRx(),g.getRy())
                col: tuple = (g.getR(),g.getG(),g.getB(),g.getOp())
                e = a41.Ellipse(cir,col)
                ell.append(e)
            self.__data.append(g)
            i = i +1
        return (circl,rec,ell)
    def getCircle(self)->list:
        """This method will return a list of cirlces"""
        return self.__circleList
    def getRectangle(self)->list:
        """This method will return a list of rectangles """
        return self.__rectangleList
    def getEllipse(self)->list:
        """This metho will return a list of ellipses """
        return self.__ellipseList
    def getShapes(self)-> list:
        """This method will return a list of all the shapes shuffed """
        shapes = []
        for c in self.getCircle():
            shapes.append(c)
        for r in self.getRectangle():
            shapes.append(r)
        for e in self.getEllipse():
            shapes.append(e)
        random.shuffle(shapes)
        return shapes
    def __str__(self):
        """This toString method will create the requested table"""
        output: str = "CNT SHA  X  Y  RAD  RX  RY  W   H  R  G  B  OP\n"
        for d in self.__data:
            output = output+ str(d)+"\n"
        return output
def main():
    func = ArtConfig()
    print(func)
