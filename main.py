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
        
        # Example: Count dots (usually '.' or '*')
        dots = pacman_map.find_character('.')
        print(f"Number of dots: {len(dots)}")