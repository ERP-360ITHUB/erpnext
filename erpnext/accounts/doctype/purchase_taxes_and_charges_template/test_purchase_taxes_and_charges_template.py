# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors and Contributors
# See license.txt
<<<<<<< HEAD

import unittest

# test_records = frappe.get_test_records('Purchase Taxes and Charges Template')


class TestPurchaseTaxesandChargesTemplate(unittest.TestCase):
=======
import unittest

from frappe.tests import IntegrationTestCase


class TestPurchaseTaxesandChargesTemplate(IntegrationTestCase):
>>>>>>> 329d14957b (fix: validate negative qty)
	pass
