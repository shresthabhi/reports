from reportlab.platypus import Table, TableStyle, Image
from reportlab.lib import colors
from pathlib import Path
import os

def generateHeader(width, height):
    
    widthList = [
        width * 20 / 100,
        width * 80 / 100
    ]
    
    MEESHO_IMAGE_PATH = os.path.join(os.getcwd(),Path('meesho_logo.png'))
    MEESHO_IMAGE = Image(MEESHO_IMAGE_PATH
                         , widthList[0]
                         , height*0.8
                         , kind = 'proportional')
    
    text = 'AFFILIATE PROGRAM REPORT'
    
    header_table = Table([
        [MEESHO_IMAGE, text]
    ], widthList, height)
    
    header_table.setStyle(TableStyle([
#         ('GRID', (0,0), (-1,-1), 1, 'red'),
        
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        
        ('FONTSIZE', (0,0), (-1,-1), 24),
        
#         ('LEFTPADDING', (0,0), (-1,-1), 20),
        
        
    ]))
    
    
    return header_table
