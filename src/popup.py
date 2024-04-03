# Importing Module
from pgu import gui

# Class widget or pop-up window
class POPDialog(gui.Dialog):
	
	# Class Constructor with variable-length Arguments
	def __init__(self,value,**params):
		
		# Title of the widget
		title = gui.Label("Popup Box")
		
		# Table in the Widget of size 100X70
		main = gui.Table(width= 100,height= 70)
		
		# Table Content or sample text
		label =gui.Label("This is a sample pop up!")
		
		# Ok Button
		btn = gui.Button("Ok")
		
		# Click Event and self.close Connection will 
		# terminate the pop-up when Click event will perform
		btn.connect(gui.CLICK, self.close, None)
		
		# Next row is created in table
		main.tr()
		
		# Label is added in the TD Container of the row
		main.td(label)
		
		# Next row 
		main.tr()
		
		# Next row
		main.tr()
		
		# Adding the button in the TD container
		main.td(btn)
		# Initializing the Constructor
		gui.Dialog.__init__(self,title,main)
		
if __name__ == '__main__':
	
	# Initial Application is created with default theme
	app = gui.Desktop()
	
	# Connecting the Quit event with app.quit function, 
	# which will terminate the gui execution
	app.connect(gui.QUIT,app.quit,None)
	
	# Initial Table
	c = gui.Table(width= 320,height= 240)
	
	# Object of the Class or widget
	dialog = POPDialog("#00ffff") 
	
	# Click me button 
	e = gui.Button("Click Me")
	
	# Connection Click event and open widget function, 
	# which will open the class widget or pop-up
	e.connect(gui.CLICK,dialog.open,None)
	
	# next row
	c.tr()
	# adding the connection in TD container
	c.td(e)
	
	# Running the initial application
	app.run(c)
