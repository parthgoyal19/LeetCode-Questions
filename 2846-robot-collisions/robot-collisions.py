class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        
        # Create a list of robots with their original index included
        # Each robot: [position, health, direction, original_index]
        robots = []
        for i in range(n):
            robots.append([positions[i], healths[i], directions[i], i])
            
        # Sort robots by their position on the line
        robots.sort(key=lambda x: x[0])
        
        stack = []  # To store robots moving to the right ('R')
        
        for robot in robots:
            # If moving Right, it won't collide with anything currently in stack
            if robot[2] == 'R':
                stack.append(robot)
            else:
                # Moving Left: resolve collisions with 'R' robots in the stack
                while stack and stack[-1][2] == 'R':
                    if stack[-1][1] < robot[1]:
                        # Right-moving robot has less health, it gets destroyed
                        stack.pop()
                        robot[1] -= 1  # Left-moving robot loses 1 health
                    elif stack[-1][1] > robot[1]:
                        # Right-moving robot has more health, Left-moving robot gets destroyed
                        stack[-1][1] -= 1
                        robot[1] = 0  # Mark left robot as destroyed
                        break
                    else:
                        # Both have equal health, both get destroyed
                        stack.pop()
                        robot[1] = 0
                        break
                
                # If the Left-moving robot survived all collisions, add it to survivors
                if robot[1] > 0:
                    stack.append(robot)
                    
        # Re-sort survivors by their original index to match the requested output format
        stack.sort(key=lambda x: x[3])
        
        # Return only the healths of the survivors
        return [robot[1] for robot in stack]