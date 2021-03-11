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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de videos

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadVideos(catalog)
    loadCategories(catalog)

def loadVideos(catalog):
    
    videosfile = cf.data_dir + 'videos-small.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)

def loadCategories(catalog):
    """
    Esta función no carga correctamente los datos de las
    categorias :'(

    el resto de funciones del documento no están basadas en como
    se enceuntran cargadas las categorias si no en coom deberían estar cargadas 
    si fuera correcta la función   

    """
   
    categoriesfile = cf.data_dir + 'category-id.csv'
    input_file = csv.DictReader(open(categoriesfile, encoding='utf-8'))
    for categorie in input_file:
        model.addCategories(catalog, categorie)
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def categorieid(categoria, catalog):
    categories = catalog["categories"]
    for categorie in categories:
        if categorie['name'].lower() == categoria.lower():
            id = categorie['id']
            
    return id

def requerimiento1(categoria, pais, n, catalog):
    model.requerimiento1(categoria, pais, n, catalog)

def requerimiento2(catalog, pais):
    model.requerimiento2(catalog, pais)
