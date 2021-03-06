from tree import Tree

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            node = stack.pop()

            ans.append(node.val)

            # add right child first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ans

    # same as above, with simplified logic
    # but many None will be appended to stack
    def preorderTraversalSimplified(self, root):
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res

    # append right child only
    def preorderTraversal2(self, root):
        stack = []
        cur = root
        ans = []
        while cur or stack:
            if not cur:
                cur = stack.pop()
            ans.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            cur = cur.left
        return ans

    # recursion logic
    def preorderTraversal3(self, root):
        ans = []
        stack = []
        cur = root
        while stack or cur:
            if cur:
                stack.append(cur)
                ans.append(cur.val)
                cur = cur.left
            else:
                cur = stack.pop().right
        return ans

    # Morris traversal O(1) space
    # for study only
    def preorderTraversalX(self, root):
        ans = []
        if not root:
            return ans
        cur = root
        prev = None
        while cur:
            if cur.left is None:
                ans.append(cur.val)
                cur = cur.right
            else:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right
                if not prev.right:
                    ans.append(cur.val)
                    prev.right = cur
                    cur = cur.left
                else:
                    prev.right = None
                    cur = cur.right
        return ans

    def preorderTraversalMorris(self, root):
        """
        Edge case:
            when input is null
            when child node is null
        """
        ans = []
        curr = root
        while curr:
            # if left is null, process curr and go right
            if not curr.left:
                ans.append(curr.val)
                curr = curr.right
            else:
                prev = curr.left
                # go right until right is null (no link) or is curr (link exists)
                while prev.right and prev.right != curr:
                    prev = prev.right
                if not prev.right:
                    # establish link and move left
                    prev.right = curr
                    ans.append(curr.val)
                    curr = curr.left
                else:
                    # remove link and move right
                    prev.right = None
                    curr = curr.right
        return ans


solver = Solution()

root = Tree([4, 2, 5, 1, 3, None, 6]).root
print(solver.preorderTraversalMorris(root))

# root = Tree([1, 2, 3, 4, 5, None, 6, None, None, 7]).root
# print(solver.preorderTraversal3(root))