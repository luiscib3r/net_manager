# -*- coding: utf-8 -*-

from odoo import models, fields, api

class cliente(models.Model):
    _inherit = 'res.users'

    name = fields.Char(string="Nombre", required=True)

    ip = fields.One2many('net_manager.ipaddress', 'client_id', string="IP", required=True, ondelete='restrict')

    servicios = fields.Many2many('net_manager.servicio', string="Servicios", ondelete='restrict')

    email = fields.Char(compute='_compute_email', default='user@soft4cuba.com')

    login = fields.Char(required=True, help="Used to log into the system", onchange='_login_change')

    @api.depends('email', 'login')
    def _login_change(self):
        self.email = self.login + '@soft4cuba.com'
    
    @api.one
    def _compute_email(self):
        self.email = self.login + '@soft4cuba.com'

    def _in_service(self, serv_id):
        for s in self.servicios:
            if serv_id == s.id:
                return True
        
        return False