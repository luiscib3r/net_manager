# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo.exceptions import ValidationError

class pago(models.Model):
    _name = 'net_manager.pago'

    cliente = fields.Many2one('res.users', string="Cliente", required=True, ondelete='restrict')

    servicio = fields.Many2one('net_manager.servicio', string="Servicio pagado", required=True, ondelete='restrict')

    company_currency = fields.Many2one('res.currency')

    fecha = fields.Date(string="Fecha de pago", required=True, default=fields.Date.today)

    is_this_week = fields.Integer(compute='_compute_is_this_week', string="Esta semana")

    estado = fields.Many2one('net_manager.estado', string="Estado", required=True, ondelete='restrict', track_visibility='onchange', index=True, default=0, group_expand='_read_group_stage_ids')

    color = fields.Integer(string="Color index")

    @api.one
    def pagar(self):
        if self.estado.id == 1:
            self.color = 10
            self.estado = 2
        else:
            self.color = 1
            self.estado = 1

    @api.one
    def _compute_is_this_week(self):
        this_day = fields.Date.today()
        this_day_n = this_day.weekday()
        lunes = this_day - this_day.resolution * this_day_n
        domingo = this_day + this_day.resolution * (6 - this_day_n)

        if (self.fecha >= lunes and self.fecha <= domingo):
            self.is_this_week = 1
        else:
            self.is_this_week = 0

    #This function is called when the scheduler goes off
    def process_pago_semana_queue(self, ids=None):
        servicios = self.env['net_manager.servicio'].search([('suscripcion', '=', 2)])
        clientes = self.env['res.users'].search([])

        for s in servicios:
            for c in clientes:
                if c._in_service(s.id):
                    self.create({
                        'cliente': c.id,
                        'servicio': s.id,
                        'estado': 1,
                        'color': 1
                    })

    def process_pago_mes_queue(self, ids=None):
        servicios = self.env['net_manager.servicio'].search([('suscripcion', '=', 1)])
        clientes = self.env['res.users'].search([])

        for s in servicios:
            for c in clientes:
                if c._in_service(s.id):
                    self.create({
                        'cliente': c.id,
                        'servicio': s.id,
                        'estado': 1,
                        'color': 1
                    })
        

    @api.model
    def _read_group_stage_ids(self,stages,domain,order):
        stage_ids = self.env['net_manager.estado'].search([])
        return stage_ids

    @api.one
    def _compute_is_this_week(self):
        this_day = fields.Date.today()
        this_day_n = this_day.weekday()
        lunes = this_day - this_day.resolution * this_day_n
        domingo = this_day + this_day.resolution * (6 - this_day_n)

        if (self.fecha >= lunes and self.fecha <= domingo):
            self.is_this_week = 1
        else:
            self.is_this_week = 0

    @api.model
    def create(self, vals):
        cliente = self.env['res.users'].browse(vals['cliente'])

        for R in cliente.servicios:
            if vals['servicio'] == R.id:
                record = super(pago, self).create(vals)
                return record

        raise ValidationError("El usuario no está subscrito al servicio pagado")
        record = False

    @api.one
    def write(self, vals):
        try:
            cliente = self.env['res.users'].browse(vals['cliente'])
        except Exception:
            cliente = self.cliente

        try:
            servicio = vals['servicio']
        except Exception:
            servicio = self.servicio.id

        for R in cliente.servicios:
            if servicio == R.id:
                record = super(pago, self).write(vals)
                return record

        raise ValidationError("El usuario no está subscrito al servicio pagado")
        record = False