def categories_id(category, data: list):
    if not category:
        return data
    data.append(category.id)
    for category in category.children.all():
        categories_id(category, data)

    return data
