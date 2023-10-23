from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle, Image, Paragraph
from pathlib import Path
import numpy as np
import pandas as pd


def capitalize_columns(columns):
    
    final_columns = [" ".join([word.capitalize() for word in col.split("_")]) for col in columns]
    
    return final_columns

def generateOrdersBody(width, height, data):  
    
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
    
    ordersBody_table = Table([
        ['', 'Orders',''],
        ['', generateOrdersTable(widthList[1], heightList[1], data), '']
    ]
    , widthList, heightList)
    
    ordersBody_table.setStyle(TableStyle([
        ('BOTTOMPADDING', (0,-1), (-1,-1), 650 - n_rows*18),
        ('FONTSIZE', (0,0), (-1,0), 20),
        ('BOTTOMPADDING', (0,0), (-1,0), 20),
        ('LEFTPADDING', (0,0), (-1,0), 10),
        ('LINEBELOW', (1,0), (-2,0), 1, color),
    ]))
    
    
    return ordersBody_table

def generateOrdersTable(width, height, data):
    
    data = data.drop(columns = ["supplier_id", "order_status", "order_status_name"])
    
    data = data[["order_date", "sub_order_num", "catalog_id", "gmv", "affiliate_charge", "product_link"]]
    data["order_date"] = data["order_date"].dt.strftime('%d %b')
    
    data = data.rename(columns = {"order_status_name" : "status"
                                  ,"order_date" : "date"
                                 ,"product_link" : "product"})
    
    
    
    columns = data.columns.tolist()
    
    columns = capitalize_columns(columns)
    
    table_data = [columns] + data.values.tolist()
    
    widthList = [
        width * 16.6/100-10, #date
        width * 16.6/100+10, #sub_order_number
        width * 16.6/100,    #catalog_id
        width * 16.6/100-30, #gmv
#         width * 14/100-15, #status
        width * 16.6/100+20, #affiliate charges
        width * 16.6/100-20, #product_link
    
    ]
    
    table = Table(table_data,\
                 widthList, 18)
    
    table.setStyle(TableStyle([
#         ('GRID', (0,0), (-1,-1), 1, 'red'),
        ('FONTSIZE', (0,0), (-1,0), 12),
        ('FONTCOLOR', (-1,0), (-1,-1), 'blue'),
        
        ('ALIGN', (0,0), (-1,-1), 'CENTRE'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold') # Bold font header for table name
    ]))
    
    return table