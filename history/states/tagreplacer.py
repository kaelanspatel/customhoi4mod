import os

for filename in os.listdir("states"):
    lines = []
    with open(filename) as infile:
        for line in infile:
            line = line.replace("GRG", "GRG")
            lines.append(line)
    with open(filename, 'w') as outfile:
        for line in lines:
            outfile.write(line)