# -*- coding: utf-8 -*-
from odoo import http

# class NetManager(http.Controller):
#     @http.route('/net_manager/net_manager/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/net_manager/net_manager/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('net_manager.listing', {
#             'root': '/net_manager/net_manager',
#             'objects': http.request.env['net_manager.net_manager'].search([]),
#         })

#     @http.route('/net_manager/net_manager/objects/<model("net_manager.net_manager"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('net_manager.object', {
#             'object': obj
#         })