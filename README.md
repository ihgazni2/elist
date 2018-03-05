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


__6. level(whichlevel,**kwargs)__
---------------------------------

        level = ltree.level(1)
        level = ltree.level(1,leaf_only=True)
        level = ltree.level(1,non_leaf_only=True)
        level = ltree.level(2)
        level = ltree.level(3)
        
![](elist/Images/ListTree.level.0.png)

__7. include(\*pathlist,**kwargs)__
-----------------------------------

        l[3][1][0]
        ltree.include(3,1,0)
        l[3][1][2]
        ltree.include(pathlist = [3,1,2])
        
![](elist/Images/ListTree.include.0.png)

__8. \_\_getitem\_\_(\*pathlist)__
----------------------------------

        ltree[1,0]
        l[1][0]
        ltree[3,1,1]
        l[3][1][1]

![](elist/Images/ListTree.__getitem__.0.png)

__9. search(value,**kwargs)__
-----------------------------

        from xdict.TestLib.genrand import gen_random_recursive_only_list_data as randlist
        # lets generate a l for test,l is a big nested-list
        l = randlist()
        #the l looks like the below:
 
![](elist/Images/ListTree.search.0.png)

        #you can see the value "v_4" appears in different levels of the nested-list:

<img src="elist/Images/ListTree.search.1.png" height="400">

        ltree = ListTree(l)
        pathlists = ltree.search('v_4')
        pathlists.__len__()
        #we will found 125 match

<img src="elist/Images/ListTree.search.2.png" height="400">
 
        #......
<img src="elist/Images/ListTree.search.3.png" height="400">

        l[0]
        l[4][2][1][0][0][3]
        l[4][2][1][0][0][19][11]
        l[11][3]

<img src="elist/Images/ListTree.search.4.png" width="400">

__ListTree lquery APIs:__


-----------------------------------------------------------------------
>├──10. [ancestor_paths](elist/Images/ListTree.ancestors.0.png)  <br>
├──11. [ancestors](elist/Images/ListTree.ancestors.0.png)  <br>
├──12. [parent_path](elist/Images/ListTree.parent.0.png)  <br>
├──13. [parent](elist/Images/ListTree.parent.0.png)  <br>
├──14. [descendant_paths](elist/Images/ListTree.descendants.1.png)  <br>
├──15. [descendants](elist/Images/ListTree.descendants.1.png)  <br>
├──16. [prevSibPath](elist/Images/ListTree.prevSib.0.png)  <br>
├──17. [prevSibling](elist/Images/ListTree.prevSib.0.png)  <br>
├──18. [nextSibPath](elist/Images/ListTree.nextSib.0.png)  <br>
├──19. [nextSibling](elist/Images/ListTree.nextSib.0.png)  <br>
├──20. [lsib_path](elist/Images/ListTree.prevSib.0.png)  <br>
├──21. [lsib](elist/Images/ListTree.prevSib.0.png)  <br>
├──22. [rsib_path](elist/Images/ListTree.nextSib.0.png)  <br>
├──23. [rsib](elist/Images/ListTree.nextSib.0.png)  <br>
├──24. [sib_paths](elist/Images/ListTree.sibs.0.png)  <br>
├──25. [sibs](elist/Images/ListTree.sibs.0.png)  <br>
├──26. [someSibPaths](elist/Images/ListTree.someSibs.0.png)  <br>
├──27. [someSibs](elist/Images/ListTree.someSibs.0.png)  <br>
├──28. [some_sib_paths](elist/Images/ListTree.someSibs.0.png)  <br>
├──29. [some_sibs](elist/Images/ListTree.someSibs.0.png)  <br>
├──30. [whichSibPath](elist/Images/ListTree.whichSib.0.png)  <br>
├──31. [whichSib](elist/Images/ListTree.whichSib.0.png)  <br>
├──32. [which_sib_path](elist/Images/ListTree.which_sib.0.png)  <br>
├──33. [which_sib](elist/Images/ListTree.which_sib.0.png)  <br>
├──34. [precedingSibPaths](elist/Images/ListTree.precedingSibs.0.png)  <br>
├──35. [precedingSibs](elist/Images/ListTree.precedingSibs.0.png)  <br>
├──36. [preceding_sib_paths](elist/Images/ListTree.precedingSibs.0.png)  <br>
├──37. [preceding_sibs](elist/Images/ListTree.precedingSibs.0.png)  <br>
├──38. [followingSibPaths](elist/Images/ListTree.followingSibs.0.png)  <br>
├──39. [followingSibs](elist/Images/ListTree.followingSibs.0.png)  <br>
├──40. [following_sib_paths](elist/Images/ListTree.followingSibs.0.png)  <br>
├──41. [following_sibs](elist/Images/ListTree.followingSibs.0.png)  <br>
├──42. [lcin_path](elist/Images/ListTree.lcin.0.png)  <br>
├──43. [lcin](elist/Images/ListTree.lcin.0.png)  <br>
├──44. [rcin_path](elist/Images/ListTree.rcin.0.png)  <br>
├──45. [rcin](elist/Images/ListTree.rcin.0.png)  <br>
├──46. [son_paths](elist/Images/ListTree.sons.0.png)  <br>
├──47. [sons](elist/Images/ListTree.sons.0.png)  <br>
├──48. [total](elist/Images/ListTree.PARAMS.0.png)  <br>
├──49. [maxLevelWidth](elist/Images/ListTree.PARAMS.0.png)  <br>
├──50. [depth](elist/Images/ListTree.PARAMS.0.png)  <br>
├──51. [flatWidth](elist/Images/ListTree.PARAMS.0.png)  <br>

-----------------------------------------------------------------------

## _elist_ functions

-----------------------------------------------------------------------
>├──0. [select_some](elist/Images/select.0.png)  <br>
├──1. [select_seqs](elist/Images/select.0.png)  <br>
├──2. [append](elist/Images/append.0.png)  <br>
├──3. [append_some](elist/Images/append_some.0.png)  <br>
├──4. [prepend](elist/Images/prepend.0.png)  <br>
├──5. [prepend_some](elist/Images/unshift.0.png)  <br>
├──5. [unshift](elist/Images/unshift.0.png)  <br>
├──6. [extend](elist/Images/extend.0.png)  <br>
├──6. [push](elist/Images/push.0.png)  <br>
├──7. [concat](elist/Images/concat.0.png)  <br>
├──8. [prextend](elist/Images/prextend.0.png)  <br>
├──9. [car](elist/Images/carcdr.0.png)  <br>
├──10. [cdr](elist/Images/carcdr.0.png)  <br>
├──11. [cons](elist/Images/cons.0.png)  <br>
├──12. [insert](elist/Images/insert.0.png)  <br>
├──13. [insert_some](elist/Images/insert_some.0.png)  <br>
├──14. [insert_many](elist/Images/insert_many.0.png)  <br>
├──14. [sort](elist/Images/sort.0.png)  <br>
├──15. [batsorted](elist/Images/batsorted.0.png)  <br>
├──16. [index_first](elist/Images/index_first.0.png)  <br>
├──17. [array_index](elist/Images/index_first.0.png)  <br>
├──18. [indexOf](elist/Images/index_first.0.png)  <br>
├──19. [index_firstnot](elist/Images/index_firstnot.0.png)  <br>
├──20. [array_indexnot](elist/Images/index_firstnot.0.png)  <br>
├──21. [indexOfnot](elist/Images/index_firstnot.0.png)  <br>
├──22. [index_last](elist/Images/index_last.0.png)  <br>
├──24. [lastIndexOf](elist/Images/index_last.0.png)  <br>
├──25. [index_lastnot](elist/Images/index_lastnot.0.png)  <br>
├──26. [lastIndexOfnot](elist/Images/index_lastnot.0.png)  <br>
├──27. [index_which](elist/Images/index_which.0.png)  <br>
├──28. [index_whichnot](elist/Images/index_whichnot.0.png)  <br>
├──29. [index_all](elist/Images/index_all.0.png)  <br>
├──30. [index_allnot](elist/Images/index_allnot.0.png)  <br>
├──31. [index_some](elist/Images/index_some.0.png)  <br>
├──32. [index_somenot](elist/Images/index_somenot.0.png)  <br>
├──33. [index_seqs](elist/Images/index_seqs.0.png)  <br>
├──34. [index_seqsnot](elist/Images/index_seqs.0.png)  <br>
├──35. [first_continuous_indexes_slice](elist/Images/firstlast_continuous_indexes_slice.0.png)  <br>
├──36. [first_continuous_indexesnot_slice](elist/Images/firstlast_continuous_indexes_slice.0.png)  <br>
├──37. [last_continuous_indexes_slice](elist/Images/firstlast_continuous_indexes_slice.0.png)  <br>
├──38. [last_continuous_indexesnot_slice](elist/Images/firstlast_continuous_indexes_slice.0.png)  <br>
├──39. [which_continuous_indexes_slice](elist/Images/which_continuous_indexes_slice.0.png)  <br>
├──40. [which_continuous_indexesnot_slice](elist/Images/which_continuous_indexes_slice.0.png)  <br>
├──41. [some_continuous_indexes_slices](elist/Images/all_some_seqs_continuous_indexes_slices.0.png)  <br>
├──42. [some_continuous_indexesnot_slices](elist/Images/all_some_seqs_continuous_indexes_slices.0.png)  <br>
├──43. [seqs_continuous_indexes_slices](elist/Images/all_some_seqs_continuous_indexes_slices.0.png)  <br>
├──44. [seqs_continuous_indexesnot_slices](elist/Images/all_some_seqs_continuous_indexes_slices.0.png)  <br>
├──45. [all_continuous_indexes_slices](elist/Images/all_some_seqs_continuous_indexes_slices.0.png)  <br>
├──46. [all_continuous_indexesnot_slices](elist/Images/all_some_seqs_continuous_indexes_slices.0.png)  <br>
├──47. [shift](elist/Images/shift.0.png)  <br>
├──48. [pop](elist/Images/pop.0.png)  <br>
├──49. [pop_range](elist/Images/pop_range.0.png)  <br>
├──50. [pop_some](elist/Images/pop_some.0.png)  <br>
├──51. [pop_indexes](elist/Images/pop_indexes.0.png)  <br>
├──52. [array_remove](elist/Images/.array_remove.0.png)  <br>
├──53. [remove_first](elist/Images/.remove_first.0.png)  <br>
├──54. [array_removenot](elist/Images/.array_removenot.0.png)  <br>
├──55. [remove_firstnot](elist/Images/.remove_firstnot.0.png)  <br>
├──56. [remove_last](elist/Images/.remove_last.0.png)  <br>
├──57. [remove_lastnot](elist/Images/.remove_lastnot.0.png)  <br>
├──58. [remove_which](elist/Images/.remove_which.0.png)  <br>
├──59. [remove_whichnot](elist/Images/.remove_whichnot.0.png)  <br>
├──60. [remove_some](elist/Images/.remove_some.0.png)  <br>
├──61. [remove_somenot](elist/Images/.remove_somenot.0.png)  <br>
├──62. [remove_seqs](elist/Images/.remove_seqs.0.png)  <br>
├──63. [remove_seqsnot](elist/Images/.remove_seqsnot.0.png)  <br>
├──64. [remove_all](elist/Images/.remove_all.0.png)  <br>
├──65. [remove_allnot](elist/Images/.remove_allnot.0.png)  <br>
├──66. [remove_many](elist/Images/.remove_many.0.png)  <br>
├──67. [remove_manynot](elist/Images/.remove_manynot.0.png)  <br>
├──68. [init](elist/Images/init.0.png)  <br>
├──69. [intlize](elist/Images/init.0.png)  <br>
├──70. [strlize](elist/Images/init.0.png)  <br>
├──71. [array_from](elist/Images/array_from.0.png)  <br>
├──72. [array_of](elist/Images/init.0.png)  <br>
├──73. [deepcopy](elist/Images/copy.0.png)  <br>
├──74. [copy_within](elist/Images/copy.0.png)  <br>
├──75. [copyWithin](elist/Images/copy.0.png)  <br>



