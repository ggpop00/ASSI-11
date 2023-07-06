import tkinter as tk
import webbrowser as wb

root = tk.Tk()
#Netflix
def display_Netflix():
    user = req.get()
    print(user)
    if user:
        l2.config(text="Where did you hear about us?")
        wb.open("https://openconnect.netflix.com/en/faq/")
    else:
        l2.config(text="Please enter information")

#Flipkart
def display_flipkart():
    user = req.get()
    print(user)
    if user: 
        l2.config(text="Where did you hear about us?")
        wb.open("https://seller.flipkart.com/sell-online/faq")
    else:
        l2.config(text="Please enter information")

#twitter
def display_twitter():
        user = req.get()
        print(user)
        if user: 
            l2.config(text="Where did you hear about us?")
            wb.open("https://help.twitter.com/en/resources/new-user-faq")
        else:
            l2.config(text="Please enter required information")

#reddit
def display_reddit():
    user = req.get()
    print(user)
    if user: 
        l2.config(text="Where did you hear about us?")
        wb.open("https://www.reddit.com/wiki/faq/")
    else:
        print("Please enter required information")

req = tk.Entry(root, font=("Times New Roman", 20), width=30)
req.grid(row=0,column=1)

l1 = tk.Label(root, text="Enter enquiry:", font=("Times New Roman", 25))
l1.grid(row=0,column=0)

l2 = tk.Label(root, font=("Times New Roman", 25))
l2.grid()

Ne = tk.Button(root, text="Netflix", font=("Times New Roman", 20), width=10, bg="red",  activebackground="black",  command=display_Netflix)
Ne.grid()

Fl= tk.Button(root, text="Flipkart", font=("Times New Roman", 20),width=10,bg="yellow", activebackground="blue", command=display_flipkart)
Fl.grid()

tw = tk.Button(root, text="Twitter", font=("Times New Roman", 20),width=10,bg="blue", activebackground="white", command=display_twitter)
tw.grid()

Re = tk.Button(root, text="Reddit", font=("Times New Roman", 20),width=10, bg="orange", activebackground="white", command=display_reddit)
Re.grid()

root.mainloop()