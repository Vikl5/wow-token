import urllib.request
import bs4
import tkinter as tk

window = tk.Tk()
close = tk.Button(window, text="Close", command=window.destroy)
close.pack()

def getWowTokenEU(url):
    res = urllib.request.urlopen("https://wowtokenprices.com/")
    
    soup = bs4.BeautifulSoup(res, "html.parser")
    elems = soup.select("#eu-money-text")
    price = "The price of a single WoW token on EU is currently "
    label = tk.Label(window, text=price + elems[0].text + " gold")
    label.pack()
    return label



rawUrl = "https://wowtokenprices.com/"
button = tk.Button(window,
                   text="Get WoW Token Price",
                   command=lambda: getWowTokenEU(rawUrl))
button.pack()

window.mainloop()