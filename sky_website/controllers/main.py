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
