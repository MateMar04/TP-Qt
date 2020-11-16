import pickle


class BaseDeDatos:
    def __init__(self, archivo):
        self.archivo = archivo
        self.listeners = []

    def add_listener(self, listener):
        self.listeners.append(listener)

    def save(self, inmuebles):
        with open(self.archivo, "wb") as file:
            pickle.dump(inmuebles, file)
        for listener in self.listeners:
            listener(inmuebles)

    def read(self):
        try:
            with open(self.archivo, "rb") as file:
                propiedades = pickle.load(file)
        except FileNotFoundError:
            propiedades = []
        return propiedades

    def add(self, inmueble):
        inmuebles = self.read()
        inmuebles.append(inmueble)
        self.save(inmuebles)

    def next_id(self):
        mayor = 0
        for inmuelble in self.read():
            cid = int(inmuelble.id)
            if cid > mayor:
                mayor = cid
        return str(mayor + 1)

    def delete(self, ids):
        result = []
        for inmuelble in self.read():
            if not inmuelble.id in ids:
                result.append(inmuelble)
        self.save(result)

    def alquilar(self, ids):
        self.set_alquilado(ids, True)

    def terminar_contrato(self, ids):
        self.set_alquilado(ids, False)

    def set_alquilado(self, ids, alquilado):
        inmuebles = self.read()
        for inmuelble in inmuebles:
            if inmuelble.id in ids:
                inmuelble.alquilado = alquilado
        self.save(inmuebles)


