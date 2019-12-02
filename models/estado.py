# -*- coding: utf-8 -*-

from odoo import models, fields, api

class estado(models.Model):
    _name = 'net_manager.estado'

    name = fields.Char('Nombre Estado', required=True)
    sequence = fields.Integer('Secuencia', default=10)

    fold = fields.Boolean()
