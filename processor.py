from psd_tools import PSDImage
import pandas as pd

psd = PSDImage.open('NX816_L_AV_1000.psd')
psd.compose().save('example.png')

for layer in psd:
    print(layer)
    if layer.is_group():
        for child in layer:
         print(child)
         
font_height = {}           
file_name = 'height_mapper.xlsx'
with open(file_name, 'rb') as f:
    df = pd.read_excel(f, sheet_name='sheet1',names = ['B','C','D'],skiprows=9,nrows=20)
     
    for array in df.values:
     font_height[array[0]] = array[1]
    print(font_height)
    

file_StringID = 'MM_00_01_StringID.xlsx'
with open(file_StringID, 'rb') as strID:
    df = pd.read_excel(strID, sheet_name='StyleID',usecols=[0,1,6],skiprows=4)
    for array in df.values:
     if not pd.isnull(array[2]) :
        print(array)
