# AVL Tree Implementation in Python

A self-balancing Binary Search Tree (AVL Tree) implemented in Python, supporting full CRUD operations with automatic rebalancing using rotations.

## Features

- **Insert** — adds a key and rebalances the tree using LL, RR, LR, RL rotations
- **Search** — checks if a key exists in O(log n) time
- **Update** — updates an existing key while keeping the tree balanced
- **Delete** — removes a key, handling leaf, one-child, and two-children cases, then rebalances
- **Traversals** — In-order (sorted output) and Pre-order
- **Visualization** — prints the tree structure sideways in the terminal after each operation
- **Height & Balance Factor** — displayed for every node
- **Comparison** — includes a regular unbalanced BST to show why AVL Trees are faster

## How AVL Tree Stays Balanced

Every node stores a `height`. After every insert/delete, the **balance factor** (left height − right height) is checked. If it becomes `+2` or `-2`, the tree performs a rotation:

| Case | Condition | Fix |
|------|-----------|-----|
| LL | Left subtree too heavy (left-left) | Right Rotation |
| RR | Right subtree too heavy (right-right) | Left Rotation |
| LR | Left subtree too heavy (left-right) | Left then Right Rotation |
| RL | Right subtree too heavy (right-left) | Right then Left Rotation |

This guarantees the tree height stays at **O(log n)**, so insert, search, and delete are always fast — even in the worst case.

## Time Complexity

| Operation | Complexity |
|-----------|------------|
| Insert | O(log n) |
| Search | O(log n) |
| Delete | O(log n) |

## Example Output

**Insert, traversals, and node info:**

![Output 1](screenshots/Screenshot%202026-06-28%20130345.png)

**Search, update, and delete:**

![Output 2](screenshots/Screenshot%202026-06-28%20130410.png)

**Delete result and BST comparison start:**

![Output 3](screenshots/Screenshot%202026-06-28%20130430.png)

**Final comparison conclusion:**

![Output 4](screenshots/Screenshot%202026-06-28%20130500.png)