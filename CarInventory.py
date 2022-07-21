''' Inventory application for used car lot. Keeps track of inventory and allows the user to search for a certain car type.
    Authors: Dylan, Lukas, Tran, Jonathan
    Last edited: 7/9/22
'''

import random
import pandas as pd
import pandastable as pt
import tkinter as tk

carList = []

'''||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||'''
# used car class
class UsedCar:
    def __init__(self, id=None, make=None, model=None, color=None, year=None):
        self.id = id
        self.make = make
        self.model = model
        self.color = color
        self.year = year

    # print out a cars attributes
    def __str__(self):
        return f'Car Info: {self.make} {self.model} {self.color} {self.year}'

    # save to file
    def save_to_file(self):
        car_info = [self.id, self.make, self.model, self.color, self.year]
        used_car_file = open('UsedCar.txt', 'a')
        for i in car_info:
            used_car_file.write("%s," % i)    # MODIFIED HERE, I want commas instead of tab space
        used_car_file.write("\n")
        used_car_file.close()
        print("Successfully add to the inventory.")

'''|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||'''
# Inventory/computer class  
class Inventory():  # MODIFIED HERE, if we want old method, just attribute and value, I can align
    def __init__(self, make_s, model_s, color_s, year_s):
        self.make_s = make_s
        self.model_s = model_s
        self.color_s = color_s
        self.year_s = year_s

    def search(self):
        df = pd.read_csv("UsedCar.txt", names=["ID", "Make", "Model", "Color", "Year"], index_col=False)
        if self.make_s is None or len(self.make_s) == 0:
            make_list = df
        else:
            make_list = df[df["Make"] == self.make_s.lower()]  # Sort dataframe by Make column

        if self.model_s is None or len(self.model_s) == 0:
            model_list = make_list
        else:
            model_list = make_list[make_list["Model"] == self.model_s.lower()]

        if self.color_s is None or len(self.color_s) == 0:
            color_list = model_list
        else:
            color_list = model_list[model_list["Color"] == self.color_s.lower()]

        if self.year_s is None or len(self.year_s) == 0:
            year_list = color_list
        else:
            year_list = color_list[color_list["Year"] == int(self.year_s)]
        return year_list

'''|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||'''
#customer class
class Customer():
    def __init__(self, name, downPayment, price, numMonths):
        self.name = name
        self.downPayment = downPayment
        self.price = price
        self.numMonths = numMonths

    def showPayments(self):
        afterMoneyDown = self.price - self.downPayment
        monthlyTotal = afterMoneyDown / self.numMonths
        print('$' + '%.2f'% float(monthlyTotal), 'per month for ' + str(self.numMonths), 'months')

'''||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||'''
#function to input car with user input
def inputCar():
    newId = random.randint(1, 50)
    newMake = input('Enter make: ')
    newModel = input('Enter model: ')
    newColor = input('Enter Color: ')
    newYear = input('Enter year: ')

    newCar = UsedCar(newId, newMake, newModel, newColor, newYear)
    newCar.save_to_file()

#function to read in from text file
def readIn():
    stuff = ''
    f = open('UsedCar.txt', 'rt')
    while True:
        line = f.readline()
        if not line:
            break
        stuff += line
    f.close()
    stuffList = list(stuff.split('\n'))
    stuffList.pop()
    for item in stuffList:
        keys = ['id', 'make', 'model', 'color', 'year']
        values = list(item.split('\t'))
        values.pop()
        carDict = {keys[i]: values[i] for i in range(len(keys))}
        carList.append(carDict)

# inputCar()

# s = Inventory()
# s.singleSearch()