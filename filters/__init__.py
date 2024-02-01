# from aiogram import Dispatcher
# # from . import admin
# # from . import gruppa
# # from . import shaxsiy
# from loader import dp
# from .admin import AdminFilter
# from .gruppa import IsGroup
# from .shaxsiy import IsPrivate
# # from .is_admin import AdminFilter


# if __name__ == "filters":
#     dp.filters_factory.bind(admin)
#     dp.filters_factory.bind(gruppa)
#     dp.filters_factory.bind(shaxsiy)
#     #dp.filters_factory.bind(is_admin)
#     pass


from loader import dp
from .admin import AdminFilter
from .gruppa import IsGroup
from .shaxsiy import IsPrivate


if __name__ == "filters":
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivate)