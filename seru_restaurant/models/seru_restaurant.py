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

    def action_confirm(self):
        self.state = 'confirm'
        return

class SeruRestaurant(models.Model):
    _name = 'seru.restaurant'
    _rec_name = 'name'
    _description = 'Seru Restaurant'

    name = fields.Char()
    alamat = fields.Text()
