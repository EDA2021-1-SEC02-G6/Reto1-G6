"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    
    catalog = {'videos': None,
               'channels': None,
               'categories': None}

    catalog['videos'] = lt.newList()
    catalog['channels'] = lt.newList('ARRAY_LIST',
                                    cmpfunction=comparechannel)
    catalog['categories'] = lt.newList()
    
    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    # Se adiciona el video a la lista de videos
    lt.addLast(catalog['videos'], video)
    # Se obtienen los canales del video
    channels = video['channel_title']
    
    for channel in channels:
        addChannels(catalog, channel.strip(), video)

def addChannels(catalog, channelname, video):
    
    channels = catalog['channels']
    poschannel = lt.isPresent(channels, channelname)
    if poschannel > 0:
        channel = lt.getElement(channels, poschannel)
    else:
        channel = newChannel(channelname)
        lt.addLast(channels, channel)
    lt.addLast(channel['videos'], video)

def addCategories(catalog, categorie):
    
    c = newCategorie(categorie['name'], categorie['id'])
    lt.addLast(catalog['categories'], c)

# Funciones para creacion de datos

def newChannel(name):
   
    channel = {'name': "", "videos": None,  "average_rating": 0}
    channel['name'] = name
    channel['videos'] = lt.newList('ARRAY_LIST')
    return channel

def newCategorie(name, id):
    
    categorie = {'name': '', 'id': ''}
    categorie['name'] = name
    categorie['id'] = id
    return categorie

# Funciones de consulta

def requerimiento1(categoria, pais, n, catalog):
    lista = lt.newList('ARRAY_LIST')
    videos = catalog["videos"]
    for video in videos:
        if video["category_id"] == categoria:
            lt.addLast(lista, videos)
    lista2 = lt.newList('ARRAY_LIST')
    for video2 in lista:
        if video2["country"] == pais:
            lt.addLast(lista2, video2)
    
    ordenado=ordenarvistas(lista2
    final=lt.subList(ordenado, 0, n)
    return (final)

def requerimiento2(catalog, pais):
    lista = lt.newList('ARRAY_LIST')
    videos = catalog["videos"]
    for video in catalog["video"]:
        if video["country"] == pais:
            lt.addLast(lista, video)
    ordenada = ordenarfecha (lista)
    mejor = 0
    final = None
    i=0
    while i < lt.size(lista):
        sig = lista[i+1]
        actual = lista[i]
        time = sig["trending_date"] - actual["trending_date"]
        if time >= mejor:
            mejor = time
            final = lista[i]
        i = i+1
    devol = [final, mejor]
    return (devol)




    
    

# Funciones utilizadas para comparar elementos dentro de una lista

def comparechannel(channelname, channel):                  
    if (channelname.lower() in channel['name'].lower()):
        return 0
    return -1

# Funciones de ordenamiento

def ordenarvistas (videos):
ordenado = sa.sort(videos["views"], compareratings)
return (ordenado)

def ordenarfecha(videos):
    ordenado = sa.sort(videos["trending_date"], compareratings)
return (ordenado)

