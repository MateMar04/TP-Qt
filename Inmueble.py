class Inmueble:
    def __init__(self, id, direccion, codigo_postal, m2, nro_ambientes, nro_dormitorios,
                 nro_banios, amueblado, habitado, precio_ars, precio_uds, alquilado):
        self.id = id
        self.direccion = direccion
        self.codigo_postal = codigo_postal
        self.m2 = m2
        self.nro_ambientes = nro_ambientes
        self.nro_dormitorios = nro_dormitorios
        self.nro_banios = nro_banios
        self.amueblado = amueblado
        self.habitado = habitado
        self.precio_ars = precio_ars
        self.precio_uds = precio_uds
        self.alquilado = alquilado
