from odoo import models, fields, api

# Cliente
class MemePetCliente(models.Model):
    _name = 'meme_pet_cliente'
    _description = 'Cliente'

    name = fields.Char(string='Nombre')
    direccion = fields.Char(string='Dirección')
    email = fields.Char(string='Correo electrónico')
    telefono = fields.Char(string='Teléfono')
    compras_ids = fields.One2many('meme_pet_venta', 'cliente_venta', string='Compras')
    num_compras = fields.Integer(string='Número de compras', compute='_compute_num_compras')

    @api.depends('compras_ids')
    def _compute_num_compras(self):
        for cliente in self:
            cliente.num_compras = len(cliente.compras_ids)

# Especie
class MemePetEspecie(models.Model):
    _name = 'meme_pet_especie'
    _description = 'especie animal'

    name = fields.Char(string='Nombre')
   

# Dependiente
class MemePetDependiente(models.Model):
    _name = 'meme_pet_dependiente'
    _description = 'Dependiente'

    name = fields.Char(string='Nombre')
    email = fields.Char(string='Correo electrónico')
    telefono = fields.Char(string='Teléfono')
    salario = fields.Float(string='Salario')
    fecha_contratacion = fields.Date(string='Fecha de contratación')
    ventas_ids = fields.One2many('meme_pet_venta', 'dependiente_venta', string='Ventas realizadas')
    total_ventas = fields.Float(string='Total de ventas', compute='_compute_total_ventas')

    @api.depends('ventas_ids.total')
    def _compute_total_ventas(self):
        for dependiente in self:
            dependiente.total_ventas = sum(venta.total for venta in dependiente.ventas_ids)

# Animales
class MemePetAnimal(models.Model):
    _name = 'meme_pet_animal'
    _description = 'Animal'

    name = fields.Char(string='Nombre')
    especie = fields.Many2one('meme_pet_especie', string='Especie')
    raza = fields.Char(string='Raza')
    fecha_nacimiento = fields.Date(string='Fecha de nacimiento')
    genero = fields.Selection([('macho', 'Macho'), ('hembra', 'Hembra')], string='Género')
    ventas_ids = fields.One2many('meme_pet_venta', 'animal_venta', string='Ventas')
    imagen = fields.Binary(string="Imagen")

# Productos
class MemePetProducto(models.Model):
    _name = 'meme_pet_producto'
    _description = 'Producto'

    name = fields.Char(string='Nombre')
    categoria = fields.Char(string='Categoría')
    precio = fields.Float(string='Precio')
    descripcion = fields.Text(string='Descripción')
    cantidad_stock = fields.Integer(string='Cantidad en stock')
    imagen = fields.Binary(string="Imagen")
    en_stock = fields.Boolean(string='En stock', compute='_compute_en_stock', store=True)
    
    @api.constrains('precio')
    def _check_precio(self):
        for producto in self:
            if producto.precio <= 0:
                raise ValidationError("El precio debe ser mayor que cero.")
    @api.depends('cantidad_stock')
    def _compute_en_stock(self):
        for producto in self:
            producto.en_stock = producto.cantidad_stock > 0


# Ventas
class MemePetVenta(models.Model):
    _name = 'meme_pet_venta'
    _description = 'Venta'

    cliente_venta = fields.Many2one('meme_pet_cliente', string='Cliente')
    dependiente_venta = fields.Many2one('meme_pet_dependiente', string='Dependiente')
    animal_venta = fields.Many2one('meme_pet_animal', string='Animal')
    producto_venta = fields.Many2one('meme_pet_producto', string='Producto')
    fecha_venta = fields.Date(string='Fecha de venta')
    cantidad = fields.Integer(string='Cantidad')
    total = fields.Float(string='Total')

    @api.depends('cantidad', 'producto_venta.precio')
    def _compute_total(self):
        for venta in self:
            venta.total = venta.cantidad * venta.producto_venta.precio