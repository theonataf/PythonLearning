import csv
import json

json_output = {}
count=0

with open('title.basics.tsv', 'r') as f:
    rd = csv.reader(f, delimiter="\t")
    json_output['movies'] = []

    for row in rd:
        if row[1] == 'movie':
            if row[5] != '\\N':
                if int(row[5]) >= 1960:
                    count += 1
                    new_movie = {
                        'Title': row[3],
                        'Year': row[5],
                        'Genres': row[8],
                        'Minutes': row[7]
                    }

                    json_output['movies'].append((new_movie))
    print(count)
with open('movies_json.json', 'w+') as output:
    output.write(json.dumps(json_output, indent='\t'))
