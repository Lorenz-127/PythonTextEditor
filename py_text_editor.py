# imports
from tkinter import *
from tkinter import filedialog
from tkinter import font


# root 
root = Tk()
root.title("Lorry's Text Editor")
root.geometry("1024x768")


# Set variable for open file name


# Create New File Function
def new_file():
	# Delete previous text
	my_text.delete("1.0", END)
	# Update status bars
	root.title("New File - New file")
	status_bar.config(text="New File        ")
	# Make global
	global open_status_name
	open_status_name = False

# Open Files

	# Delete previous text


	# Grab Filename

	# Check to see if there is a file name

		# Make filename global so we can access it later

	# Update Status bars

	# Open the file

	# Add file to textbox

	# Close the opened file


# Save As File

		# Update Status Bars

		# Save the file

		# Close the file


# Save File

		# Save the file

		# Close the file

		# Put status update or popup code

# Cut Text

	# Check to see if keyboard shortcut used

			# Grab selected text from text box

			# Delete Selected Text from text box

			# Clear the clipboard then append


# Copy Text

	# check to see if we used keyboard shortcuts

		# Grab selected text from text box

		# Clear the clipboard then append

# Paste Text

	#Check to see if keyboard shortcut used


# Bold Text

	# Create our font


	# Configure a tag


	# Define Current tags


	# If statement to see if tag has been set


# Italics Text

	# Create our font


	# Configure a tag


	# Define Current tags


	# If statement to see if tag has been set


# Change Selected Text Color

	# Pick a color

		# Create our font


		# Configure a tag


		# Define Current tags


		# If statement to see if tag has been set


# Change bg color


# Change ALL Text Color


# Print File Function

	#printer_name = win32print.GetDefaultPrinter()
	#status_bar.config(text=printer_name)
	
	# Grab Filename


	# Check to see if we grabbed a filename

		# Print the file


# Select all Text

	# Add sel tag to select all text


# Clear All Text


# Turn on Night Mode

	# toolbar buttons

	# file menu colors



# Turn Off Night Mode:

	# toolbar buttons

	# file menu colors






# Create a toolbar frame


# Create Main Frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# Create our Scrollbar For the Text Box


# Horizontal Scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Create Text Box
my_text = Text(
    my_frame, 
    width=97, 
    height=25, 
    font=("Consolas", 18), 
    selectbackground="yellow", 
    selectforeground="black", 
    undo=True, 
    yscrollcommand=text_scroll.set
)
my_text.pack()

# Configure our Scrollbar
text_scroll.config(command=my_text.yview)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add File Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_command(label="Save As")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")
edit_menu.add_command(label="Select All")
edit_menu.add_command(label="Clear")


# Add Color Menu


# Add Options Menu



# Add Status Bar To Bottom Of App
status_bar = Label(root, text='Ready        ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)


# Edit Bindings

# Select Binding



#fee = "John Elder"
#my_label = Label(root, text=fee[:-1]).pack()

# Create Buttons

# Bold Button

# Italics Button


# Undo/Redo Buttons


# Text Color

root.mainloop()