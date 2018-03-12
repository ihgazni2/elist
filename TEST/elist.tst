



from elist.elist import *
from xdict.jprint import pobj
from xdict.jprint import pdir

#1. __init__(alist)
l = [1, [4], 2, [3, [5, 6]]]
ltree = ListTree(l)

#2. __repr__
l = [1, [4], 2, [3, [5, 6]]]
ltree = ListTree(l)
l
ltree
pobj(ltree.showlog)


#3. tree(**kwargs)
l = [1, [4], 2, [3, [5, 6]]]
ltree = ListTree(l)
pathlists = ltree.tree()
pathlists
pathlists = ltree.tree(leaf_only=True)
pathlists
pathlists = ltree.tree(leaf_only=True,from_lv=1,to_lv=2)
pathlists
pathlists = ltree.tree(non_leaf_only=True)
pathlists


#4 flatten
l = [1, [4], 2, [3, [5, 6]]]
ltree = ListTree(l)
flat = ltree.flatten()
flat
ltree.flatWidth
ltree.depth

#5. dig
l = [1, [4], 2, [3, [5, 6]]]
ltree = ListTree(l)
depthfirst = ltree.dig()
depthfirst = ltree.dig(2)
depthfirst = ltree.dig(5)


#6. level
l = [1, [4], 2, [3, [5, 6]]]
ltree = ListTree(l)
level = ltree.level(1)
level = ltree.level(1,leaf_only=True)
level = ltree.level(1,non_leaf_only=True)
level = ltree.level(2)
level = ltree.level(3)

#7. include
l = [1, [4], 2, [3, [5, 6]]]
ltree = ListTree(l)
l[3][1][0]
ltree.include(3,1,0)
l[3][1][2]
ltree.include(pathlist = [3,1,2])

#8. __getitem__
l = [1, [4], 2, [3, [5, 6]]]
ltree = ListTree(l)
ltree[1,0]
l[1][0]
ltree[3,1,1]
l[3][1][1]


#9. search

from xdict.TestLib.genrand import gen_random_recursive_only_list_data as randlist
l = randlist()
l = [
 'v_4',
 'v_7',
 'v_6',
 'v_8',
 [
  'v_7',
  'v_1',
  [
   'v_2',
   [
    [
     [
      'v_3',
      'v_6',
      [
       'v_1',
       'v_7',
       [],
       'v_3',
       'v_2',
       'v_8',
       'v_3',
       'v_8',
       'v_8',
       'v_7',
       [],
       'v_6',
       'v_8',
       'v_2'
      ],
      'v_4',
      'v_3',
      'v_2',
      'v_3',
      'v_5',
      'v_3',
      'v_5',
      [
       [],
       'v_1'
      ],
      'v_8',
      'v_4',
      'v_7',
      'v_6',
      [
       'v_4',
       [],
       'v_4',
       'v_2',
       'v_7',
       [],
       'v_5',
       'v_6',
       'v_2',
       'v_1',
       'v_7',
       'v_3',
       []
      ],
      'v_8',
      'v_1',
      'v_1',
      [
       'v_8',
       'v_3',
       [],
       'v_6',
       'v_7',
       'v_2',
       'v_2',
       'v_1',
       'v_5',
       'v_7',
       [],
       'v_4',
       'v_5',
       'v_7',
       'v_7',
       'v_3',
       'v_4',
       'v_5',
       'v_7',
       'v_8'
      ]
     ],
     'v_4',
     'v_5',
     'v_6',
     'v_4',
     'v_3',
     'v_4',
     'v_1',
     'v_2',
     [
      'v_2',
      'v_2',
      'v_8',
      [
       'v_1',
       'v_1',
       'v_2',
       [],
       'v_7',
       'v_4',
       'v_4',
       'v_8',
       'v_6',
       'v_8',
       'v_3',
       'v_5',
       'v_6',
       'v_7'
      ],
      'v_5',
      [
       'v_4',
       'v_7',
       'v_1',
       [],
       'v_8',
       [],
       'v_5',
       'v_6',
       'v_3',
       'v_1',
       'v_6',
       'v_2',
       [],
       'v_5'
      ],
      'v_2',
      'v_7'
     ],
     'v_3',
     'v_4',
     'v_2',
     [
      [
       'v_1',
       'v_3',
       'v_2',
       [],
       []
      ],
      [
       'v_8',
       'v_6',
       'v_6',
       'v_5'
      ],
      'v_8',
      'v_6',
      [
       'v_3',
       'v_8',
       'v_8',
       'v_5',
       'v_6',
       'v_2',
       'v_1',
       'v_4',
       'v_5',
       'v_2',
       'v_2',
       'v_8',
       [],
       'v_8',
       'v_6'
      ],
      'v_4',
      'v_1',
      'v_3',
      'v_4',
      [
       'v_2',
       'v_4',
       'v_6',
       'v_5',
       'v_1'
      ],
      'v_7',
      'v_2',
      'v_6',
      'v_2',
      'v_7',
      'v_6',
      'v_1',
      [
       'v_1',
       [],
       [],
       'v_8',
       'v_1'
      ],
      [
       'v_5',
       'v_6',
       'v_3',
       'v_3',
       'v_5',
       'v_3',
       'v_6',
       'v_5'
      ]
     ],
     [
      'v_5',
      'v_6',
      'v_1',
      'v_7',
      'v_7',
      'v_4',
      'v_7',
      [
       'v_4',
       'v_1',
       'v_8',
       'v_1',
       'v_1',
       'v_2',
       'v_5',
       []
      ],
      'v_5'
     ],
     [
      'v_5',
      'v_7',
      'v_1',
      'v_8'
     ],
     'v_1',
     'v_5',
     'v_4'
    ],
    'v_2',
    'v_7',
    [
     'v_1',
     'v_8',
     'v_6',
     'v_3',
     'v_1',
     [
      'v_5',
      'v_6',
      'v_6',
      [
       'v_5',
       [],
       'v_8',
       [],
       'v_6',
       [],
       'v_1',
       'v_6',
       'v_6',
       'v_1',
       'v_3',
       'v_7',
       'v_7',
       'v_2',
       'v_8',
       'v_7',
       [],
       [],
       'v_1',
       []
      ],
      'v_7',
      'v_4',
      'v_3',
      [
       [],
       'v_1',
       'v_7',
       'v_2',
       'v_1',
       'v_3',
       'v_1',
       'v_1',
       'v_2',
       'v_6',
       'v_8',
       'v_3'
      ]
     ],
     'v_7',
     'v_1',
     'v_4',
     'v_2',
     'v_2',
     'v_7',
     'v_3',
     'v_4',
     [
      'v_3',
      'v_5',
      'v_4',
      'v_8',
      'v_2',
      'v_6',
      'v_4',
      'v_2',
      [
       'v_1'
      ],
      'v_8',
      'v_7',
      'v_5',
      'v_6',
      [
       [],
       [],
       'v_2',
       'v_8',
       [],
       'v_5',
       'v_3',
       'v_8',
       [],
       'v_5'
      ],
      'v_6',
      'v_6',
      'v_8',
      [
       'v_7',
       'v_7',
       'v_3',
       'v_7',
       'v_1',
       'v_8',
       'v_6',
       [],
       'v_4',
       'v_2',
       'v_2',
       'v_3'
      ],
      'v_6'
     ]
    ],
    'v_3',
    'v_1',
    'v_2',
    'v_7',
    'v_8',
    'v_1',
    'v_7',
    'v_4'
   ],
   'v_7',
   'v_1',
   'v_4',
   'v_6'
  ],
  'v_8',
  [
   'v_4',
   'v_2',
   'v_6',
   'v_4'
  ],
  'v_4',
  'v_6',
  'v_4',
  'v_2',
  'v_3',
  'v_5',
  [
   [
    'v_7',
    'v_8',
    'v_7',
    'v_2',
    'v_8',
    'v_2',
    'v_6',
    'v_4',
    'v_6',
    'v_6',
    [
     [
      'v_4',
      'v_5',
      'v_8',
      'v_2',
      [
       'v_1',
       'v_1',
       'v_5',
       [],
       'v_6',
       'v_3',
       'v_3',
       'v_2',
       'v_1',
       'v_1',
       'v_1',
       [],
       'v_4',
       'v_8',
       'v_8'
      ]
     ],
     'v_1',
     'v_1',
     'v_8',
     'v_1',
     'v_2',
     'v_2',
     'v_1',
     'v_1',
     [
      [
       'v_7'
      ],
      'v_4',
      'v_4',
      'v_3',
      [
       [],
       'v_4',
       'v_7',
       'v_1',
       'v_6',
       'v_6'
      ],
      [
       [],
       'v_2',
       'v_8',
       'v_7',
       'v_8',
       'v_5',
       'v_5',
       'v_5',
       'v_6',
       [],
       [],
       'v_6',
       'v_2',
       [],
       'v_7',
       'v_8',
       'v_2'
      ],
      [
       'v_4',
       'v_5',
       [],
       'v_1',
       [],
       'v_1',
       'v_6',
       'v_5',
       'v_3',
       'v_6',
       'v_4',
       'v_2',
       'v_7',
       'v_6',
       'v_3',
       'v_3',
       'v_8',
       'v_3',
       'v_5',
       'v_8'
      ],
      'v_5',
      'v_3',
      'v_7',
      [
       'v_5',
       [],
       'v_2',
       'v_3',
       'v_8',
       'v_5',
       'v_1',
       'v_4',
       'v_5',
       'v_5',
       'v_3',
       'v_4',
       'v_5',
       'v_2',
       [],
       'v_7',
       'v_1',
       'v_1',
       'v_3',
       'v_3'
      ],
      'v_5',
      'v_4',
      'v_1',
      'v_4',
      'v_3',
      'v_3',
      'v_6'
     ],
     'v_1',
     [
      'v_8',
      'v_3',
      'v_5',
      'v_4',
      'v_4',
      'v_6',
      'v_5',
      [
       'v_4',
       'v_6',
       'v_3',
       'v_3'
      ],
      [
       'v_5',
       'v_7',
       'v_3',
       'v_7',
       'v_1',
       'v_4',
       'v_3',
       'v_7',
       'v_5',
       'v_6',
       'v_3',
       'v_6',
       [],
       [],
       'v_6'
      ],
      'v_4',
      'v_3',
      'v_4'
     ],
     'v_8',
     'v_7',
     'v_1',
     'v_8',
     'v_2',
     'v_1',
     'v_2',
     [
      'v_6',
      'v_5',
      'v_2',
      'v_5',
      'v_2',
      'v_7',
      'v_3',
      'v_5',
      'v_2',
      [
       'v_6',
       'v_6',
       'v_8',
       'v_2',
       'v_2',
       'v_2',
       'v_7',
       'v_3',
       'v_5',
       'v_4',
       'v_4',
       'v_5'
      ],
      'v_6'
     ]
    ],
    'v_3',
    'v_5',
    [
     'v_6',
     'v_5',
     [
      'v_4',
      'v_3',
      'v_6',
      'v_7'
     ],
     'v_7',
     'v_3',
     [
      'v_4',
      'v_8',
      'v_8',
      'v_6',
      'v_4',
      'v_6',
      'v_8',
      [
       'v_4',
       'v_8'
      ],
      'v_7',
      'v_3',
      'v_6',
      'v_6',
      'v_3',
      'v_2',
      [
       'v_4',
       [],
       [],
       'v_8',
       'v_3',
       'v_1',
       'v_6',
       'v_4',
       [],
       'v_3',
       'v_8',
       'v_8',
       'v_8',
       [],
       'v_2',
       'v_8'
      ]
     ],
     'v_5',
     'v_8',
     'v_5',
     'v_6',
     'v_8',
     'v_1',
     'v_8',
     'v_2',
     [
      'v_5'
     ]
    ],
    'v_8'
   ],
   'v_8',
   'v_3',
   'v_4',
   'v_2',
   'v_8',
   'v_4',
   'v_8',
   [
    'v_1',
    [
     'v_6',
     'v_8',
     'v_3',
     'v_1',
     [
      'v_4',
      'v_4',
      'v_3',
      'v_4',
      'v_6',
      'v_5',
      'v_7',
      [
       [],
       'v_4',
       'v_5',
       'v_5',
       'v_7',
       'v_8',
       'v_2',
       'v_4',
       'v_7',
       [],
       'v_1',
       'v_1',
       'v_6',
       'v_6'
      ],
      [
       'v_1',
       'v_2',
       'v_1',
       'v_3',
       'v_8',
       'v_7',
       'v_5',
       'v_5',
       'v_1',
       'v_6'
      ],
      'v_6'
     ],
     'v_7',
     'v_8',
     [
      'v_4',
      [
       [],
       'v_8',
       'v_8',
       [],
       'v_6',
       'v_3',
       'v_8',
       'v_3',
       'v_4',
       'v_2',
       [],
       'v_4',
       []
      ],
      [
       'v_8',
       [],
       'v_4',
       'v_7',
       'v_8',
       [],
       'v_5'
      ],
      'v_1',
      'v_4',
      'v_7',
      'v_5',
      [
       'v_5',
       'v_5',
       'v_6',
       'v_8',
       'v_4',
       'v_3',
       'v_7',
       'v_7',
       'v_4',
       'v_6',
       'v_4',
       'v_7',
       'v_3',
       'v_5',
       'v_6'
      ],
      'v_1',
      'v_1',
      'v_4',
      [
       'v_4',
       'v_5',
       'v_7',
       'v_7',
       'v_4',
       [],
       [],
       'v_8',
       'v_1',
       'v_2',
       'v_6',
       [],
       'v_6',
       'v_1'
      ],
      'v_4'
     ],
     [
      'v_5',
      'v_4',
      'v_1',
      [
       'v_1',
       [],
       'v_7',
       'v_1',
       'v_5',
       'v_8',
       [],
       'v_6',
       [],
       'v_2',
       'v_5',
       'v_2',
       'v_6',
       []
      ],
      'v_4',
      'v_5',
      [
       'v_5',
       'v_2',
       'v_4',
       'v_4'
      ],
      'v_2',
      [
       'v_5',
       'v_7',
       'v_3'
      ],
      'v_7',
      'v_7',
      [
       'v_8',
       'v_3'
      ],
      'v_2',
      'v_3',
      'v_3',
      'v_1',
      'v_8',
      'v_3',
      'v_6'
     ],
     'v_1',
     'v_5',
     'v_8',
     'v_3',
     'v_6',
     'v_2'
    ],
    'v_4',
    'v_8',
    'v_4',
    [
     'v_4'
    ],
    'v_5',
    [
     'v_3',
     'v_2',
     [
      [
       'v_5',
       'v_4',
       'v_1',
       'v_7',
       'v_2',
       'v_7',
       'v_2',
       'v_3',
       [],
       [],
       'v_8',
       'v_1',
       'v_7'
      ],
      'v_2',
      'v_7',
      [
       'v_5',
       'v_2',
       'v_8',
       'v_3',
       'v_4',
       'v_3',
       'v_5',
       []
      ],
      'v_5',
      'v_8',
      'v_5',
      [
       [],
       'v_3',
       [],
       [],
       'v_1',
       'v_4',
       'v_2',
       'v_2',
       'v_3',
       'v_7',
       []
      ],
      'v_8',
      'v_5',
      'v_3'
     ],
     'v_2',
     'v_1',
     'v_7',
     'v_6',
     'v_3'
    ],
    'v_3',
    'v_7',
    'v_8',
    'v_4',
    'v_5',
    [
     'v_1',
     'v_3',
     'v_6',
     'v_4',
     [
      'v_5',
      [
       'v_8',
       'v_6',
       [],
       'v_2'
      ],
      'v_5',
      'v_1',
      'v_3',
      'v_2',
      'v_7',
      'v_8',
      [
       'v_8',
       [],
       'v_6',
       'v_4',
       'v_7'
      ]
     ]
    ],
    'v_3',
    [
     'v_3',
     'v_5',
     'v_6',
     'v_7',
     [
      'v_7',
      'v_6',
      'v_1',
      'v_4',
      'v_8'
     ]
    ],
    'v_1'
   ],
   'v_4',
   'v_6',
   'v_3',
   'v_7',
   'v_1',
   'v_8',
   'v_3',
   [
    [
     'v_5',
     'v_3',
     'v_7',
     'v_5',
     [
      [
       'v_2',
       'v_7',
       'v_5',
       'v_4'
      ],
      'v_4',
      [
       'v_2',
       'v_8',
       [],
       'v_2',
       'v_7',
       'v_3',
       'v_7'
      ],
      'v_1'
     ],
     'v_3',
     [
      'v_4',
      'v_1',
      'v_8',
      'v_7',
      'v_1',
      'v_2',
      'v_3',
      [
       [],
       'v_3',
       'v_4',
       'v_2',
       'v_5',
       'v_5',
       'v_7',
       'v_6',
       'v_1',
       'v_1',
       'v_2',
       'v_8',
       [],
       'v_4'
      ],
      'v_1',
      'v_8',
      'v_4',
      'v_8',
      'v_5',
      'v_6',
      [
       [],
       [],
       'v_8',
       'v_8',
       [],
       'v_3',
       'v_4',
       'v_4',
       [],
       'v_4',
       'v_8'
      ],
      'v_4',
      [
       'v_7',
       'v_5',
       'v_3',
       'v_7',
       [],
       'v_1'
      ],
      'v_7'
     ],
     'v_1',
     [
      'v_5',
      'v_7',
      [
       [],
       'v_5',
       'v_6',
       'v_2',
       'v_1',
       'v_3',
       [],
       [],
       'v_5'
      ],
      'v_5',
      'v_3',
      'v_8',
      'v_5',
      'v_7',
      'v_3',
      'v_3',
      'v_2'
     ],
     'v_1',
     [
      'v_5',
      'v_2',
      'v_3',
      [
       'v_6',
       'v_4',
       'v_3',
       'v_1',
       [],
       'v_6',
       'v_5',
       [],
       'v_1',
       'v_6',
       'v_8',
       'v_4',
       'v_7',
       'v_1',
       'v_4'
      ],
      'v_4',
      'v_2',
      'v_7',
      'v_3',
      [
       [],
       []
      ],
      'v_1',
      [
       'v_8',
       'v_2',
       'v_7',
       'v_3',
       'v_4',
       'v_3',
       'v_4',
       'v_7',
       'v_5',
       [],
       'v_6',
       'v_8',
       'v_1',
       []
      ],
      'v_6',
      'v_7',
      'v_2',
      'v_8'
     ],
     [
      'v_4',
      'v_3',
      'v_4',
      'v_3',
      'v_5',
      'v_6',
      'v_7',
      'v_4',
      [
       'v_8',
       'v_5'
      ],
      'v_3',
      'v_8',
      'v_1',
      [
       'v_2',
       'v_5',
       'v_1',
       'v_6',
       'v_8',
       'v_2',
       [],
       'v_5',
       'v_1',
       'v_6',
       'v_8',
       'v_7',
       'v_8',
       'v_8',
       'v_4',
       'v_6'
      ],
      'v_5',
      'v_2',
      'v_5',
      'v_2',
      'v_5'
     ],
     'v_4',
     'v_4',
     [
      [
       'v_4',
       'v_4',
       'v_7'
      ],
      'v_3',
      'v_7',
      [
       []
      ],
      'v_5',
      'v_7',
      'v_3',
      'v_2',
      'v_1',
      'v_8',
      [
       [],
       'v_2',
       'v_3',
       'v_4',
       [],
       'v_4',
       'v_7',
       'v_5',
       'v_5',
       'v_3',
       'v_2'
      ],
      'v_2',
      'v_6',
      'v_1',
      'v_8',
      'v_5',
      [
       'v_7',
       'v_4',
       'v_2',
       'v_3',
       'v_2',
       'v_4',
       'v_8',
       'v_7',
       'v_2'
      ]
     ],
     'v_4'
    ],
    'v_2'
   ],
   'v_7',
   'v_1'
  ],
  [
   'v_1',
   'v_7',
   'v_1',
   'v_6',
   'v_2',
   'v_2',
   'v_5',
   'v_4',
   'v_3',
   'v_3',
   'v_6',
   'v_8'
  ],
  'v_5'
 ],
 'v_3',
 'v_3',
 [
  'v_6'
 ],
 'v_7',
 'v_2',
 'v_3',
 [
  'v_7',
  'v_2',
  'v_4',
  'v_4',
  'v_5',
  'v_8',
  'v_2',
  'v_3',
  'v_1',
  'v_3',
  [
   'v_5',
   'v_2',
   'v_8'
  ]
 ]
]

l = ['v_4', 'v_7', 'v_6', 'v_8', ['v_7', 'v_1', ['v_2', [
        [
            ['v_3', 'v_6', ['v_1', 'v_7', [], 'v_3', 'v_2', 'v_8', 'v_3', 'v_8', 'v_8', 'v_7', [], 'v_6', 'v_8', 'v_2'], 'v_4', 'v_3', 'v_2', 'v_3', 'v_5', 'v_3', 'v_5', [
                [], 'v_1'
            ], 'v_8', 'v_4', 'v_7', 'v_6', ['v_4', [], 'v_4', 'v_2', 'v_7', [], 'v_5', 'v_6', 'v_2', 'v_1', 'v_7', 'v_3', []], 'v_8', 'v_1', 'v_1', ['v_8', 'v_3', [], 'v_6', 'v_7', 'v_2', 'v_2', 'v_1', 'v_5', 'v_7', [], 'v_4', 'v_5', 'v_7', 'v_7', 'v_3', 'v_4', 'v_5', 'v_7', 'v_8']], 'v_4', 'v_5', 'v_6', 'v_4', 'v_3', 'v_4', 'v_1', 'v_2', ['v_2', 'v_2', 'v_8', ['v_1', 'v_1', 'v_2', [], 'v_7', 'v_4', 'v_4', 'v_8', 'v_6', 'v_8', 'v_3', 'v_5', 'v_6', 'v_7'], 'v_5', ['v_4', 'v_7', 'v_1', [], 'v_8', [], 'v_5', 'v_6', 'v_3', 'v_1', 'v_6', 'v_2', [], 'v_5'], 'v_2', 'v_7'], 'v_3', 'v_4', 'v_2', [
                ['v_1', 'v_3', 'v_2', [],
                    []
                ],
                ['v_8', 'v_6', 'v_6', 'v_5'], 'v_8', 'v_6', ['v_3', 'v_8', 'v_8', 'v_5', 'v_6', 'v_2', 'v_1', 'v_4', 'v_5', 'v_2', 'v_2', 'v_8', [], 'v_8', 'v_6'], 'v_4', 'v_1', 'v_3', 'v_4', ['v_2', 'v_4', 'v_6', 'v_5', 'v_1'], 'v_7', 'v_2', 'v_6', 'v_2', 'v_7', 'v_6', 'v_1', ['v_1', [],
                    [], 'v_8', 'v_1'
                ],
                ['v_5', 'v_6', 'v_3', 'v_3', 'v_5', 'v_3', 'v_6', 'v_5']
            ],
            ['v_5', 'v_6', 'v_1', 'v_7', 'v_7', 'v_4', 'v_7', ['v_4', 'v_1', 'v_8', 'v_1', 'v_1', 'v_2', 'v_5', []], 'v_5'],
            ['v_5', 'v_7', 'v_1', 'v_8'], 'v_1', 'v_5', 'v_4'
        ], 'v_2', 'v_7', ['v_1', 'v_8', 'v_6', 'v_3', 'v_1', ['v_5', 'v_6', 'v_6', ['v_5', [], 'v_8', [], 'v_6', [], 'v_1', 'v_6', 'v_6', 'v_1', 'v_3', 'v_7', 'v_7', 'v_2', 'v_8', 'v_7', [],
            [], 'v_1', []
        ], 'v_7', 'v_4', 'v_3', [
            [], 'v_1', 'v_7', 'v_2', 'v_1', 'v_3', 'v_1', 'v_1', 'v_2', 'v_6', 'v_8', 'v_3'
        ]], 'v_7', 'v_1', 'v_4', 'v_2', 'v_2', 'v_7', 'v_3', 'v_4', ['v_3', 'v_5', 'v_4', 'v_8', 'v_2', 'v_6', 'v_4', 'v_2', ['v_1'], 'v_8', 'v_7', 'v_5', 'v_6', [
            [],
            [], 'v_2', 'v_8', [], 'v_5', 'v_3', 'v_8', [], 'v_5'
        ], 'v_6', 'v_6', 'v_8', ['v_7', 'v_7', 'v_3', 'v_7', 'v_1', 'v_8', 'v_6', [], 'v_4', 'v_2', 'v_2', 'v_3'], 'v_6']], 'v_3', 'v_1', 'v_2', 'v_7', 'v_8', 'v_1', 'v_7', 'v_4'
    ], 'v_7', 'v_1', 'v_4', 'v_6'], 'v_8', ['v_4', 'v_2', 'v_6', 'v_4'], 'v_4', 'v_6', 'v_4', 'v_2', 'v_3', 'v_5', [
        ['v_7', 'v_8', 'v_7', 'v_2', 'v_8', 'v_2', 'v_6', 'v_4', 'v_6', 'v_6', [
            ['v_4', 'v_5', 'v_8', 'v_2', ['v_1', 'v_1', 'v_5', [], 'v_6', 'v_3', 'v_3', 'v_2', 'v_1', 'v_1', 'v_1', [], 'v_4', 'v_8', 'v_8']], 'v_1', 'v_1', 'v_8', 'v_1', 'v_2', 'v_2', 'v_1', 'v_1', [
                ['v_7'], 'v_4', 'v_4', 'v_3', [
                    [], 'v_4', 'v_7', 'v_1', 'v_6', 'v_6'
                ],
                [
                    [], 'v_2', 'v_8', 'v_7', 'v_8', 'v_5', 'v_5', 'v_5', 'v_6', [],
                    [], 'v_6', 'v_2', [], 'v_7', 'v_8', 'v_2'
                ],
                ['v_4', 'v_5', [], 'v_1', [], 'v_1', 'v_6', 'v_5', 'v_3', 'v_6', 'v_4', 'v_2', 'v_7', 'v_6', 'v_3', 'v_3', 'v_8', 'v_3', 'v_5', 'v_8'], 'v_5', 'v_3', 'v_7', ['v_5', [], 'v_2', 'v_3', 'v_8', 'v_5', 'v_1', 'v_4', 'v_5', 'v_5', 'v_3', 'v_4', 'v_5', 'v_2', [], 'v_7', 'v_1', 'v_1', 'v_3', 'v_3'], 'v_5', 'v_4', 'v_1', 'v_4', 'v_3', 'v_3', 'v_6'
            ], 'v_1', ['v_8', 'v_3', 'v_5', 'v_4', 'v_4', 'v_6', 'v_5', ['v_4', 'v_6', 'v_3', 'v_3'],
                ['v_5', 'v_7', 'v_3', 'v_7', 'v_1', 'v_4', 'v_3', 'v_7', 'v_5', 'v_6', 'v_3', 'v_6', [],
                    [], 'v_6'
                ], 'v_4', 'v_3', 'v_4'
            ], 'v_8', 'v_7', 'v_1', 'v_8', 'v_2', 'v_1', 'v_2', ['v_6', 'v_5', 'v_2', 'v_5', 'v_2', 'v_7', 'v_3', 'v_5', 'v_2', ['v_6', 'v_6', 'v_8', 'v_2', 'v_2', 'v_2', 'v_7', 'v_3', 'v_5', 'v_4', 'v_4', 'v_5'], 'v_6']
        ], 'v_3', 'v_5', ['v_6', 'v_5', ['v_4', 'v_3', 'v_6', 'v_7'], 'v_7', 'v_3', ['v_4', 'v_8', 'v_8', 'v_6', 'v_4', 'v_6', 'v_8', ['v_4', 'v_8'], 'v_7', 'v_3', 'v_6', 'v_6', 'v_3', 'v_2', ['v_4', [],
            [], 'v_8', 'v_3', 'v_1', 'v_6', 'v_4', [], 'v_3', 'v_8', 'v_8', 'v_8', [], 'v_2', 'v_8'
        ]], 'v_5', 'v_8', 'v_5', 'v_6', 'v_8', 'v_1', 'v_8', 'v_2', ['v_5']], 'v_8'], 'v_8', 'v_3', 'v_4', 'v_2', 'v_8', 'v_4', 'v_8', ['v_1', ['v_6', 'v_8', 'v_3', 'v_1', ['v_4', 'v_4', 'v_3', 'v_4', 'v_6', 'v_5', 'v_7', [
                    [], 'v_4', 'v_5', 'v_5', 'v_7', 'v_8', 'v_2', 'v_4', 'v_7', [], 'v_1', 'v_1', 'v_6', 'v_6'
                ],
                ['v_1', 'v_2', 'v_1', 'v_3', 'v_8', 'v_7', 'v_5', 'v_5', 'v_1', 'v_6'], 'v_6'
            ], 'v_7', 'v_8', ['v_4', [
                    [], 'v_8', 'v_8', [], 'v_6', 'v_3', 'v_8', 'v_3', 'v_4', 'v_2', [], 'v_4', []
                ],
                ['v_8', [], 'v_4', 'v_7', 'v_8', [], 'v_5'], 'v_1', 'v_4', 'v_7', 'v_5', ['v_5', 'v_5', 'v_6', 'v_8', 'v_4', 'v_3', 'v_7', 'v_7', 'v_4', 'v_6', 'v_4', 'v_7', 'v_3', 'v_5', 'v_6'], 'v_1', 'v_1', 'v_4', ['v_4', 'v_5', 'v_7', 'v_7', 'v_4', [],
                    [], 'v_8', 'v_1', 'v_2', 'v_6', [], 'v_6', 'v_1'
                ], 'v_4'
            ],
            ['v_5', 'v_4', 'v_1', ['v_1', [], 'v_7', 'v_1', 'v_5', 'v_8', [], 'v_6', [], 'v_2', 'v_5', 'v_2', 'v_6', []], 'v_4', 'v_5', ['v_5', 'v_2', 'v_4', 'v_4'], 'v_2', ['v_5', 'v_7', 'v_3'], 'v_7', 'v_7', ['v_8', 'v_3'], 'v_2', 'v_3', 'v_3', 'v_1', 'v_8', 'v_3', 'v_6'], 'v_1', 'v_5', 'v_8', 'v_3', 'v_6', 'v_2'
        ], 'v_4', 'v_8', 'v_4', ['v_4'], 'v_5', ['v_3', 'v_2', [
            ['v_5', 'v_4', 'v_1', 'v_7', 'v_2', 'v_7', 'v_2', 'v_3', [],
                [], 'v_8', 'v_1', 'v_7'
            ], 'v_2', 'v_7', ['v_5', 'v_2', 'v_8', 'v_3', 'v_4', 'v_3', 'v_5', []], 'v_5', 'v_8', 'v_5', [
                [], 'v_3', [],
                [], 'v_1', 'v_4', 'v_2', 'v_2', 'v_3', 'v_7', []
            ], 'v_8', 'v_5', 'v_3'
        ], 'v_2', 'v_1', 'v_7', 'v_6', 'v_3'], 'v_3', 'v_7', 'v_8', 'v_4', 'v_5', ['v_1', 'v_3', 'v_6', 'v_4', ['v_5', ['v_8', 'v_6', [], 'v_2'], 'v_5', 'v_1', 'v_3', 'v_2', 'v_7', 'v_8', ['v_8', [], 'v_6', 'v_4', 'v_7']]], 'v_3', ['v_3', 'v_5', 'v_6', 'v_7', ['v_7', 'v_6', 'v_1', 'v_4', 'v_8']], 'v_1'], 'v_4', 'v_6', 'v_3', 'v_7', 'v_1', 'v_8', 'v_3', [
            ['v_5', 'v_3', 'v_7', 'v_5', [
                    ['v_2', 'v_7', 'v_5', 'v_4'], 'v_4', ['v_2', 'v_8', [], 'v_2', 'v_7', 'v_3', 'v_7'], 'v_1'
                ], 'v_3', ['v_4', 'v_1', 'v_8', 'v_7', 'v_1', 'v_2', 'v_3', [
                    [], 'v_3', 'v_4', 'v_2', 'v_5', 'v_5', 'v_7', 'v_6', 'v_1', 'v_1', 'v_2', 'v_8', [], 'v_4'
                ], 'v_1', 'v_8', 'v_4', 'v_8', 'v_5', 'v_6', [
                    [],
                    [], 'v_8', 'v_8', [], 'v_3', 'v_4', 'v_4', [], 'v_4', 'v_8'
                ], 'v_4', ['v_7', 'v_5', 'v_3', 'v_7', [], 'v_1'], 'v_7'], 'v_1', ['v_5', 'v_7', [
                    [], 'v_5', 'v_6', 'v_2', 'v_1', 'v_3', [],
                    [], 'v_5'
                ], 'v_5', 'v_3', 'v_8', 'v_5', 'v_7', 'v_3', 'v_3', 'v_2'], 'v_1', ['v_5', 'v_2', 'v_3', ['v_6', 'v_4', 'v_3', 'v_1', [], 'v_6', 'v_5', [], 'v_1', 'v_6', 'v_8', 'v_4', 'v_7', 'v_1', 'v_4'], 'v_4', 'v_2', 'v_7', 'v_3', [
                    [],
                    []
                ], 'v_1', ['v_8', 'v_2', 'v_7', 'v_3', 'v_4', 'v_3', 'v_4', 'v_7', 'v_5', [], 'v_6', 'v_8', 'v_1', []], 'v_6', 'v_7', 'v_2', 'v_8'],
                ['v_4', 'v_3', 'v_4', 'v_3', 'v_5', 'v_6', 'v_7', 'v_4', ['v_8', 'v_5'], 'v_3', 'v_8', 'v_1', ['v_2', 'v_5', 'v_1', 'v_6', 'v_8', 'v_2', [], 'v_5', 'v_1', 'v_6', 'v_8', 'v_7', 'v_8', 'v_8', 'v_4', 'v_6'], 'v_5', 'v_2', 'v_5', 'v_2', 'v_5'], 'v_4', 'v_4', [
                    ['v_4', 'v_4', 'v_7'], 'v_3', 'v_7', [
                        []
                    ], 'v_5', 'v_7', 'v_3', 'v_2', 'v_1', 'v_8', [
                        [], 'v_2', 'v_3', 'v_4', [], 'v_4', 'v_7', 'v_5', 'v_5', 'v_3', 'v_2'
                    ], 'v_2', 'v_6', 'v_1', 'v_8', 'v_5', ['v_7', 'v_4', 'v_2', 'v_3', 'v_2', 'v_4', 'v_8', 'v_7', 'v_2']
                ], 'v_4'
            ], 'v_2'
        ], 'v_7', 'v_1'
    ],
    ['v_1', 'v_7', 'v_1', 'v_6', 'v_2', 'v_2', 'v_5', 'v_4', 'v_3', 'v_3', 'v_6', 'v_8'], 'v_5'
], 'v_3', 'v_3', ['v_6'], 'v_7', 'v_2', 'v_3', ['v_7', 'v_2', 'v_4', 'v_4', 'v_5', 'v_8', 'v_2', 'v_3', 'v_1', 'v_3', ['v_5', 'v_2', 'v_8']]]

from xdict.TestLib.genrand import gen_random_recursive_only_list_data as randlist
l = randlist()
ltree = ListTree(l)
pathlists = ltree.search('v_4')

pathlists.__len__()
l[0]
l[4][2][1][0][0][3]
l[4][2][1][0][0][19][11]
l[11][3]

#cond_search

pl1=ltree.search('v_4')
pl1.__len__() 
#we found 125 match of "v_4"
pl2=ltree.search('v_8')
pl2.__len__()
#we found 117 match of "v_8"

#the next we need to found "v_4" or "v_8" whose pathlist includes <14>, and the <14> appears at index <4> in the pathlist
def cond_func(ele_value,ele_pathlist,position):
    cond1 = ("4" in ele_value) | ("8" in ele_value)
    cond2 = (14 in ele_pathlist)
    cond3 = False
    if(cond2):
        cond3 = (ele_pathlist.index(14) == position)
    else:
        pass
    return(cond1 & cond2 & cond3)

position = 4

pl = ltree.cond_search(cond_func=cond_func,cond_func_args=[position])


#lquery
#ancestors
l = [1, [4], 2, [3, [5, 6]]]
ltree = ListTree(l)
ltree
ltree.ancestor_paths(3,1,0)
ltree.ancestors(3,1,0)
l[3]
l[3][1]

#parent
l = [1, [4], 2, [3, [5, 6]]]
ltree = ListTree(l)
ltree
ltree.parent_path(3,1,0)
ltree.parent(3,1,0)
l[3][1]


#descendants
l = [1, [4], 2, [3, [5, 6]]]
ltree = ListTree(l)
ltree
ltree.descendant_paths(3)
ltree.descendants(3)
ltree.descendant_paths(3,leaf_only=True)
ltree.descendants(3,leaf_only=True)
ltree.descendant_paths(3,non_leaf_only=True)
ltree.descendants(3,non_leaf_only=True)
l[3][1]


#prevSib
l = [1, [4], 2, [3, [5, 6]]]
ltree = ListTree(l)
ltree
# ltree.lsib_path
ltree.prevSibPath(3,1,1)
# ltree.lsib
ltree.prevSibling(3,1,1)
ltree.prevSibPath(3,1,0) == None
#l[3][1][0] has no left sibling





#nextSib
l = [1, [4], 2, [3, [5, 6]]]
ltree = ListTree(l)
ltree
# ltree.rsib_path
ltree.nextSibPath(3,1,0)
# ltree.rsib
ltree.nextSibling(3,1,0)
ltree.nextSibPath(3,1,1) == None
#l[3][1][1] has no right sibling


#sibs

l = [1, [4], 2, [3, [5, 6],7,[8,9]]]
ltree = ListTree(l)
ltree
ltree.sib_paths(3,1)
ltree.sibs(3,1)
ltree.sib_paths(3,1,leaf_only=True)
ltree.sibs(3,1,leaf_only=True)
ltree.sib_paths(3,1,non_leaf_only=True)
ltree.sibs(3,1,non_leaf_only=True)

#some_sibs
l = [1, [4], 2, [3, [5, 6],7,[8,9]]]
ltree = ListTree(l)
ltree
#ltree.some_sib_paths
ltree.someSibPaths(3,1,some=[0,3])
#ltree.some_sibs
ltree.someSibs(3,1,some=[0,3])

ltree.someSibPaths(3,1,some=[0,3],leaf_only=True)
ltree.someSibs(3,1,some=[0,3],leaf_only=True)
ltree.someSibPaths(3,1,some=[0,3],non_leaf_only=True)
ltree.someSibs(3,1,some=[0,3],non_leaf_only=True)



#whichSib
l = [1, [4], 2, [3, [5, 6],7,[8,9]]]
ltree = ListTree(l)
ltree
#ltree.which_sib_path
ltree.whichSibPath(3,1,which=2)
#ltree.which_sib
ltree.whichSib(3,1,which=2)

ltree.whichSibPath(3,1,which=1,leaf_only=True)
ltree.whichSib(3,1,which=1,leaf_only=True)
ltree.whichSibPath(3,1,which=1,non_leaf_only=True)
ltree.whichSib(3,1,which=1,non_leaf_only=True)


#precedingSibs
l = [1, [4], 2, [3, [5, 6],7,[8,9]]]
ltree = ListTree(l)
ltree
#ltree.preceding_sib_paths
ltree.precedingSibPaths(3,1)
#ltree.preceding_sibs
ltree.precedingSibs(3,1)

ltree.precedingSibPaths(3,1,leaf_only=True)
ltree.precedingSibs(3,1,leaf_only=True)
ltree.precedingSibPaths(3,1,non_leaf_only=True)
ltree.precedingSibs(3,1,non_leaf_only=True)


#followingSibs
l = [1, [4], 2, [3, [5, 6],7,[8,9]]]
ltree = ListTree(l)
ltree
#ltree.following_sib_paths
ltree.followingSibPaths(3,1)
#ltree.following_sibs
ltree.followingSibs(3,1)

ltree.followingSibPaths(3,1,leaf_only=True)
ltree.followingSibs(3,1,leaf_only=True)
ltree.followingSibPaths(3,1,non_leaf_only=True)
ltree.followingSibs(3,1,non_leaf_only=True)




# lcin 
l = [1, [4], 2, [3, [5, 6],[8,9],7]]
ltree = ListTree(l)
ltree
ltree.lcin_path(3,2,0)
l[3][1][1]
ltree.lcin(3,2,0)
l[3][2][0]

#rcin
l = [1, [4], 2, [3, [5, 6],[8,9],7]]
ltree = ListTree(l)
ltree
ltree.rcin_path(3,1,1)
l[3][2][0]
ltree.rcin(3,1,1)
l[3][1][1]

#sons
l = [1, [4], 2, [3, [5, 6],[8,9],7]]
ltree = ListTree(l)
ltree
ltree.son_paths(3)
ltree.sons(3)
ltree.son_paths(3,leaf_only=True)
ltree.sons(3,leaf_only=True)
ltree.son_paths(3,non_leaf_only=True)
ltree.sons(3,non_leaf_only=True)


#PARAMS
l = [1, [4], 2, [3, [5, 6],[8,9],7]]
ltree = ListTree(l)
ltree
ltree.depth
ltree.total
ltree.flatWidth
ltree.maxLevelWidth









#cond_remove_seqs
from elist.elist import *
ol = [1,'X',3,'b',5,'c',6,'A',7,'b',8,'B',9]
id(ol)

def afterCH(ele,ch):
    cond = (ord(str(ele)) > ord(ch))
    return(cond)

new = cond_remove_seqs(ol,[0,2],cond_func=afterCH,cond_func_args=['B'])
ol
new
id(ol)
id(new)
####
ol = [1,'X',3,'b',5,'c',6,'A',7,'b',8,'B',9]
id(ol)
rslt = cond_remove_seqs(ol,[0,2],cond_func=afterCH,cond_func_args=['B'],mode='original')
ol
rslt
id(ol)
id(rslt)


#cond_remove_some
from elist.elist import *
ol = [1,'X',3,'b',5,'c',6,'A',7,'b',8,'B',9]
id(ol)

def afterCH(ele,ch):
    cond = (ord(str(ele)) > ord(ch))
    return(cond)

new = cond_remove_some(ol,0,2,cond_func=afterCH,cond_func_args=['B'])
ol
new
id(ol)
id(new)
####
ol = [1,'X',3,'b',5,'c',6,'A',7,'b',8,'B',9]
id(ol)
rslt = cond_remove_some(ol,0,2,cond_func=afterCH,cond_func_args=['B'],mode='original')
ol
rslt
id(ol)
id(rslt)


#cond_remove_all        
from elist.elist import *
ol = [1,'X',3,'b',5,'c',6,'A',7,'b',8,'B',9]
id(ol)
def afterCH(ele,ch):
    cond = (ord(str(ele)) > ord(ch))
    return(cond)

new = cond_remove_all(ol,cond_func=afterCH,cond_func_args=['B'])
ol
new
id(ol)
id(new)
####
ol = [1,'X',3,'b',5,'c',6,'A',7,'b',8,'B',9]
id(ol)
rslt = cond_remove_all(ol,cond_func=afterCH,cond_func_args=['B'],mode='original')
ol
rslt
id(ol)
id(rslt)







#cond_replace_value_all

from elist.elist import *
ol = [1,'X',3,'b',5,'c',6,'A',7,'b',8,'B',9]
id(ol)
def afterCH(ele,ch):
    cond = (ord(str(ele)) > ord(ch))
    return(cond)

new = cond_replace_value_all(ol,"REPLACED",cond_func=afterCH,cond_func_args=['B'])
ol
new
id(ol)
id(new)
####
ol = [1,'X',3,'b',5,'c',6,'A',7,'b',8,'B',9]
id(ol)
rslt = cond_replace_value_all(ol,"REPLACED",cond_func=afterCH,cond_func_args=['B'],mode="original")
ol
rslt
id(ol)
id(rslt)


# >>> #cond_replace_value_all
# ...
# >>> from elist.elist import *
# >>> ol = [1,'X',3,'b',5,'c',6,'A',7,'b',8,'B',9]
# >>> id(ol)
# 139927002027016
# >>> def afterCH(ele,ch):
# ...     cond = (ord(str(ele)) > ord(ch))
# ...     return(cond)
# ...
# >>> new = cond_replace_value_all(ol,"REPLACED",cond_func=afterCH,cond_func_args=['B'])
# >>> ol
# [1, 'X', 3, 'b', 5, 'c', 6, 'A', 7, 'b', 8, 'B', 9]
# >>> new
# [1, 'REPLACED', 3, 'REPLACED', 5, 'REPLACED', 6, 'A', 7, 'REPLACED', 8, 'B', 9]
# >>> id(ol)
# 139927002027016
# >>> id(new)
# 139927014765896
# >>> ####
# ... ol = [1,'X',3,'b',5,'c',6,'A',7,'b',8,'B',9]
# >>> id(ol)
# 139927002026184
# >>> rslt = cond_replace_value_all(ol,"REPLACED",cond_func=afterCH,cond_func_args=['B'],                                   mode="original")
# >>> ol
# [1, 'REPLACED', 3, 'REPLACED', 5, 'REPLACED', 6, 'A', 7, 'REPLACED', 8, 'B', 9]
# >>> rslt
# [1, 'REPLACED', 3, 'REPLACED', 5, 'REPLACED', 6, 'A', 7, 'REPLACED', 8, 'B', 9]
# >>> id(ol)
# 139927002026184
# >>> id(rslt)
# 139927002026184


from elist.elist import *
ol = [1,'X',3,'b',5,'c',6,'A',7,'b',8,'B',9]
id(ol)
def afterCH(ele,ch):
    cond = (ord(str(ele)) > ord(ch))
    return(cond)

new = cond_replace_value_seqs(ol,"REPLACED",[0,2],cond_func=afterCH,cond_func_args=['B'])
ol
new
id(ol)
id(new)
####
ol = [1,'X',3,'b',5,'c',6,'A',7,'b',8,'B',9]
id(ol)
rslt = cond_replace_value_seqs(ol,"REPLACED",[0,2],cond_func=afterCH,cond_func_args=['B'],mode="original")
ol
rslt
id(ol)
id(rslt)


# >>>
# >>> from elist.elist import *
# >>> ol = [1,'X',3,'b',5,'c',6,'A',7,'b',8,'B',9]
# >>> id(ol)
# 139927002027016
# >>> def afterCH(ele,ch):
# ...     cond = (ord(str(ele)) > ord(ch))
# ...     return(cond)
# ...
# >>> new = cond_replace_value_seqs(ol,"REPLACED",[0,2],cond_func=afterCH,cond_func_args=['B'])
# id(new)
# >>> ol
# [1, 'X', 3, 'b', 5, 'c', 6, 'A', 7, 'b', 8, 'B', 9]
# >>> new
# [1, 'REPLACED', 3, 'b', 5, 'REPLACED', 6, 'A', 7, 'b', 8, 'B', 9]
# >>> id(ol)
# 139927002027016
# >>> id(new)
# 139927002026312
# >>> ####
# ... ol = [1,'X',3,'b',5,'c',6,'A',7,'b',8,'B',9]
# >>> id(ol)
# 139927014765896
# >>> rslt = cond_replace_value_seqs(ol,"REPLACED",[0,2],cond_func=afterCH,cond_func_args=['B'],mode="original")
# >>> ol
# [1, 'REPLACED', 3, 'b', 5, 'REPLACED', 6, 'A', 7, 'b', 8, 'B', 9]
# >>> rslt
# [1, 'REPLACED', 3, 'b', 5, 'REPLACED', 6, 'A', 7, 'b', 8, 'B', 9]
# >>> id(ol)
# 139927014765896
# >>> id(rslt)
# 139927014765896
# >>>


from elist.elist import *
ol = [1,'X',3,'b',5,'c',6,'A',7,'b',8,'B',9]
id(ol)
def afterCH(ele,ch):
    cond = (ord(str(ele)) > ord(ch))
    return(cond)

new = cond_replace_value_some(ol,"REPLACED",0,2,cond_func=afterCH,cond_func_args=['B'])
ol
new
id(ol)
id(new)
####
ol = [1,'X',3,'b',5,'c',6,'A',7,'b',8,'B',9]
id(ol)
rslt = cond_replace_value_some(ol,"REPLACED",0,2,cond_func=afterCH,cond_func_args=['B'],mode="original")
ol
rslt
id(ol)
id(rslt)

# >>>
# >>> from elist.elist import *
# >>> ol = [1,'X',3,'b',5,'c',6,'A',7,'b',8,'B',9]
# >>> id(ol)
# 139927002028680
# >>> def afterCH(ele,ch):
# ...     cond = (ord(str(ele)) > ord(ch))
# ...     return(cond)
# ...
# >>> new = cond_replace_value_some(ol,"REPLACED",0,2,cond_func=afterCH,cond_func_args=['B'])
# >>> ol
# [1, 'X', 3, 'b', 5, 'c', 6, 'A', 7, 'b', 8, 'B', 9]
# >>> new
# [1, 'REPLACED', 3, 'b', 5, 'REPLACED', 6, 'A', 7, 'b', 8, 'B', 9]
# >>> id(ol)
# 139927002028680
# >>> id(new)
# 139927002028168
# >>> ####
# ... ol = [1,'X',3,'b',5,'c',6,'A',7,'b',8,'B',9]
# >>> id(ol)
# 139927002027784
# >>> rslt = cond_replace_value_some(ol,"REPLACED",0,2,cond_func=afterCH,cond_func_args=['B'],mode="original")
# >>> ol
# [1, 'REPLACED', 3, 'b', 5, 'REPLACED', 6, 'A', 7, 'b', 8, 'B', 9]
# >>> rslt
# [1, 'REPLACED', 3, 'b', 5, 'REPLACED', 6, 'A', 7, 'b', 8, 'B', 9]
# >>> id(ol)
# 139927002027784
# >>> id(rslt)
# 139927002027784
# >>>
# >>>





