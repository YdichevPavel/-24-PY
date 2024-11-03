# TODO Напишите функцию для поиска индекса товара
def search_by_index(items_list, find_item):
    
    # items_list - списко предметов 
    # find_item - искомый предмет
    
    for index, item in enumerate(items_list):       
         if item == find_item:
            return index


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']


for find_item in ['банан', 'груша', 'персик']:
    index_item = search_by_index(items_list, find_item)  
    # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
