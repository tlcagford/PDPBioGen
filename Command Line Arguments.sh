# Basic academic bio
pdp-biogen --name "Dr. Jane Smith" --role "Professor" --institution "Stanford University" --expertise "machine learning"

# Corporate style with output file
pdp-biogen --name "John Doe" --role "CTO" --institution "Tech Corp" --expertise "cloud infrastructure" --style corporate --output bio.md

# Using JSON input file
pdp-biogen --input examples/input_academic.json --output biography.txt
