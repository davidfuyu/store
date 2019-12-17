import os

with open(os.path.join(os.path.dirname(__file__),"21_property.tsv"), "rU") as fin:
    records = fin.readlines()

with open(os.path.join(os.path.dirname(__file__),"23_insert.sql"), "a+") as f:
    f.write("use general;\n")
    for row in records:
        attrs = row.strip().split("\t")
        name = attrs[0].strip('"').strip() if attrs[0] else None
        desc = attrs[1].strip('"').strip() if attrs[1] else None
        type = attrs[2].strip('"').strip()
        category = attrs[3].strip('"').strip()
        q = "INSERT INTO property (property_name, property_desc, property_type_id, property_category_id) VALUES ("
        q += f"'{name}', " if name else "null, "
        q += f"'{desc}', " if desc else "null, "
        q += f"(select property_type_id from property_type where lower(property_type_name) = lower('{type}') limit 1), "
        q += f"(select property_category_id from property_category where property_category_name = '{category}' limit 1)); \n"
        f.write(q)