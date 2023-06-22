# -*- encoding: utf-8 -*-
#########################################################################################
#
#    Copyright (C) 2019 Skyscend Business Solutions (https://www.skyscendbs.com)
#    Copyright (C) 2020 Skyscend Business Solutions  Pvt. Ltd.(<https://skyscendbs.com>)
#
#########################################################################################

from odoo import http, fields, tools
from odoo.http import request


class SkyWebsite(http.Controller):

    @http.route(['/'], type='http', auth="public", website=True)
    def sky_home_website(self, **kwargs):
        """
        This method will be used to display sky website
        -----------------------------------------------
        @param self: object pointer
        @param kwargs: dictionary containing fields and values
        """
        return request.render("sky_website.home_sky_website_template")

    @http.route(['/services'], type='http', auth="public", website=True)
    def sky_services(self, **kwargs):
        """
        This method will be used to display Services
        --------------------------------------------
        @param self: object pointer
        @param kwargs: dictionary containing fields and values
        """
        return request.render("sky_website.services_sky_website_template")

    @http.route(['/training'], type='http', auth="public", website=True)
    def sky_training(self, **kwargs):
        """
        This method will be used to display training page
        -------------------------------------------------
        @param self: object pointer
        @param kwargs: dictionary containing fields and values
        """
        return request.render("sky_website.training_sky_website_template")

    @http.route(['/training'], type='http', auth="public", website=True)
    def sky_training(self, **kwargs):
        """
        This method will be used to display training page
        -------------------------------------------------
        @param self: object pointer
        @param kwargs: dictionary containing fields and values
        """
        return request.render("sky_website.training_sky_website_template")

    @http.route(['/aboutus'], type='http', auth="public", website=True)
    def sky_about_us(self, **kwargs):
        """
        This method will be used to display Sky about us page
        -----------------------------------------------------
        @param self: object pointer
        @param kwargs: dictionary containing fields and values
        """
        return request.render("sky_website.sky_about_us_template")
