# -*- coding: utf-8 -*-

from odoo import models, fields, api

import platform    # For getting the operating system name
import subprocess  # For executing a shell command

class ipaddress(models.Model):
    _name = 'net_manager.ipaddress'

    name = fields.Char(string="IP", unique=True)

    client_id = fields.Integer()

    cliente_name = fields.Char("Cliente", compute='_compute_cliente')

    color = fields.Integer(default=10, required=True)

    active = fields.Boolean(string="Active", compute='_compute_active')

    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         "Ya esta IP está registrada"),
    ]

    @api.one
    def _compute_cliente(self):
        cliente = self.env['res.users'].browse(self.client_id)

        self.cliente_name = cliente.name

    @api.one
    def _compute_active(self):
        self.active = self.ping(self.name)

    def ping(self, host):
        """
            Returns True if host (str) responds to a ping request.
            Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
        """

        # Option for the number of packets as a function of
        param = '-n' if platform.system().lower()=='windows' else '-c'

        # Building the command. Ex: "ping -c 1 google.com"
        command = ['ping', param, '1', host]

        return subprocess.call(command) == 0
