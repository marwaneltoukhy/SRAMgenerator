#!/usr/bin/env python
import math
from gdsMill import gdsMill

def main():
    count = int(input("Enter number of words: "))
    size = int(input("Enter word size: "))
    mainLayout(size, count)


def mainLayout(size, count):
    myTopLevelLayout = gdsMill.VlsiLayout("filledLayout")
    myTopLevelLayout.rename("testLayoutB")
    arr = []
    cell(count, size, arr)
    dec(size, arr)
    cir_arr(size, arr)
    myTopLevelLayout.addInstance(arr[0])
    writer = gdsMill.Gds2writer(myTopLevelLayout)
    writer.writeToFile("./output/FinalLayout.gds")

    myTopLevelLayout.addInstance(arr[1])

    #and now dump the filled layout to a new GDS file
    writer = gdsMill.Gds2writer(myTopLevelLayout)
    writer.writeToFile("./output/FinalLayout.gds")

    myTopLevelLayout.addInstance(arr[2])

    #and now dump the filled layout to a new GDS file
    writer = gdsMill.Gds2writer(myTopLevelLayout)
    writer.writeToFile("./output/FinalLayout.gds")


def cell(count, size, arr):
    arrayCellLayout2 = gdsMill.VlsiLayout()
    reader2 = gdsMill.Gds2reader(arrayCellLayout2)
    reader2.loadFromFile("SRAM_cell.gds")
    newLayout2 = gdsMill.VlsiLayout(name="arrayExample")
    newLayout2.rename("cell")
    for xIndex in range(0,size):
        for yIndex in range(0,count):
            newLayout2.addInstance(arrayCellLayout2, offsetInMicrons = (xIndex*4.5+28.85,yIndex*6.895-41.5-9.565-1.05))

    #newLayout.addInstance(dec())
    newLayout2.prepareForWrite()

    #and now dump the filled layout to a new GDS file
    writer = gdsMill.Gds2writer(newLayout2)
    writer.writeToFile("./output/SRAMcells.gds")
    arr.append(newLayout2)

def dec(count, arr):
    arrayCellLayout = gdsMill.VlsiLayout()
    reader = gdsMill.Gds2reader(arrayCellLayout)
    reader.loadFromFile("3x8_decoder.gds")
    arrayCellLayout.rename("arrayCell")
    newLayout = gdsMill.VlsiLayout(name="arrayExample")
    newLayout.rename("dec")
    for yIndex in range(0,count):
        newLayout.addInstance(arrayCellLayout, offsetInMicrons = (33,yIndex*55.16))

    newLayout.addInstance(arrayCellLayout, offsetInMicrons = (0,0))

    for i in range(0,count):
        newLayout.addBox(layerNumber = 49, offsetInMicrons = (22.4+2.6-(i*3),-1.33-48.265+(i*6.895)), width = 0.4, height = 49.778+0.307+(i*48.265)) 
        newLayout.addBox(layerNumber = 49, offsetInMicrons = (22.4+2.6-(i*3),0.3-0.09+(i*55.16)), width = (i*3), height = 0.28)
        newLayout.addBox(layerNumber = 49, offsetInMicrons = (3,-1.33-48.265+(i*6.895)), width = 22.4 - (i*3), height = 0.21)

    newLayout.addBox(layerNumber = 51, offsetInMicrons = (3,-34.23-3.955), width = 27.925+0.535, height = 0.21)
    newLayout.addBox(layerNumber = 49, offsetInMicrons = (0.525,-0.5), width = 0.21, height = count*55.16-47.335+0.8) 
    newLayout.addBox(layerNumber = 49, offsetInMicrons = (0.525,count*55.16-47.315-0.04), width = (33.21), height = 0.28)
    #newLayout.addBox(layerNumber = 49, offsetInMicrons = (33.525, 299.145+83.51+9.6), width = 0.21, height = 1.935)
    
    newLayout.prepareForWrite()

    #and now dump the filled layout to a new GDS file
    writer = gdsMill.Gds2writer(newLayout)
    writer.writeToFile("./output/decoder_hirarchy.gds")
    arr.append(newLayout)

def cir_arr(count, arr):
    arrayCellLayout3 = gdsMill.VlsiLayout()
    reader3 = gdsMill.Gds2reader(arrayCellLayout3)
    reader3.loadFromFile("col_cir.gds")
    newLayout3 = gdsMill.VlsiLayout(name="arrayExample")
    #newLayout3.rename("col_cir")
    for xIndex in range(0,count):
        newLayout3.addInstance(arrayCellLayout3, offsetInMicrons = (xIndex*4.5+37.495,-57.5))
    #newLayout.addInstance(dec())
    newLayout3.prepareForWrite()

    #and now dump the filled layout to a new GDS file
    writer = gdsMill.Gds2writer(newLayout3)
    writer.writeToFile("./output/column_cir.gds")
    arr.append(newLayout3)

main()