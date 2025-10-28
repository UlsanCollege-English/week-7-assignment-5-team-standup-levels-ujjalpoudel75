from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    """
    Performs a level-order traversal (BFS) of the tree.
    Returns a list of lists, where each inner list contains the
    node values for that level.
    """
    if not root:
        return []
    
    queue = deque([root])
    all_levels = []
    
    while queue:
        # Get the number of nodes at the current level
        level_size = len(queue)
        current_level_vals = []
        
        # Process all nodes for the current level
        for _ in range(level_size):
            node = queue.popleft()
            current_level_vals.append(node.val)
            
            # Add children to the queue for the next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        # Add the completed level's values to the main list
        all_levels.append(current_level_vals)
        
    return all_levels

def zigzag_level_order(root):
    """
    Performs a zigzag level-order traversal of the tree.
    Returns a list of lists, with levels alternating between
    left-to-right and right-to-left order.
    """
    if not root:
        return []
    
    queue = deque([root])
    all_levels = []
    left_to_right = True
    
    while queue:
        level_size = len(queue)
        current_level_vals = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level_vals.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Add the level, reversing if necessary
        if left_to_right:
            all_levels.append(current_level_vals)
        else:
            all_levels.append(current_level_vals[::-1]) # Reverse the list
        
        # Flip the direction for the next level
        left_to_right = not left_to_right
        
    return all_levels

def right_side_view(root):
    """
    Performs a level-order traversal, returning only the value
    of the right-most node at each level.
    """
    if not root:
        return []
    
    queue = deque([root])
    view = []
    
    while queue:
        level_size = len(queue)
        
        # Process all nodes for the current level
        for i in range(level_size):
            node = queue.popleft()
            
            # If this is the last node on the level, add it to the view
            if i == level_size - 1:
                view.append(node.val)
                
            # Add children to the queue for the next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
    return view
