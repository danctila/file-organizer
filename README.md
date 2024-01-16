 # File Organizer

file-organizer is a simple python script to move files of any type from any folder to a redirect folder of choice.

## Installation

Copy the import_os.py file to your desktop for easiest access


## Usage
1. Change the file type you want to move if necessary. The default usage is Trim.mp4 for clips taken from games.

`if filename.endswith("Trim.mp4"):`

2. Set the source folder to grab files from.

` source_folder = r"c:\Users\User\Downloads"`


3. Set the destination folder to move files to. If it does not exist, it will be created by default as redirect.
   
`destination_folder = r"c:\Users\User\Desktop\redirect"`

## Reflection

**- What was the context for this project?**

When taking game clips with Nvidia GeForce Experience software, video files are sent to the downloads folder. This causes video files to become easily lost with the nature of the downloads folder holding so many files and constantly growing. 

**- What was buillt?**

This script allows for quick removal of any files in any folder with specified preferences into a seperate location with the click of one button instead of searching a specific folder for certain file types.

**- What tools were used?**

This program is built purely out of python using the os module for the use of manipulating files.



