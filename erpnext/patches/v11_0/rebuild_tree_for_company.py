import frappe
from frappe.utils.nestedset import rebuild_tree


def execute():
	frappe.reload_doc("setup", "doctype", "company")
<<<<<<< HEAD
	rebuild_tree("Company", "parent_company")
=======
	rebuild_tree("Company")
>>>>>>> 329d14957b (fix: validate negative qty)
