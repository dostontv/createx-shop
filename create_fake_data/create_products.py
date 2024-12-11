# from translate import Translator
#
# from faker import Faker
# from random import choice
# from apps.products.models import Product, Category
#
# # poetry add python-Levenshtein
#
# from fuzzywuzzy import fuzz
#
#
# def translate_text(text, src_lang='en'):
#     translator_uz = Translator(from_lang=src_lang, to_lang="uz")
#     translated_uz = translator_uz.translate(text)
#
#     translator_ru = Translator(from_lang=src_lang, to_lang="ru")
#     translated_ru = translator_ru.translate(text)
#
#     return translated_uz, translated_ru
#
#
# def find_matching_category(product_name):
#     categories = Category.objects.all()
#
#     best_match = None
#     highest_score = 0
#
#     for category in categories:
#         score = fuzz.partial_ratio(product_name.lower(), category.name.lower())
#         if score > highest_score:
#             highest_score = score
#             best_match = category
#
#     if best_match:
#         return best_match.id
#     else:
#         return Category.objects.get_or_create(name='Other')[0].id
#
#
# fake = Faker()
# clothing_names = [
#     'Shirt',
#     'Jeans',
#     'Jacket',
#     'Sweater',
#     'T-shirt',
#     'Dress',
#     'Shoes',
#     'Socks',
#     'Hat',
#     'Scarf',
#     'Shorts',
#     'Skirt',
#     'Blouse',
#     'Suit',
#     'Coat',
#     'Pants',
#     'Boots',
#     'Gloves',
#     'Belt',
#     'Cap',
#     'Sandals',
#     'Tie',
#     'Vest',
#     'Leggings',
#     'Tunic',
#     'Hoodie',
#     'Raincoat',
#     'Slippers',
#     'Cardigan',
#     'Blazer',
#     'Bathrobe',
#     'Beanie',
#     'Tracksuit',
#     'Poncho',
#     'Swimsuit',
#     'Tank Top',
#     'Overalls',
#     'Romper',
#     'Mittens',
#     'Sneakers',
#     'Wedges',
#     'Espadrilles',
#     'Ankle Boots',
#     'High Heels',
#     'Flip Flops',
#     'Loafers',
#     'Polo Shirt',
#     'Dungarees',
#     'Kimono',
#     'Sarong'
# ]
#
#
# def create_product():
#     product_name = choice(clothing_names)
#
#     name_uz, name_ru = translate_text(product_name)
#
#     description_en = fake.text()
#     description_uz, description_ru = translate_text(description_en)
#
#     category_id = find_matching_category(product_name)
#
#     product = Product(
#         name=product_name,
#         name_uz=name_uz,
#         name_ru=name_ru,
#         description=description_en,
#         description_uz=description_uz,
#         description_ru=description_ru,
#         category_id=category_id,
#         views=fake.random_int(min=0, max=1000)
#     )
#     product.save()
#
#
# def create_product_():
#     for _ in range(1000):
#         create_product()
#
#     print("1000 ta kiyim-kechak mahsuloti yaratildi.")
