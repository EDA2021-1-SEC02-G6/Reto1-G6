"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Buscar los n videos con más views que son tendencia en un país para una categoria especifica")
    print("3- Video que más días ha sido trending en un país")
    print("0 - Salir")

def initCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

def PrimerVideo(catalog):

    video = lt.firstElement(catalog['videos'])
    print('Titulo: ' + str(video['title']))
    print('Canal: ' + str(video['channel_title']))
    print('Fecha de trending: ' + str(video['trending_date']))
    print('País: ' + str(video['country']))
    print('Vistas: ' + str(video['views']))
    print('likes: ' + str(video['likes']))
    print('dislikes: ' + str(video['dislikes']))

def categories(catalog):
    
    categorias = catalog['categories']
    for categoria in categorias:
        print(categoria)

def requerimiento1(lista):
    for video in lista:
        print('Fecha de trending: ' + str(video['trending_date']))
        print('Titulo: ' + str(video['title']))
        print('Canal: ' + str(video['channel_title']))
        print('Timepo publicado: ' + str(video['publish_time']))
        print('Vistas: ' + str(video['views']))
        print('likes: ' + str(video['likes']))
        print('dislikes: ' + str(video['dislikes']))

def requerimiento2(mejor):
    print('Titulo: ' + str(mejor['title']))
    print('Canal: ' + str(mejor['channel_title']))
    print('País: ' + str(mejor['country']))
    

    

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        print("Información del primer video: ")
        print("------------------------------")
        PrimerVideo(catalog)
        print("Categorias: ")
        categories(catalog)

    elif int(inputs[0]) == 2:
        categoria = input("Introduzca la categoria: ")
        pais = input("Introduzca el país: ")
        n = input("número de videos que quiere listar: ")
        categoria_id=controller.categorieid(categoria, catalog)
        lista= controller.requerimiento1(categoria_id, pais, n, catalog)
        requerimiento1(lista)
        

    elif int(inputs[0]) == 3:
        pais = input("Introduzca el país: ")
        mejor = controller.requerimiento2(catalog, pais)
        requerimiento2(mejor[0])
        print('Fecha de trending: ' + str(lista[1]))



    else:
        sys.exit(0)
sys.exit(0)
