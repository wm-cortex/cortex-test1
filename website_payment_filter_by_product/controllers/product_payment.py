# Copyright 2020 CorTex IT Solutions Ltd. (<https://cortexsolutions.net/>)
# License OPL-1


from odoo import http, _
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSale(WebsiteSale):


    def _get_shop_payment_values(self, order, **kwargs):
        values = super(WebsiteSale, self)._get_shop_payment_values(order, **kwargs)
        order_lines = order.website_order_line

        # Custom code
        no_empty_acquire = True
        products_acquirers = []

        for order in order_lines:
            # check if the product have acquirer
            if order.product_id and order.product_id.acquirer_ids:
                product_acquirer_enabled = False
                for acquirer in order.product_id.acquirer_ids:

                    # check if the product have at least one acquirer enabled
                    if acquirer.state != 'disabled':
                        product_acquirer_enabled = True

                        # check if the product acquirer is in the list and not duplicated
                        if acquirer in values.get('acquirers') and acquirer not in products_acquirers:
                            products_acquirers.append(acquirer)

                # If a product doesnt have any enabled acquirer then show all acquirers
                if not product_acquirer_enabled:
                    no_empty_acquire = False
                    break

            else:
                no_empty_acquire = False
                break

        if no_empty_acquire and products_acquirers:
            values['acquirers'] = products_acquirers
        # end of override
        return values
