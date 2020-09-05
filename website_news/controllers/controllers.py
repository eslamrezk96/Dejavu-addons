# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class WebsiteNews(http.Controller):
    @http.route('/website_news/news/', auth="public", website=True)
    def news(self, **kw):
        news = request.env['news.news'].sudo().search([])
        return request.render('website_news.listing', {
            'news': news
        })
