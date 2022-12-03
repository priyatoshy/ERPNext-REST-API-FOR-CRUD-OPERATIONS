from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in custom_inventory_management/__init__.py
from custom_inventory_management import __version__ as version

setup(
	name="custom_inventory_management",
	version=version,
	description="Custom Inventory Management Along With Standard ERPNext features",
	author="sage analytics",
	author_email="priyatoshsatpati1@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
