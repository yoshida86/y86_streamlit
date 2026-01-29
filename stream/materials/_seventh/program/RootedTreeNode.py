class RootedTreeNode:

    """
    親のノード、辺、自身の深さをまとめて持つクラス
    """

    def __init__(self,parentnode,parentedge,depth):
        self.parentnode = parentnode
        self.parentedge = parentedge
        self.depth = depth
