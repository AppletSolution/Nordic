# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, tools, _, SUPERUSER_ID


class StockMove(models.Model):
    _inherit = "stock.move"

    area = fields.Float('Area',related='product_id.area', store=True)
    volume = fields.Float('Volume(CBM)', related='product_id.volume', store=True)



class StockQuant(models.Model):
    _inherit = "stock.quant"

    area = fields.Float('Area', related='product_id.area', store=True)
    volume = fields.Float('Volume(CBM)', related='product_id.volume', store=True)