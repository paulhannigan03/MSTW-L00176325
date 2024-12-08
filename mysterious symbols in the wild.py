import random

# Define the grid size
GRID_SIZE = 5

# Define a set of symbols and their corresponding meanings
SYMBOLS = {
    "@": "Hidden treasure nearby",
    "#": "An ancient ruin is close",
    "$": "A valuable artifact is buried here",
    "%": "A mysterious danger lurks here",
    "&": "A sacred shrine is nearby",
}

# Function to generate a random grid with symbols
def generate_grid(grid_size, symbols):
    grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]
    num_symbols = random.randint(1, grid_size)  # Place 1 to grid_size symbols
    for _ in range(num_symbols):
        x = random.randint(0, grid_size - 1)
        y = random.randint(0, grid_size - 1)
        grid[x][y] = random.choice(list(symbols.keys()))
    return grid

# Function to display the grid
def display_grid(grid):
    print("\nGrid:")
    for row in grid:
        print(" ".join(row))

# Function to decode a symbol
def decode_symbol(symbol):
    return SYMBOLS.get(symbol, "Unknown symbol")

# Main interactive loop
def explore_grid(grid):
    while True:
        user_input = input("\nEnter coordinates to explore (e.g., 2 3) or 'exit' to quit: ").strip()
        if user_input.lower() == "exit":
            print("Exiting exploration. Goodbye!")
            break
        try:
            x, y = map(int, user_input.split())
            if grid[x][y] in SYMBOLS:
                print(f"You found a symbol '{grid[x][y]}': {decode_symbol(grid[x][y])}")
            else:
                print("Nothing interesting here...")
        except (ValueError, IndexError):
            print("Invalid input. Please enter valid coordinates.")

# Run the program
if __name__ == "__main__":
    random.seed(42)  # For consistent random output (optional)
    grid = generate_grid(GRID_SIZE, SYMBOLS)
    display_grid(grid)
    explore_grid(grid)
