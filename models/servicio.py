# -*- coding: utf-8 -*-

from odoo import models, fields, api

dict_suscripcion = ['', 'Mensual', 'Semanal']

class servicio(models.Model):
    _name = 'net_manager.servicio'

    name = fields.Char(string="Servicio", compute='_compute_name')

    company_currency = fields.Many2one('res.currency')

    nombre = fields.Char(string="Nombre", required=True)

    precio = fields.Monetary(string="Precio", required=True, currency_field='company_currency')

    suscripcion = fields.Selection(selection=[(1, 'Mensual'), (2, 'Semanal')], required=True, string="Tipo de suscripción")

    @api.one
    def _compute_name(self):
        self.name = self.nombre + ' - $ ' + str(self.precio) + ' ' + dict_suscripcion[self.suscripcion]