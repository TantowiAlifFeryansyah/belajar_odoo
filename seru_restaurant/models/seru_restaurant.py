from odoo import api, fields, models
from odoo.exceptions import ValidationError, UserError


class SeruMenu(models.Model):
    _name = 'seru.menu'
    _rec_name = 'name'
    _description = 'Seru Menu'

    name = fields.Char()
    harga = fields.Float()

    state = fields.Selection(string="Status", selection=[
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('reject', 'Reject')
    ], default='draft', )

    image = fields.Binary(string="Image",  )
    attachment_ids = fields.Many2many(comodel_name="ir.attachment", string="Attachments", )
    # new_field_ids = fields.One2many(comodel_name="", inverse_name="", string="", required=False, )
    # new_field_id = fields.Many2one(comodel_name="", string="", required=False, )

    def action_confirm(self):
        self.state = 'confirm'
        return

class SeruRestaurant(models.Model):
    _name = 'seru.restaurant'
    _rec_name = 'name'
    _description = 'Seru Restaurant'

    name = fields.Char(required=True)
    alamat = fields.Text()
    no_handphone = fields.Char(readonly=True)
    no_induk = fields.Char()

    menu_ids = fields.One2many(comodel_name="restaurant.menu", inverse_name="restaurant_id", string="Menu", required=False, )

class RestaurantMenu(models.Model):
    _name = 'restaurant.menu'
    _description = 'Restaurant Menu'

    restaurant_id = fields.Many2one(comodel_name="seru.restaurant", string="Restaurant", required=False, )
    menu_id = fields.Many2one(comodel_name="seru.menu", string="Menu", required=False, )

    harga = fields.Float()
    harga_menu = fields.Float(related="menu_id.harga")

