# Copyright 2020 CorTex IT Solutions Ltd. (<https://cortexsolutions.net/>)
# License OPL-1

from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = "product.template"

    acquirer_ids = fields.Many2many('payment.acquirer', string='Payment Acquirer',
                                    domain="[('state', '!=', 'disabled')]")
