from odoo import api, fields, models
from odoo.exceptions import ValidationError, UserError


class SeruMenu(models.Model):
    _name = 'seru.menu'
    _rec_name = 'name'
    _description = 'Seru Menu'

    name = fields.Char()
    harga = fields.Float()
