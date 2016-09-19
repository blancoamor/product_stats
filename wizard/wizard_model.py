# -*- coding: utf-8 -*-
from datetime import datetime
import logging
from openerp.exceptions import Warning
from openerp import SUPERUSER_ID
import openerp.addons.decimal_precision as dp
_logger = logging.getLogger(__name__)
from openerp import models, fields, api


class product_generate_abastecimiento(models.TransientModel):
	_name= 'product.generate.abastecimiento'

	@api.multi
	def generate_abastecimiento(self):
		import pdb;pdb.set_trace()
		return None		

