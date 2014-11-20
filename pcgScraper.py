__author__ = 'Rossco'


"""

PROJECT GOAL...

- develop a basic familiarity with Python (2.7) : syntax, libraries (mechanize, Tkinter),
and IDE (Pycharm 3.4)


WHAT IT DOES...

- accesses desired URL (http://pdxcodeguild.com/apply/) in a headless browser via mechanize

- console is launched with input via keyboard press <ENTER>, which terminates the UI (Tkinter)

- displays HTML of desired page, with Page Title and URL to IDE console

- auto-saves URL content as .html file in current workspace directory

- auto-saves PCG Logo from desired HTML page to local machine

- utilizes UserAgent spoofing

"""

#REF: http://wwwsearch.sourceforge.net/mechanize/
import os
import mechanize
from Tkinter import *
import Tkinter


#create window
root = Tk()
#window layout : title and dimensions are cast
root.title("pcg HTML Scraper")
root.geometry("600x460")
#set the background of the rootLayout to #000
root.config(bg='black')
#set custom icon (PCG Logo)
root.iconbitmap(os.path.dirname(os.path.realpath(__file__)) + '\guild_logo.ico')


#access desired URL in headless browser (via mechanize),
#set up single-key input termination of console via <ENTER> key w/var "btn_command"
#display this HTML to console
def btn_command(*args):
    access_url = mechanize.urlopen("http://pdxcodeguild.com/apply/")
    page_data = access_url.read()
    print page_data
    root.destroy()


#bind key-press <ENTER> w/var "button" : styling attributes for "button"
root.bind("<Return>", btn_command)
button = Tkinter.Button(root, text='get HTML', width='100', height='10', background='black',
                        fg='yellow', cursor='spider', command=btn_command)
button.pack()


#display helpful instruction to end-user : styling attributes for "text"
text = Text(root, height=17, width=100, background='black', fg='yellow', font='console',
          cursor='trek', insertbackground='yellow', wrap='word')
text.pack(side=LEFT)
text.insert(END, "Press <ENTER> to load HTML in IDE console, or click \"get HTML\" to do same...")


#end this loop for "root"
root.mainloop()


#set-up (headless) Browser object and assign to var "br"
br = mechanize.Browser()
br.open("http://pdxcodeguild.com/apply/")

#useragent spoofer : simulates a UserAgent [sans proxies, cookies]
br.addheaders = [('User-agent',
                  'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) '
                  'Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


#access URL via mechanize lib and assign to var "response"
response = mechanize.urlopen("http://pdxcodeguild.com/apply/")

#on click of button, get this page's HTML
html_data = response.read()

#save URL page's HTML to "pageData.html" : (save to current/workspace directly)
with open('pageData.html', 'w') as content:
    content.write(html_data)


#/nl
print ''

#URL title && address
print 'page title: ' + br.title()
print 'URL accessed: ' + br.geturl()

#/nl
print ''

print 'UserAgent spoofing... '
print br.addheaders

#/nl
print ''

#display default save location of .html page location in console
print 'HTML source has been saved to: ' + os.path.dirname(os.path.realpath(__file__)) + '\pageData.html'

#/nl
print ''

#download and displays default save location of PCG Logo location in IDE console
f = br.retrieve('http://pdxcodeguild.com/static/images/guild_logo_orange.png')[0]
print 'PCG Logo has been saved to: ' + f


"""
USEFUL functions for later use (included below)
"""

#mechanize

'''
#get all links on page
for link in br.links():
    print link.text, link.url
'''

'''
#find all forms on page
for f in br.forms():
    print f
'''

'''
#display HTML of desired URL
print br.response().read()
'''


#Tkinter

'''
label = Label(root, text = 'pick a number of seconds for the function to recur in', bg='white')
label.pack()
'''