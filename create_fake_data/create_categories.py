# from apps.products.models import Category
#
# data1 = {
#     "Women": {
#         "Clothes": [
#             {"en": "Coats", "ru": "Пальто", "uz": "Palto"},
#             {"en": "Jackets", "ru": "Куртки", "uz": "Kurtkalar"},
#             {"en": "Suits", "ru": "Костюмы", "uz": "Kostyumlar"},
#             {"en": "Dresses", "ru": "Платья", "uz": "Ko'ylaklar"}
#         ],
#         "Shoes": [
#             {"en": "Boots", "ru": "Сапоги", "uz": "Botinkalar"},
#             {"en": "Flat shoes", "ru": "Балетки", "uz": "Yassi oyoq kiyimlar"},
#             {"en": "Heels", "ru": "Туфли на каблуке", "uz": "Tovonli poyabzal"},
#             {"en": "Sandals", "ru": "Сандалии", "uz": "Sandalilar"}
#         ],
#     },
#     "Men": {
#         "Clothes": [
#             {"en": "Suits", "ru": "Костюмы", "uz": "Kostyumlar"},
#             {"en": "Shirts", "ru": "Рубашки", "uz": "Ko'ylaklar"},
#             {"en": "Pants", "ru": "Штаны", "uz": "Shimlar"}
#         ],
#         "Shoes": [
#             {"en": "Boots", "ru": "Сапоги", "uz": "Botinkalar"},
#             {"en": "Sneakers", "ru": "Кроссовки", "uz": "Krossovkalar"}
#         ]
#     },
#     "Girls": {
#         "Clothes": [
#             {"en": "Dresses", "ru": "Платья", "uz": "Ko'ylaklar"},
#             {"en": "Skirts", "ru": "Юбки", "uz": "Yubkalar"}
#         ]
#     },
#     "Boys": {
#         "Clothes": [
#             {"en": "T-shirts", "ru": "Футболки", "uz": "Futbolkalar"},
#             {"en": "Shorts", "ru": "Шорты", "uz": "Shortiklar"}
#         ]
#     }
# }
#
#
# def create_categories(data=data1, parent=None):
#     for category_name, subcategories in data.items():
#         category = Category.objects.create(
#             name=category_name,
#             name_ru=category_name,
#             name_uz=category_name,
#             parent=parent
#         )
#         if isinstance(subcategories, dict):
#             create_categories(subcategories, category)
#         elif isinstance(subcategories, list):
#             for subcategory in subcategories:
#                 Category.objects.create(
#                     name=subcategory["en"],
#                     name_ru=subcategory["ru"],
#                     name_uz=subcategory["uz"],
#                     parent=category
#                 )
