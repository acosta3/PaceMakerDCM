# from tkinter import *
# from tkinter import ttk
# from SqlConnection import create_db_connection
# from Login import USERDATA
# db_connection = create_db_connection()
#
#
#
#
# upper_limit = "0"
# lower_limit = 0
# atrial_amp = 0
# atrial_pulse = 0
# ventricular_amp = 0
# ventricular_pulse = 0
# vrp = 0
# arp = 0
# detected = True
# in_range = True
# lost_due_to_noise = False
# model_number = 0000000
# revision_numer = 000000
# serial_number = 000000
# institution_name = ""
# username=""
#
# ##Import SQL Connection###########
#
#
#
# def Start():
#     home_window = Tk()
#     home_window.title("Pacemaker Project")
#     home_window.config(bg="#063326")
#
#     notebook = ttk.Notebook(home_window)
#     notebook.pack(pady=15)
#
#     tab1 = Frame(notebook, width=800, height=500)
#     tab2 = Frame(notebook, width=800, height=500)
#     tab3 = Frame(notebook, width=800, height=500)
#     tab4 = Frame(notebook, width=800, height=500)
#     tab5 = Frame(notebook, width=800, height=500)
#     tab6 = Frame(notebook, width=800, height=500)
#
#     tab1.pack(fill="both", expand=1)
#     tab2.pack(fill="both", expand=1)
#     tab3.pack(fill="both", expand=1)
#     tab4.pack(fill="both", expand=1)
#     tab5.pack(fill="both", expand=1)
#     tab6.pack(fill="both", expand=1)
#
#     notebook.add(tab1, text="Home")
#     notebook.add(tab2, text="AAO")
#     notebook.add(tab3, text="VOO")
#     notebook.add(tab4, text="AAI")
#     notebook.add(tab5, text="VVI")
#     notebook.add(tab6, text="About")
#
#     Label(tab1, text="Welcome (Name)!").pack(pady=10)
#     Label(tab1, text="Programmable Parameters").pack()
#     Label(tab1, text='Pacemaker Detected: ' + str(detected)).place(x=30, y=285)
#     Label(tab1, text='\nIn Range: ' + str(in_range)).place(x=220, y=270)
#     Label(tab1, text='\nLost Due to Noise: ' + str(lost_due_to_noise)).place(x=350, y=270)
#
#     Label(tab1, text='Upper Rate Limit ').place(x=100, y=60)
#     Label(tab1, text='Lower Rate Limit ').place(x=100, y=90)
#     Label(tab1, text='Atrial Amplitude ').place(x=100, y=120)
#     Label(tab1, text='Atrial Pulses Width ').place(x=100, y=150)
#     Label(tab1, text='Ventricular Amplitude ').place(x=300, y=60)
#     Label(tab1, text='Ventricular Pulse Width ').place(x=300, y=90)
#     Label(tab1, text='VRP ').place(x=300, y=120)
#     Label(tab1, text='ARP ').place(x=300, y=150)
#
#     Label(tab2, text="Upper Limit Rate: ").place(x=0, y=17)
#     my_entry = Entry(tab2)
#     my_entry.grid(row=0, column=2, pady=20, padx=200)
#
#     Label(tab2, text="Lower Limit Rate: ").place(x=0, y=77)
#     my_entry2 = Entry(tab2)
#     my_entry2.grid(row=1, column=2, pady=20, padx=100)
#
#     Label(tab2, text="Atrial Pulse Width: ").place(x=0, y=137)
#     my_entry3 = Entry(tab2)
#     my_entry3.grid(row=2, column=2, pady=20, padx=100)
#
#     Label(tab2, text="Atrial Amplitude: ").place(x=0, y=197)
#     my_entry4 = Entry(tab2)
#     my_entry4.grid(row=3, column=2, pady=20, padx=100)
#
#     Finalize_AAO = Button(tab2, text="Program", width=10, command=SubmitAAO(my_entry.get(),my_entry2.get(),my_entry3.get(),my_entry4.get())).place(x=35, y=250)
#
#     Label(tab3, text="Upper Limit Rate: ").place(x=0, y=17)
#     my_entry5 = Entry(tab3)
#     my_entry5.grid(row=0, column=2, pady=20, padx=200)
#
#     Label(tab3, text="Lower Limit Rate: ").place(x=0, y=77)
#     my_entry6 = Entry(tab3)
#     my_entry6.grid(row=1, column=2, pady=20, padx=100)
#
#     Label(tab3, text="Ventricular Amplitude: ").place(x=0, y=137)
#     my_entry7 = Entry(tab3)
#     my_entry7.grid(row=2, column=2, pady=20, padx=100)
#
#     Label(tab3, text="Ventricular Pulse Width: ").place(x=0, y=197)
#     my_entry8 = Entry(tab3)
#     my_entry8.grid(row=3, column=2, pady=20, padx=100)
#
#     Finalize_VOO = Button(tab3, text="Program", width=10, command=SubmitVOO(my_entry5.get(),my_entry6.get(),my_entry7.get(),my_entry8.get())).place(x=35, y=250)
#
#     Label(tab4, text="Upper Limit Rate: ").place(x=0, y=17)
#     my_entry9 = Entry(tab4)
#     my_entry9.grid(row=0, column=2, pady=20, padx=200)
#
#     Label(tab4, text="Lower Limit Rate: ").place(x=0, y=77)
#     my_entry10 = Entry(tab4)
#     my_entry10.grid(row=1, column=2, pady=20, padx=100)
#
#     Label(tab4, text="Atrial Amplitude: ").place(x=0, y=137)
#     my_entry11 = Entry(tab4)
#     my_entry11.grid(row=2, column=2, pady=20, padx=100)
#
#     Label(tab4, text="Atrial Pulse Width: ").place(x=0, y=197)
#     my_entry12 = Entry(tab4)
#     my_entry12.grid(row=3, column=2, pady=20, padx=100)
#
#     Finalize_AII = Button(tab4, text="Program", width=10, command=SubmitAII(my_entry9.get(),my_entry10.get(),my_entry11.get(),my_entry12.get())).place(x=35, y=250)
#
#     Label(tab5, text="Upper Limit Rate: ").place(x=0, y=17)
#     my_entry13 = Entry(tab5)
#     my_entry13.grid(row=0, column=2, pady=20, padx=200)
#
#     Label(tab5, text="Lower Limit Rate: ").place(x=0, y=77)
#     my_entry14 = Entry(tab5)
#     my_entry14.grid(row=1, column=2, pady=20, padx=100)
#
#     Label(tab5, text="Ventricular Amplitude: ").place(x=0, y=137)
#     my_entry15 = Entry(tab5)
#     my_entry15.grid(row=2, column=2, pady=20, padx=100)
#
#     Label(tab5, text="Ventricular Pulse Width: ").place(x=0, y=197)
#     my_entry16 = Entry(tab5)
#     my_entry16.grid(row=3, column=2, pady=20, padx=100)
#
#     Finalize_VOO = Button(tab5, text="Program", width=10, command=SubmitVOO2(my_entry13.get(),my_entry14.get(),my_entry15.get(),my_entry16.get())).place(x=35, y=250)
#
#     Label(tab6, text='Application Model Number: ' + str(model_number), width=50, height=5).pack()
#     Label(tab6, text='Application Software Revision Number: ' + str(revision_numer), width=50, height=5).pack()
#     Label(tab6, text='DCM Serial Number: ' + str(serial_number), width=50, height=5).pack()
#     Label(tab6, text='Institution Name: ' + institution_name, width=50, height=5).pack()
#
#     home_window.mainloop()
#
# def SubmitVOO(upper_rate_limit,lower_rate_limit,v_amplitude,v_pulswidth):
#     voo_submitted = Toplevel()
#     voo_submitted.geometry("700x500")
#     Label(voo_submitted, text='Upper Rate Limit: ' + str(upper_rate_limit)).place(x=10, y=60)
#     Label(voo_submitted, text='Lower Rate Limit: ' + str(lower_rate_limit)).place(x=10, y=90)
#     Label(voo_submitted, text='Atrial Amplitude: x').place(x=10, y=120)
#     Label(voo_submitted, text='Atrial Pulse Width: x').place(x=10, y=150)
#     Label(voo_submitted, text='Ventricular Amplitude: ' + str(v_amplitude)).place(x=185, y=60)
#     Label(voo_submitted, text='Ventricular Pulse Width: ' + str(v_pulswidth)).place(x=185, y=90)
#     Label(voo_submitted, text='VRP: x').place(x=185, y=120)
#     Label(voo_submitted, text='ARP: x').place(x=185, y=150)
#
# def SubmitAII(upper_rate_limit,lower_rate_limit,atrial_amplitude,atrial_pulse_width):
#     aii_submitted = Toplevel()
#     aii_submitted.geometry("700x500")
#     Label(aii_submitted, text='Upper Rate Limit: ' + str(upper_rate_limit)).place(x=10, y=60)
#     Label(aii_submitted, text='Lower Rate Limit: ' + str(lower_rate_limit)).place(x=10, y=90)
#     Label(aii_submitted, text='Atrial Amplitude: ' + str(atrial_amplitude)).place(x=10, y=120)
#     Label(aii_submitted, text='Atrial Pulse Width: ' + str(atrial_pulse_width)).place(x=10, y=150)
#     Label(aii_submitted, text='Ventricular Amplitude: x').place(x=185, y=60)
#     Label(aii_submitted, text='Ventricular Pulse Width: x').place(x=185, y=90)
#     Label(aii_submitted, text='VRP: x').place(x=185, y=120)
#     Label(aii_submitted, text='ARP: x').place(x=185, y=150)
#
#
# def SubmitAAO(upper_rate_limit,lower_rate_limit,atrial_amplitude,atrial_pulse_width):
#     aao_submitted = Toplevel()
#     aao_submitted.geometry("700x500")
#     Label(aao_submitted, text='Upper Rate Limit: ' + str(upper_rate_limit)).place(x=10, y=60)
#     Label(aao_submitted, text='Lower Rate Limit: ' + str(lower_rate_limit)).place(x=10, y=90)
#     Label(aao_submitted, text='Atrial Amplitude: ' + str(atrial_amplitude)).place(x=10, y=120)
#     Label(aao_submitted, text='Atrial Pulse Width: ' + str(atrial_pulse_width)).place(x=10, y=150)
#     Label(aao_submitted, text='Ventricular Amplitude: x').place(x=185, y=60)
#     Label(aao_submitted, text='Ventricular Pulse Width: x').place(x=185, y=90)
#     Label(aao_submitted, text='VRP: x').place(x=185, y=120)
#     Label(aao_submitted, text='ARP: x').place(x=185, y=150)
#
# def SubmitVOO2(upper_rate_limit,lower_rate_limit,v_amplitude,v_pulswidth):
#     voo_submitted = Toplevel()
#     voo_submitted.geometry("700x500")
#     Label(voo_submitted, text='Upper Rate Limit: ' + str(upper_rate_limit)).place(x=10, y=60)
#     Label(voo_submitted, text='Lower Rate Limit: ' + str(lower_rate_limit)).place(x=10, y=90)
#     Label(voo_submitted, text='Atrial Amplitude: x').place(x=10, y=120)
#     Label(voo_submitted, text='Atrial Pulse Width: x').place(x=10, y=150)
#     Label(voo_submitted, text='Ventricular Amplitude: ' + str(v_amplitude)).place(x=185, y=60)
#     Label(voo_submitted, text='Ventricular Pulse Width: ' + str(v_pulswidth)).place(x=185, y=90)
#     Label(voo_submitted, text='VRP: x').place(x=185, y=120)
#     Label(voo_submitted, text='ARP: x').place(x=185, y=150)
#
#
# print(USERDATA)
# if (USERDATA!=None):
#     Start()
import shelve
import sqlProcedure
from SqlConnection import create_db_connection
from tkinter import *
from tkinter import ttk
from tkinter import messagebox




with shelve.open('mydata') as db:
    stored_fetched_data = db.get('fetched_userdata')

# Now you can work with the stored data
if stored_fetched_data:
    print(stored_fetched_data)

upper_limit = "0"
lower_limit = 0
atrial_amp = 0
atrial_pulse = 0
ventricular_amp = 0
ventricular_pulse = 0
vrp = 0
arp = 0
detected = True
in_range = True
lost_due_to_noise = False
model_number = 0000000
revision_numer = 000000
serial_number = 000000
institution_name = ""

with shelve.open('mydata') as db:
    stored_fetched_data = db.get('fetched_userdata')


# Now you can work with the stored data
if stored_fetched_data:
    print("yes", stored_fetched_data)
else:
    print("No data fetched ")

loginID=int(stored_fetched_data[0])
STATEID=1 # Constant
home_window = Tk()
home_window.title("Pacemaker Project")
home_window.config(bg="#063326")

notebook = ttk.Notebook(home_window)
notebook.pack(pady=15)

tab1 = Frame(notebook, width=800, height=500)
tab2 = Frame(notebook, width=800, height=500)
tab3 = Frame(notebook, width=800, height=500)
tab4 = Frame(notebook, width=800, height=500)
tab5 = Frame(notebook, width=800, height=500)
tab7 = Frame(notebook, width=800, height=500)
tab6 = Frame(notebook, width=800, height=500)

tab1.pack(fill="both", expand=1)
tab2.pack(fill="both", expand=1)
tab3.pack(fill="both", expand=1)
tab4.pack(fill="both", expand=1)
tab5.pack(fill="both", expand=1)
tab7.pack(fill="both", expand=1)
tab6.pack(fill="both", expand=1)

notebook.add(tab1, text="Permanent State")
notebook.add(tab2, text="AOO")
notebook.add(tab3, text="VOO")
notebook.add(tab4, text="AAI")
notebook.add(tab5, text="VVI")
notebook.add(tab7, text="Egram Data")
notebook.add(tab6, text="About")
dcm_communication= True
new_pacemaker = True
Label(tab1, text="Welcome: "+str(stored_fetched_data[1])).pack(pady=10)
Label(tab1, text="Programmable Parameters").pack()
Label(tab1,text='Pacemaker Detected: ' + str(detected), font=("Arial",8)).place(x=20, y=285)
Label(tab1,text='DCM Communicating: ' + str(dcm_communication), font=("Arial",8)).place(x=180, y=285)
Label(tab1,text='New PACEMAKER Approached: ' + str(new_pacemaker), font=("Arial",8)).place(x=330, y=285)

Label(tab1, text='Upper Rate Limit ').place(x=100, y=60)
Label(tab1, text='Lower Rate Limit ').place(x=100, y=90)
Label(tab1, text='Atrial Amplitude ').place(x=100, y=120)
Label(tab1, text='Atrial Pulses Width ').place(x=100, y=150)
Label(tab1, text='Ventricular Amplitude ').place(x=300, y=60)
Label(tab1, text='Ventricular Pulse Width ').place(x=300, y=90)
Label(tab1, text='VRP ').place(x=300, y=120)
Label(tab1, text='ARP ').place(x=300, y=150)



def Set_to_PermanentState():

    AOO=sqlProcedure.get_AOO(loginID,STATEID)
    VVI = sqlProcedure.get_VVI(loginID, STATEID)
    AAI = sqlProcedure.get_AAI(loginID, STATEID)
    VOO = sqlProcedure.get_VOO(loginID, STATEID)

    print(AOO)
    print(VVI)
    print(AAI)
    print(VOO)
    if not AOO:
        messagebox.showinfo("Not Valid", "AOO is not a valid value")
    if not VVI:
        messagebox.showinfo("Not Valid", "VVI is not a valid value")
    if not AAI:
        messagebox.showinfo("Not Valid", "AAI is not a valid value")
    if not VOO:
        messagebox.showinfo("Not Valid", "VOO is not a valid value")


    if AOO and VVI and AAI and VOO:
        # All procedures returned valid data, so you can display their values
        print("AOO:", AOO)
        print("VVI:", VVI)
        print("AAI:", AAI)
        print("VOO:", VOO)




# button_activate_permanent_State = Button(tab1, text="Set Permanent State", command=Set_to_PermanentState)
#
# button_activate_permanent_State.pack()
# button_activate_permanent_State.place(x=200, y=200)

AOO=sqlProcedure.get_AOO(loginID,STATEID)


Label(tab2, text="Upper Limit Rate: ").place(x=0, y=17)

my_entry = Entry(tab2)
if AOO:  # Check if AOO is not empty
    my_entry.insert(0, float(AOO[0]))  # Set the value to the first element of AOO
my_entry.grid(row=0, column=2, pady=20, padx=200)

Label(tab2, text="Lower Limit Rate: ").place(x=0, y=77)
my_entry2 = Entry(tab2)
if AOO:  # Check if AOO is not empty
    my_entry2.insert(0, float(AOO[1]))
my_entry2.grid(row=1, column=2, pady=20, padx=100)

Label(tab2, text="Atrial Pulse Width: ").place(x=0, y=137)
my_entry3 = Entry(tab2)
if AOO:  # Check if AOO is not empty
    my_entry3.insert(0, float(AOO[2]))
my_entry3.grid(row=2, column=2, pady=20, padx=100)

Label(tab2, text="Atrial Amplitude: ").place(x=0, y=197)
my_entry4 = Entry(tab2)
if AOO:  # Check if AOO is not empty
    my_entry4.insert(0, float(AOO[3]))
my_entry4.grid(row=3, column=2, pady=20, padx=100)




def SubmitAAO():
    aao_submitted = Toplevel()
    aao_submitted.geometry("700x500")
    Label(aao_submitted, text='Upper Rate Limit: ' + str(my_entry.get())).place(x=10, y=60)
    Label(aao_submitted, text='Lower Rate Limit: ' + str(my_entry2.get())).place(x=10, y=90)
    Label(aao_submitted, text='Atrial Amplitude: ' + str(my_entry3.get())).place(x=10, y=120)
    Label(aao_submitted, text='Atrial Pulse Width: ' + str(my_entry4.get())).place(x=10, y=150)
    Label(aao_submitted, text='Ventricular Amplitude: x').place(x=185, y=60)
    Label(aao_submitted, text='Ventricular Pulse Width: x').place(x=185, y=90)
    Label(aao_submitted, text='VRP: x').place(x=185, y=120)
    Label(aao_submitted, text='ARP: x').place(x=185, y=150)
    AOO=sqlProcedure.get_AOO(loginID,STATEID)
    if not AOO:
        print("Set")
        sqlProcedure.set_AOO(STATEID,loginID,float(my_entry.get()),float(my_entry2.get()),float(my_entry3.get()),float(my_entry4.get()))
    else:
        print("Update")
        sqlProcedure.update_AOO(STATEID,loginID,float(my_entry.get()),float(my_entry2.get()),float(my_entry3.get()),float(my_entry4.get()))
    global current_state
    current_state = "AAO"
    Label(tab1, text='Current State: ' + str(current_state), font=("Arial", 8)).place(x=150, y=200)



Finalize_AAO = Button(tab2, text="Program", width=10, command=SubmitAAO).place(x=400, y=250)

VOO=sqlProcedure.get_VOO(loginID,STATEID)


Label(tab3, text="Upper Limit Rate: ").place(x=0, y=17)

my_entry5 = Entry(tab3)
if VOO:  # Check if AOO is not empty
    my_entry5.insert(0, float(VOO[0]))
my_entry5.grid(row=0, column=2, pady=20, padx=200)

Label(tab3, text="Lower Limit Rate: ").place(x=0, y=77)
my_entry6 = Entry(tab3)
if VOO:  # Check if AOO is not empty
    my_entry6.insert(0, float(VOO[1]))
my_entry6.grid(row=1, column=2, pady=20, padx=100)

Label(tab3, text="Ventricular Amplitude: ").place(x=0, y=137)
my_entry7 = Entry(tab3)
if VOO:  # Check if AOO is not empty
    my_entry7.insert(0, float(VOO[2]))
my_entry7.grid(row=2, column=2, pady=20, padx=100)

Label(tab3, text="Ventricular Pulse Width: ").place(x=0, y=197)
my_entry8 = Entry(tab3)
if VOO:  # Check if AOO is not empty
    my_entry8.insert(0, float(VOO[3]))
my_entry8.grid(row=3, column=2, pady=20, padx=100)


def SubmitVOO():
    voo_submitted = Toplevel()
    voo_submitted.geometry("700x500")
    Label(voo_submitted, text='Upper Rate Limit: ' + str(my_entry5.get())).place(x=10, y=60)
    Label(voo_submitted, text='Lower Rate Limit: ' + str(my_entry6.get())).place(x=10, y=90)
    Label(voo_submitted, text='Atrial Amplitude: x').place(x=10, y=120)
    Label(voo_submitted, text='Atrial Pulse Width: x').place(x=10, y=150)
    Label(voo_submitted, text='Ventricular Amplitude: ' + str(my_entry7.get())).place(x=185, y=60)
    Label(voo_submitted, text='Ventricular Pulse Width: ' + str(my_entry8.get())).place(x=185, y=90)
    Label(voo_submitted, text='VRP: x').place(x=185, y=120)
    Label(voo_submitted, text='ARP: x').place(x=185, y=150)
    VOO = sqlProcedure.get_VOO(loginID, STATEID)
    if not VOO:
        sqlProcedure.set_VOO(STATEID,loginID,float(my_entry5.get()),float(my_entry6.get()),float(my_entry7.get()),float(my_entry8.get()))
    else:
        sqlProcedure.update_VOO(STATEID,loginID,float(my_entry5.get()), float(my_entry6.get()), float(my_entry7.get()), float(my_entry8.get()))
    global current_state
    current_state = "VOO"
    Label(tab1, text='Current State: ' + str(current_state), font=("Arial", 8)).place(x=150, y=200)



Finalize_VOO = Button(tab3, text="Program", width=10, command=SubmitVOO).place(x=400, y=250)


AAI=sqlProcedure.get_AAI(loginID,STATEID)
Label(tab4, text="Upper Limit Rate: ").place(x=0, y=17)
my_entry9 = Entry(tab4)
if AAI:  # Check if AOO is not empty
    my_entry9.insert(0, float(AAI[0]))
my_entry9.grid(row=0, column=2, pady=20, padx=200)

Label(tab4, text="Lower Limit Rate: ").place(x=0, y=77)
my_entry10 = Entry(tab4)
if AAI:  # Check if AOO is not empty
    my_entry10.insert(0, float(AAI[1]))
my_entry10.grid(row=1, column=2, pady=20, padx=100)

Label(tab4, text="Atrial Amplitude: ").place(x=0, y=137)
my_entry11 = Entry(tab4)
if AAI:  # Check if AOO is not empty
    my_entry11.insert(0, float(AAI[2]))
my_entry11.grid(row=2, column=2, pady=20, padx=100)

Label(tab4, text="Atrial Pulse Width: ").place(x=0, y=197)
my_entry12 = Entry(tab4)
if AAI:  # Check if AOO is not empty
    my_entry12.insert(0, float(AAI[3]))
my_entry12.grid(row=3, column=2, pady=20, padx=100)

Label(tab4, text="ARP: ").place(x=0, y=257)
my_entry18 = Entry(tab4)
if AAI:  # Check if AOO is not empty
    my_entry18.insert(0, float(AAI[4]))
my_entry18.grid(row=4, column=2, pady=20, padx=100)


def SubmitAAI():
    aii_submitted = Toplevel()
    aii_submitted.geometry("700x500")
    Label(aii_submitted, text='Upper Rate Limit: ' + str(my_entry9.get())).place(x=10, y=60)
    Label(aii_submitted, text='Lower Rate Limit: ' + str(my_entry10.get())).place(x=10, y=90)
    Label(aii_submitted, text='Atrial Amplitude: ' + str(my_entry11.get())).place(x=10, y=120)
    Label(aii_submitted, text='Atrial Pulse Width: ' + str(my_entry12.get())).place(x=10, y=150)
    Label(aii_submitted, text='Ventricular Amplitude: x').place(x=185, y=60)
    Label(aii_submitted, text='Ventricular Pulse Width: x').place(x=185, y=90)
    Label(aii_submitted, text='VRP: x').place(x=185, y=120)
    Label(aii_submitted, text='ARP: ' + str(my_entry18.get())).place(x=185, y=150)
    # setting to database
    AAI=sqlProcedure.get_AAI(loginID,STATEID)
    if not AAI:
        sqlProcedure.set_AAI(STATEID,loginID,float(my_entry9.get()),float(my_entry10.get()),float(my_entry11.get()),my_entry12.get(),float(my_entry18.get()))
    else:
        sqlProcedure.update_AAI(STATEID,loginID,float(my_entry9.get()),float(my_entry10.get()),float(my_entry11.get()),my_entry12.get(),float(my_entry18.get()))
    current_state = "AAI"
    Label(tab1, text='Current State: ' + str(current_state), font=("Arial", 8)).place(x=150, y=200)


Finalize_AII = Button(tab4, text="Program", width=10, command=SubmitAAI).place(x=400, y=250)


VVI=sqlProcedure.get_VVI(loginID,STATEID)

Label(tab5, text="Upper Limit Rate: ").place(x=0, y=17)
my_entry13 = Entry(tab5)
if VVI:  # Check if AOO is not empty
    my_entry13.insert(0, float(VVI[0]))
my_entry13.grid(row=0, column=2, pady=20, padx=200)

Label(tab5, text="Lower Limit Rate: ").place(x=0, y=77)
my_entry14 = Entry(tab5)
if VVI:  # Check if AOO is not empty
    my_entry14.insert(0, float(VVI[1]))
my_entry14.grid(row=1, column=2, pady=20, padx=100)

Label(tab5, text="Ventricular Amplitude: ").place(x=0, y=137)
my_entry15 = Entry(tab5)
if VVI:  # Check if AOO is not empty
    my_entry15.insert(0, float(VVI[2]))
my_entry15.grid(row=2, column=2, pady=20, padx=100)

Label(tab5, text="Ventricular Pulse Width: ").place(x=0, y=197)
my_entry16 = Entry(tab5)
if VVI:  # Check if AOO is not empty
    my_entry16.insert(0, float(VVI[3]))
my_entry16.grid(row=3, column=2, pady=20, padx=100)

Label(tab5, text="VRP: ").place(x=0, y=257)
my_entry19 = Entry(tab5)
if VVI:  # Check if AOO is not empty
    my_entry19.insert(0, float(VVI[4]))
my_entry19.grid(row=4, column=2, pady=20, padx=100)


def SubmitVVI():
    vvi_submitted = Toplevel()
    vvi_submitted.geometry("700x500")
    Label(vvi_submitted, text='Upper Rate Limit: ' + str(my_entry13.get())).place(x=10, y=60)
    Label(vvi_submitted, text='Lower Rate Limit: ' + str(my_entry14.get())).place(x=10, y=90)
    Label(vvi_submitted, text='Atrial Amplitude: x').place(x=10, y=120)
    Label(vvi_submitted, text='Atrial Pulse Width: x').place(x=10, y=150)
    Label(vvi_submitted, text='Ventricular Amplitude: ' + str(my_entry15.get())).place(x=185, y=60)
    Label(vvi_submitted, text='Ventricular Pulse Width: ' + str(my_entry16.get())).place(x=185, y=90)
    Label(vvi_submitted, text='VRP: ' + str(my_entry19.get())).place(x=185, y=120)
    Label(vvi_submitted, text='ARP: x').place(x=185, y=150)
    VVI = sqlProcedure.get_VVI(loginID, STATEID)
    if not VVI:
        sqlProcedure.set_VVI(STATEID, loginID, float(my_entry13.get()), float(my_entry14.get()), float(my_entry15.get()),float(my_entry16.get()),float(my_entry19.get()))
    else:
        sqlProcedure.update_VVI(STATEID, loginID, float(my_entry13.get()), float(my_entry14.get()), float(my_entry15.get()),
                             float(my_entry16.get()), float(my_entry19.get()))
    current_state="VVI"
    Label(tab1, text='Current State: ' + str(current_state), font=("Arial", 8)).place(x=150, y=200)


Finalize_VII = Button(tab5, text="Program", width=10, command=SubmitVVI).place(x=400, y=250)

Label(tab6, text='Application Model Number: ' + str(model_number), width=50, height=5).pack()
Label(tab6, text='Application Software Revision Number: ' + str(revision_numer), width=50, height=5).pack()
Label(tab6, text='DCM Serial Number: ' + str(serial_number), width=50, height=5).pack()
Label(tab6, text='Institution Name: ' + institution_name, width=50, height=5).pack()



home_window.mainloop()
