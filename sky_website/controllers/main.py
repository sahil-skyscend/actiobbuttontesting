# -*- encoding: utf-8 -*-
#########################################################################################
#
#    Copyright (C) 2019 Skyscend Business Solutions (https://www.skyscendbs.com)
#    Copyright (C) 2020 Skyscend Business Solutions  Pvt. Ltd.(<https://skyscendbs.com>)
#
#########################################################################################

from odoo import http
from odoo.http import request

print("Testing Action Button")
print("Testing Action Button")


class SkyWebsite(http.Controller):
    @http.route(["/"], type="http", auth="public", website=True)
    def sky_home_website(self, **kwargs):
        """
        This method will be used to display sky website
        -----------------------------------------------
        @param self: object pointer
        @param kwargs: dictionary containing fields and values
        """
        return request.render("sky_website.home_sky_website_template")
