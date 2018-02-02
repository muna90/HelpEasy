from Tkinter import *
from PIL import Image, ImageTk
from resizeimage import resizeimage
from phone import *
import sqlite3
import ttk
import datetime
from tkFont import Font, nametofont
##from ttkcalendar import *
##from calculator import Calc

import webbrowser


class HelpEasy(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.pack(side = TOP)
    
        self.initUI()

    def initUI(self):
        
        self.style = ttk.Style()
        self.parent.title('Help_Easy')
        self.parent.configure(background = 'white')
        self.parent.resizable(True, False) #resizable(xdirection, ydirection)

        self.img_back = Image.open(r'C:\Users\Administrator\Desktop\new Project\.vscode\files\orange.gif')
        eimg_back = ImageTk.PhotoImage(self.img_back) #adds backgroound pic to the screen
        self.lbl_background = ttk.Label(self.parent, text ='    Orange     ',
        compound = 'top',borderwidth=0, image = eimg_back, font = 'Forte 32', background = 'white', )#add text to the background
        self.lbl_background.image = eimg_back
        self.lbl_background.place(x=170, y=60)


        ttk.Label(self.parent, text = 'Orange Pharmacy', relief = 'sunken',background = 'orange3',font = 'arial 22 bold', anchor = 'center').pack(side = BOTTOM, fill = BOTH)

            
        self.option_add('*Font', 'cambria 10')
        self.option_add('*tearOff', False)
        menubar = Menu(self.parent)
        self.parent.config(menu = menubar)
        toolbar = Frame(self.parent, bd = 1, relief = RAISED)

        self.img = Image.open (r'C:\Users\Administrator\Desktop\new Project\.vscode\edith.png')
        eimg = ImageTk.PhotoImage(self.img)
        
        exitButton = Button(toolbar, text = ' Exit',compound = 'top',image = eimg, relief = FLAT, command = self.quit)
        exitButton.image = eimg
        exitButton.pack(side =RIGHT, padx = 2, pady = 2)
        toolbar.pack(side = TOP, fill = X)

        self.cashup = Image.open (r'C:\Users\Administrator\Desktop\new Project\.vscode\cashup.png')
        ecashup = ImageTk.PhotoImage(self.cashup)
        
        cashButton = Button(toolbar, text = 'Cashup',compound = TOP, image = ecashup, relief = FLAT, command = cashUp)
        cashButton.image = ecashup
        cashButton.pack(side = LEFT, padx = 2, pady = 2)
        toolbar.pack(side = TOP, fill = X)

        self.contact = Image.open (r'C:\Users\Administrator\Desktop\new Project\.vscode\Contacts.png')
        econtact  = ImageTk.PhotoImage(self.contact)
        
        contactButton = Button(toolbar, text ='Contacts', compound = TOP, image = econtact , relief = FLAT, command = Contacts)
        contactButton.image = econtact 
        contactButton.pack(side = LEFT, padx = 30, pady = 2)
        toolbar.pack(side = TOP)

        self.calculator = Image.open (r'C:\Users\Administrator\Desktop\new Project\.vscode\calc.png')
        ecalculator = ImageTk.PhotoImage(self.calculator)
        
        calculatorButton = Button(toolbar, text = 'Calculator', compound = 'top',image = ecalculator , relief = FLAT, command = doNothing)
        calculatorButton.image = ecalculator 
        calculatorButton.pack(side = LEFT, padx = 2, pady = 2)
        toolbar.pack(side = TOP)

        

        fileMenu = Menu(menubar)
        subMenu = Menu(fileMenu)
        UtilityMenu = Menu(menubar)
        suggestionMenu = Menu(menubar)
        contactsMenu = Menu(menubar)

        for topic, menu in (('Medical Aids',fileMenu ), ('Utilities',UtilityMenu), ('Suggestions', suggestionMenu), ('Contacts',contactsMenu)):
            menubar.add_cascade(label = topic, menu = menu)
        
        fileMenu.add_cascade(label= 'First Mutual', menu = subMenu, underline= 1)
        for fml_sub, comm in (('Login info', loginInfo), ('Procedure', fmlProcedure)):
            subMenu.add_command(label = fml_sub, command = comm)

        fileMenu.add_separator()

        for med_aid, comm in (('Fidelity',fidelity),('Cellmed',Cellmed),('Altfin',Altfin)):
            fileMenu.add_command(label= med_aid, command =comm )
       
        fileMenu.add_separator()

        for med_aid, comm in (('Generation',generation ), ('Liberty', doNothing),('Cimas', doNothing)):
            fileMenu.add_command(label= med_aid, command = comm)
      
        fileMenu.add_separator()
        fileMenu.add_command(label= 'Exit', command = self.quit)

        Utility = (('Monthend Procedure', Monthup), ('Cash up Procedure', cashUp), ('Master password', doNothing))
        for med_aid, comm in Utility:
            UtilityMenu.add_command(label = med_aid, command = comm)
       
        suggestion = (('Pharmacy staff', StaffRating), ('Improving sales', improvingSales), ('About HelpEasy', doNothing))
        for med_aid, comm in suggestion:
            suggestionMenu.add_command(label = med_aid, command =comm)

        contactsMenu.add_command(label ='Contact information', command = self.trying)

    def trying(self):
        cd = CalendarDialog(self)
        result = cd.result
        self.selected_date.set(result.strftime("%m/%d/%Y"))


    def Calculatore(self):
        new_window = Toplevel()
        app_calc = Calc(new_window)
def doNothing():
    print ('to improve')

def Contacts():
    top= Toplevel()
    top.geometry('+250+150')
    top.title('Contacts Information')
    infor = '''
    1.Phone Number: 0773 276 662(you can also whatsapp)\n
    2.Email: tichmutasa1990@gmail.com or tmtasa@greenwoodwsalers.co.zw
            '''

    contact_info = Label(top, text = infor,justify = LEFT)
    contact_info.pack(side = TOP)
    exit_button = Button(top, text = '**Done**', command = top.withdraw)
    exit_button.pack(side = RIGHT)
   

def loginInfo():
    top = Toplevel()

    top.title('Login Information')
    login_info = '''
    The Username is:Greenwood Chitungwiza
    and
    The password is: Greenw00d1
    '''
    fml= Label(top, width = 40, height = 6, text = login_info, font = 'cambria 14 bold', justify = LEFT)
    fml.pack(side = TOP)
    exit_button = Button(top, text = '**Done**', command = top.withdraw)
    exit_button.pack(side = RIGHT)
    
def fmlProcedure():
    top = Toplevel()
    top.geometry('+250+150')
    top.title('Procedure')
    procedure1 = '''
    The url is ...http://www.fmlmedical.co.zw/ and click login(far top right)\n
    After loging in!!\n
    1. Select the M/Aid\n 
    2. Click member lookup and input the M/aid # and search\n 
    3. Enquire by click a sign at the end of the line\n 
    5. NB check the active status if suspended PLEASE DONT DISPENSE!\n 
    6. If not click the sign on benefts\n 
    7. Select year AND then prescription drugs
    8. Click the sign on view and add bookings and then add new booking\n 
    9. Book now!NB:On single claim the response is always YES\n 
    10.WELL DONE!!
    '''
    
    fml=Label(top, width = 60, height = 22, text = procedure1, justify = LEFT)
    fml.pack(side = TOP)
    exit_button = Button(top, text = '**Done**', command = top.withdraw)
    exit_button.pack(side = RIGHT)

def Cellmed():
    top = Toplevel()
    top.geometry('+250+150')
    top.title('Cellmed Authorisation')

    cellmed_infor ='''
    The Username is Greenwood chitungwiza and password is greenwood\n
    The url is ... https://services.healthip.co.zw/provider\n
    Here you will find cellmed also!!\n
    1. Select the M/Aid\n 
    2. Click member lookup and input the M/aid # and search\n 
    3. Enquire by click a sign at the end of the line\n 
    5. NB check the active status if suspended PLEASE DONT DISPENSE!\n 
    6. If not click the sign on benefts\n 
    7. Select year AND then MOJOR SUBLIMIT\n
    8. Click the sign on view and add bookings and then add new booking\n 
    9. Book now!NB:On single claim the response is always YES\n 
    10. WELL DONE!!
    '''
    cellmedlabel = Label(top, text = cellmed_infor, width = 60, height = 25, justify = LEFT)
    cellmedlabel.pack(side = TOP)
    exit_button = Button(top, text = '**Done**', command = top.withdraw)
    exit_button.pack(side = RIGHT)

def Altfin():
    top = Toplevel()
    top.geometry('+250+150')
    top.title('Altfin Authorisation')

    altfin_infor ='''
    The Username is Greenwood chitungwiza and password is greenwood\n
    The url is ... https://services.healthip.co.zw/provider\n
    Here you will find cellmed also!!\n
    1. Select the M/Aid\n 
    2. Click member lookup and input the M/aid # and search\n 
    3. Enquire by click a sign at the end of the line\n 
    5. NB check the active status if suspended PLEASE DONT DISPENSE!\n 
    6. If not click the sign on benefts\n 
    7. Select year AND then CHRONIC OR ACUTE MEDICATION\n
    8. Click the sign on view and add bookings and then add new booking\n 
    9. Book now!NB:On single claim the response is always YES\n 
    10. WELL DONE!!
    '''

    lableframe = LabelFrame(top, text = 'Altfin Information')
    lableframe.grid(column = 0, row = 0)
    Altfinlabel = Label(lableframe, text = altfin_infor, width = 60, height = 25, justify = LEFT)
    Altfinlabel.grid(column = 0, row = 1)
    exit_button = Button(top, text = '**Done**', command = top.withdraw)
    exit_button.grid(column = 3, row = 3, sticky = E)

    lableframe2 = LabelFrame(top, text = 'Links')
    lableframe2.grid(column = 3, row = 0, sticky = N)

    def callback(event):
        webbrowser.open_new(r"https://services.healthip.co.zw/pls/apex/f?p=50000:LOGIN_DESKTOP:1568191912156")

    def callback2(event):
        webbrowser.open_new(r'file://C:\Users\Administrator\Desktop\new Project\.vscode\files\authorisation.mht')


    
    font = Font(underline = True)
    link = Label(lableframe2, text="Altfin authorisation link", fg="blue", cursor="hand2", font = font)
    link.grid(column = 3, row =0, sticky = N)
    link.bind("<Button-1>", callback)

    linklabel = Label(lableframe2, text="Here are the steps in pictures.", cursor="hand2")
    linklabel.grid(column = 3, row= 1)
   
    link2 = Label(lableframe2, text="Link to picture tutorials", cursor="hand2", font = font, fg = 'blue')
    link2.grid(column = 3, row= 2)
    link2.bind("<Button-1>", callback2)

def generation():
    top = Toplevel()
    top.geometry('+250+150')
    top.title('Generation Procedure')
    genertext = '''
    HERE IS THE PROCEDURE!\n
    1.Click the shortcut on the desktop and login\n
    2.Click the +booked benefit and then book entry\n
    3.Click create(top far right) and input members # then /\ sign at the end of the box\n
    4.Select add drugs and type the drug abd click /\ at the end of the next box\n
    5.After finding ad selecting the drung from a screen that pops up\n
    6.Input other parameters required and if done select apply changes (far top right)\n     if not select add row again.\n
    7.Repeat.'''
    labelframe = LabelFrame(top, text ="Generation Information")
    labelframe.grid(column = 0, row = 0)
    gener =Label(labelframe, height = 20,text = genertext, justify = LEFT)
    exitbut = Button(labelframe, relief =RAISED,text = '**Done**', command = top.withdraw)
    gener.grid(row = 1, column = 0, sticky = (N,S,E,W))
    exitbut.grid(row = 2, column = 0, sticky =E)

    #improving the app 16 September 2017

    lableframe2 = LabelFrame(top, text = 'Links')
    lableframe2.grid(column = 3, row = 0, sticky = N)

    def callback(event):
        webbrowser.open_new(r"http://196.29.39.134:8080/apex/f?p=103:LOGIN_DESKTOP:7439500171737")

    def callback2(event):
        webbrowser.open_new(r'http://196.29.39.134:8080/apex/f?p=103:LOGIN_DESKTOP:7439500171737')

    font = Font(underline = True)
    generation_web_link = Label(lableframe2, text = "Generation Authorisation Link", fg = 'blue', cursor= "hand2", font = font)
    generation_web_link.grid(column = 3, row = 0, sticky =N)
    generation_web_link.bind("<Button-1>", callback)

    picture_label = Label(lableframe2, text = "Here are the steps in pictures")
    picture_label.grid(column = 3, row = 1)

    picture_link = Label(lableframe2, text = "Link to picture tutorials", cursor = "hand2", font = font, fg = "blue")
    picture_link.grid(column = 3, row = 2)
    picture_link.bind("Button-1", callback2)



    
   


    

def fidelity():  
    top = Toplevel()
    top.geometry('+250+150')
    top.title('Fidelity Medical Aid')
    fidetext = '''
    The Username is Greenwood chitungwiza and password is greenwood\n
    You can click the link to your right.\n
    Here you will find cellmed also!!\n
    1. Select the M/Aid\n 
    2. Click member lookup and input the M/aid # and search\n 
    3. Enquire by click a sign at the end of the line\n 
    5. NB check the active status if suspended PLEASE DONT DISPENSE!\n 
    6. If not click the sign on benefts\n 
    7. Select year AND then PRESCRIBED CHRONIC DRUGS\n
    8. Click the sign on view and add bookings and then add new booking\n 
    9. Book now!NB:On single claim the response is always YES\n 
    10. WELL DONE!!
    '''
    #ammendemnt on 16 September 2017 and i was adding links
    

    fide_pic = Image.open (r"C:\Users\Administrator\Desktop\new Project\.vscode\fid.png")
    efide_pick = ImageTk.PhotoImage(fide_pic)
    Fidelity_Lableframe = LabelFrame(top, text = "Fidelity Authorisation", fg = "blue")
    Fidelity_Lableframe.grid(column = 0, row = 0, sticky = (N,S,E,W))

    fide_back_label = Label(Fidelity_Lableframe, image =efide_pick, text = fidetext, compound = TOP,justify = LEFT)
    fide_back_label.image = efide_pick
    fide_back_label.place(x= 0, y = 0)
    fide_back_label.grid(column = 0, row =1)



    




    # Fidelity_Lableframe = LabelFrame(top, text = "Fidelity Authorisation", fg = "blue")
    # Fidelity_Lableframe.grid(column = 0, row = 0, sticky = (N,S,E,W))

    # fide = Label(top, text = fidetext, justify = LEFT) #find how to align text
    # fide.grid(column = 0, row = 1)

    created_font = Font(underline = True)

    

    def Call_fidelity(event):
        webbrowser.open_new(r"C:\Users\Administrator\Desktop\new Project\.vscode\ice_video_20180131-123547.webm")
    #the function above takes you to the link for authorisation

    lableframe = LabelFrame(top, text = "Links", fg = "blue")
    lableframe.grid(column = 3, row = 0, sticky = N)

    Fide_label = Label(lableframe, text = "Fidelity Authorisation link",compound =LEFT, image = efide_pick,cursor = "hand2", font =  created_font, fg = "blue")
    Fide_label.grid(column = 3, row = 1)
    Fide_label.bind("Button-1",Call_fidelity)



    



  



def cashUp():
    top = Toplevel()
    top.geometry('+250+150')
    top.title('Cash_up Procedure')
    cashtext = '''
    HERE IS THE PROCEDURE!!\n
    1. Open PosWin and click on Cash Up\n
    2. Input the password\n
    3. Change the Till number to 7(top left) and refresh\n
    4. Input the AmountCounted and CreditCards and then click SaveAnal and IncRunNo. (middle bottom)\n
    5. WELL DONE!!
    '''
    cashup = Label(top, width = 80, height = 15, text = cashtext,justify = LEFT)
    exitbut = Button(top, relief =RAISED,text = '**Done**', command = top.withdraw)
    cashup.pack(side = TOP)
    exitbut.pack(side = RIGHT)

def Monthup():
    top = Toplevel()
    top.geometry('+250+150')
    top.title('Monthend procedure')
    monthtext1= '''
    MONTHEND PROCEDURE\n
    1.Open POSWIN and go to MAINTAINANCE.\n
    2.Click Monthend End Procedure and then Ageing\n
    3.Put the password when prompted to enter paswword\n
    4.Click the button PROCEED WITH AGEING  on the rigth bottom corner\n
    5.Click YES when asked NOT all scripts are imported into RECWIN, Proceed\n
    6.Click NO when asked INTREST HAS NOT BEEN CHARGED, CHARGE INTREST?\n
    7.Click OK when asked NO AGEING E-MAIL ADRESS IS AVAILABLE IS AVAILABLE FOR SENDING AGEING INFORMATION\n
    8.Well Done!! If your need more help see Help.
    '''
    mnthend = Label(top, width = 100, height = 20, text = monthtext1,justify = LEFT)
    exitbut = Button(top, relief =RAISED,text = '**Done**', command = top.withdraw)
    mnthend.pack(side = TOP)
    exitbut.pack(side = RIGHT)
    
    
    

def loginbox():
    label1 = Label(root, text = 'Name')
    label2 = Label(root,  text = 'Password')
    entry1 = Entry(root)
    entry2 = Entry(root)
    
    label1.grid(row = 0, sticky = E)
    label2.grid(row= 1, sticky =E)
    entry1.grid(row = 0, column = 1)
    entry2.grid(row= 1, column = 1)
    c= Checkbutton(root, text = 'Keep me logged in')
    c.grid(columnspan = 2)


     
def StaffRating():
    top = Toplevel()
    top.geometry('+250+150')
    top.title('Staff comments')

    staff = ('Rating','Comments')

    label1 = Label(top, text = 'Name')
    label1.grid(column = 0,row = 0, sticky = W)
    #creating an entry box for user to enter text
    entry1 = Entry(top)
    entry1.grid( row = 0, column = 1, sticky =(E,W))
    top.grid_rowconfigure(0, weight =3)


    Zerolabel = Label(top)
    Zerolabel.grid(row = 1, columnspan = 3)

    #creating the title for the textbox
    boxtitle = Label(top, text= 'Type your suggestion here', foreground = 'blue')
    boxtitle.grid(row = 2, column = 0,sticky = W)

    #creating the textbox for user to enter the suggestions
    textBox = Text(top, bd = 2, wrap = WORD, width = 35,height = 8, font = 'cambria 10')
    textBox.grid(row = 3, column = 0,columnspan = 2, sticky = (E,W))
    textBox.insert(1.0, 'Type here!')
    # textBox.get('1.0', END)

    save_button = Button(top, text = 'Save and Exit', cursor = 'arrow',command = doNothing)
    save_button.grid(row = 4, column = 1, sticky = E)



 #creating a database to store values

## con = sqlite3.connect('Improvingsales.db')
## cur = con.cursor()
## cur.execute('create table if not exists salesdata(name TEXT, sug INT)')
## con.commit()
## print('DB created')
## The problem is when I run it it tells me that the cur.execute line requires strings as parameters, but I have already defined text1 as string with StringVar.

def savedata(nameVar, suggestionVar):
    con = sqlite3.connect('improvingSales.db')
    cur = con.cursor()
    cur.execute('create table if not exists salesdata(name TEXT, sug INT)')
    cur.execute('INSERT INTO salesdata (name, sug) VALUES (?,?)', (nameVar.get(), suggestionVar.get()))
    con.commit()
    print('record inserted in salesdata')   

def search(nameVar):
    conn = sqlite3.connect('improvingSales.db')
    

    cursor = conn.execute("SELECT * from salesdata")
    for row in cursor:
        if row[0] == nameVar.get():
            print row[1]
        elif row[1] == nameVar.get():
            print row[0]
            
    print "Operation done successfully";
    conn.close()

def improvingSales():
    Db_name = 'Sales.db'
    with sqlite3.connect(Db_name) as conn:
        cursor = conn.cursor()
        query_result = cursor.execute('CREATE TABLE IF NOT EXISTS sugtable(unix REAL, NAME TEXT, Phone_number REAL, Suggestion TEXT)')

    def run_query(query, parameters =()):
        with sqlite3.connect(Db_name) as conn:
            cursor = conn.cursor()
            query_result = cursor.execute(query, parameters)
        return query_result

    def validation ():
        return len(nameEntry.get()) and len(phoneEntry.get())


    def adding():
        
        if validation():
            query = 'INSERT INTO sugtable VALUES (?,?,?,?)'
            parameters = (datetime.datetime.now(), nameEntry.get(), phoneEntry.get(), textBox.get('1.0', END))
            run_query(query, parameters)
            # message['text'] = 'Record %s added' %(nameEntry.get())
            nameEntry.delete(0, END)
            phoneEntry.delete(0, END)
            textBox.delete(1.0, END)
            
            # message['text'] = 'Fields empty!'
        
    top = Toplevel()
    top.geometry('+250+150')
    top.title('Sales Suggestions')
    frame1 =ttk.LabelFrame(top, text = 'Suggestions')
    frame1.grid()

##    creating the labels and entry
    sales = ('Name/Nickname', 'Phone Number')

    index = 0
    for sale in sales:
        ttk.Label(frame1, text = sale).grid(column = 1, row =index, sticky = E)
        index +=1

    nameEntry = StringVar()
    phoneEntry = StringVar()

    nameEntry  =ttk.Entry(frame1)
    nameEntry.grid( row = 0, column = 2, sticky = W)
    phoneEntry = ttk.Entry(frame1)
    phoneEntry.grid( row = 1, column = 2, sticky = W)
    
    ttk.Label(frame1, text = 'Enter your suggestions here!', foreground = 'red').grid(column = 1, row = 3)
    textBox = Text(frame1, bd = 2, wrap = WORD, width = 40,height =6)
    textBox.grid(row = 4, column = 2,columnspan = 2, sticky = (E,W))

    ttk.Button(frame1, text = 'Add records', command = adding).grid(column  =2, row = 5)

    message = ttk.Label(frame1, text = '', foreground= 'red').grid(column = 0, row = 5)

    tree = ttk.Treeview(frame1, height = 8)
    columnz = ('Date','Name', 'Phone Number', 'Suggestions')
    tree['columns'] = columnz

    tree.heading("#0", text = 'Time', anchor = W)
    tree.column("#0", stretch =NO, width =5, anchor =W)

    for col in columnz:
        tree.column(col, width = 50)
        tree.heading(col, text = col, anchor = 'center')
        if col == 'Date':
            tree.column(col, width= 5)

    tree.grid(row = 6,column = 0, columnspan = 4, sticky = (E,W))


   

    def viewing_records():
        records = tree.get_children()
        for record in records:
            tree.delete(record)
        query = 'SELECT * FROM sugtable ORDER BY NAME DESC'
        Db_rows = run_query(query)
        conn.close()
        cursor.close
        for row in Db_rows:
            tree.insert('', 0, text= row[0], values = (row[0], row[1],  row[2], row[3]))


    viewing_records()

    
def main():
    root = Tk()
    root.geometry('600x500+200+100')
    app = HelpEasy(root)
    root.mainloop()


if __name__ =='__main__':
    main()
