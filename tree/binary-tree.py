def binary_tree(r):
    return [r,[],[]]
def insert_child(root, position, new_branch):
    t = root.pop(position)
    if len(t) > 0:
        root.insert(position,[new_branch, t, []])
    else:
        root.insert(position,[new_branch,[],[]])

def get_root_val(root):
    return root[0]

def set_root_val(root, new_value):
    root[0] = new_value

def get_child(root, position):
    return root[position]


k = binary_tree(2)

print(k)
set_root_val(k,5)
insert_child(k,1, 5)
insert_child(k,2,6)
print(k)
j = [2,[5]]
print(j)
insert_child(j, 1, 4)
print(j)

