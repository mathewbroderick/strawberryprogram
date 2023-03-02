
# ------ STRAWBERRY SIMULATOR VERSION 1.0.1.2.3 -------------
#
# patch notes v. 1.2: removed feature that would explode your computer 
#
# this program works (amazing, right?)! you may need to pip install a few modules
#
#

#importing needed modules for both gui and data analysis
import os
import tkinter as tk
from PIL import Image, ImageTk
import webbrowser
import pandas as pd
import numpy as np
import plotly.express as px
import plotly
from tkinterweb import HtmlFrame

#-------------DATA ANALYSIS STUFF------


#BEACH STRAWBERRY

#reading in the csv and "cleansing" the data - there were some species that got into the data
#set that shouldn't have been there - like mushrooms and birds

dirtybeachData = pd.read_csv("beachdata.csv")


#creating empty dataframe 

beachData = pd.DataFrame(columns = dirtybeachData.columns)

#appending rows that have the proper scientific name into the new dataframe

for i, row in dirtybeachData.iterrows():
    if 'Fragaria chiloensis' in dirtybeachData['scientific_name']:
       beachData.append()
    else:
        pass


#making the heatmap for beach strawberries

beachFig = px.density_mapbox(beachData, lat='latitude', lon='longitude', mapbox_style="stamen-terrain")

#and exporting it. this also opens the file which is kind of annoying but whatever

plotly.offline.plot(beachFig, filename="beachmap.html")


#VIRGINIA STRAWBERRY


#rinse and repeat, didn't have to clean this data since it didn't have any anomalies

virginiaData = pd.read_csv("virginiastrawberrydata.csv")

virginiaFig = px.density_mapbox(virginiaData, lat='latitude', lon='longitude', mapbox_style="stamen-terrain")

plotly.offline.plot(virginiaFig, filename="virginiamap.html")

#WILD STRAWBERRY

#i DID have to clean this data

dirtywildData = pd.read_csv("woodlanddata.csv")


#creating empty dataframe 

wildData = pd.DataFrame(columns = dirtywildData.columns)

#appending rows that have the proper scientific name into the new dataframe

for i, row in dirtywildData.iterrows():
    if 'Fragaria chiloensis' in dirtywildData['scientific_name']:
       wildData.append()
    else:
        pass

wildFig = px.density_mapbox(wildData, lat='latitude', lon='longitude', mapbox_style="stamen-terrain")

plotly.offline.plot(wildFig, filename="wildmap.html")



#-----GUI STUFF---------

#making the GUI for the main page of the program

#creating the window
window = tk.Tk()

window.geometry("1000x1000")

#this creates the frame for the main label and the label itself
mainlabelFrame = tk.Frame(master=window,
                          highlightbackground="#594F4F",
                          highlightthickness = 1,
                          width=600,
                          height=5,
                          bg="#547980")

#used .pack for this entire GUI - looking back i would have used .grid since it's a little more specific
#and would have made a nicer end product

mainlabelFrame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)


#creating the main label
mainLabel = tk.Label(
    mainlabelFrame,
    font=("Arial", 20),
    text="Please select a species of strawberry",
    width=50,
    height=5,
    bg="#547980"
    )

mainLabel.pack(padx=5, pady=2)

#this creates the frame for the buttons

buttonFrame = tk.Frame(master=window,
                      highlightbackground="#594F4F",
                      highlightthickness = 1,
                      width=600,
                      height=10,
                      bg="#9DE0AD")
buttonFrame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

#this creates the buttons for the different species of strawberries
#and here starts my misspelling of beach as beech - i fixed it where it counts
#but you'll see beech everywhere in the code and i didn't catch it until
#it was too late - whoopsies

beechButton = tk.Button(
    buttonFrame,
    font=("Arial", 7, 'bold'),
    text="Beach strawberry \n (Fragaria chiloensis)",
    width=30,
    height=8,
    bg="#594F4F",
    fg="black",
)

beechButton.pack(padx=5, pady=5, side=tk.LEFT, expand=True)

virginiaButton = tk.Button(
    buttonFrame,
    font=("Arial", 7, 'bold'),
    text="Virginia strawberry \n (Fragaria virginiana)",
    width=30,
    height=8,
    bg="#594F4F",
    fg="black",
)

virginiaButton.pack(padx=5, pady=5, side=tk.LEFT, expand=True)


wildButton = tk.Button(
    buttonFrame,
    font=("Arial", 7, 'bold'),
    text="Wild strawberry \n (Fragaria vesca)",
    width=30,
    height=8,
    bg="#594F4F",
    fg="black",
)

wildButton.pack(padx=5, pady=5, side=tk.LEFT, expand=True)


#this creates the sublabel for the window

sublabelFrame = tk.Frame(master=window,
                         highlightbackground="#594F4F",
                         highlightthickness = 1,
                         width=600,
                         height=100,
                         bg="#547980")

sublabelFrame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

#this is the sublabel below the buttons

subLabel = tk.Label(
    sublabelFrame,
    font=("Arial", 10),
    text="Clicking a button will open a window to view information \n about the selected species \n 🍓",
    width=50,
    height=10,
    bg="#547980"
    )

subLabel.pack(padx=5, pady=2)

#making the buttons functional

#there is a LOT of code packed into these since they call on data

#opening the window for the beech button

#defining a callback that opens a new tab in a web browser for wikipedia links
def callback(url):
   webbrowser.open_new_tab(url)

def beech_click(event):
   #opening a window above the original
    beechWindow= tk.Toplevel()
    beechWindow.geometry("1000x1000")
    #most of this is rinse and repeat of what I did for the original

 
    mainbeechlabelFrame = tk.Frame(master=beechWindow,
                          highlightbackground="#594F4F",
                          highlightthickness = 1,
                          width=100,
                          height=5,
                          bg="#547980")

    mainbeechlabelFrame.pack(fill=tk.BOTH, side=tk.TOP, ipadx= 1, ipady = 1, expand=True)

       
    mainbeechLabel = tk.Label(
        mainbeechlabelFrame,
        font=("Arial", 20),
        text="Beach strawberry (Fragari chiloensis)",
        width=100,
        height=5,
        bg="#547980"
        )
    mainbeechLabel.pack(padx=1, pady=1, ipadx=1, ipady = 1)
    #opening the image and resizing it to find into the window

    beechImage = Image.open("beech.jpg")
    smallbeechImage = beechImage.resize((250, 250))
    beechPhoto = ImageTk.PhotoImage(smallbeechImage)

    bimageLabel = tk.Label(mainbeechlabelFrame, image= beechPhoto)
    bimageLabel.image = beechPhoto
    bimageLabel.pack()




    subbeechFrame1 = tk.Frame(master=beechWindow,
                          highlightbackground="#594F4F",
                          highlightthickness = 1,
                          width=600,
                          height=5,
                          bg="#E5FCC2")
    subbeechFrame1.pack(fill=tk.BOTH, side=tk.TOP, ipadx=100, ipady = 100, expand=True)
    #making the wiki section of the window

    wikibeechLabel = tk.Label(
        subbeechFrame1,
        font=("Arial", 10),
        text="Fragaria chiloensis, the beach strawberry, \n Chilean strawberry, or coastal strawberry, \n is one of two species of wild \n strawberry that were hybridized \n to create the modern garden \n strawberry (F. × ananassa). \n It is native to the Pacific Ocean coasts of \n North and South America. \n Click to go to wikipedia page!",
        cursor="hand2", #changing the cursor to a link cursor since the text takes you to wikipedia
        width=40,
        height=20,
        bg="#9DE0AD",
        highlightbackground="#594F4F",
        highlightthickness = 1,
        )
    
    wikibeechLabel.pack(side=tk.LEFT, padx = 10, pady = 10, ipadx=10, ipady = 10)
    #making the section clickable, and providing a link to the wikipedia page

    wikibeechLabel.bind("<Button-1>", lambda e:
    callback("https://en.wikipedia.org/wiki/Fragaria_chiloensis"))

    mapbeechLabel = tk.Label(
        subbeechFrame1,
        font=("Arial", 10),
        text="",
        width=30,
        height=15,
        bg="#9DE0AD",
        highlightbackground="#594F4F",
        highlightthickness = 1,
        )
    mapbeechLabel.pack(side=tk.LEFT, padx = 10, pady = 10, ipadx=10, ipady = 10)
    #making the frame for the html file provided when the map coding is ran 

    mapbeechFrame = HtmlFrame(mapbeechLabel, horizontal_scrollbar="auto")
    mapbeechFrame.load_url("file://beachmap.html") 
    mapbeechFrame.pack(fill="both", expand=True)
 

    beechWindow.mainloop()

beechButton.bind("<Button-1>", beech_click)

#opening the window for the virg button. most of this is rinse and repeat from above


def virg_click(event):
    virgWindow= tk.Toplevel()
    virgWindow.geometry("1000x1000")

 
    mainvirglabelFrame = tk.Frame(master=virgWindow,
                          highlightbackground="#594F4F",
                          highlightthickness = 1,
                          width=100,
                          height=5,
                          bg="#547980")

    mainvirglabelFrame.pack(fill=tk.BOTH, side=tk.TOP, ipadx= 1, ipady = 1, expand=True)

       
    mainvirgLabel = tk.Label(
        mainvirglabelFrame,
        font=("Arial", 20),
        text="Virginia strawberry (Fragaria virginiana)",
        width=100,
        height=5,
        bg="#547980"
        )
    mainvirgLabel.pack(padx=1, pady=1, ipadx=1, ipady = 1)

    virgImage = Image.open("virg.jpg")
    smallvirgImage = virgImage.resize((250, 250))
    virgPhoto = ImageTk.PhotoImage(smallvirgImage)

    vimageLabel = tk.Label(mainvirglabelFrame, image= virgPhoto)
    vimageLabel.image = virgPhoto
    vimageLabel.pack()




    subvirgFrame1 = tk.Frame(master=virgWindow,
                          highlightbackground="#594F4F",
                          highlightthickness = 1,
                          width=600,
                          height=5,
                          bg="#E5FCC2")
    subvirgFrame1.pack(fill=tk.BOTH, side=tk.TOP, ipadx=100, ipady = 100, expand=True)

    wikivirgLabel = tk.Label(
        subvirgFrame1,
        font=("Arial", 10),
        text="Fragaria virginiana, known as Virginia strawberry, \n wild strawberry, common strawberry, \n or mountain strawberry, \n is a North American strawberry that grows across \n much of the United States \n and southern Canada. \n It is one of the two species of \n wild strawberry that were hybridized to create the \n modern domesticated garden strawberry \n (Fragaria × ananassa). \n Click to go to wikipedia page!",
        cursor="hand2",
        width=40,
        height=20,
        bg="#9DE0AD",
        highlightbackground="#594F4F",
        highlightthickness = 1,
        )
    
    wikivirgLabel.pack(side=tk.LEFT, padx = 10, pady = 10, ipadx=10, ipady = 10)

    wikivirgLabel.bind("<Button-1>", lambda e:
    callback("https://en.wikipedia.org/wiki/Fragaria_virginiana"))

    mapvirgLabel = tk.Label(
        subvirgFrame1,
        font=("Arial", 10),
        text="",
        width=30,
        height=15,
        bg="#9DE0AD",
        highlightbackground="#594F4F",
        highlightthickness = 1,
        )
    mapvirgLabel.pack(side=tk.LEFT, padx = 10, pady = 10, ipadx=10, ipady = 10)

    mapvirgFrame = HtmlFrame(mapvirgLabel, horizontal_scrollbar="auto")
    mapvirgFrame.load_url("virginiamap.html") 
    mapvirgFrame.pack(fill="both", expand=True)
 

    virgWindow.mainloop()

virginiaButton.bind("<Button-1>", virg_click) #binding the function above to the button I created earlier

#i love the way this event ended up being named

#opening the window for the ~wild~ button

def wild_click(event):
    wildWindow= tk.Toplevel()
    wildWindow.geometry("1000x1000")

 
    mainwildlabelFrame = tk.Frame(master=wildWindow,
                          highlightbackground="#594F4F",
                          highlightthickness = 1,
                          width=100,
                          height=5,
                          bg="#547980")

    mainwildlabelFrame.pack(fill=tk.BOTH, side=tk.TOP, ipadx= 1, ipady = 1, expand=True)

       
    mainwildLabel = tk.Label(
        mainwildlabelFrame,
        font=("Arial", 20),
        text="Wild strawberry (Fragaria vesca)",
        width=100,
        height=5,
        bg="#547980"
        )
    mainwildLabel.pack(padx=1, pady=1, ipadx=1, ipady = 1)

    wildImage = Image.open("wild.jpg")
    smallwildImage = wildImage.resize((250, 250))
    wildPhoto = ImageTk.PhotoImage(smallwildImage)

    wimageLabel = tk.Label(mainwildlabelFrame, image= wildPhoto)
    wimageLabel.image = wildPhoto
    wimageLabel.pack()




    subwildFrame1 = tk.Frame(master=wildWindow,
                          highlightbackground="#594F4F",
                          highlightthickness = 1,
                          width=600,
                          height=5,
                          bg="#E5FCC2")
    subwildFrame1.pack(fill=tk.BOTH, side=tk.TOP, ipadx=100, ipady = 100, expand=True)

    wikiwildLabel = tk.Label(
        subwildFrame1,
        font=("Arial", 10),
        text="Fragaria vesca, commonly called the wild strawberry, \n woodland strawberry, Alpine strawberry, \n Carpathian strawberry or European strawberry, \n is a perennial herbaceous plant in the rose \n family that grows naturally throughout much of the \n Northern Hemisphere, and that produces edible fruits. \n Click to go to wikipedia page!",
        cursor="hand2",
        width=40,
        height=20,
        bg="#9DE0AD",
        highlightbackground="#594F4F",
        highlightthickness = 1,
        )
    
    wikiwildLabel.pack(side=tk.LEFT, padx = 10, pady = 10, ipadx=10, ipady = 10)

    wikiwildLabel.bind("<Button-1>", lambda e:
    callback("https://en.wikipedia.org/wiki/Fragaria_vesca"))

    mapwildLabel = tk.Label(
        subwildFrame1,
        font=("Arial", 10),
        text="",
        width=30,
        height=15,
        bg="#9DE0AD",
        highlightbackground="#594F4F",
        highlightthickness = 1,
        )
    mapwildLabel.pack(side=tk.LEFT, padx = 10, pady = 10, ipadx=10, ipady = 10)

    mapwildFrame = HtmlFrame(mapwildLabel, horizontal_scrollbar="auto")
    mapwildFrame.load_url("wildmap.html") 
    mapwildFrame.pack(fill="both", expand=True)
 

    wildWindow.mainloop() #this loops the program so it "knows" that its waiting for a click

wildButton.bind("<Button-1>", wild_click)



window.mainloop() #finally, this loops the ENTIRE window as above.


