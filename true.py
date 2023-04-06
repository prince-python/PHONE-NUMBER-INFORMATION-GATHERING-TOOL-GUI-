def search():
    from truecallerpy import search_phonenumber
    id ="a2i0W--ed4Cn0-6-hIpg3_XhquQXjwmYPPQ4oI1UyWTAEnbx0MT_-jmLX6khrItJ"
    response=(search_phonenumber(number.get(), "IN", id))
    print(response)
    data=response["data"][0]

    name=data['name']

    khali.config(text="User name is "+name)

    


from tkinter import *


window=Tk()
window.title('PHONE NUMBER INFORMATION GATHERING')
window.geometry('600x600')

number=StringVar()

Label1=Label(window,text="ENTER A INDIAN NUMBER TO SEARCH",fg="green",font="Sans")
Label1.pack(pady='10')
text=Entry(window,textvariable=number,fg="black",font="Sans")
text.pack()
btn=Button(window,command=search,text='Search',fg="black",font="Sans")
btn.pack(pady='10')


khali=Label(window,fg="black",font="Sans")
khali.pack(pady='10')
birthday=Label(window,fg="black",font="Sans")
birthday.pack(pady='10')
sim=Label(window,fg="black",font="Sans")
sim.pack(pady='10')

window.mainloop()



