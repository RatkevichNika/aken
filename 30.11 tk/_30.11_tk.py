from tkinter import *
klik=0
def klikker(event): #scitqvaem sobqtie
    global klik
    klik+=1
    lbl.configure(text=klik)
def klikker2(event):
    global klik
    if klik>0:
        klik-=1
    else:
        klik=0
    lbl.configure(text=klik)
def text_to_lbl(event):
    text=ent.get()
    lbl.configure(text=text)
    ent.delete(0,END)
def valik():
    val=str(var.get()) # znachenie 1, 2 ili 3
    ent.insert(END,val+', ')


aken=Tk() #akna loomine
aken.title('Akna nimetus')
aken.geometry('600x400') #pikseli, razmer

btn=Button(aken,text='Vajuta siia',font='Arial 20',fg='green',bg='lightblue', width=20, height=3) #font-wrift, bg-background, width-wirina
lbl=Label(aken, text='...') #aken piwem, chto bq nahodilos v okne Pealkiri
ent=Entry(aken,fg='blue',width=20,font='Arial 20') #Rida teksti sisestamiseks
var=IntVar() #StringVar()
var.set(2) #valib kolmas button 
r1=Radiobutton(aken,text='Esimene',variable=var,value=1,command=valik) #variable- csoistvo kotoroe svazqvaet nas s peremennoi. valik-vqbor
r2=Radiobutton(aken,text='Teine',variable=var,value=2,command=valik) 
r3=Radiobutton(aken,text='Kolmas',variable=var,value=3,command=valik) 

btn.bind('<Button-1>', klikker) #chto budet zapuskat '<>',  levaja knopka, (klikker- pridumali sami- funkcia)
btn.bind('<Button-3>', klikker2) #pravaja knopka mqwi
ent.bind('<Return>', text_to_lbl) #enter
lbl.pack()
btn.pack()
ent.pack()
r1.pack(side=LEFT)
r2.pack(side=LEFT)
r3.pack(side=LEFT)
aken.mainloop()



#-1 levaja knopka mqwi, -2 kolesiko, -3 pravaja knopka