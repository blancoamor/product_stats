from openerp import models, fields, api, _
from openerp.osv import osv
from openerp.exceptions import except_orm, ValidationError
from StringIO import StringIO
import urllib2, httplib, urlparse, gzip, requests, json
import openerp.addons.decimal_precision as dp
import logging
import datetime
from openerp.fields import Date as newdate
from datetime import datetime, timedelta, date
from dateutil import relativedelta
#Get the logger
_logger = logging.getLogger(__name__)


class product_product(models.Model):
	_inherit = 'product.product'

	@api.multi
	def _update_product_rank(self):
		previous_date = date.today() - timedelta(days=365)
		invoices = self.env['account.invoice'].search([('date_invoice','>=',previous_date),
			('state','in',['open','paid'])])
		product_amount = {}
		for invoice in invoices:
			for invoice_line in invoice.invoice_line:
				if invoice_line.product_id:
					if invoice_line.product_id.id not in product_amount.keys():
						product_amount[invoice_line.product_id.id] = invoice_line.price_subtotal
					else:
						product_amount[invoice_line.product_id.id] += invoice_line.price_subtotal
		list_products = sorted(product_amount, key=product_amount.__getitem__)
		index = 0
		for product_id in list_products:
			index += 1
			vals = {
				'product_rank': index
				}
			product = self.env['product.product'].browse(product_id)
			product.write(vals)


	@api.multi
	def _update_product_abc(self):
		products = self.env['product.product'].search([('porcentaje_total_ventas','>',0)],order='porcentaje_total_ventas desc')
		running_total = 0
		for product in products:
			running_total += product.porcentaje_total_ventas
			if running_total <= 70:
				classification_value = 'A'
			else:
				if running_total <= 90:
					classification_value = 'B'
				else:
					classification_value = 'C'
			product.write({'product_abc': classification_value})

	@api.multi
	def _update_porcentaje_total_ventas(self):
		previous_date = date.today() - timedelta(days=365)
		invoices = self.env['account.invoice'].search([('date_invoice','>=',previous_date),
			('state','in',['open','paid'])])
		product_amount = {}
		for invoice in invoices:
			for invoice_line in invoice.invoice_line:
				if invoice_line.product_id:
					if invoice_line.product_id.id not in product_amount.keys():
						product_amount[invoice_line.product_id.id] = invoice_line.price_subtotal
					else:
						product_amount[invoice_line.product_id.id] += invoice_line.price_subtotal
		total_amount = 0
		for amount in product_amount.values():
			total_amount = total_amount + amount
		if total_amount > 0:
			for product in product_amount.keys():
				amount = product_amount[product]
				percentaje = (amount / total_amount) * 100
				vals = {
					'porcentaje_del_total': percentaje,
					}
				product = self.env['product.product'].browse(product)
				product.write(vals)
					
		


	product_rank = fields.Integer('Ranking')
	porcentaje_del_total = fields.Float('Porcentaje del Total de Ventas')
	product_abc = fields.Selection(selection=[('A','A'),('B','B'),('C','C')],string='Clasificacion ABC')
