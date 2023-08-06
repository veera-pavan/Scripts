import xml.etree.ElementTree as ET
from prettytable import PrettyTable
from textwrap import fill
import sys
import os
    

xmlfile = "test.xml"
tree = ET.parse(xmlfile)
root = tree.getroot()

column_names=['column1','column2', 'column3', 'column4', 'column5']
table = PrettyTable(field_names=column_names, align='l')

for (targetxmltag1_val, targetxmltag2_val, targetxmltag3_val, targetxmltag4_val, targetxmltag5_val) in zip(
    root.findall('./xmltag1/childxmltag1/targetxmltag1'), 
    root.findall('./xmltag2/childxmltag2/targetxmltag2'), 
    root.findall('./xmltag3/childxmltag3/targetxmltag3'), 
    root.findall('./xmltag4/childxmltag4/targetxmltag4'),
    root.findall('./xmltag5/childxmltag5/targetxmltag5')):
    
    targetxmltag1_val = targetxmltag1_val.text.encode('utf8').decode('utf8')
    targetxmltag2_val = targetxmltag2_val.text.encode('utf8').decode('utf8')
    targetxmltag3_val = targetxmltag3_val.text.encode('utf8').decode('utf8')
    targetxmltag4_val = targetxmltag4_val.text.encode('utf8').decode('utf8')
    targetxmltag5_val = targetxmltag5_val.text.encode('utf8').decode('utf8')
     
        
    try:
        targetxmltag5_val = str(targetxmltag5_val.text.encode('utf8').decode('utf8')).replace('"', '')        
    except:
        targetxmltag5_val = "No messsage to print."
    
    table.add_row([targetxmltag1_val, targetxmltag2_val, fill(targetxmltag3_val, width=50), fill(targetxmltag4_val, width=50), 
                   Status_val+'/'+Result_val, fill(targetxmltag5_val, width=30)])
    
print(table)