# Catalytic converter removes 98% of the toxic emmisions from vehicle exhausts
# A typical passenger vehicle emits about 4.6 metric tons of carbon dioxide per year. This assumes the average gasoline vehicle on the road today has a fuel economy of
# about 22.0 miles per gallon and drives around 11,500 miles per year. Every gallon of gasoline burned creates about 8,887 grams of CO2
# A typical passenger vehicle emits about 4.6 metric tons of carbon dioxide per year. This assumes the average gasoline vehicle on the road today has a fuel economy
# of about 22.0 miles per gallon and drives around 11,500 miles per year. Every gallon of gasoline burned creates about 8,887 grams of CO2

import tkinter as tk
from tkinter import messagebox

window = tk.Tk()

_using_catalytic_converter = tk.IntVar()

window.geometry("500x400")
window.title("CO2 Car Emmisions Calculator")

tk.Label(text="MJIS Science - Calculating toxic gas emmisions from cars", fg = '#43476a').pack()
tk.Label(text="Extra Info - The average American travelled about 21,700 km in 2021", fg = '#43476a').pack()

input_text = tk.Frame(window)
input_text.pack(side = 'top')
check_box = tk.Frame(window)
check_box.pack(side = 'top')
start_button = tk.Frame(window)
start_button.pack(side = 'top')

L1 = tk.Label(input_text, text = "Distance Drove in KM")
L1.pack(side = 'left')
E1 = tk.Entry(input_text, bd = 5)
E1.pack(side = 'right')
C1 = tk.Checkbutton(check_box,text="Catalytic Converter?", variable = _using_catalytic_converter)
C1.pack(side = 'bottom')

def calculateCO2():
    try:
        distance_per_year = int(E1.get())
    except:
        messagebox.showinfo("Error!",f"Please insert a value in the distance travelled field.")
        return
    if _using_catalytic_converter.get() == 1:
        messagebox.showinfo("Result",f"{round(((distance_per_year / 35) * 8887) / 1000,1)} kg of CO2 emmisions per year are produced. The catalytic converter helped reduce 98% of the toxic gas emissions!\nThe catalytic converter converts a number of toxic gases, which include Nitrogen Oxides, Carbon Monoxide, and Hydrocarbon, into Nitrogen, Oxygen, Carbon Dioxide and water. \n Catalytic converters play a vital role in reducing the toxic gases that come out of exhaust and turns them into less harmful gases.")
    else:
        myValue = 100*(round(((distance_per_year / 35) * 8887) / 1000,1) / 2)
        messagebox.showinfo("Result",f"A catalytic converter is not used.\nTherefore, there are 98% more toxic gases being produced from your vehicle.\nA total of {myValue} kg of toxic gas emmissions has been produced from your vehicle.")
        
B1 = tk.Button(start_button, text = "Calculate!", command = calculateCO2)
B1.pack()
L2 = tk.Text(window,wrap='word')
L2.insert('insert',"Catalytic converters were first widely introduced in American production cars in 1975 due to EPA regulations on toxic emissions reductions. The United States Clean Air Act required a 75% decrease in emissions in all new model vehicles after 1975, a decrease to be carried out with the use of catalytic converters. Without catalytic converters, vehicles release hydrocarbons, carbon monoxide, and nitrogen oxide.")
L2.pack()

window.mainloop()
