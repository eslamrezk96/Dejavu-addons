# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BlogPost(models.Model):
    _inherit = 'blog.post'
    # _inherit = ['image.mixin']

    description = fields.Html(default='Add Post')
    content = fields.Html(related='description')
    image = fields.Binary(string="Cover Photo")
    cover_properties = fields.Text('Cover Properties', compute='compute_method')

    @api.depends('image')
    def compute_method(self):
        for rec in self:
            if rec.image:
                post_id = rec._origin.id
                rec.cover_properties = """{
                                         "background-image": "url('/website/image/blog.post/%d/image')", 
                                         "resize_class": "o_record_has_cover cover_mid",
                                         "text_size_class": "o_record_cover_font_big",
                                         "text_align_class": "text-center",
                                         "background-color": "oe_black",
                                         "opacity": "0.2"
                                         }""" % post_id
            else:
                rec.cover_properties = """{"background-image": "none", "background-color": "oe_black", "opacity": 
                                            "0.2", "resize_class": "cover_mid"} """


class BlogBlog(models.Model):
    _inherit = 'blog.blog'
    # _inherit = ['image.mixin']

    cover_blog = fields.Binary(string="Cover Blog")
    cover_properties = fields.Text('Cover Properties', compute='compute_method')

    @api.depends('cover_blog')
    def compute_method(self):
        for rec in self:
            if rec.cover_blog:
                post_id = rec._origin.id
                rec.cover_properties = """{
                                         "background-image": "url('/website/image/blog.blog/%d/cover_blog')", 
                                         "resize_class": "o_record_has_cover cover_mid",
                                         "text_size_class": "o_record_cover_font_big",
                                         "text_align_class": "text-center",
                                         "background-color": "oe_black",
                                         "opacity": "0.2"
                                         }""" % post_id
            else:
                rec.cover_properties = """{"background-image": "none", "background-color": "oe_black", "opacity": 
                                            "0.2", "resize_class": "cover_mid"} """