from faker import Faker

class GeneradorDeNombres:
    def __init__(self, pais):
        self.pais = pais
    
    def generar_nombre_completo(self):
        fake = Faker(self.pais)

        nombre_aleatorio = fake.first_name()
        apellido_aleatorio = fake.last_name()

        correo_aleatorio = f"{nombre_aleatorio.lower()}.{apellido_aleatorio.lower()}"

        return f"{nombre_aleatorio} {apellido_aleatorio} ({correo_aleatorio})"


country = ["en_US", "es_MX", "pt_BR"]
generador = GeneradorDeNombres(country[2])
nombre_completo = generador.generar_nombre_completo()
print(nombre_completo)
