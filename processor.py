from psd_tools import PSDImage

psd = PSDImage.open('km816_L_012.psd')
psd.compose().save('example.png')

for layer in psd:
    print(layer)
    if layer.is_group():
        for child in layer:
         print(child)
    
