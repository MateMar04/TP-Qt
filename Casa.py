from Inmueble import Inmueble


class Casa(Inmueble):

    def __init__(self, id, direccion, codigo_postal, m2, cant_pisos, nro_ambientes, nro_dormitorios, nro_banios, amueblado,
                 habitado, precio_ars, precio_uds):

        super().__init__(id, direccion, codigo_postal, m2, nro_ambientes, nro_dormitorios, nro_banios, amueblado, habitado,
                         precio_ars, precio_uds, False)

        self.cant_pisos = cant_pisos

    def is_empty_h(self):
        return self.direccion == "" or self.codigo_postal == "" or self.m2 == "" or self.cant_pisos == "" or \
               self.nro_ambientes == "" or self.nro_dormitorios == "" or self.nro_banios == "" or self.precio_ars == \
               ""
