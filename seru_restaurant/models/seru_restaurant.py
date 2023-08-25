from odoo import api, fields, models
from odoo.exceptions import ValidationError, UserError


class SeruMenu(models.Model):
    _name = 'seru.menu'
    _rec_name = 'name'
    _description = 'Seru Menu'

    name = fields.Char()
    harga = fields.Float()
    no_menu = fields.Char()

    state = fields.Selection(string="Status", selection=[
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('reject', 'Reject')
    ], default='draft', )

    image = fields.Binary(string="Image",  )
    attachment_ids = fields.Many2many(comodel_name="ir.attachment", string="Attachments", )
    # new_field_ids = fields.One2many(comodel_name="", inverse_name="", string="", required=False, )
    # new_field_id = fields.Many2one(comodel_name="", string="", required=False, )

    @api.model
    def create(self, values):
        values['no_menu'] = self.env.ref('seru_restaurant.seq_restaurant_menu').next_by_id()
        res = super(SeruMenu, self).create(values)
        return res

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

    @api.model
    def create(self, values):
        values['no_induk'] = self.env.ref('seru_restaurant.seq_seru_restaurant').next_by_id()
        return super(SeruRestaurant, self).create(values)

class RestaurantMenu(models.Model):
    _name = 'restaurant.menu'
    _description = 'Restaurant Menu'

    restaurant_id = fields.Many2one(comodel_name="seru.restaurant", string="Restaurant", required=False, )
    menu_id = fields.Many2one(comodel_name="seru.menu", string="Menu", required=False, )

    harga = fields.Float()
    harga_menu = fields.Float(related="menu_id.harga")
    diskon = fields.Float()
    netto = fields.Float(compute='compute_netto')
    voucher = fields.Float()
    setelah_voucher = fields.Float(compute='compute_voucher',store=True)

    @api.onchange('harga', 'diskon')
    def compute_netto(self):
        for me in self:
            #import ipdb;ipdb.set_trace()
            me.netto = me.harga-(me.diskon*me.harga/100)
        return

    @api.onchange('harga', 'voucher')
    def compute_voucher(self):
        for me in self:
            me.setelah_voucher = me.harga-me.voucher



