# import pandas as pd
# import xml.etree.ElementTree as ET


# tree = ET.parse(r'D:\\projetos_python\\read_xml\\data\\test_integra.xml')
import xml.etree.ElementTree as ET

# Carrega o arquivo XML
tree = ET.parse(r'D:\\projetos_python\\read_xml\\data\\202310250836.xml')
root = tree.getroot()

# Itera sobre os elementos do XML
for child in root:
    print(child.tag, child.attrib)
    for subchild in child:
        print("\t", subchild.tag, subchild.attrib, subchild.text)
