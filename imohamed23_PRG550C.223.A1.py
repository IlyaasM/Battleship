# Your solution may ONLY use the python modules listed below
# program: a1main.py
# author:  danny abesdris
# date:    october 13, 2022
# purpose: python main( ) program for PRG550 FALL 2022 Assignment #1
# version: 1.01

import math
import random
import string
import collections
import datetime
import re
import time
import copy
import types


# YOUR CODE BELOW...


def generateGameBoard(nRows, nCols):
    board = [['~' for i in range(nCols)] for j in range(nRows)]
    # print("  Python Battleship@Seneca..."+"\n"+"  123456789ABCDEFGHIJKLMNOPQRST")
    # for i in range(1, nRows + 1):
    #     if i<=9:
    #         print(i, "|", "".join(map(str,board[i])), "|", sep="")
    #     else:
    #         print(chr(i+55), "|", "".join(map(str,board[i-1])), "|", sep="")
    return board


def loadShip(boardData, nRows, nCols, coord, ship):

    rowString = string.digits[1:] + string.ascii_uppercase[:nRows - 9]
    colString = string.digits[1:] + string.ascii_uppercase[:nCols - 9]
    first = rowString.find(coord[0])
    sec = colString.find(coord[1])
    for i in range(len(ship)):
        boardData[first][sec + i] = ship[i]
    return boardData


def checkCoord(nRows, nCols, coord):
    first = coord[0:1]
    sec = coord[1:2]
    temp1 = 0
    temp2 = 0
    if coord == "AZ":
        return False
    if len(coord) == 2 and coord != "  ":
        if coord[0].isnumeric() == True or coord[0].isalpha() == True:
            if coord[1].isnumeric() == True or coord[1].isalpha() == True:
                temp1 = (ord(first) - 64)
                temp2 = (ord(sec) - 64)
                if temp1 >= nRows or temp1 <= nRows or temp2 >= nCols or temp2 <= nCols:
                    return True
    else:
        return False


def updateGameBoard(boardData, boardMask, nRows, nCols, coord, score, lastMove):
    if checkCoord(nRows,nCols,coord) == True or checkCoord(nRows,nCols,coord) == False:
        rowString = string.digits[1:] + string.ascii_uppercase[:nRows - 9]
        colString = string.digits[1:] + string.ascii_uppercase[:nCols - 9]
        first = rowString.find(coord[0])
        sec = colString.find(coord[1])
        coords = []
        for i in range(1):
            coords.append(coord)
        coords = list(coord)

        print("  Python Battleship@Seneca...")
        string.digits = "0123456789" "ABCDEFGHIJKLMNOPQRST"

        colString = "  " + string.digits[1:] + string.ascii_uppercase[:nCols - 9]
        rowString = string.digits[1:] + string.ascii_uppercase[:nRows - 9]

        if checkCoord(nRows,nCols,coord) == True :
            if boardData[first][sec] != "X" and boardData[first][sec] != "~":
                i = 1
                score += 5
                j = 1
                lastMove = coord
                boardMask[first][sec] = boardData[first][sec]
                while boardData[first][sec - i] != "X" and boardData[first][sec - i] != "~":
                    if boardData[first][sec - i] != "[":
                        boardMask[first][sec - i] = boardData[first][sec - i]
                        i += 1
                        score += 5
                    else:
                        break

                while boardData[first][sec + j] != "X" and boardData[first][sec + j] != "~":
                    if boardData[first][sec + j] != ">":
                        boardMask[first][sec + j] = boardData[first][sec + j]
                        score += 5
                        j += 1
                    else:
                        break

                if boardData[first][sec + j] == ">":
                    boardMask[first][sec + j] = boardData[first][sec + j]
                    score += 5

                if boardData[first][sec - i] == "[":
                    boardMask[first][sec - i] = boardData[first][sec - i]
                    score += 5

                for k in range(nCols + 2):
                    print(colString[k], end="")
                print(" ")

                for l in range(nRows):
                    print(rowString[l] + "|", end="")
                    for j in range(nCols):
                        print(boardMask[l][j], end="")
                    print("|")

                print("Current Score:" + str("{:03d}".format(score)) + " Last Move: Torpedo HIT '" + str(boardData[first][sec]) + "' at [" + str(coords[0]) + "," + str(coords[1]) + "]")
            else:
                boardMask[first][sec] = "X"
                for m in range(nCols + 2):
                    print(colString[m], end="")
                print(" ")
                for n in range(nRows):
                    print(rowString[n] + "|", end="")
                    for j in range(nCols):
                        print(boardMask[n][j], end="")
                    print("|")
                print("Current Score:" + str("{:03d}".format(score)) + " Last Move: Torpedo MISS at [" + str(coords[0]) + "," + str(coords[1]) + "]")

        else:
            for o in range(nCols + 2):
                print(colString[o], end="")
            print(" ")
            for p in range(nRows):
                print(rowString[p] + "|", end="")
                for j in range(nCols):
                    print(boardMask[p][j], end="")
                print("|")
            print("Current Score:" + str("{:03d}".format(score)) + " Last Move: [" + str(coords[0]) + "," + str(coords[1]) + "] is an INVALID COORDINATE")

    return boardData, boardMask, score, lastMove


def main():
    r, c = 16, 29
    iCoords = ["11", "1O", "G1", "GM", "77"]
    ships = ["[CARRIER=>", "[FRG=>", "[BCRUSR=>", "[DSTYR=>", "[SUBM=>"]
    score = 0
    lastMove = ""
    #                       carrier      frigate     submarine   cruiser             destroyer
    #           false miss  hit   false  hit   miss  hit   miss  hit    false  miss  hit   miss
    pCoords = ["AZ", "37", "1A", "CXA", "1O", "99", "79", "AP", "G2", "  ", "5K", "GO", "2B"]

    gBoard = generateGameBoard(r, c)

    gMask = copy.deepcopy(gBoard)

    for i in range(len(iCoords)):
        gBoard = loadShip(gBoard, r, c, iCoords[i], ships[i])
    for j in pCoords:
        print(checkCoord(r, c, j))

    for j in pCoords:
        print()
        (gBoard, gMask, score, lastMove) = updateGameBoard(gBoard, gMask, r, c, j, score, lastMove)


if __name__ == "__main__":
    main()
