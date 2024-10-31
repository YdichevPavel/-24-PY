# TODO Напишите функцию для поиска индекса товара
def search_by_index(items_list, find_item):
    
    
    for i in range(0, len(items_list)):       
         if items_list[i]==find_item:
            item = i
            return item


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']


for find_item in ['банан', 'груша', 'персик']:
    index_item = search_by_index(items_list, find_item)  
    # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
