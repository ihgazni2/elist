



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

#verify
l[4][2][1][0][14][5]
l[4][2][1][0][14][7][2]
l[4][11][16][0][14][16][5]
l[4][11][16][0][14][16][6]

pobj(ltree.showlog)







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


#select_seqs
ol = ['a','b','c','d']
select_some(ol,[1,2])

#select_some
ol = ['a','b','c','d']
select_seqs(ol,1,2)

#append
ol = [1,2,3,4]
ele = 5
id(ol)
append(ol,ele,mode="original")
ol
id(ol)
####
ol = [1,2,3,4]
ele = 5
id(ol)
new = append(ol,ele)
new
id(new)


#append_some

ol = [1,2,3,4]
id(ol)
append_some(ol,5,6,7,8,mode="original")
ol
id(ol)
####
ol = [1,2,3,4]
id(ol)
new = append_some(ol,5,6,7,8)
new
id(new)












####################################
def text_extend():
    expected = [1,2,3,4,5,6,7,8]
    ol = [1,2,3,4]
    nl = [5,6,7,8]
    id_1 = id(ol)
    extend(ol,nl,mode="original")
    id_2 = id(ol)
    ol = [1,2,3,4]
    nl = [5,6,7,8]
    id_o = id(ol)
    new = extend(ol,nl)
    id_n = id(new)
    cond_1 = (ol == expected)
    cond_2 = (id_2 == id_1)
    cond_3 = (new == expected)
    cond_4 = not(id_n == id_o)
    print(cond_1)
    print(cond_2)
    print(cond_3)
    print(cond_4)


def test_scan():
    l = [1, 2, [4], [3, [5, 6]]]
    m = [[{'rsib_path': None, 'lcin_path': None, 'depth': 0, 'lsib_path': None, 'parent_path': [], 'sib_seq': None, 'breadth_path': [], 'path': [], 'non_leaf_son_paths': [[2], [3]], 'rcin_path': None, 'sons_count': 4, 'parent_breadth_path': [], 'flat_len': None, 'non_leaf_descendant_paths': [[2], [3]], 'leaf_son_paths': [[0], [1]], 'breadth': None, 'leaf': False, 'flat_offset': None, 'leaf_descendant_paths': [[0], [1]]}], [{'rsib_path': [1], 'lcin_path': None, 'depth': 1, 'lsib_path': None, 'parent_path': [], 'sib_seq': 0, 'breadth_path': [0], 'path': [0], 'non_leaf_son_paths': None, 'rcin_path': None, 'sons_count': 0, 'parent_breadth_path': [], 'flat_len': None, 'non_leaf_descendant_paths': None, 'leaf_son_paths': None, 'breadth': 0, 'leaf': True, 'flat_offset': None, 'leaf_descendant_paths': None}, {'rsib_path': [2], 'lcin_path': None, 'depth': 1, 'lsib_path': [0], 'parent_path': [], 'sib_seq': 1, 'breadth_path': [1], 'path': [1], 'non_leaf_son_paths': None, 'rcin_path': None, 'sons_count': 0, 'parent_breadth_path': [], 'flat_len': None, 'non_leaf_descendant_paths': None, 'leaf_son_paths': None, 'breadth': 1, 'leaf': True, 'flat_offset': None, 'leaf_descendant_paths': None}, {'rsib_path': [3], 'lcin_path': None, 'depth': 1, 'lsib_path': [1], 'parent_path': [], 'sib_seq': 2, 'breadth_path': [2], 'path': [2], 'non_leaf_son_paths': [], 'rcin_path': None, 'sons_count': 1, 'parent_breadth_path': [], 'flat_len': None, 'non_leaf_descendant_paths': [], 'leaf_son_paths': [[2, 0]], 'breadth': 2, 'leaf': False, 'flat_offset': None, 'leaf_descendant_paths': [[2, 0]]}, {'rsib_path': None, 'lcin_path': None, 'depth': 1, 'lsib_path': [2], 'parent_path': [], 'sib_seq': 3, 'breadth_path': [3], 'path': [3], 'non_leaf_son_paths': [[3, 1]], 'rcin_path': None, 'sons_count': 2, 'parent_breadth_path': [], 'flat_len': None, 'non_leaf_descendant_paths': [[3, 1]], 'leaf_son_paths': [[3, 0]], 'breadth': 3, 'leaf': False, 'flat_offset': None, 'leaf_descendant_paths': [[3, 0]]}], [{'rsib_path': None, 'lcin_path': None, 'depth': 2, 'lsib_path': None, 'parent_path': [2], 'sib_seq': 0, 'breadth_path': [2, 0], 'path': [2, 0], 'non_leaf_son_paths': None, 'rcin_path': [3, 0], 'sons_count': 0, 'parent_breadth_path': [2], 'flat_len': None, 'non_leaf_descendant_paths': None, 'leaf_son_paths': None, 'breadth': 0, 'leaf': True, 'flat_offset': None, 'leaf_descendant_paths': None}, {'rsib_path': [3, 1], 'lcin_path': [2, 0], 'depth': 2, 'lsib_path': None, 'parent_path': [3], 'sib_seq': 0, 'breadth_path': [3, 1], 'path': [3, 0], 'non_leaf_son_paths': None, 'rcin_path': None, 'sons_count': 0, 'parent_breadth_path': [3], 'flat_len': None, 'non_leaf_descendant_paths': None, 'leaf_son_paths': None, 'breadth': 1, 'leaf': True, 'flat_offset': None, 'leaf_descendant_paths': None}, {'rsib_path': None, 'lcin_path': None, 'depth': 2, 'lsib_path': [3, 0], 'parent_path': [3], 'sib_seq': 1, 'breadth_path': [3, 2], 'path': [3, 1], 'non_leaf_son_paths': [], 'rcin_path': None, 'sons_count': 2, 'parent_breadth_path': [3], 'flat_len': None, 'non_leaf_descendant_paths': [], 'leaf_son_paths': [[3, 1, 0], [3, 1, 1]], 'breadth': 2, 'leaf': False, 'flat_offset': None, 'leaf_descendant_paths': [[3, 1, 0], [3, 1, 1]]}], [{'rsib_path': [3, 1, 1], 'lcin_path': None, 'depth': 3, 'lsib_path': None, 'parent_path': [3, 1], 'sib_seq': 0, 'breadth_path': [3, 2, 0], 'path': [3, 1, 0], 'non_leaf_son_paths': None, 'rcin_path': None, 'sons_count': 0, 'parent_breadth_path': [3, 2], 'flat_len': None, 'non_leaf_descendant_paths': None, 'leaf_son_paths': None, 'breadth': 0, 'leaf': True, 'flat_offset': None, 'leaf_descendant_paths': None}, {'rsib_path': None, 'lcin_path': None, 'depth': 3, 'lsib_path': [3, 1, 0], 'parent_path': [3, 1], 'sib_seq': 1, 'breadth_path': [3, 2, 1], 'path': [3, 1, 1], 'non_leaf_son_paths': None, 'rcin_path': None, 'sons_count': 0, 'parent_breadth_path': [3, 2], 'flat_len': None, 'non_leaf_descendant_paths': None, 'leaf_son_paths': None, 'breadth': 1, 'leaf': True, 'flat_offset': None, 'leaf_descendant_paths': None}]]
    print(scan(l) == m)
    fm = [[{'rsib_path': None, 'lcin_path': None, 'depth': 0, 'lsib_path': None, 'parent_path': [], 'sib_seq': None, 'breadth_path': [], 'path': [], 'non_leaf_son_paths': [[2], [3]], 'rcin_path': None, 'sons_count': 4, 'parent_breadth_path': [], 'flat_len': 6, 'non_leaf_descendant_paths': [[2], [3], [3, 1]], 'leaf_son_paths': [[0], [1]], 'breadth': None, 'leaf': False, 'flat_offset': (0, 6), 'leaf_descendant_paths': [[0], [1], [3, 0], [3, 1, 0], [3, 1, 1], [2, 0]]}], [{'rsib_path': [1], 'lcin_path': None, 'depth': 1, 'lsib_path': None, 'parent_path': [], 'sib_seq': 0, 'breadth_path': [0], 'path': [0], 'non_leaf_son_paths': [], 'rcin_path': None, 'sons_count': 0, 'parent_breadth_path': [], 'flat_len': 1, 'non_leaf_descendant_paths': [], 'leaf_son_paths': [], 'breadth': 0, 'leaf': True, 'flat_offset': (5, 6), 'leaf_descendant_paths': []}, {'rsib_path': [2], 'lcin_path': None, 'depth': 1, 'lsib_path': [0], 'parent_path': [], 'sib_seq': 1, 'breadth_path': [1], 'path': [1], 'non_leaf_son_paths': [], 'rcin_path': None, 'sons_count': 0, 'parent_breadth_path': [], 'flat_len': 1, 'non_leaf_descendant_paths': [], 'leaf_son_paths': [], 'breadth': 1, 'leaf': True, 'flat_offset': (4, 5), 'leaf_descendant_paths': []}, {'rsib_path': [3], 'lcin_path': None, 'depth': 1, 'lsib_path': [1], 'parent_path': [], 'sib_seq': 2, 'breadth_path': [2], 'path': [2], 'non_leaf_son_paths': [], 'rcin_path': None, 'sons_count': 1, 'parent_breadth_path': [], 'flat_len': 1, 'non_leaf_descendant_paths': [], 'leaf_son_paths': [[2, 0]], 'breadth': 2, 'leaf': False, 'flat_offset': (3, 4), 'leaf_descendant_paths': [[2, 0]]}, {'rsib_path': None, 'lcin_path': None, 'depth': 1, 'lsib_path': [2], 'parent_path': [], 'sib_seq': 3, 'breadth_path': [3], 'path': [3], 'non_leaf_son_paths': [[3, 1]], 'rcin_path': None, 'sons_count': 2, 'parent_breadth_path': [], 'flat_len': 3, 'non_leaf_descendant_paths': [[3, 1]], 'leaf_son_paths': [[3, 0]], 'breadth': 3, 'leaf': False, 'flat_offset': (0, 3), 'leaf_descendant_paths': [[3, 0], [3, 1, 0], [3, 1, 1]]}], [{'rsib_path': None, 'lcin_path': None, 'depth': 2, 'lsib_path': None, 'parent_path': [2], 'sib_seq': 0, 'breadth_path': [2, 0], 'path': [2, 0], 'non_leaf_son_paths': [], 'rcin_path': [3, 0], 'sons_count': 0, 'parent_breadth_path': [2], 'flat_len': 1, 'non_leaf_descendant_paths': [], 'leaf_son_paths': [], 'breadth': 0, 'leaf': True, 'flat_offset': (3, 4), 'leaf_descendant_paths': []}, {'rsib_path': [3, 1], 'lcin_path': [2, 0], 'depth': 2, 'lsib_path': None, 'parent_path': [3], 'sib_seq': 0, 'breadth_path': [3, 1], 'path': [3, 0], 'non_leaf_son_paths': [], 'rcin_path': None, 'sons_count': 0, 'parent_breadth_path': [3], 'flat_len': 1, 'non_leaf_descendant_paths': [], 'leaf_son_paths': [], 'breadth': 1, 'leaf': True, 'flat_offset': (2, 3), 'leaf_descendant_paths': []}, {'rsib_path': None, 'lcin_path': None, 'depth': 2, 'lsib_path': [3, 0], 'parent_path': [3], 'sib_seq': 1, 'breadth_path': [3, 2], 'path': [3, 1], 'non_leaf_son_paths': [], 'rcin_path': None, 'sons_count': 2, 'parent_breadth_path': [3], 'flat_len': 2, 'non_leaf_descendant_paths': [], 'leaf_son_paths': [[3, 1, 0], [3, 1, 1]], 'breadth': 2, 'leaf': False, 'flat_offset': (0, 2), 'leaf_descendant_paths': [[3, 1, 0], [3, 1, 1]]}], [{'rsib_path': [3, 1, 1], 'lcin_path': None, 'depth': 3, 'lsib_path': None, 'parent_path': [3, 1], 'sib_seq': 0, 'breadth_path': [3, 2, 0], 'path': [3, 1, 0], 'non_leaf_son_paths': [], 'rcin_path': None, 'sons_count': 0, 'parent_breadth_path': [3, 2], 'flat_len': 1, 'non_leaf_descendant_paths': [], 'leaf_son_paths': [], 'breadth': 0, 'leaf': True, 'flat_offset': (1, 2), 'leaf_descendant_paths': []}, {'rsib_path': None, 'lcin_path': None, 'depth': 3, 'lsib_path': [3, 1, 0], 'parent_path': [3, 1], 'sib_seq': 1, 'breadth_path': [3, 2, 1], 'path': [3, 1, 1], 'non_leaf_son_paths': [], 'rcin_path': None, 'sons_count': 0, 'parent_breadth_path': [3, 2], 'flat_len': 1, 'non_leaf_descendant_paths': [], 'leaf_son_paths': [], 'breadth': 1, 'leaf': True, 'flat_offset': (0, 1), 'leaf_descendant_paths': []}]]
    print(fullfill_descendants_info(m) == fm)
    l = [1,[4],2,[3,[5,6]]]
    m = [[{'rsib_path': None, 'lcin_path': None, 'depth': 0, 'lsib_path': None, 'parent_path': [], 'sib_seq': None, 'breadth_path': [], 'path': [], 'non_leaf_son_paths': [[1], [3]], 'rcin_path': None, 'sons_count': 4, 'parent_breadth_path': [], 'flat_len': None, 'non_leaf_descendant_paths': [[1], [3]], 'leaf_son_paths': [[0], [2]], 'breadth': None, 'leaf': False, 'flat_offset': None, 'leaf_descendant_paths': [[0], [2]]}], [{'rsib_path': [1], 'lcin_path': None, 'depth': 1, 'lsib_path': None, 'parent_path': [], 'sib_seq': 0, 'breadth_path': [0], 'path': [0], 'non_leaf_son_paths': None, 'rcin_path': None, 'sons_count': 0, 'parent_breadth_path': [], 'flat_len': None, 'non_leaf_descendant_paths': None, 'leaf_son_paths': None, 'breadth': 0, 'leaf': True, 'flat_offset': None, 'leaf_descendant_paths': None}, {'rsib_path': [2], 'lcin_path': None, 'depth': 1, 'lsib_path': [0], 'parent_path': [], 'sib_seq': 1, 'breadth_path': [1], 'path': [1], 'non_leaf_son_paths': [], 'rcin_path': None, 'sons_count': 1, 'parent_breadth_path': [], 'flat_len': None, 'non_leaf_descendant_paths': [], 'leaf_son_paths': [[1, 0]], 'breadth': 1, 'leaf': False, 'flat_offset': None, 'leaf_descendant_paths': [[1, 0]]}, {'rsib_path': [3], 'lcin_path': None, 'depth': 1, 'lsib_path': [1], 'parent_path': [], 'sib_seq': 2, 'breadth_path': [2], 'path': [2], 'non_leaf_son_paths': None, 'rcin_path': None, 'sons_count': 0, 'parent_breadth_path': [], 'flat_len': None, 'non_leaf_descendant_paths': None, 'leaf_son_paths': None, 'breadth': 2, 'leaf': True, 'flat_offset': None, 'leaf_descendant_paths': None}, {'rsib_path': None, 'lcin_path': None, 'depth': 1, 'lsib_path': [2], 'parent_path': [], 'sib_seq': 3, 'breadth_path': [3], 'path': [3], 'non_leaf_son_paths': [[3, 1]], 'rcin_path': None, 'sons_count': 2, 'parent_breadth_path': [], 'flat_len': None, 'non_leaf_descendant_paths': [[3, 1]], 'leaf_son_paths': [[3, 0]], 'breadth': 3, 'leaf': False, 'flat_offset': None, 'leaf_descendant_paths': [[3, 0]]}], [{'rsib_path': None, 'lcin_path': None, 'depth': 2, 'lsib_path': None, 'parent_path': [1], 'sib_seq': 0, 'breadth_path': [1, 0], 'path': [1, 0], 'non_leaf_son_paths': None, 'rcin_path': None, 'sons_count': 0, 'parent_breadth_path': [1], 'flat_len': None, 'non_leaf_descendant_paths': None, 'leaf_son_paths': None, 'breadth': 0, 'leaf': True, 'flat_offset': None, 'leaf_descendant_paths': None}, {'rsib_path': [3, 1], 'lcin_path': None, 'depth': 2, 'lsib_path': None, 'parent_path': [3], 'sib_seq': 0, 'breadth_path': [3, 1], 'path': [3, 0], 'non_leaf_son_paths': None, 'rcin_path': None, 'sons_count': 0, 'parent_breadth_path': [3], 'flat_len': None, 'non_leaf_descendant_paths': None, 'leaf_son_paths': None, 'breadth': 1, 'leaf': True, 'flat_offset': None, 'leaf_descendant_paths': None}, {'rsib_path': None, 'lcin_path': None, 'depth': 2, 'lsib_path': [3, 0], 'parent_path': [3], 'sib_seq': 1, 'breadth_path': [3, 2], 'path': [3, 1], 'non_leaf_son_paths': [], 'rcin_path': None, 'sons_count': 2, 'parent_breadth_path': [3], 'flat_len': None, 'non_leaf_descendant_paths': [], 'leaf_son_paths': [[3, 1, 0], [3, 1, 1]], 'breadth': 2, 'leaf': False, 'flat_offset': None, 'leaf_descendant_paths': [[3, 1, 0], [3, 1, 1]]}], [{'rsib_path': [3, 1, 1], 'lcin_path': None, 'depth': 3, 'lsib_path': None, 'parent_path': [3, 1], 'sib_seq': 0, 'breadth_path': [3, 2, 0], 'path': [3, 1, 0], 'non_leaf_son_paths': None, 'rcin_path': None, 'sons_count': 0, 'parent_breadth_path': [3, 2], 'flat_len': None, 'non_leaf_descendant_paths': None, 'leaf_son_paths': None, 'breadth': 0, 'leaf': True, 'flat_offset': None, 'leaf_descendant_paths': None}, {'rsib_path': None, 'lcin_path': None, 'depth': 3, 'lsib_path': [3, 1, 0], 'parent_path': [3, 1], 'sib_seq': 1, 'breadth_path': [3, 2, 1], 'path': [3, 1, 1], 'non_leaf_son_paths': None, 'rcin_path': None, 'sons_count': 0, 'parent_breadth_path': [3, 2], 'flat_len': None, 'non_leaf_descendant_paths': None, 'leaf_son_paths': None, 'breadth': 1, 'leaf': True, 'flat_offset': None, 'leaf_descendant_paths': None}]]
    print(scan(l) == m)
    fm = 
    print(fullfill_descendants_info(m) == fm)



