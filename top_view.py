class node:
    def __init__(self,node,hkey):
        self.node=node
        self.hkey=hkey
def topview(root):
    temp=node(root,0)
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
            if curr.hkey not in key_dict.keys():
                key_dict[curr.hkey]=curr.node.value
            if curr.node.left !=None:
                temp=node(curr.node.left,curr.hkey-1)
                q.append(temp)
            if curr.node.right !=None:
                temp=node(curr.node.right,curr.hkey+1)
                q.append(temp)

    for i in sorted (key_dict):
            print(key_dict[i])
    if __name__=="__main__":
         root=node(1)
         root.left=node(2)
         root.left.left=node(3)
         root.left.right=node(4)
         root.left.right.left=node(9)
         root.left.right.left.right=node(10)
         root.left.right.left.right.left=node(14)
         root.right=node(5)
         root.right.right=node(6)
         root.right.right.left=node(7)
         root.right.right.right=node(8)
         root.right.right.left.right=node(11)
         root.right.right.left.right.left=node(12)
         root.right.right.left.right.left.right=node(13)
         
            
    print(key_dict)    