# -*- coding: utf-8 -*-
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo import models, fields, api


class SelectStockMoveProducts(models.TransientModel):

    _name = 'select.stock.move.line.products'
    _description = 'Select Products'

    product_ids = fields.Many2many('product.product', string='Products')

    def select_move_line_products(self):
        order_id = self.env['stock.picking'].browse(self._context.get('active_id', False))
        for product in self.product_ids:
            self.env['stock.move.line'].create({
                'picking_id': order_id.id,
                'product_id': product.id,
                'product_uom_qty': 0,
                'company_id': order_id.company_id.id,
                'product_uom_id': product.uom_id.id,
                'location_id': order_id.location_id.id,
                'location_dest_id': order_id.location_dest_id.id,
            })
