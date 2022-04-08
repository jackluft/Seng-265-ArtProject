#!/usr/bin/env python3
'''Jack luft Seng265 Assignment 4 Part 1'''

from typing import IO
class Circle:
    """Circle class"""
    def __init__(self,cir: tuple, col: tuple):
        self.__cx: int = cir[0]
        self.__cy: int = cir[1]
        self.__rad : int = cir[2]
        self.__red: int = col[0]
        self.__green: int = col[1]
        self.__blue: int = col[2]
        self.__op: float = col[3]
    def draw(self,f: IO[str], t:int):
        '''drawCircle method'''
        ts: str = "   " * t 
        line: str = f'<circle cx="{self.__cx}" cy="{self.__cy}" r="{self.__rad}" fill="rgb({self.__red}, {self.__green}, {self.__blue})" fill-opacity="{self.__op}"></circle>'
        f.write(f"{ts}{line}\n")
    def __str__(self):
        return f"Circle at x: {self.__cx}, y: {self.__cy} rad: {self.__rad}"
class Rectanlge:
    """Rectangle class"""
    def __init__(self,cir:tuple,col:tuple):
        self.__x:int = cir[0]
        self.__y:int = cir[1]
        self.__width: int = cir[2]
        self.__height: int = cir[3]
        
        self.__red: int = col[0]
        self.__green: int = col[1]
        self.__blue: int = col[2]
        self.__op: float = col[3]
    def draw(self,f: IO[str], t: int):
        ts: str = "   " * t 
        string:str  = f'<rect x="{self.__x}" y="{self.__y}" width= {self.__width} height = {self.__height} fill="rgb({self.__red}, {self.__green}, {self.__blue})" fill-opacity="{self.__op}"></rect>'
        f.write(f"{ts}{string}\n")
    def __str__(self):
        return f"Rectangle at x: {self.__x}, y: {self.__y}, width: {self.__width}, height: {self.__height}"
class ProEpiloge:
    """ProEpilog class"""
    def __init__(self,fileName:str, width:int, height:int,shapes: list):
        self.__fileName: str = fileName+".html"
        self.__width: int = width
        self.__height: int = height
        self.__shapes: list = shapes
        self.__createFile()
    def __addShapes(self,f: IO[str], t: int,shapes: list):
        for s in shapes:
            s.draw(f,t)
    def __createFile(self):
        winTitle = "My Art"
        f: IO[str] = open(self.__fileName, "w")
        self.__writeHTMLHeader(f, winTitle)
        self.__openSVGcanvas(f, 1, (self.__width,self.__height))
        self.__addShapes(f,2,self.__shapes)
        self.__closeSVGcanvas(f, 1)
        f.close()
    def __writeHTMLline(self,f: IO[str], t: int, line: str):
        '''writeLineHTML method'''
        ts = "   " * t
        f.write(f"{ts}{line}\n")
    def __openSVGcanvas(self,f: IO[str], t: int, canvas: tuple):
        '''openSVGcanvas method'''
        ts: str = "   " * t
        self.__writeHTMLcomment(f, t, "Define SVG drawing box")
        f.write(f'{ts}<svg width="{canvas[0]}" height="{canvas[1]}">\n') 
    def __closeSVGcanvas(self,f: IO[str], t: int):
        '''closeSVGcanvas method'''
        ts: str = "   " * t
        f.write(f'{ts}</svg>\n')
        f.write(f'</body>\n')
        f.write(f'</html>\n')
    def __writeHTMLHeader(self,f: IO[str], winTitle: str):
        '''writeHeadHTML method'''
        self.__writeHTMLline(f, 0, "<html>")
        self.__writeHTMLline(f, 0, "<head>")
        self.__writeHTMLline(f, 1, f"<title>{winTitle}</title>")
        self.__writeHTMLline(f, 0, "</head>")
        self.__writeHTMLline(f, 0, "<body>")
    def __writeHTMLcomment(self,f: IO[str], t: int, com: str):
        '''writeHTMLcomment method'''
        ts: str = "   " * t
        f.write(f'{ts}<!--{com}-->\n')
class Ellipse:
    """Ellipse"""
    def __init__(self,cir:tuple, col: tuple):
        self.__cx:int = cir[0]
        self.__cy: int = cir[1]
        self.__rx: int = cir[2]
        self.__ry: int = cir[3]
        
        self.__red: int = col[0]
        self.__green: int = col[1]
        self.__blue: int = col[2]
        self.__op: float = col[3]
    def draw(self,f:IO[str], t:int):
        '''drawEllipse method'''
        ts: str = "   " * t 
        line: str = f'<ellipse cx="{self.__cx}" cy="{self.__cy}" rx="{self.__rx}" ry={self.__ry} fill="rgb({self.__red}, {self.__green}, {self.__blue})" fill-opacity="{self.__op}"></ellipse>'
        f.write(f"{ts}{line}\n")
    def __str__(self):
        return f"Ellipse at x: {self.__cx}, y: {self.__cy}, rx: {self.__rx}, ry: {self.__ry}"        
        
def main():
    '''main method'''
    #5 red cirlces
    c = []
    i: int = 0
    x:int = 50
    while(i < 5):
        c1 = Circle((x,50,50),(255,0,0,1.0))
        c.append(c1)
        i = i+1
        x = x +100
    
    #5 blue circle
    i = 0
    x = 50
    while(i < 5):
        c1 = Circle((x,250,50),(0,0,255,1.0))
        c.append(c1)
        x = x+100
        i = i +1
    ProEpiloge("a41",500,300,c)

