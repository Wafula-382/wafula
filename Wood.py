# file_operations.py

def write_to_file(filename, content):
    """Writes content to a file, creating it if it doesn't exist."""
    # The 'with open(...)' structure is the "Pythonic" way to handle files.
    # It ensures the file is automatically closed, even if errors occur.
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Successfully wrote to '{filename}'")

def read_from_file(filename):
    """Reads and returns the entire content of a file."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"\nContent of '{filename}':\n---")
            print(content)
            print("---")
            return content
    except FileNotFoundError:
        print(f"\nError: File '{filename}' not found.")
        return None

# --- Main execution block ---

if __name__ == "_main_":
    # Create a new file, perhaps named after a type of wood!
    wood_file = "cedar_log.txt"

    # Write some data to the file
    write_to_file(wood_file, "This is the first line of my cedar log.\nIt smells great (in my imagination).\nAnother line of code-wood.")

    # Read the data back from the file
    read_from_file(wood_file)
