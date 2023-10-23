from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle, Image
from pathlib import Path
import os


def capitalize_columns(columns):
    
    final_columns = [" ".join([word.capitalize() for word in col.split("_")]) for col in columns]
    
    return final_columns


def generateVideoBody(width, height, data):

    n_rows = data.shape[0]+1 
    
    heightList = [
        height * 10/100,
        height * 90/100
    ]
    
    widthList = [
        width * 5/100,
        width * 90/100,
        width * 5/100
    ]
    
    color = colors.gray
    
    videos_structure_table = Table([
        ['', 'Videos',''],
        ['', generateVideosTable(widthList[1], heightList[1], data), '']
    ]
    , widthList, heightList)
    
    videos_structure_table.setStyle(TableStyle([
        ('BOTTOMPADDING', (0,-1), (-1,-1), 650 - n_rows*18),
        ('FONTSIZE', (0,0), (-1,0), 20),
        ('BOTTOMPADDING', (0,0), (-1,0), 20),
        ('LEFTPADDING', (0,0), (-1,0), 10),
        ('LINEBELOW', (1,0), (-2,0), 1, color),
    ]))
    
    
    return videos_structure_table


def generateVideosTable(width, height, data):
    
    
    data = data.drop(columns = ["supplier_id", "final_post_id",])
    
    data = data[["catalog_name", "creator_db_name", "product_link", "post_url"]]
    
    
    data['catalog_name'] = data['catalog_name'].astype(str).str.slice(0, 30) + (data['catalog_name'].astype(str).str.slice(30) > '').map(lambda x: '...' if x else '')
    
    data = data.rename(columns = {"order_status_name" : "status"
                                  ,"order_date" : "date"
                                 ,"product_link" : "product"
                                 , "creator_db_name" : "creator"})
    
    columns = data.columns.tolist()
    
    columns = capitalize_columns(columns)
    
    table_data = [columns] + data.values.tolist()
    
    widthList = [
        width * 40/100, #date
        width * 20/100,
        width * 15/100, #sub_order_number
        width * 25/100,
    ]
    
    table = Table(table_data,\
                 widthList, 18)
    
    table.setStyle(TableStyle([
#         ('GRID', (0,0), (-1,-1), 1, 'red'),
        ('FONTSIZE', (0,0), (-1,0), 12),
        ('FONTCOLOR', (-1,0), (-1,-1), 'blue'),
        
#         ('ALIGN', (0,0), (-1,-1), 'CENTRE'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold') # Bold font header for table name
    ]))
    
    return table