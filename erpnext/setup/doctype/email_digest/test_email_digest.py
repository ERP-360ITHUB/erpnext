# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt
<<<<<<< HEAD

import unittest

# test_records = frappe.get_test_records('Email Digest')


class TestEmailDigest(unittest.TestCase):
=======
import unittest

from frappe.tests import IntegrationTestCase


class TestEmailDigest(IntegrationTestCase):
>>>>>>> 329d14957b (fix: validate negative qty)
	pass
