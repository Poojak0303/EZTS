
##bottom view
class node_data:
    def __init__(self,node,hkey):
        self.node=node
        self.hkey=hkey
def bottomview(root):
    temp=node_data(root,0)
    q=[temp]
    q.append(None)
    
    key_dict={}
    
    while len(q)!=0:
        curr =q.pop(0)
        if curr ==None:
            if len(q)==0:
                break
            else:
                q.append(None)
        else:
              key_dict[curr.hkey]=curr.node.value
              if curr.node.left !=None:
                temp=node_data(curr.node.left,curr.hkey-1)
                q.append(temp)
              if curr.node.right !=None:
                temp=node_data(curr.node.right,curr.hkey+1)
                q.append(temp)

    for i in sorted (key_dict):
            print(key_dict[i])


    print(key_dict)    
bottomview(root)