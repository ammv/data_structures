'''
github/ammv/data_structures
author: Artem Momatov
vk: vk.com/mimo113
'''

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = {}
        self.parent = None

    def __getattr__(self, name):
        '''The ability to get child elements via an attribute
            head.body.data -> 'body'
            head.body.legs.leg1.data = 10
            head.body.legs.leg1.data -> 10
        '''
        try:
            return self.children[name]
        except KeyError:
            raise AttributeError(f"'TreeNode' object has no attribute {name}")

    def add_child(self, *args):
        '''Add child to self tree'''
        for child in args:
            child.parent = self
            self.children[child.data] = child

    def get_level(self):
        '''get child deep level'''
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        '''show tree'''
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ''
        print(prefix + self.data)
        for child in self.children.values():
            child.print_tree()

head = TreeNode('HEAD')
body = TreeNode('BODY')
arm1 = TreeNode('ARM1')
arm2 = TreeNode('ARM2')
legs = TreeNode('LEGS')
leg1 = TreeNode('LEG1')
leg2 = TreeNode('LEG2')
legs.add_child(leg1, leg2)
body.add_child(arm1, legs, arm2)
head.add_child(body)

print(leg1.data)

#head.print_tree()