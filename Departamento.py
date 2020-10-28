class Departamento:

    def __init__(self, direccion, codigo_postal, m2, nro_piso, nro_dpto, nro_ambientes, nro_dormitorios, nro_banios, amueblado,
                 habitado, precio_ars, precio_uds):
        self.direccion = direccion
        self.codigo_postal = codigo_postal
        self.m2 = m2
        self.nro_piso = nro_piso
        self.nro_depto = nro_dpto
        self.nro_ambientes = nro_ambientes
        self.nro_dormitorios = nro_dormitorios
        self.nro_banios = nro_banios
        self.amueblado = amueblado
        self.habitado = habitado
        self.precio_ars = precio_ars
        self.precio_uds = precio_uds

    def is_empty_f(self):
        return self.direccion == "" or self.codigo_postal == "" or self.m2 == "" or self.nro_piso == "" \
               or self.nro_depto == "" or self.nro_ambientes == "" or self.nro_dormitorios == "" or self.nro_banios == \
                "" or self.precio_ars == ""
