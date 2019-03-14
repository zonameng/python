#!/usr/bin/python3
#这是一个物品清单得小测试
stuff={'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}
def displayInventory(inventory):
    print('Inventory:')
    items_top=0
    for k,v in inventory.items():
        print(str(v)+' '+k)
        items_top+=v
    print('total number of items: '+str(items_top))
displayInventory(stuff)