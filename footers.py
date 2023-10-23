from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle, Image, Paragraph
from pathlib import Path

def generateFooter(widht, height):
    
    text = ""
    background_color = colors.HexColor('#580A46')
    
    
    footer_table = Table([[text]], widht, height)
    footer_table.setStyle(TableStyle([
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('BACKGROUND', (0,0), (-1,-1), background_color),
        ('TEXTCOLOR', (0,0), (-1,-1), 'white'),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        
    ]))
    
    return footer_table