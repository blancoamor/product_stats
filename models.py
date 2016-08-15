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

	@api.one
	def _compute_product_rank(self):
		return_value = 0
		self.product_rank = return_value

	product_rank = fields.Integer('Ranking',compute=_compute_product_rank)
