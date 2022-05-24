# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, tools, _, SUPERUSER_ID


class ProductTemplate(models.Model):
    _inherit = "product.template"

    def _compute_area_uom_name(self):
        self.area_uom_name = self._get_area_uom_name_from_ir_config_parameter()

    @api.model
    def _get_area_uom_name_from_ir_config_parameter(self):
        return self._get_area_uom_id_from_ir_config_parameter().display_name

    @api.model
    def _get_area_uom_id_from_ir_config_parameter(self):
        """ Get the unit of measure to interpret the `volume` field. By default, we consider
        that volumes are expressed in cubic meters. Users can configure to express them in cubic feet
        by adding an ir.config_parameter record with "product.volume_in_cubic_feet" as key
        and "1" as value.
        """
        return self.env.ref('nordic_stock.product_uom_square_meter')

    def _set_area(self):
        for template in self:
            if len(template.product_variant_ids) == 1:
                template.product_variant_ids.area = template.area

    def _set_pallet(self):
        for template in self:
            if len(template.product_variant_ids) == 1:
                template.product_variant_ids.pallet = template.pallet

    pallet = fields.Float('Pallet', inverse='_set_pallet')
    area = fields.Float(
        'Area', compute='_compute_area', inverse='_set_area', digits='Area', store=True)
    area_uom_name = fields.Char(string='Area unit of measure label', compute='_compute_area_uom_name')


    @api.depends('product_variant_ids', 'product_variant_ids.area','product_variant_ids.pallet')
    def _compute_area(self):
        unique_variants = self.filtered(lambda template: len(template.product_variant_ids) == 1)
        for template in unique_variants:
            template.area = template.product_variant_ids.area
            template.pallet = template.product_variant_ids.pallet
        for template in (self - unique_variants):
            template.area = 0.0
            template.pallet = 0.0


class ProductProduct(models.Model):
    _inherit = "product.product"

    area = fields.Float('Area', digits='Area')
    pallet = fields.Float('Pallet')