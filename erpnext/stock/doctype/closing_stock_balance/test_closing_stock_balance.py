# Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt

# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestClosingStockBalance(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestClosingStockBalance(UnitTestCase):
	"""
	Unit tests for ClosingStockBalance.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestClosingStockBalance(IntegrationTestCase):
>>>>>>> 329d14957b (fix: validate negative qty)
	pass
