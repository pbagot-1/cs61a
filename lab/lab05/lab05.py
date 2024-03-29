""" Lab 05: Mutable Sequences and Trees """

# Q1
def acorn_finder(t):
    """Returns True if t contains a node with the value 'acorn' and
    False otherwise.

    >>> scrat = tree('acorn')
    >>> acorn_finder(scrat)
    True
    >>> sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('acorn')]), tree('branch2')])
    >>> acorn_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> acorn_finder(numbers)
    False
    """
    """firstItem = []
    if label(t) == 'acorn':
       firstItem = [True]"""
    l = []
    inorder_transversal(t,l)
  
    for check in l:
        if check == 'acorn':
            return True
    return False


    """if len(firstItem) > 0:
        return True
    return False"""
def inorder_transversal(t, l):
    if (not branches(t)):
        l.append(label(t))
        return
    
    if (branches(t)):
        inorder_transversal(t[1], l)
    
        l.append(label(t))
    
        inorder_transversal(t[2], l)
    
    
# Q2
def prune_leaves(t, vals):
    """Return a modified copy of t with all leaves that have a label
    that appears in vals removed.  Return None if the entire tree is
    pruned away.

    >>> t = tree(2)
    >>> print(prune_leaves(t, (1, 2)))
    None
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    >>> print_tree(prune_leaves(numbers, (3, 4, 6, 7)))
    1
      2
      3
        5
      6
    """
    for val in vals:
        if val == label(t):
            return None
            
    inorder_transversal_remover(t, vals)

    return t
    
def inorder_transversal_remover(t, vals):
    if (not branches(t)):
        for val in vals:
            if val == label(t):
                t[0] = ''
           
        return
    
    if (branches(t)):
        inorder_transversal_remover(t[1], vals)
    
        inorder_transversal_remover(t[2], vals)
# Q3
def memory(n):
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """
    m = memorizer(n)
    ret = lambda x : m.memorize(x)
    return ret
class memorizer:
    def __init__(self, n):
        self.n=n
        
    def memorize(self, x):
        self.n = x(self.n)
        return self.n

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])