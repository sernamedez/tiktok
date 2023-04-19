from faker import Faker
import re
import random
import string


class GeneradorDeNombres:
    def __init__(self, pais):
        self.pais = pais
    
    def generar_nombre_completo(self):
        fake = Faker(self.pais)
        nombre_aleatorio = fake.first_name()
        apellido_aleatorio = fake.last_name()
        nombre = f"{nombre_aleatorio.lower()} {apellido_aleatorio.lower()}"
        return nombre

country = ["en_US", "es_MX", "pt_BR"]
generadornombrre = GeneradorDeNombres(country[2])
nombre_completo = generadornombrre.generar_nombre_completo()

def eliminar_caracteres_especiales(texto):
    patron = r'[^a-zA-Z0-9]'

    texto_limpio = re.sub(patron, ' ', texto)

    return texto_limpio

texto_limpio = eliminar_caracteres_especiales(nombre_completo)

def generar_apodo(nombre):
    prefijos = ['genial', 'amable', 'divertido', 'atrevido', 'valiente', 'loco', 'audaz', 'gracioso']
    sufijos = ['man', 'girl', 'boy', 'kid', 'champ', 'ace', 'hero', 'queen']
    palabras = nombre.lower().split()
    iniciales = [palabra[:2] for palabra in palabras]
    letras_aleatorias = ''.join(random.choices(string.ascii_lowercase, k=3))
    prefijo_aleatorio = random.choice(prefijos)
    sufijo_aleatorio = random.choice(sufijos)
    numero_aleatorio = random.randint(0, 100)
    apodo = f"{iniciales[0]}{iniciales[1]}{letras_aleatorias}{prefijo_aleatorio}{sufijo_aleatorio}{numero_aleatorio}"

    return apodo


def creatoremal():
    email_name = generar_apodo(texto_limpio)
    print(texto_limpio)
    return email_name


