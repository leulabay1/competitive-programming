# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return " "
        
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        
        root_val = root.val if root.val >= 0 else 1000 - root.val
        subtree = str(root_val) + "l" + left + "r" + right
        
        return subtree

    def deserialize(self, data, idx = 0):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        root = TreeNode()
        
        if data[idx] == " ":
            if idx == 0:
                return None
            return None, idx
        
        left_start = idx
        while data[left_start] != "l":
            left_start += 1
        
        left, last_left = self.deserialize(data, left_start + 1)
        
        
        right, last_right = self.deserialize(data, last_left + 2)
        
        root.left = left
        root.right = right
        root.val = int(data[idx: left_start]) if int(data[idx:left_start]) <= 1000 else 1000 - int(data[idx:left_start])
        
        if idx == 0:
            return root
        return root, last_right

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))