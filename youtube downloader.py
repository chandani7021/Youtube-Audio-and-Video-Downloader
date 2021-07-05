from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube #pip install pytube3
import  tkinter  as tk
from tkinter import messagebox
import pywhatkit as kit
 

Folder_Name = ""

#file location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="#184a1e",bg = "#6d9ba6")

    else:
        messagebox . showinfo('choose folder','Please Choose Folder!!')

#donwload video
def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytdError.config(text="Paste Link again!!",fg="red")


    #download function
    select.download(Folder_Name)
    messagebox . showinfo('downloaded','Download Completed!!! Enjoy your music offline')
  



root = Tk()
root.title("Minitube Downloader")
root.geometry("800x800") #set window
root.columnconfigure(0,weight=1)#set all content in center.


# Creating a canvas 
canvas1 = tk.Canvas(root,height = 800,width = 800,bg = "#6d9ba6")
# Attaching the canvas
canvas1.pack()




#name label 
nameLabel = tk.Label(root,text="Youtube Audio &"" Video Downloader",font=("jost",25),bg = "#6d9ba6")
# placing the label in the canvas
canvas1.create_window(400,70,window = nameLabel)

#Ytd Link Label
ytdLabel = Label(root,text="Enter the URL of the Video",font=("jost",18),bg = "#6d9ba6")
# placing the label in the canvas
canvas1.create_window(280,150,window = ytdLabel)

#Entry Box
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=70,textvariable=ytdEntryVar)
# placing the label in the canvas
canvas1.create_window(380,190,window = ytdEntry)


#Error Msg
ytdError = Label(root,text=" ",fg="red",font=("jost",20))
print()
canvas1.create_window(400,190,window = ytdEntry)




# Function that performs something
def  function_button():
    n1 = str(ytdEntry.get())
    kit.playonyt(n1)
    messagebox . showinfo ( 'We found your music!' , 'Have fun enjoying your music!' )

#Asking play file label
playLabel = Label(root,text="Play the Video File",font=("jost",18),bg = "#6d9ba6")
# placing the label in the canvas
canvas1.create_window(230,270, window = playLabel)


#Creating a function button
button_1  =  Button (root,width=12, text="Play",font=("jost",15),bg="#ff3826",fg="white", command=function_button)
# placing the label in the canvas
canvas1.create_window(550,270,window = button_1)




#Asking save file label
saveLabel = Label(root,text="Save the Video File",font=("jost",18),bg = "#6d9ba6")
# placing the label in the canvas
canvas1.create_window(230,370,window = saveLabel)




#btn of save file
saveEntry = Button(root,width=12,bg="#ff3826",font=("jost",15),fg="white",text="Choose Path",command=openLocation)
# placing the label in the canvas
canvas1.create_window(550,370,window = saveEntry)





#Error Msg location
locationError = Label(root,text=" ",fg="red",font=("jost",15),bg = "#6d9ba6")
# placing the label in the canvas
canvas1.create_window(400,440,window = locationError)

#Download Quality
ytdQuality = Label(root,text="Select Quality",font=("jost",18),bg = "#6d9ba6")
# placing the label in the canvas
canvas1.create_window(240,510,window = ytdQuality)

#combobox
choices = ["720p","144p","Only Audio"]
ytdchoices = ttk.Combobox(root,values=choices,width=20)
# placing the label in the canvas
canvas1.create_window(550,510,window = ytdchoices)

#donwload btn
downloadbtn = Button(root,text="Download",width=15,font=("jost",18),bg="#c21000",fg="white",command=DownloadVideo)
# placing the label in the canvas
canvas1.create_window(410,620,window = downloadbtn)


#developer Label
developerlabel = Label(root,text="Enjoy your music!!!😄",font=("jost",25),bg = "#6d9ba6")
# placing the label in the canvas
canvas1.create_window(410,700,window = developerlabel)
root.mainloop()