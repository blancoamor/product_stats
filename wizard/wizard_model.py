# -*- coding: utf-8 -*-
#################################################################################
#
#    Copyright (c) 2015-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#
#################################################################################
from datetime import datetime
import logging
from openerp.exceptions import Warning
from openerp import SUPERUSER_ID
import openerp.addons.decimal_precision as dp
from openerp.addons.dhl_delivery_carrier.models.dhl_delivery_carrier import get_encoded
_logger = logging.getLogger(__name__)
from openerp import models, fields, api


class product_generate_abastecimiento(models.TransientModel):
	_name= 'product.generate.abastecimiento'

	@api.multi
	def generate_bbx_shipment_label(self):
		import pdb;pdb.set_trace()
		

