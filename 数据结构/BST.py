class BSTNode:

    def __init__(self, dlnode):
        self.ptr = dlnode
        self.l = None
        self.r = None


class BST:

    def __init__(self, head):
        self.root = BSTNode(head)

    def insert(self, dlnode):

        def insertHelper(root, dlnode, min_, max_):
            if dlnode.v <= root.ptr.v:
                if not root.l:
                    root.l = BSTNode(dlnode)
                    if min_:
                        min_ = min_.ptr
                    return min_, root.ptr
                return insertHelper(root.l, dlnode, min_, root)
            else:
                if not root.r:
                    root.r = BSTNode(dlnode)
                    if max_:
                        max_ = max_.ptr
                    return root.ptr, max_
                return insertHelper(root.r, dlnode, root, max_)

        return insertHelper(self.root, dlnode, None, None)

    def delNode(self, node):
        tmp, prev = self.root, None
        while tmp and node != tmp.ptr:
            prev = tmp
            if node.v <= tmp.ptr.v:
                tmp = tmp.l
            else:
                tmp = tmp.r

        if tmp == None:
            return f'Something went wrong, Node {node} not found...'
        else:
            if tmp.l and tmp.r:
                tmp2, prev2 = tmp.r, None
                while tmp2.l:
                    prev2 = tmp2
                    tmp2 = tmp2.l

                if prev2:
                    prev2.l = tmp2.r

                if prev:
                    if prev.l == tmp:
                        prev.l = tmp2
                    elif prev.r == tmp:
                        prev.r = tmp2
                    else:
                        return 'Something went wrong.'
                else:
                    self.root = tmp2

                tmp2.l = tmp.l
                if tmp2 != tmp.r:
                    tmp2.r = tmp.r
            elif tmp.l:
                if prev:
                    if prev.l == tmp:
                        prev.l = tmp.l
                    elif prev.r == tmp:
                        prev.r = tmp.l
                    else:
                        return 'Something went wrong.'
                else:
                    self.root = tmp.l
            elif tmp.r:
                if prev:
                    if prev.l == tmp:
                        prev.l = tmp.r
                    elif prev.r == tmp:
                        prev.r = tmp.r
                    else:
                        return 'Something went wrong.'
                else:
                    self.root = tmp.r
            else:
                if prev:
                    if prev.l == tmp:
                        prev.l = None
                    elif prev.r == tmp:
                        prev.r = None
                    else:
                        return 'Something went wrong.'
                else:
                    self.root = tmp.r

            del tmp

    def popByorder(self):
        def inorderPop(root):
            nodes = []

            if root.l:
                nodes += inorderPop(root.l)
            nodes += [root.ptr]
            if root.r:
                nodes += inorderPop(root.r)

            return nodes

        return inorderPop(self.root)

    def __str__(self):
        def inorder(root):
            s = ''

            if root.l:
                s += inorder(root.l)
            s += f' -> {root.ptr.v}'
            if root.r:
                s += inorder(root.r)

            return s

        return 'BST' + inorder(self.root)


class DLNode:

    def __init__(self, v):
        self.v = v
        self.next = None
        self.prev = None


class DList:

    def __init__(self, v):
        self.head = DLNode(v) if isinstance(v, int) else v
        self.tail = self.head

    def append(self, node):
        if self.head == self.tail:
            self.head.next = node
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def insert(self, l, m, r):
        if l and r:
            l.next = m
            m.next = r
            r.prev = m
            m.prev = l
        elif l:
            self.tail = m
            l.next = m
            m.prev = l
        elif r:
            self.head = m
            m.next = r
            r.prev = m
        # else:
        #     Wrong...

    def delHead(self):
        tmp = self.head
        self.head = self.head.next
        self.head.prev = None
        del tmp

    def delTail(self):
        tmp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        del tmp

    def delNode(self, d):
        if d == self.head:
            self.delHead()
        elif d == self.tail:
            self.delTail()
        else:
            d.prev.next = d.next
            d.next.prev = d.prev
            del d

    def __str__(self):
        s = f'{self.head.v}'
        tmp = self.head.next
        while tmp:
            s += f' -> {tmp.v}'
            tmp = tmp.next
        return s


#################################
