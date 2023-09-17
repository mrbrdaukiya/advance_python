# Module main class 29

import Admin.service
Admin.service.admin_service()

print()

import Admin.product
Admin.product.admin_product()

print()

import Admin.Common.header
Admin.Common.header.admin_common_header()

print()

import Admin.Common.footer
Admin.Common.footer.admin_common_footer()

print()

import Tech.profile
Tech.profile.tech_profile()


print()

import Tech.work
Tech.work.tech_work()


print()

import User.profile
User.profile.user_profile()

print()

import User.request
User.request.user_request()



print("********************************* 2nd")

# from Admin import *
from Admin import product
product.admin_product()

print()

from Admin import service
service.admin_service()

print()

from Admin.Common import header
header.admin_common_header()

print()

from Admin.Common import footer
footer.admin_common_footer()

print()

from Tech import profile
profile.tech_profile()

print()

from Tech import work
work.tech_work()

print()

from User import profile
profile.user_profile()


print()

from User import request
request.user_request()



print("3rd ******************************")


from Admin.service import admin_service
admin_service()

print()

from Admin.product import admin_product
admin_product()

print()

from Admin.Common.footer import admin_common_footer
admin_common_footer()

print()

from Admin.Common.header import admin_common_header
admin_common_header()

print()

from User.profile import user_profile
user_profile()

print()

from User.profile import user_profile
user_profile()

print()

from Tech.profile import tech_profile
tech_profile()

print()

from Tech.work import tech_work
tech_work()

print("4th ****************************")

from Admin import *
service.admin_service()
product.admin_product()

print()

from Admin.Common import *
header.admin_common_header()
footer.admin_common_footer()

print()

from Tech import *
profile.tech_profile()
work.tech_work()

print()

from User import *
profile.user_profile()
request.user_request()


print(" 5th ********************************")


from Tech import work
work.tech_work()