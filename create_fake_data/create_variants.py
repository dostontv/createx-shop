# import random
#
# from apps.products.models import Product, ProductVariant, Content, Size, Brand, Color, Material
# from create_fake_data.create_products import fake_uz
#
# colors = ['White', 'Blue', 'Red', 'Black']
#
# product_data = {
#     'Shirt': {
#         'sizes': ['S', 'M', 'L', 'XL'],
#         'brands': ['Nike', 'Adidas', 'Puma', 'H&M'],
#         'images': [
#             "https://example.com/shirt1.jpg", "https://example.com/shirt2.jpg"
#         ],
#         'materials': ['Cotton', 'Linen', 'Polyester']  # Yangi qo'shilgan material
#     },
#     'Jeans': {
#         'sizes': ['28', '30', '32', '34', '36'],
#         'brands': ['Levi\'s', 'Wrangler', 'Lee'],
#         'images': [
#             "https://example.com/jeans1.jpg", "https://example.com/jeans2.jpg"
#         ],
#         'materials': ['Denim', 'Cotton', 'Spandex']  # Yangi qo'shilgan material
#     },
#     'Jacket': {
#         'sizes': ['S', 'M', 'L', 'XL'],
#         'brands': ['NorthFace', 'Columbia', 'Patagonia'],
#         'images': [
#             "https://example.com/jacket1.jpg", "https://example.com/jacket2.jpg"
#         ],
#         'materials': ['Leather', 'Wool', 'Nylon']  # Yangi qo'shilgan material
#     },
#     'Sweater': {
#         'sizes': ['S', 'M', 'L', 'XL'],
#         'brands': ['Zara', 'Uniqlo', 'H&M'],
#         'images': [
#             "https://example.com/sweater1.jpg", "https://example.com/sweater2.jpg"
#         ],
#         'materials': ['Wool', 'Cotton', 'Cashmere']  # Yangi qo'shilgan material
#     },
#     'T-shirt': {
#         'sizes': ['S', 'M', 'L', 'XL'],
#         'brands': ['Nike', 'Adidas', 'Puma'],
#         'images': [
#             "https://example.com/tshirt1.jpg", "https://example.com/tshirt2.jpg"
#         ],
#         'materials': ['Cotton', 'Polyester', 'Bamboo']  # Yangi qo'shilgan material
#     },
#     'Dress': {
#         'sizes': ['S', 'M', 'L'],
#         'brands': ['Gucci', 'Chanel', 'Zara'],
#         'images': [
#             "https://example.com/dress1.jpg", "https://example.com/dress2.jpg"
#         ],
#         'materials': ['Silk', 'Cotton', 'Lace']  # Yangi qo'shilgan material
#     },
#     'Shoes': {
#         'sizes': ['6', '7', '8', '9', '10'],
#         'brands': ['Nike', 'Adidas', 'Reebok'],
#         'images': [
#             "https://example.com/shoes1.jpg", "https://example.com/shoes2.jpg"
#         ],
#         'materials': ['Leather', 'Rubber', 'Mesh']  # Yangi qo'shilgan material
#     },
#     'Socks': {
#         'sizes': ['S', 'M', 'L'],
#         'brands': ['Nike', 'Adidas', 'Puma'],
#         'images': [
#             "https://example.com/socks1.jpg", "https://example.com/socks2.jpg"
#         ],
#         'materials': ['Cotton', 'Wool', 'Polyester']  # Yangi qo'shilgan material
#     },
#     'Hat': {
#         'sizes': ['One Size'],
#         'brands': ['Nike', 'Adidas', 'New Era'],
#         'images': [
#             "https://example.com/hat1.jpg", "https://example.com/hat2.jpg"
#         ],
#         'materials': ['Wool', 'Cotton', 'Polyester']  # Yangi qo'shilgan material
#     },
#     'Scarf': {
#         'sizes': ['One Size'],
#         'brands': ['Gucci', 'Zara', 'H&M'],
#         'images': [
#             "https://example.com/scarf1.jpg", "https://example.com/scarf2.jpg"
#         ],
#         'materials': ['Wool', 'Cashmere', 'Silk']  # Yangi qo'shilgan material
#     },
# }
#
#
# def fetch_random_image_url():
#     return f"https://picsum.photos/seed/{random.randint(1, 1000)}/500"
#
#
# def select_product(product_name):
#     if product_name not in product_data:
#         return
#
#     product = product_data[product_name]
#     size = random.choice(product['sizes'])
#     brand = random.choice(product['brands'])
#     material = random.choice(product['materials'])
#
#     size = Size.objects.get_or_create(name=size)
#     brand = Brand.objects.get_or_create(name=brand)
#     material = Material.objects.get_or_create(name=material)
#     return {
#         'size_id': size[0].id,
#         'brand_id': brand[0].id,
#         'material_id': material[0].id,
#         'image': product['images']
#     }
#
#
# def create_product_variants():
#     products = Product.objects.all()
#     for product in products:
#         selected_product = select_product(product.name)
#         quantity = random.randint(1, 100)
#         price = random.randint(10, 1000)
#         color = random.choice(colors)
#         color = Color.objects.get_or_create(name=color)[0]
#         if selected_product:
#             images = selected_product.pop('image')
#             product_variant = ProductVariant.objects.create(product=product, quantity=quantity, price=price,
#                                                             color=color, views=fake_uz.random_int(min=0, max=1000),
#                                                             **selected_product)
#             for image in images:
#                 Content.objects.create(product_variant=product_variant, content=image)
#         else:
#             material = Material.objects.order_by('?').first()
#             brand = Brand.objects.order_by('?').first()
#             size = Size.objects.order_by('?').first()
#             image = fetch_random_image_url()
#             product_variant = ProductVariant.objects.create(product=product, quantity=quantity, price=price,
#                                                             size=size,
#                                                             material=material,
#                                                             brand=brand,
#                                                             color=color,
#                                                             views=fake_uz.random_int(min=0, max=1000))
#             Content.objects.create(product_variant=product_variant, content=image)
