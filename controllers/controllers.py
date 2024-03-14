# -*- coding: utf-8 -*-
# from odoo import http


# class MemePet(http.Controller):
#     @http.route('/meme_pet/meme_pet', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/meme_pet/meme_pet/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('meme_pet.listing', {
#             'root': '/meme_pet/meme_pet',
#             'objects': http.request.env['meme_pet.meme_pet'].search([]),
#         })

#     @http.route('/meme_pet/meme_pet/objects/<model("meme_pet.meme_pet"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('meme_pet.object', {
#             'object': obj
#         })
