import os

orders = {
    "order1": "pydoc-markdown -I src -m cp_lookup.cp_lookup --no-render-toc > docs/cp_lookup.cp_lookup.md",
    "order2": "pydoc-markdown -I src -m cp_lookup.add_ll --no-render-toc > docs/cp_lookup.add_ll.md",
    "order3": "pydoc-markdown -I src -m cp_lookup.mygeo --no-render-toc > docs/cp_lookup.mygeo.md",
    "order4": "pydoc-markdown -I src -m index_calmeth.non_dimension --no-render-toc > docs/index_calmeth.non_dimension.md",
    "order5": "pydoc-markdown -I src -m index_calmeth.weights --no-render-toc > docs/index_calmeth.weights.md",
    "order6": "pydoc-markdown -I src -m index_calmeth.non_dimension --no-render-toc > docs/index_calmeth.non_dimension.md",
}

for value in orders.values():
    os.system(value)
