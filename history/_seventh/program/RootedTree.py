class RootedTree:

    """
    RootedTreeNodeを要素にもち、根付き木として木を管理するクラス
    """
    def __init__(self,startV):
        self.treeinfo = {}
        self.treeinfo[startV] = RootedTreeNode(-1,-1,1)


    def insert(self,Nodenum,parentV,parentE):
        """
        辞書型にノードの情報を追加する関数
        """
        self.treeinfo[Nodenum] = RootedTreeNode(parentV,parentE,self.treeinfo[parentV].depth + 1)


        
    def LCAcycle(self,leftnode,rightnode):
        """
        最小共通祖先の探索により見つけたサイクルに含まれる辺の列を返す

        Args:
            leftnode(int):一つ目の頂点の番号
            rightnode(int):二つ目の頂点の番号

        Returns:
            list:サイクルに含まれる辺の列
        """

        ret = []

        ##深さをそろえる
        if self.treeinfo[leftnode].depth > self.treeinfo[rightnode].depth:
            n = self.treeinfo[leftnode].depth - self.treeinfo[rightnode].depth
            for i in range(n):
                ret.append(self.treeinfo[leftnode].parentedge)
                leftnode = self.treeinfo[leftnode].parentnode
        elif self.treeinfo[leftnode].depth < self.treeinfo[rightnode].depth:
            n = self.treeinfo[rightnode].depth - self.treeinfo[leftnode].depth
            for i in range(n):
                ret.append(self.treeinfo[rightnode].parentedge)
                rightnode = self.treeinfo[rightnode].parentnode
        
        while leftnode != rightnode:
            #left側を一個上る
            ret.append(self.treeinfo[leftnode].parentedge)
            leftnode = self.treeinfo[leftnode].parentnode
            #right側を一個上る
            ret.append(self.treeinfo[rightnode].parentedge)
            rightnode = self.treeinfo[rightnode].parentnode

        return ret