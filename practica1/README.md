En esta primera práctica vamos a desarrollar un agente para extraer datos de información relacionada con revistas científicas del área de la inteligencia artificial. Tendrá que ser capaz de sacar el máximo número de información pública de los artículos que se publican en dichas revistas.  

Las webs de estas revistas están compuestas de maneras muy diferentes, por lo que cada grupo tendrá que ingeniárselas para intentar descubrir cómo extrar como mínimo los datos que se piden.

Objetivos
    Desarrollar en el lenguaje de programación Python un agente de información que extraiga los siguientes datos de un número determinado de artículos:  
      
      
   -Nombre de la publicación: El nombre de la publicación (no tiene por qué extraerse, ya que para cada grupo sólo se usa una única publicación.  
        
   -Título del artículo: Cadena de texto sin caracteres extraños y sin espacios alrededor.  
        
   -Fecha de publicación: Cadena de texto en en formato YYYYMMDD. Por ejemplo, el 10 de febrero de 2023 sería 20230210.  
        
   -Abstract del artículo: Cadena de texto sin caracteres extraños y sin espacios alrededor.  
        
   -Palabras clave: En el caso de que exista, lista de cadenas de texto sin caracteres extraños y sin espacios alrededor. Si no existe, una lista vacía.   
        
        

    De la extracción se tendrá que ocupar una única función con el siguiente contrato:
        def extract(n, since=None):
            """Extrae la información de ilos últimos n artículos hasta since
        
            :param n: El número de artículos de los que extraer datos. Debe
                ser un entero mayor que 0.
            :param since: La fecha desde cuándo sacar la información. Debe
                ser un objeto datetime. si no se especifica, se presupone la
                fecha del día en el que se ejecuta la función
            :return: Una lista de tuplas donde cada tupla tendrá la
                siguiente forma: (str, str, str, str, List[str])
    Tódo el código necesario además de la anterior función deberá estar contenido dentro de un único fichero con el nombre nombre-de-equipo-en-kebab-case.py.
