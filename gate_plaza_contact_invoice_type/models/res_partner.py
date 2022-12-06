# -*- coding: utf-8 -*-

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    invoice_type = fields.Selection([
        ('regular', 'Regular'),('percent', 'Percentage')
        ])

    percentage = fields.Float('Percent %')

