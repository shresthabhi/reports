from reportlab.lib import colors
from reportlab.platypus import Table, Image, TableStyle
from pathlib import Path
import os
import locale

## locale.setlocale(locale.LC_ALL, 'en_IN')

sub_directory = ''
 
image_orders = Path(os.path.join(sub_directory, "orders_icon.png"))
image_gmv = Path(os.path.join(sub_directory, "money_icon.png"))
image_affiliate_charge = image_gmv
image_roi = Path(os.path.join(sub_directory, "roi_icon.png"))
image_video =  Path(os.path.join(sub_directory, "video_icon.png"))

def generateSummaryBody(width, height, meta_data = None, video = False):
    
    widthList = [
        
        width * 5 / 100, # Left padding
        width * 90 / 100, # Main Body
        width * 5 / 100, # Right padding
    ]
    
    heightList = [
        height * 10/100,
        height * 90/100
    ]
    
    if video:
        main_data = getSummaryVideoTable(widthList[1], heightList[1], meta_data)
        bottomPadding = 470
    else:
        main_data = getSummaryTable(widthList[1], heightList[1], meta_data)
        bottomPadding = 500
    
    summary_table_structure = Table([
        ['', "Summary", ''],
        ['', main_data, ''],
    ], widthList, heightList)
    
    summary_table_structure.setStyle(TableStyle([
        
#         (('GRID'), (0,0), (-1,-1), 0.5, 'red'),
        
#         ('BOTTOMPADDING', (0,-1), (-1,-1), 650 - n_rows*18),
        ('FONTSIZE', (0,0), (-1,0), 20),
        ('BOTTOMPADDING', (0,0), (-1,0), 20),
        ('BOTTOMPADDING', (0,-1), (-1,-1), bottomPadding),
        ('LEFTPADDING', (0,0), (-1,0), 10),
        ('LINEBELOW', (1,0), (-2,0), 1, colors.gray),
    ]))
    
    return summary_table_structure


def getSummaryTable(width, height, meta_data):
    
    
    # Orders
    # GMV
    # Affiliate Charge
    # RoI
    # Videos
    
    n_orders = locale.format_string("%d", meta_data["n_orders"], grouping=True)
    gmv = locale.format_string("%d", meta_data["gmv"], grouping=True)
    roi = locale.format_string("%d", meta_data["roi"], grouping=True)
    affiliate_charge = locale.format_string("%d", meta_data["fee"], grouping=True)
    
    heightList = [
        height * 25 /100,
        height * 25 /100,
        height * 25 /100,
        height * 25 /100,    
    ]
    
    rowHeight = 30
    
    widthList = [
        
        width * 15/100, # Left Padding
        width * 10/100, # Image column
        width * 30/100, # Main data
        width * 30/100, # Main data
        width * 15/100, # Right Padding
    
    ]
    
    ImageOrders = Image(image_orders
                        , height = rowHeight
                        , width = widthList[1]
                        , kind = 'proportional')
    ImageGMV = Image(image_gmv
                     , height = rowHeight
                     , width = widthList[1]
                     , kind = 'proportional')
    ImageAffiliateCharges = Image(image_affiliate_charge
                                  , height = rowHeight
                                  , width = widthList[1]
                                  , kind = 'proportional')
    ImageROI = Image(image_roi
                    , height = rowHeight
                    , width = widthList[1]
                    , kind = 'proportional')
    
    
    summary_table = Table([
        ['',ImageOrders,'# Orders',n_orders,''],
        ['',ImageGMV,'GMV',gmv,''],
        ['',ImageAffiliateCharges,'Affiliate Charges',affiliate_charge,''],
        ['',ImageROI,'RoI',roi,''],
    ], widthList, rowHeight)
       
    summary_table.setStyle(TableStyle([
#         ('GRID', (0,0), (-1,-1), 1, 'red'),
        
        ('ALIGN', (3,0), (3,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        
        ('FONTSIZE', (0,0), (-1,-1), 15),
        ('BOTTOMPADDING', (2,0), (3,-1), 7.5),
    ]))
    
    return summary_table

def getSummaryVideoTable(width, height, meta_data):
    
    
    # Orders
    # GMV
    # Affiliate Charge
    # RoI
    # Videos
    
    n_videos = locale.format_string("%d", meta_data["n_videos"], grouping=True)
    n_orders = locale.format_string("%d", meta_data["n_orders"], grouping=True)
    gmv = locale.format_string("%d", meta_data["gmv"], grouping=True)
    roi = locale.format_string("%d", meta_data["roi"], grouping=True)
    affiliate_charge = locale.format_string("%d", meta_data["fee"], grouping=True)
    
    sub_directory = ''
    
    heightList = [
        height * 25 /100,
        height * 25 /100,
        height * 25 /100,
        height * 25 /100,    
    ]
    
    rowHeight = 30
    
    widthList = [
        
        width * 15/100, # Left Padding
        width * 10/100, # Image column
        width * 30/100, # Main data
        width * 30/100, # Main data
        width * 15/100, # Right Padding
    
    ]
    
    ImageOrders = Image(image_orders
                        , height = rowHeight
                        , width = widthList[1]
                        , kind = 'proportional')
    ImageGMV = Image(image_gmv
                     , height = rowHeight
                     , width = widthList[1]
                     , kind = 'proportional')
    ImageAffiliateCharges = Image(image_affiliate_charge
                                  , height = rowHeight
                                  , width = widthList[1]
                                  , kind = 'proportional')
    ImageROI = Image(image_roi
                    , height = rowHeight
                    , width = widthList[1]
                    , kind = 'proportional')
    ImageViedo = Image(image_video
                      , height = rowHeight
                      , width = widthList[1]
                      , kind = 'proportional')
    
    summary_table = Table([
        ['',ImageViedo, "# Vidoes", n_videos,''],
        ['',ImageOrders,'# Orders',n_orders,''],
        ['',ImageGMV,'GMV',gmv,''],
        ['',ImageAffiliateCharges,'Affiliate Charges',affiliate_charge,''],
        ['',ImageROI,'RoI',roi,''],
    ], widthList, rowHeight)
       
    summary_table.setStyle(TableStyle([
#         ('GRID', (0,0), (-1,-1), 1, 'red'),
        
        ('ALIGN', (3,0), (3,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        
        ('FONTSIZE', (0,0), (-1,-1), 15),
        ('BOTTOMPADDING', (2,0), (3,-1), 7.5),
    ]))
    
    return summary_table
    