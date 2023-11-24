from reportlab.lib import colors
from reportlab.platypus import Table, Image, TableStyle
from pathlib import Path
import requests
from io import BytesIO
import io
import locale

def get_content_from_url(url):
    """
    Fetches content from a URL and returns a file-like object.

    Args:
    url: The URL from which to fetch the content.

    Returns:
    A BytesIO object containing the content fetched from the URL.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

        return BytesIO(response.content)
    except requests.RequestException as e:
        print(f"An error occurred while fetching content from the URL: {e}")
        return None

## locale.setlocale(locale.LC_ALL, 'en_IN')

sub_directory = os.path.join(os.getcwd(),'report')
 
image_orders = Path(os.path.join(sub_directory, Path("orders_icon.png")))
image_gmv = Path(os.path.join(sub_directory, Path("money_icon.png")))
image_affiliate_charge = image_gmv
image_gst = Path(os.path.join(sub_directory, Path("gst_icon.png")))
image_roi = Path(os.path.join(sub_directory, Path("roi_icon.png")))
image_video =  Path(os.path.join(sub_directory, Path("video_icon.png")))

# image_orders = get_content_from_url("https://drive.google.com/uc?export=view&id=1f8h0-YY_nYJq6ZsUKt5GT_1TVjjR5191")
# image_gmv = get_content_from_url("https://drive.google.com/uc?export=view&id=1f41yDyF84VHrXqGlba0xcUH4whh5dmJD")
# image_affiliate_charge = image_gmv
# image_gst = get_content_from_url("https://drive.google.com/uc?export=view&id=1f6X-HXVfC6iVGGWP-DifyVLpNR_xFXnx")
# image_roi = get_content_from_url("https://drive.google.com/uc?export=view&id=1f2jV1jjibbT_btRfm-HsqaiuW6jlFRph")
# image_video =  get_content_from_url("https://drive.google.com/uc?export=view&id=1f7Z5eTt8jy9hHA8dVZixkuB7H1BWxYTf")


def generateSummaryBody(width, height, meta_data = None, video = False):
    print(image_video)
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
        bottomPadding = 440
    else:
        main_data = getSummaryTable(widthList[1], heightList[1], meta_data)
        bottomPadding = 470
    
    summary_table_structure = Table([
        ['', "Summary [1st September - 15th October]", ''],
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
    print(image_video)
    
    # Orders
    # GMV
    # Affiliate Charge
    # RoI
    # Videos
    
    n_orders = locale.format_string("%d", meta_data["n_orders"], grouping=True)
    gmv = locale.format_string("%d", meta_data["gmv"], grouping=True)
    roi = locale.format_string("%d", meta_data["roi"], grouping=True)
    affiliate_charge = locale.format_string("%d", meta_data["fee"], grouping=True)
    gst_charge =  locale.format("%d", meta_data["gst"], grouping = True)
    
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
    
    ImageGST = Image(image_gst
                     , height = rowHeight
                     , width = widthList[1]
                     , kind = 'proportional')
    
    
    summary_table = Table([
        ['',ImageOrders,'# Orders',n_orders,''],
        ['',ImageGMV,'GMV',gmv,''],
        ['',ImageAffiliateCharges,'Affiliate Charges',affiliate_charge,''],
        ['',ImageGST,"GST",gst_charge,""],
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
    print(image_video)
    
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
    gst_charge =  locale.format("%d", meta_data["gst"], grouping = True)
    
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
    ImageGST = Image(image_gst
                     , height = rowHeight
                     , width = widthList[1]
                     , kind = 'proportional')
    
    summary_table = Table([
        ['',ImageViedo, "# Vidoes", n_videos,''],
        ['',ImageOrders,'# Orders',n_orders,''],
        ['',ImageGMV,'GMV',gmv,''],
        ['',ImageAffiliateCharges,'Affiliate Charges',affiliate_charge,''],
        ['',ImageGST,"GST",gst_charge,""],
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
    
