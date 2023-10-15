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
from tkinter import *
from tkinter import ttk

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
tab6 = Frame(notebook, width=800, height=500)

tab1.pack(fill="both", expand=1)
tab2.pack(fill="both", expand=1)
tab3.pack(fill="both", expand=1)
tab4.pack(fill="both", expand=1)
tab5.pack(fill="both", expand=1)
tab6.pack(fill="both", expand=1)

notebook.add(tab1, text="Home")
notebook.add(tab2, text="AOO")
notebook.add(tab3, text="VOO")
notebook.add(tab4, text="AAI")
notebook.add(tab5, text="VVI")
notebook.add(tab6, text="About")

Label(tab1, text="Welcome "+ str(stored_fetched_data[1])).pack(pady=10)
Label(tab1, text="Programmable Parameters").pack()
Label(tab1, text='Pacemaker Detected: ' + str(detected)).place(x=30, y=285)
Label(tab1, text='\nIn Range: ' + str(in_range)).place(x=220, y=270)
Label(tab1, text='\nLost Due to Noise: ' + str(lost_due_to_noise)).place(x=350, y=270)

Label(tab1, text='Upper Rate Limit ').place(x=100, y=60)
Label(tab1, text='Lower Rate Limit ').place(x=100, y=90)
Label(tab1, text='Atrial Amplitude ').place(x=100, y=120)
Label(tab1, text='Atrial Pulses Width ').place(x=100, y=150)
Label(tab1, text='Ventricular Amplitude ').place(x=300, y=60)
Label(tab1, text='Ventricular Pulse Width ').place(x=300, y=90)
Label(tab1, text='VRP ').place(x=300, y=120)
Label(tab1, text='ARP ').place(x=300, y=150)

Label(tab2, text="Upper Limit Rate: ").place(x=0, y=17)
my_entry = Entry(tab2)
my_entry.grid(row=0, column=2, pady=20, padx=200)

Label(tab2, text="Lower Limit Rate: ").place(x=0, y=77)
my_entry2 = Entry(tab2)
my_entry2.grid(row=1, column=2, pady=20, padx=100)

Label(tab2, text="Atrial Pulse Width: ").place(x=0, y=137)
my_entry3 = Entry(tab2)
my_entry3.grid(row=2, column=2, pady=20, padx=100)

Label(tab2, text="Atrial Amplitude: ").place(x=0, y=197)
my_entry4 = Entry(tab2)
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


Finalize_AAO = Button(tab2, text="Program", width=10, command=SubmitAAO).place(x=35, y=250)

Label(tab3, text="Upper Limit Rate: ").place(x=0, y=17)
my_entry5 = Entry(tab3)
my_entry5.grid(row=0, column=2, pady=20, padx=200)

Label(tab3, text="Lower Limit Rate: ").place(x=0, y=77)
my_entry6 = Entry(tab3)
my_entry6.grid(row=1, column=2, pady=20, padx=100)

Label(tab3, text="Ventricular Amplitude: ").place(x=0, y=137)
my_entry7 = Entry(tab3)
my_entry7.grid(row=2, column=2, pady=20, padx=100)

Label(tab3, text="Ventricular Pulse Width: ").place(x=0, y=197)
my_entry8 = Entry(tab3)
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


Finalize_VOO = Button(tab3, text="Program", width=10, command=SubmitVOO).place(x=35, y=250)

Label(tab4, text="Upper Limit Rate: ").place(x=0, y=17)
my_entry9 = Entry(tab4)
my_entry9.grid(row=0, column=2, pady=20, padx=200)

Label(tab4, text="Lower Limit Rate: ").place(x=0, y=77)
my_entry10 = Entry(tab4)
my_entry10.grid(row=1, column=2, pady=20, padx=100)

Label(tab4, text="Atrial Amplitude: ").place(x=0, y=137)
my_entry11 = Entry(tab4)
my_entry11.grid(row=2, column=2, pady=20, padx=100)

Label(tab4, text="Atrial Pulse Width: ").place(x=0, y=197)
my_entry12 = Entry(tab4)
my_entry12.grid(row=3, column=2, pady=20, padx=100)


def SubmitAII():
    aii_submitted = Toplevel()
    aii_submitted.geometry("700x500")
    Label(aii_submitted, text='Upper Rate Limit: ' + str(my_entry9.get())).place(x=10, y=60)
    Label(aii_submitted, text='Lower Rate Limit: ' + str(my_entry10.get())).place(x=10, y=90)
    Label(aii_submitted, text='Atrial Amplitude: ' + str(my_entry11.get())).place(x=10, y=120)
    Label(aii_submitted, text='Atrial Pulse Width: ' + str(my_entry12.get())).place(x=10, y=150)
    Label(aii_submitted, text='Ventricular Amplitude: x').place(x=185, y=60)
    Label(aii_submitted, text='Ventricular Pulse Width: x').place(x=185, y=90)
    Label(aii_submitted, text='VRP: x').place(x=185, y=120)
    Label(aii_submitted, text='ARP: x').place(x=185, y=150)


Finalize_AII = Button(tab4, text="Program", width=10, command=SubmitAII).place(x=35, y=250)

Label(tab5, text="Upper Limit Rate: ").place(x=0, y=17)
my_entry13 = Entry(tab5)
my_entry13.grid(row=0, column=2, pady=20, padx=200)

Label(tab5, text="Lower Limit Rate: ").place(x=0, y=77)
my_entry14 = Entry(tab5)
my_entry14.grid(row=1, column=2, pady=20, padx=100)

Label(tab5, text="Ventricular Amplitude: ").place(x=0, y=137)
my_entry15 = Entry(tab5)
my_entry15.grid(row=2, column=2, pady=20, padx=100)

Label(tab5, text="Ventricular Pulse Width: ").place(x=0, y=197)
my_entry16 = Entry(tab5)
my_entry16.grid(row=3, column=2, pady=20, padx=100)


def SubmitVOO():
    voo_submitted = Toplevel()
    voo_submitted.geometry("700x500")
    Label(voo_submitted, text='Upper Rate Limit: ' + str(my_entry13.get())).place(x=10, y=60)
    Label(voo_submitted, text='Lower Rate Limit: ' + str(my_entry14.get())).place(x=10, y=90)
    Label(voo_submitted, text='Atrial Amplitude: x').place(x=10, y=120)
    Label(voo_submitted, text='Atrial Pulse Width: x').place(x=10, y=150)
    Label(voo_submitted, text='Ventricular Amplitude: ' + str(my_entry15.get())).place(x=185, y=60)
    Label(voo_submitted, text='Ventricular Pulse Width: ' + str(my_entry16.get())).place(x=185, y=90)
    Label(voo_submitted, text='VRP: x').place(x=185, y=120)
    Label(voo_submitted, text='ARP: x').place(x=185, y=150)


Finalize_VOO = Button(tab5, text="Program", width=10, command=SubmitVOO).place(x=35, y=250)

Label(tab6, text='Application Model Number: ' + str(model_number), width=50, height=5).pack()
Label(tab6, text='Application Software Revision Number: ' + str(revision_numer), width=50, height=5).pack()
Label(tab6, text='DCM Serial Number: ' + str(serial_number), width=50, height=5).pack()
Label(tab6, text='Institution Name: ' + institution_name, width=50, height=5).pack()

home_window.mainloop()