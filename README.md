# elist
>__handle list ,nested list tree__

# install
>__pip3 install elist__

## _class_ ListTree

__1. \_\_init\_\_(alist)__
--------------------------

        from elist.elist import *
        from xdict.jprint import pobj
        from xdict.jprint import pdir
        l = [1, [4], 2, [3, [5, 6]]]
        ltree = ListTree(l)

![](elist/Images/ListTree.__init__.0.png)

__2. \_\_repr\_\___
-------------------

        l
        ltree
        pobj(ltree.showlog)

![](elist/Images/ListTree.__repr__.0.png)


__3. tree(**kwargs)__
---------------------

        pathlists = ltree.tree()
        pathlists = ltree.tree(leaf_only=True)
        pathlists = ltree.tree(leaf_only=True,from_lv=1,to_lv=2)
        pathlists = ltree.tree(non_leaf_only=True)

![](elist/Images/ListTree.tree.0.png)

__4. flatten()__
----------------

        flat = ltree.flatten()
        flat
        ltree.flatWidth
        ltree.depth

![](elist/Images/ListTree.flatten.0.png)

__5. dig(howmanysteps)__
------------------------

        depthfirst = ltree.dig()
        depthfirst = ltree.dig(2)
        depthfirst = ltree.dig(5)

![](elist/Images/ListTree.dig.0.png)


