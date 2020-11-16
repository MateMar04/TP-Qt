from Inmueble import Inmueble


class Departamento(Inmueble):

    def __init__(self, id, direccion, codigo_postal, m2, nro_piso, nro_dpto, nro_ambientes, nro_dormitorios, nro_banios,
                 amueblado, habitado, precio_ars, precio_uds):

        super().__init__(id, direccion, codigo_postal, m2, nro_ambientes, nro_dormitorios, nro_banios, amueblado, habitado,
                         precio_ars, precio_uds, False)

        self.nro_piso = nro_piso
        self.nro_depto = nro_dpto

    def is_empty_f(self):
        return self.direccion == "" or self.codigo_postal == "" or self.m2 == "" or self.nro_piso == "" \
               or self.nro_depto == "" or self.nro_ambientes == "" or self.nro_dormitorios == "" or self.nro_banios == \
                "" or self.precio_ars == ""
