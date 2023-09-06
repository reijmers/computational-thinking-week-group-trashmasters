import pandas as pd

a=['Mika Maria Isis Rosa Maja Damaris',
   'Emily Celia Carine Sabrina Maria Gur',
   'Elisa Sari Dave Dima Jesper Martyna',
    'Kelt Sebastian Quanpu Ruben Sofia Gabriella', 
    'Kian Sahir Tom Gonzalo Ameer Teun', 
    'Angelica Matas Caleb Angeline Raven Paulina', 
    'Martyna Maja Mate Vincent Eryk Emma', 
    'Hielke Liss Beatris Caio Sally Sanne', 
    'Atlas Elli Felix Diana Yash', 
    'Akanksha Charlie Andrey Max Hugo Al-fatihi', 
    'Misha Ioanna Ella Cristian Alicja Vanessa', 
    'Luca Rachna Jelle Karolina Yuyue Alexia']



def solution_station_5(name):
    ans=0
    for i in range(0, 12):
        if name in a[i]:
            ans=i
    return int(ans+1)
    

#function outputs the group number that the person is in


