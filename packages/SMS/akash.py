import Admin.service
Admin.service.admin_service()
import Admin.product
Admin.product.admin_product()
print()

import Admin.Common.footer
Admin.Common.footer.admin_common_footer()
import Admin.Common.header
Admin.Common.header.admin_common_header()
print()

'''import Tech.profile
Tech.profile.tech_profile()
import Tech.work
Tech.work.tech_work()'''
print()

print('------------------------------------------------------------------------')

print('another method to importing modules:')

from Admin import service , product
service.admin_service()
product.admin_product()

print()

from Admin.service import admin_service
admin_service()
from Admin.product import admin_product
admin_product()
print()

from Admin.Common.footer import admin_common_footer 
admin_common_footer()
from Admin.Common.header import admin_common_header
admin_common_header()
print()

from User.profile import user_profile
user_profile()
from User.request import user_request
user_request()

print()

print('-------------------------------------------------------------------------')

print('importing modules with astrisk(*):')

from Admin import *
service.admin_service()
product.admin_product()

print()

print('----------------------------------------------')

from Tech import work
work.tech_work_2()