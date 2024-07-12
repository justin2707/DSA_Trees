def root_to_leaf(self,root): ->int 
   def dfs(cur , num):
     if not cur:
       return 0

     num=num*10+cur.val
     if not cur.left and cur.right:
       return num
     return dfs(cur.left,num)+dfs(cur.right,num)

  dfs(root, 0)

    
