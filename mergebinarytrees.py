
def mergetrees(t1:treeNode , t2:treeNode) -> rootNode
{
  if not t1 and not t2:
    return None;

  v1=t1.val if t1 else 0;
  v2=t2.val if t2 else 0;
  rootNode=(v1+v2)

  root.left=self.mergeTrees(t1.left if t1 else None , t2.left if t2 else None)
  root.right=self.mergeTrees(t1.right if t1 else None , t2.right if t2 else None)

  return rootNode;

}
  
