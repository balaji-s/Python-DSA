def binary_tree(r):
    return [r,[],[]]
def insert_left(root,  new_branch):
    t = root.pop(1)
    if len(t) > 0:
        root.insert(1,[new_branch, t, []])
    else:
        root.insert(1,[new_branch,[],[]])
def insert_right(root, new_branch):
    t = root.pop(2)
    if len(t) > 0:
        root.insert(2,[new_branch, [],t])
    else:
        root.insert(2,[new_branch,[],[]])
def get_root_val(root):
    return root[0]

def set_root_val(root, new_value):
    root[0] = new_value

def get_child(root, position):
    return root[position]


k = binary_tree(2)

print(k)
set_root_val(k, 5)
insert_left( k, 5)
insert_right(k, 6)
print(k)
j = [2,[5]]
print(j)
insert_left(j, 4)
print(j)