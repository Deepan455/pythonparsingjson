# Tree

Assume a tree-like data structure with the following properties:

* Each node contains a unique `id` (str) and a non-unique `name` (str).
* Each node has either `branches` or `leaves`, but not both;
  * `branches` contain a list of one or more nodes,
  * `leaves` contain a list of strings.
* A tree may have an arbitrary depth (nodes in branches may branch further).

Write a program in Python3 that accepts path to a `json` file on the input 
and prints on the standard output:
* list of all leaves, and
* all leaves that are directly or indirectly descendant from a node as a list of key (node `id`), pair (leaves) values. 

Example:

input.json
```json
[
    {
        "id": "1",
        "name": "node1",
        "branches": [
            {
                "id": "2",
                "name": "node2",
                "branches": [
                    {
                        "id": "3",
                        "name": "node3",
                        "leaves": [
                            "leaf1",
                            "leaf2"
                        ]
                    }, {
                        "id": "4",
                        "name": "node4",
                        "leaves": [
                            "leaf3",
                            "leaf4"
                        ]
                    }
                ]
            }
        ]
    }, {
        "id": "5",
        "name": "node5",
        "branches": [
            {
                "id": "6",
                "name": "node6",
                "leaves": [
                    "leaf5"
                ]
            }
        ]
    }
]
```

```bash
$ python tree.py input.json
```
```text
Leaves: ['leaf1', 'leaf2', 'leaf3', 'leaf4', 'leaf5']
Leaves per node:
[('1', ['leaf1', 'leaf2', 'leaf3', 'leaf4']),
 ('2', ['leaf1', 'leaf2', 'leaf3', 'leaf4']),
 ('3', ['leaf1', 'leaf2']),
 ('4', ['leaf3', 'leaf4']),
 ('5', ['leaf5']),
 ('6', ['leaf5'])]
```