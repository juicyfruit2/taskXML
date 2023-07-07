import xml.etree.ElementTree as ET
tree = ET.parse('movie.xml')
root = tree.getroot()

print(root.tag)

print(root.attrib)

for child in root:
    print(child.tag, child.attrib)


import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('movie.xml')
root = tree.getroot()

# Find the 'movie' element
movie_element = root.find('movie')

# Check if 'movie' element is found
if movie_element is not None:

# Iterate over the child tags of the movie element
    for child in movie_element.iter():
        print(child.tag)
else:
    print("The 'movie' element is not found in the XML file.")   


import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('movie.xml')
root = tree.getroot()

# Find the movie description elements
description_elements = root.findall('.description')

# Iterate over the description elements and print their text content
for description_element in description_elements:
    for text in description_element.itertext():
        print(text)



import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('movie.xml')
root = tree.getroot()

# Initialize counters
favorites_count = 0
non_favorites_count = 0

# Find all movie elements
movie_elements = root.findall('movie')

# Iterate over the movie elements
for movie_element in movie_elements:
    # Check if the movie is marked as favorite
    is_favorite = movie_element.get('favorite')
    if is_favorite and is_favorite.lower() == 'true':
        favorites_count += 1
    else:
        non_favorites_count += 1

# Print the results
print("Number of favorite movies:", favorites_count)
print("Number of non-favorite movies:", non_favorites_count)






