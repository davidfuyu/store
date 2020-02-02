import os

with open(os.path.join(os.path.dirname(__file__), "41_test.tsv"), "rU") as fin:
    records = fin.readlines()

header = records[0].strip().split("\t")
del(records[0])

with open(os.path.join(os.path.dirname(__file__), "43_insert_test.sql"), "w+") as f:
    f.write("use general;\n")
    for row in records:
        items = row.strip().split("\t")
        name = items[0] + ("_" + items[1] if items[1] else '')
        q = f"INSERT INTO organism (organism_name) VALUES ('{name}');\n"

        for i in range(1, len(items)):
            organism_id = f"(SELECT organism_id from organism where organism_name = '{name}')"
            value = items[i].replace("'", "''")

            if value and value != '' and i not in (6, 7, 9, 10, 67, 71):
                property_id = f"(SELECT property_id from property where lower(property_name) = lower('{header[i]}'))"
                q += f"INSERT INTO organism_property (organism_id, property_id, value) VALUES ({organism_id}, {property_id}, '{value}');\n"
                q += f"    INSERT INTO organism_property_log (organism_property_id, status_id, user_id) VALUES(LAST_INSERT_ID(), 1, 1);\n"
            
        f.write(q)
