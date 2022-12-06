# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    customer_amount = fields.Float('Customer Amount')
    partner_percent = fields.Float(string='Customer Percentage %')

    @api.onchange('customer_amount')
    def oncahnge_customer_amount(self):
        self.price_unit = (self.customer_amount * self.partner_percent) / 100


class AccountMove(models.Model):
    _inherit = 'account.move'

    partner_percent = fields.Float(string='Customer Percentage %', compute='_compute_partner_percent')
    partner_invoicing_check = fields.Boolean(compute='_compute_partner_percent')


    @api.depends('partner_id')
    def _compute_partner_percent(self):
        self.partner_percent = 0
        self.partner_invoicing_check = False

        if self.partner_id.invoice_type == 'percent' and self.state != 'posted':
            self.partner_invoicing_check = True
            self.partner_percent = self.partner_id.percentage

            for line in self.line_ids:
                line.partner_percent = self.partner_percent
                line.price_unit = (line.customer_amount * line.partner_percent) / 100

