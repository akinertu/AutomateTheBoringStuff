#DICTIONARY VERSION
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
print('Inventory:',end='\n')

def displayInventory(inv):
    total = 0
    for i, k in inv.items():
        print(k,'',i)
        total += k
    print('Total number of items:', total)

displayInventory(inventory)


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def addToInventory(inv, addedItems):
    new_inv = {}
    for i, k in inv.items():
        k += addedItems.count(i)
        new_inv.setdefault(i,k)
    for i in addedItems:
        if i in new_inv.keys():
            continue
        else:
            new_inv.setdefault(i,addedItems.count(i))   
    return new_inv
        
    
inventory = addToInventory(inventory, dragonLoot)
displayInventory(inventory)
