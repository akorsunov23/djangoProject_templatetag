from django import template
from app_templatetags.models import Item


register = template.Library()


@register.inclusion_tag('app_templatetags/menu.html', takes_context=True)
def draw_menu(context, menu) -> dict:

    global primary_item
    try:
        items = Item.objects.filter(menu__title=menu).select_related('menu', 'parent')
        items_values = items.values()
        primary_item = [item for item in items_values.filter(parent=None)]
        selected_item_slug = context['request'].GET[menu]
        selected_item = items.get(slug=selected_item_slug)
        selected_item_id_list = get_selected_item_id_list(selected_item, primary_item, selected_item_slug)

        for item in primary_item:
            if item['id'] in selected_item_id_list:
                item['child_items'] = get_child_items(items_values, item['id'], selected_item_id_list)
        result_dict = {'items': primary_item}

    except:
        result_dict = {'items': primary_item}

    result_dict['menu'] = menu
    return result_dict


def get_child_items(items_values, current_item_id, selected_item_id_list) -> list:
    item_list = [item for item in items_values.filter(parent_id=current_item_id)]
    for item in item_list:
        if item['id'] in selected_item_id_list:
            item['child_items'] = get_child_items(items_values, item['id'], selected_item_id_list)
    if len(item_list) > 0:
        return item_list


def get_selected_item_id_list(parent, primary_item, selected_item_slug) -> list:
    selected_item_slug_list = []

    while parent:
        selected_item_slug_list.append(parent.id)
        parent = parent.parent
    if not selected_item_slug_list:
        for item in primary_item:
            if item['slug'] == selected_item_slug:
                selected_item_slug_list.append(selected_item_slug)
    return selected_item_slug_list
