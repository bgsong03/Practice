class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def printTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
    print(TreeNode(self.val))

root = TreeNode(1)
root.printTrees()