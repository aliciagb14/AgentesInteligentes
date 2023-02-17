import requests
from bs4 import BeautifulSoup as b

from lxml import html

import urllib
from urllib.request import Request, urlopen

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import re
from datetime import datetime
import calendar
"""Agente extractor de datos de artículos



Este agente se encarga de la extracción de datos de la revista
COMOSELLAME.

Para funcionar, el script requiere que estén instaladas las
bibliotecas `numpy` y `requests`.

Para más información acerca de buenas prácticas de documentación
de código el siguiente enlace es muy bueno:

    - https://realpython.com/documenting-python-code/

También, para una introducción rápida a Python con bastante cosas que
ya habéis visto y otras tantas nuevas, podéis visitar los siguientes
enlaces:

    - https://docs.python.org/3/tutorial/
    - https://try.codecademy.com/learn-python-3
    - https://realpython.com/python-first-steps/
"""

"""Desarrollar en el lenguaje de programación Python un agente de información que extraiga los siguientes datos de un número determinado de artículos:
Nombre de la publicación: El nombre de la publicación (no tiene por qué extraerse, ya que para cada grupo sólo se usa una única publicación.
Título del artículo: Cadena de texto sin caracteres extraños y sin espacios alrededor.
Fecha de publicación: Cadena de texto en en formato YYYYMMDD. Por ejemplo, el 10 de febrero de 2023 sería 20230210.
Abstract del artículo: Cadena de texto sin caracteres extraños y sin espacios alrededor.
Palabras clave: En el caso de que exista, lista de cadenas de texto sin caracteres extraños y sin espacios alrededor. Si no existe, una lista vacía."""

"""Extrae la información de ilos últimos n artículos hasta since
  
    :param n: El número de artículos de los que extraer datos. Debe
        ser un entero mayor que 0.
    :param since: La fecha desde cuándo sacar la información. Debe
        ser un objeto date. si no se especifica, se presupone la
        fecha del día en el que se ejecuta la función
    :return: Una lista de tuplas donde cada tupla tendrá la
        siguiente forma: (str, str, str, str, List[str])
    """
def extract(n, since=None):

    #User-Agent: python-requests/2.28.2
    
    html = requests.get('https://www.nowpublishers.com/MAL')
    content = html.text         #obtener el texto de la respuesta
    soup = b(content, 'lxml')   #manipular la info en el formato html
   
    results = soup.find('div', {'class': 'row flex-column'})
   # results.get_text()
   # elements = results.find_all('div', class_='panel panel-default')
    elements = results.find_all('div', class_='panel panel-default')
    for element in elements:
        title = element.find('h4', class_='panel-title').text
        nameVolume = re.findall('href="/article/Details/MAL-\d{3}', str(element))
        # nameVolume = element.find('div',{'class':'search-result'})
        for h2 in element.find_all('h2'):
            for a in h2.find_all('a', href=True):
                tituloArt = a.text
                print('\t' + title.strip() + ": " + tituloArt.strip())

                enlace = requests.get('https://www.nowpublishers.com' + a['href'])
                contentEnlace = enlace.text 
                soup2 = b(contentEnlace, 'lxml')
                divArt = soup2.find('div', {'class': 'article-details'})
                patron_fecha = ('[a-zA-Z]*\s[a-zA-Z]*:\s[0-9]+\s[a-zA-Z]*\s[0-9]+')
                fecha_matches = re.findall(patron_fecha, str(divArt))
                for fecha_match in fecha_matches:
                    fecha = fecha_match
                    fecha_fin = re.sub("Publication Date:", "", fecha)
                    objdate= datetime.strptime(fecha_fin, ' %d %b %Y')
                    print('\t\t' + objdate.strftime('%Y%m%d'))
    str_final = tituloArt + ','
    result = [str_final]
    return result


if __name__ == '__main__':
    for row in extract(n=20):
        print(row)
