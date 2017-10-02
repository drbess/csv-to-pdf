"""
This Python Script will prompt the user to choose from a menu of four options

@Authors: Devin and Geofrrey
"""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
import matplotlib.pyplot as plt
import time
import cStringIO
from reportlab.lib.utils import ImageReader
import csv
from matplotlib.pyplot import plot, draw, show
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
import time 

loop = 1 # Loop counter 

while loop == 1:
	print("Hello Mr. Shiggs! What would you like to do today?")
	print("Your options are:")
	print("1) Print PDF")
	print("2) Print Plot")
	print("3) Print Both PDF & Plot")
	print("4) Exit")
	choice = input("Choose your option: ")
	
	if choice == 1:
		YourBalance = 'name.csv'

		def import_shiggs(): # Defines the path
			balance_name = csv.reader(open('name.csv', 'rb')) # The csv reader, also defines the global name
			c = canvas.Canvas('Plotname.pdf', pagesize=landscape(letter))
			# Header text size, sets coordinates for the text on the page
			c.setFont('Helvetica', 48, leading=None)
			c.drawCentredString(415, 500, "YourBalance")
			i = 0
			topyval = 450
			PlotDict = {} # Variable for Plot Dictionary
			PrevDay = 0
			for row in balance_name: # For loop which counts each row in the csv file
				post_date = row[0]
				location = row[1]
				account = row[2]
				description = row[3]
				amount = row[4]
				balance = row[5]
				if i != 0:
					if row[0] == PrevDay: # if statement for adding the current row and previous row in the csv file
						 PlotDict[row[0]] = PlotDict[row[0]] + float(row[4])
					else:
						 PlotDict[row[0]] = float(amount)
				PrevDay = row[0]
				c.setFont('Helvetica', 9, leading=None)
				c.drawString(100, topyval - 30 * i, post_date),
				c.setFont('Helvetica', 9, leading=None)
				c.drawString(200, topyval - 30 * i, location)
				c.setFont('Helvetica', 9, leading=None)
				c.drawString(300, topyval - 30 * i, account)
				c.setFont('Helvetica', 9, leading=None)
				c.drawString(400, topyval - 30 * i, description)
				c.setFont('Helvetica', 9, leading=None)
				c.drawString(500, topyval - 30 * i, amount)
				c.setFont('Helvetica', 9, leading=None)
				c.drawString(600, topyval - 30 * i, balance)
			
				if i == 14: # the csv file contains more than
				   c.showPage()
				   topyval = 500
				   i = 0
				i = i + 1
			c.showPage()
			""" Generates a pdf without a graph
				fig = plt.figure(figsize=(8,6)) # draws the graph on the canvas
				plt.title('Daily Balance')
				plt.xlabel('Date')
				plt.ylabel('Amount')
				plt.bar(range(len(PlotDict)), PlotDict.values(), align='center')
				plt.xticks(range(len(PlotDict)), PlotDict.keys())
				imgdata = cStringIO.StringIO()
				fig.savefig(imgdata, format='png')
				imgdata.seek(0)
				Image = ImageReader(imgdata)
				
				c.drawImage(Image, cm, cm, 8 * inch, 5 * inch)    
				c.setFont('Courier-Bold', 48, leading=None)   
				#c.drawCentredString(415, 500, "")
				c.showPage()
				plt.show()
			"""
			print 'generating Pdf'
			c.save()
		import_name()
      


	elif choice == 3:
		 YourBalance = 'name.csv'

		 def import_shiggs(): # Defines the path
			 balance_name = csv.reader(open('name.csv', 'rb')) # Defines the global name
			 c = canvas.Canvas('YourBalance.pdf', pagesize=landscape(letter))
			 # Header text size, sets coordinates for the text on the page
			 c.setFont('Helvetica', 48, leading=None)
			 c.drawCentredString(415, 500, "YourBalance")
			 i = 0
			 topyval = 450
			 PlotDict = {} # Variable for Plot Dictionary
			 PrevDay = 0
			 for row in balance_name:
				 post_date = row[0]
				 location = row[1]
				 account = row[2]
				 description = row[3]
				 amount = row[4]
				 balance = row[5]
				 if i != 0:
					 if row[0] == PrevDay:
						  PlotDict[row[0]] = PlotDict[row[0]] + float(row[4])
					 else:
						  PlotDict[row[0]] = float(amount)
				 PrevDay = row[0]
				 
				 c.setFont('Helvetica', 9, leading=None)
				 c.drawString(100, topyval - 30 * i, post_date),
				 c.setFont('Helvetica', 9, leading=None)
				 c.drawString(200, topyval - 30 * i, location)
				 c.setFont('Helvetica', 9, leading=None)
				 c.drawString(300, topyval - 30 * i, account)
				 c.setFont('Helvetica', 9, leading=None)
				 c.drawString(400, topyval - 30 * i, description)
				 c.setFont('Helvetica', 9, leading=None)
				 c.drawString(500, topyval - 30 * i, amount)
				 c.setFont('Helvetica', 9, leading=None)
				 c.drawString(600, topyval - 30 * i, balance)
			
				 if i == 14:
					c.showPage()
					topyval = 500
					i = 0
				 i = i + 1
			 c.showPage()
				 
			 fig = plt.figure(figsize=(8, 6)) # draws the graph on the canvas
			 plt.title('Daily Balance')
			 plt.xlabel('Date')
			 plt.ylabel('Amount')
			 plt.bar(range(len(PlotDict)), PlotDict.values(), align='center')
			 plt.xticks(range(len(PlotDict)), PlotDict.keys())
			 imgdata = cStringIO.StringIO()
			 fig.savefig(imgdata, format='png')
			 imgdata.seek(0)
			 Image = ImageReader(imgdata)
				
			 c.drawImage(Image, cm, cm, 8 * inch, 5 * inch)    
			 c.setFont('Courier-Bold', 48, leading=None)   
			 #c.drawCentredString(415, 500, "")
			 c.showPage()
			 plt.show()
			
			 print 'generating Pdf'
			 c.save()
		 import_name()
	

	

	elif choice == 2:
		  YourBalance = 'name.csv'

		  def import_name(): # Defines the path
			  balance_name = csv.reader(open('Shiggs2.csv', 'rb')) # Defines the global name
			
			  c = canvas.Canvas('PlotName.pdf', pagesize=landscape(letter))
			  """
			  # Header text size, sets coordinates for the text on the page
			  c.setFont('Helvetica', 48, leading=None)
			  c.drawCentredString(415, 500, "NameBalance")
			  """
			  i = 0
			  topyval = 450
			  PlotDict = {} # Variable for Plot Dictionary
			  PrevDay = 0
			  for row in balance_name:
				  post_date = row[0]
				  location = row[1]
				  account = row[2]
				  description = row[3]
				  amount = row[4]
				  balance = row[5]
				  if i != 0:
					  if row[0] == PrevDay:
						   PlotDict[row[0]] = PlotDict[row[0]] + float(row[4])
					  else:
						   PlotDict[row[0]] = float(amount)
				  PrevDay = row[0]
				  """
				  c.setFont('Helvetica', 9, leading=None)
				  c.drawString(100, topyval - 30 * i, post_date),
				  c.setFont('Helvetica', 9, leading=None)
				  c.drawString(200, topyval - 30 * i, location)
				  c.setFont('Helvetica', 9, leading=None)
				  c.drawString(300, topyval - 30 * i, account)
				  c.setFont('Helvetica', 9, leading=None)
				  c.drawString(400, topyval - 30 * i, description)
				  c.setFont('Helvetica', 9, leading=None)
				  c.drawString(500, topyval - 30 * i, amount)
				  c.setFont('Helvetica', 9, leading=None)
				  c.drawString(600, topyval - 30 * i, balance)
				  """
			
				  if i == 14:
				     c.showPage()
				     topyval = 500
				     i = 0
				  i = i + 1
			  c.showPage()
		
			  fig = plt.figure(figsize=(8, 6)) # draws the graph on the canvas
			  plt.title('Daily Balance')
			  plt.xlabel('Date')
			  plt.ylabel('Amount')
			  plt.bar(range(len(PlotDict)), PlotDict.values(), align='center')
			  plt.xticks(range(len(PlotDict)), PlotDict.keys())
			  imgdata = cStringIO.StringIO()
			  fig.savefig(imgdata, format='png')
			  imgdata.seek(0)
			  Image = ImageReader(imgdata)
			
			  c.drawImage(Image, cm, cm, 8 * inch, 5 * inch)    
			  c.setFont('Courier-Bold', 48, leading=None)   
			  #c.drawCentredString(415, 500, "")
			  c.showPage()
			  plt.show()
		   
			  print 'generating Pdf'
			  c.save()
		  import_name()
		  
	elif choice == 4:
		   print("\n Goodbye!")
		   ans = None
		   
