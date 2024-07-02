import re

# Specify the file path (update this to the file you want to process)
file_path = '/Users/will/Dropbox/Projects/zettelkasten/Web/notes/201904270500  Ω Benefit others without the hope of thanks.md'

# Read the content of the file into 'lines'
with open(file_path, 'r') as file:
    lines = file.readlines()

pattern = r'^\d{2}-.*$'  # Update this pattern based on your testing on regex101.com

# Find all matches
matches = [m.group(0) for m in re.finditer(pattern, ''.join(lines), flags=re.MULTILINE)]

# Print matched lines for verification
for match in matches:
    print("Matched line:", match)

# Ask for confirmation before deletion
confirmation = input("Proceed with deletion? (y/n): ")
if confirmation.lower() == 'y':
    # Logic to remove the matched lines and the two lines following the last match
    if matches:
        # Convert the matched lines back to indices to find where to start deletion
        match_indices = [lines.index(m+"\n") for m in matches]  # Adding newline since 'lines' includes them
        # Assuming we want to remove the last occurrence and the two lines following it
        start_line = match_indices[-1]
        del lines[start_line:start_line+3]  # Adjust this as needed based on the actual structure of your data

        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.writelines(lines)

        print("Lines have been removed.")
    else:
        print("No matches found, no lines removed.")
else:
    print("Deletion cancelled.")