# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    transfer_account_id = fields.Many2one('account.account',
                                                     related='company_id.transfer_account_id',
                                                      readonly=False)