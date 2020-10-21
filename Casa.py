class Casa:

    def __init__(self, direccion, codigo_postal, m2, cant_pisos, nro_ambientes, nro_dormitorios, nro_banios, amueblado,
                 habitado, precio_ars, precio_uds):
        self.direccion = direccion
        self.codigo_postal = codigo_postal
        self.m2 = m2
        self.cant_pisos = cant_pisos
        self.nro_ambientes = nro_ambientes
        self.nro_dormitorios = nro_dormitorios
        self.nro_banios = nro_banios
        self.amueblado = amueblado
        self.habitado = habitado
        self.precio_ars = precio_ars
        self.precio_uds = precio_uds

    def is_empty_h(self):
        return self.direccion == "" or self.codigo_postal == "" or self.m2 == "" or self.cant_pisos == "" or \
               self.nro_ambientes == "" or self.nro_dormitorios == "" or self.nro_banios == "" or self.precio_ars == \
               ".." or self.precio_uds == "."
