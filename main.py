"""
File: Caveman Pacman Main 
Author: David Sarkies
Initial: 4 September 2025
Update: 4 September 2025
Version: 0.0
"""

from map import PacmanMap

# Example usage
if __name__ == "__main__":
    # Create a PacmanMap object
    pacman_map = PacmanMap("map.txt")
    
    if pacman_map.map_data:
        print(f"Map loaded: {pacman_map.width}x{pacman_map.height}")
        print("\nMap:")
        pacman_map.print_map()
        
        # Example: Find Pac-Man's starting position (usually 'P')
        pacman_positions = pacman_map.find_character('P')
        if pacman_positions:
            print(f"\nPac-Man starts at: {pacman_positions[0]}")

        # Example: Find deer starting position (usually 'P')
        deer_positions = pacman_map.find_deer('d')
        if deer_positions:
            print(f"\nDeer start at: {deer_positions}")

        # Example: Find bear starting position (usually 'P')
        bear_positions = pacman_map.find_bear('B')
        if bear_positions:
            print(f"\nBears start at: {bear_positions}")
        
        # Example: Count dots (usually '.' or '*')
        dots = pacman_map.find_character('.')
        print(f"Number of dots: {len(dots)}")

"""
4 September 2025 - Created File