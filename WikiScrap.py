# importo las librerias que quiero usar
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
#Indico la URL a la que voy a hacer la consulta

url='https://es.wikipedia.org/wiki/Provincias_de_Argentina'
#Hago la consulta
page = requests.get(url).text 
soup = BeautifulSoup(page, "lxml")

#Identifico la tabla y los elementos de donde quiero extraer los valores que necesito
tabla = soup.find('table',{'class':'wikitable sortable'})
links = tabla.findAll('a')

#Extraigo. Primero ingreso a la tabla, luego la recorro celda por celda

tabla_final=[]
provincia=""
habitantes=""
capital=""
nroFila=0
for fila in tabla.find_all("tr"):
    if nroFila>0:
        nroCelda=0
        for celda in fila.find_all('td'):
            if nroCelda==0:
                provincia=celda.text
                print("Provincia:", provincia)
            if nroCelda==3:
                habitantes=celda.text
                print("Habitantes:", habitantes)
            if nroCelda==6:
                capital=celda.text
                print("Capital:", capital)
                tabla_final.append((provincia,habitantes,capital))
            nroCelda=nroCelda+1
    nroFila=nroFila+1
    
#Opcion 1: Lo extraemos como csv para usarlo en lo que necesitemos
with open('WikiScrap.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    for provincia,habitantes,capital in tabla_final:
        writer.writerow([provincia, habitantes, capital])

# #Opcion 2: lo convertimos en un DataFrame para comenzar a trabajarlo
# import pandas as pd
# df = pd.DataFrame()
# df['Provincia', 'Habitantes'] = tabla_final

# #Tambien la podemos extraer como csv o xlsx
# df.to_csv("WikiScrap.csv")