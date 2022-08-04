from setuptools import setup

from sp_api.__version__ import __version__

setup(
    name='python-amazon-sp-api',
    version=__version__,
    install_requires=[
        "requests==2.25.1",
        "six==1.16.0",
        "boto3==1.24.45",
        "cachetools==3.1.1",
        "setuptools==44.0.0",
        "pytz==2020.5",
        "confuse==1.4.0",
        "enum34==1.1.10",
        "future-fstrings==1.2.0"
    ],
    packages=['tests', 'tests.api', 'tests.api.orders', 'tests.api.sellers', 'tests.api.finances',
              'tests.api.product_fees', 'tests.api.notifications', 'tests.api.reports', 'tests.client',
              'sp_api',
              'sp_api.api',
              'sp_api.api.orders',
              'sp_api.api.sellers',
              'sp_api.api.finances',
              'sp_api.api.product_fees',
              'sp_api.api.products',
              'sp_api.api.feeds',
              'sp_api.api.sales',
              'sp_api.api.catalog',
              'sp_api.api.notifications',
              'sp_api.api.reports',
              'sp_api.api.inventories',
              'sp_api.api.messaging',
              'sp_api.api.upload',
              'sp_api.api.merchant_fulfillment',
              'sp_api.api.fulfillment_inbound',
              'sp_api.auth',
              'sp_api.base',
              'sp_api.util',
                ##### DO NOT DELETE ########## INSERT PACKAGE HERE #######
              'sp_api.api.listings_restrictions',
    

              'sp_api.api.catalog_items',
              'sp_api.api.product_type_definitions',
              'sp_api.api.listings_items',
              'sp_api.api.vendor_transaction_status',
              'sp_api.api.vendor_shipments',
              'sp_api.api.vendor_orders',
              'sp_api.api.vendor_invoices',
              'sp_api.api.vendor_direct_fulfillment_transactions',
              'sp_api.api.vendor_direct_fulfillment_shipping',
              'sp_api.api.vendor_direct_fulfillment_payments',
              'sp_api.api.vendor_direct_fulfillment_orders',
              'sp_api.api.vendor_direct_fulfillment_inventory',
              'sp_api.api.tokens',
              'sp_api.api.solicitations',
              'sp_api.api.shipping',
              'sp_api.api.services',
              'sp_api.api.fba_small_and_light',
              'sp_api.api.fba_inbound_eligibility',
              'sp_api.api.authorization',
              'sp_api.api.aplus_content',
              'sp_api.api.fulfillment_outbound',
              ],
    scripts=['make_endpoint/make_endpoint'],
    url='https://github.com/saleweaver/python-amazon-sp-api',
    license='MIT',
    author='Michael',
    author_email='info@saleweaver.com',
    description='Python wrapper for the Amazon Selling-Partner API'
)

