import pprint
import json
import os
from  omdbapi.movie_search  import  GetMovie
from dotenv import load_dotenv

load_dotenv()

# Extrae la clave de la variable de entorno
key = os.getenv("MY_KEY")
# client secret, client public, token
# python dont env
#crear archivo env TOKEN = 'EOIHIURGNRU'
# git ignore contener .env

película = GetMovie(api_key = key)

#pprint.pprint(película.get_movie(title = 'Interestelar'))

laPeli = open('pelicula.JSON', 'wb')
peliculajson = json.dumps(película.get_movie(title = 'Matrix'), sort_keys=True, indent=4).encode('utf-8')
laPeli.write(peliculajson)

laPeli.close()