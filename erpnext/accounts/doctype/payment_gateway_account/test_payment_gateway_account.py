# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt
<<<<<<< HEAD

import unittest

# test_records = frappe.get_test_records('Payment Gateway Account')


class TestPaymentGatewayAccount(unittest.TestCase):
=======
import unittest

from frappe.tests import IntegrationTestCase

IGNORE_TEST_RECORD_DEPENDENCIES = ["Payment Gateway"]


class TestPaymentGatewayAccount(IntegrationTestCase):
>>>>>>> 329d14957b (fix: validate negative qty)
	pass
