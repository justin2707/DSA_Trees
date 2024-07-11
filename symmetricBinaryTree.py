def symmetricBinaryTree(self , TreeNode) --> bool
  def dfs(t1,t2):
      if not t1 and not t2:
           return True
      if  not t1 or not t2:
            return False

      return ( t1.val==t2.val and
            dfs(t1.left , t2.right) and
            dfs(t1.right,t2.left) )
      return dfs(t1.node , t2.node)
