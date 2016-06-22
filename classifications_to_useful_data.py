import csv
import json

myfile = open("classification_data.csv", 'wb')
wr = csv.writer(myfile)

csvrow = ["id", "bar", "bulge"]
wr.writerow(csvrow)

counts = {}

with open('barbulge-classifications.csv', 'rb') as f:
    reader=csv.reader(f)
    next(reader)
    for row in reader:
        subject_id = row[13].split(';')[0]
        annotations = json.loads(row[11])

        if not subject_id in counts:
            counts[subject_id] = {'total': 0, 'bar': 0, 'bulge': 0}

        counts[subject_id]['total'] += 1

        if annotations[0]['value'] == "Yes, there's a bar":
            counts[subject_id]['bar'] += 1
        elif annotations[0]['value'] == "No, there is no bar. ":
            pass
        else:
            print 'wtf?', annotations[0]

        if annotations[1]['value'] == "Yes, there's a bulge":
            counts[subject_id]['bulge'] += 1
        elif annotations[1]['value'] == "No, there's no bulge. ":
            pass
        else:
            print 'wtf?', annotations[1]

for subject_id, numbers in counts.iteritems():
    wr.writerow([subject_id, int(round(numbers['bar'] / float(numbers['total']))), int(round(numbers['bulge'] / float(numbers['total'])))])