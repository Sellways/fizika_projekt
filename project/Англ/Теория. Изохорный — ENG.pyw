from tkinter import *
from tkinter import messagebox

a = "nothing"

root = Tk()
root.title("Theory. Isochoric process")
root.geometry("1300x300")

Task = Label(text = "Isochoric process")
Task.grid(row = 1, column = 0, sticky = "w")
Task1 = Label(text = "An isochore process is a process that occurs at a constant volume (V = const) and under the condition m = const and M = const.")
Task1.grid(row = 2, column = 0, sticky = "w")
Task2 = Label(text = "Under these conditions, the equation of state of an ideal gas for two temperature values T₀ and T follows: P₀V = m, PV = MRT, or P/P₀ = T/T₀")
Task2.grid(row = 3, column = 0, sticky = "w")
Task3 = Label(text = "For a gas of a given mass, the pressure-to-temperature ratio is constant if the volume of the gas does not change.")
Task3.grid(row = 4, column = 0, sticky = "w")
Task4 = Label(text = "When P₁/P₂ = T₁/T₂ (this equation is called Charles's law), it is applicable for the isochoric process: V = const.")
Task4.grid(row = 5, column = 0, sticky = "w")
Task5 = Label(text = "If V is the volume of gas at absolute temperature T, V₀ is the volume of gas at 0° C;")
Task5.grid(row = 6, column = 0, sticky = "w")
Task6 = Label(text = "coefficient a, equal to 1/273 K¯¹, called the temperature coefficient of the volume expansion of gases, the equation for the isochoric process can be written as P = P₀ × a × T.")
Task6.grid(row = 7, column = 0, sticky = "w")
Task7 = Label(text = "The curve of an isochore process is called an isochore.")
Task7.grid(row = 8, column = 0, sticky = "w")
Task8 = Label(text = "The isochore, represented in a rectangular coordinate system (P – V), on the ordinate axis of which the gas pressure is calculated, and on the abscissa axis - its volume, is a straight line parallel to the ordinate axis")
Task8.grid(row = 9, column = 0, sticky = "w")
Task9 = Label(text = "The isochore shown in a rectangular coordinate system (V – T) is a straight line parallel to the abscissa axis")
Task9.grid(row = 10, column = 0, sticky = "w")
Task10 = Label(text = "Isochore depicted in a rectangular coordinate system (P – T), the ordinate of which to calculate the gas pressure and x — axis is its absolute temperature is a straight line passing through the origin")
Task10.grid(row = 11, column = 0, sticky = "w")
Task11 = Label(text = "The dependence of gas pressure on temperature was experimentally investigated by the French physicist Jacques Charles in 1787")
Task11.grid(row = 12, column = 0, sticky = "w")
Task12 = Label(text = "The isochoric process can be carried out, for example, by heating the air at a constant volume.")
Task12.grid(row = 13, column = 0, sticky = "w")
Task13 = Label(text = "Source: https://studfiles.net/preview/5661952/page:3/")
Task13.grid(row = 14, column = 0, sticky = "w")
root.mainloop()