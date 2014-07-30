import csv
import sys

out = open("submission.csv","rU")
data = csv.reader(out)
data = [row for row in data]
out.close()

#create a 2d list for newdata
newdata = [[]]
newdata.append([])
for i in range(119):
    newdata[1].append('')



#print data
scoretitle = data[1][4]
instrumentation = data[1][12]
typeofwork = data[1][9]
typeofens = data[1][10]
arranger = data[1][6] + ", " + data[1][5]
arrangerfirstlast = data[1][5] + " " + data[1][6]
composer = data[1][8] + ", " + data[1][7]
composerfirstlast = data[1][7] + " " + data[1][8]
era = data[1][14]
form = data[1][15]
origin = data[1][19]
university = data[1][21]    
description = data[1][22]
priceold = data[1][23]
#pricenew = int(float(priceold[1:]))

#math.trunc(x)

productname = scoretitle + " by " + data[1][8] +"/" + data[1][6]

# enter data into the export row

newdata[1][0] = "Product"
newdata[1][2] = productname
newdata[1][6] = arranger
newdata[1][8] = "Right"

# product description

newdata[1][9] = "<p><strong>Composer:&nbsp;</strong> <span> " + composerfirstlast + "</span>&nbsp;</p> <p><strong>Arranger:&nbsp;</strong> " + arrangerfirstlast + "</p> <p><strong>Description:&nbsp;</strong>" + description + "</p><p><strong>Instrumentation:</strong>&nbsp;" + instrumentation + "</p> <p><strong>Era:</strong>&nbsp;<span>" + era + "</span></p>  <p><strong>Form:</strong>&nbsp;<span>" + form + "</span></p> <p><strong></strong><strong>Type of Work:&nbsp;</strong>" + typeofwork + "</p> <p><strong><span>Type of Ensemble:</span></strong>&nbsp;<span>" + typeofens + "</span></p> <p><strong><span><span>Nationality:</span></span></strong>&nbsp;<span>" + origin + "</span></p> <p><strong>Parts:&nbsp;</strong> Score</p> <p><strong>Publisher:</strong> SECONDAPRATTICA.ORG</p>"

#newdata[1][10] = pricenew
newdata[1][11] = "0"
#newdata[1][12] = pricenew
newdata[1][13] = "0"
newdata[1][14] = "0"
newdata[1][15] = "N"
newdata[1][21] = "Y"
newdata[1][22] = "N"
newdata[1][24] = "none"
newdata[1][27] = "Guitar"

# search keywords
newdata[1][88] = "Sheet Music, Music Score, Download Sheet Music, Downloadable PDF, " + typeofwork + ", " + typeofens + ", " + instrumentation

newdata[1][89] = productname

# meta keyword
newdata[1][90] = productname + ", Sheet Music, Music Score, Download Sheet Music, Downloadable PDF, " + typeofwork + ", " + typeofens + ", " + instrumentation

newdata[1][91] = description

newdata[1][118] = "Y"

if instrumentation == "Guitar" or "Guitar ":
    catalog = "Guitar"

if catalog == "Guitar" and typeofwork == "Chamber Music":
	subcatalog = "Guitar/Chamber Music/"
if origin == "Spain":
    nationality = "Spanish"
if origin == "France":
    nationality = "French"
if origin == "American":
    nationality = "American"
    
"""
out = ""

out.append(subcatalog + "Instrumentation/" + instrumentation + "/" + instrumentation + " " + typeofens)
out.append(";")
out.append(subcatalog + "Era/" + era)
out.append(";")
out.append(subcatalog + "Arrangers/See All Arrangers/" + arranger)
out.append(";")
out.append(subcatalog + "Composers/See All Composers/" + composer)
out.append(";")
out.append(subcatalog + "Form/" + form)
if nationality != NULL:
    out.append(";")
    out.append(subcatalog + "Nationality/" + nationality)

if university != "":
    out.append(";")
    out.append("Universities/" + university)

# write catalog
newdata[1][27] = out
"""
    
#write headers to first row
newdata[0] = ["Item Type","Product ID","Product Name","Product Type","Product Code/SKU","Bin Picking Number","Brand Name","Option Set","Option Set Align","Product Description","Price","Cost Price","Retail Price","Sale Price","Fixed Shipping Cost","Free Shipping","Product Warranty","Product Weight","Product Width","Product Height","Product Depth","Allow Purchases?","Product Visible?","Product Availability","Track Inventory","Current Stock Level","Low Stock Level","Category","Product File - 1","Product File Description - 1","Product File Max Downloads - 1","Product File Expires After - 1","Product File - 2","Product File Description - 2","Product File Max Downloads - 2","Product File Expires After - 2","Product File - 3","Product File Description - 3","Product File Max Downloads - 3","Product File Expires After - 3","Product File - 4","Product File Description - 4","Product File Max Downloads - 4","Product File Expires After - 4","Product File - 5","Product File Description - 5","Product File Max Downloads - 5","Product File Expires After - 5","Product Image ID - 1","Product Image File - 1","Product Image Description - 1","Product Image Is Thumbnail - 1","Product Image Sort - 1","Product Image ID - 2","Product Image File - 2","Product Image Description - 2","Product Image Is Thumbnail - 2","Product Image Sort - 2","Product Image ID - 3","Product Image File - 3","Product Image Description - 3","Product Image Is Thumbnail - 3","Product Image Sort - 3","Product Image ID - 4","Product Image File - 4","Product Image Description - 4","Product Image Is Thumbnail - 4","Product Image Sort - 4","Product Image ID - 5","Product Image File - 5","Product Image Description - 5","Product Image Is Thumbnail - 5","Product Image Sort - 5","Product Image ID - 6","Product Image File - 6","Product Image Description - 6","Product Image Is Thumbnail - 6","Product Image Sort - 6","Product Image ID - 7","Product Image File - 7","Product Image Description - 7","Product Image Is Thumbnail - 7","Product Image Sort - 7","Product Image ID - 8","Product Image File - 8","Product Image Description - 8","Product Image Is Thumbnail - 8","Product Image Sort - 8","Search Keywords","Page Title","Meta Keywords","Meta Description","MYOB Asset Acct","MYOB Income Acct","MYOB Expense Acct","Product Condition","Show Product Condition?","Event Date Required?","Event Date Name","Event Date Is Limited?","Event Date Start Date","Event Date End Date","Sort Order","Product Tax Class","Product UPC/EAN","Stop Processing Rules","Product URL","Redirect Old URL?","GPS Global Trade Item Number","GPS Manufacturer Part Number","GPS Gender","GPS Age Group","GPS Color","GPS Size","GPS Material","GPS Pattern","GPS Item Group ID","GPS Category","GPS Enabled"]

#newdata.append(data[1])
    
with open('converted.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(newdata)
    
    
