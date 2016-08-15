from openerp import models, fields, api, _
from openerp.osv import osv
from openerp.exceptions import except_orm, ValidationError
from StringIO import StringIO
import urllib2, httplib, urlparse, gzip, requests, json
import openerp.addons.decimal_precision as dp
import logging
import datetime
from openerp.fields import Date as newdate
from datetime import datetime, timedelta
from dateutil import relativedelta
#Get the logger
_logger = logging.getLogger(__name__)


class product_product(models.Model):
	_inherit = 'product.product'

	@api.multi
	def _update_product_rank(self):
		return_value = 0
		import pdb;pdb.set_trace()
		previous_date = date.today() - timedelta(days=365)
		invoices = self.env['account.invoice'].search([('date_invoice','>=',previous_date),
			('state','in',['open','paid'])])
		product_amount = {}
		for invoice in invoices:
			for invoice_line in invoice.invoice_line:
				if invoice_line.product_id.id not in product_amount.keys():
					product_amount[invoice_line.product_id.id] = invoice_line.price_subtotal
				else:
					product_amount[invoice_line.product_id.id] += invoice_line.price_subtotal
		self.product_rank = return_value

	product_rank = fields.Integer('Ranking')
