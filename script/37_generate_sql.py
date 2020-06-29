import os, json

with open(os.path.join(os.path.dirname(__file__), "36_microbe-directory_20200220.json"), "rU") as fin:
    records = fin.readline()


dic = json.loads(records)
with open(os.path.join(os.path.dirname(__file__), "38_insert.sql"), "w+") as fout:
    q = "use general;\n"

    k = []
    p = []
    c = []
    o = []
    f = []
    g = []
    s = []

    for m in dic:
        d = dic[m]
        t_kingdom = d['kingdom'].lower()
        t_phylum = d['phylum'].lower()
        t_class = d['class'].lower()
        t_order = d['order'].lower()
        t_family = d['family'].lower()
        t_genus = d['genus'].lower()
        t_species = d['species'].lower()

        if t_kingdom not in k:
            k.append(t_kingdom)
            q += f"INSERT INTO taxonomy(name, taxonomy_level_id) VALUES ('{t_kingdom}', 1);\n"

        if t_phylum not in p:
            p.append(t_phylum)
            q += f"INSERT INTO taxonomy(name, taxonomy_level_id, parent_id) VALUES ('{t_phylum}', 2, (SELECT t.taxonomy_id FROM taxonomy t WHERE t.name = '{t_kingdom}' AND t.taxonomy_level_id = 1 LIMIT 1));\n"

        if t_class not in c:
            c.append(t_class)
            q += f"INSERT INTO taxonomy(name, taxonomy_level_id, parent_id) VALUES ('{t_class}', 3, (SELECT t.taxonomy_id FROM taxonomy t WHERE t.name = '{t_phylum}' AND t.taxonomy_level_id = 2 LIMIT 1));\n"

        if t_order not in o:
            o.append(t_order)
            q += f"INSERT INTO taxonomy(name, taxonomy_level_id, parent_id) VALUES ('{t_order}', 4, (SELECT t.taxonomy_id FROM taxonomy t WHERE t.name = '{t_class}' AND t.taxonomy_level_id = 3 LIMIT 1));\n"

        if t_family not in f:
            f.append(t_family)
            q += f"INSERT INTO taxonomy(name, taxonomy_level_id, parent_id) VALUES ('{t_family}', 5, (SELECT t.taxonomy_id FROM taxonomy t WHERE t.name = '{t_order}' AND t.taxonomy_level_id = 4 LIMIT 1));\n"

        if t_genus not in g:
            g.append(t_genus)
            q += f"INSERT INTO taxonomy(name, taxonomy_level_id, parent_id) VALUES ('{t_genus}', 6, (SELECT t.taxonomy_id FROM taxonomy t WHERE t.name = '{t_family}' AND t.taxonomy_level_id = 5 LIMIT 1));\n"

        if t_species not in s:
            s.append(t_species)
            q += f"INSERT INTO taxonomy(name, taxonomy_level_id, parent_id) VALUES ('{t_species}', 7, (SELECT t.taxonomy_id FROM taxonomy t WHERE t.name = '{t_genus}' AND t.taxonomy_level_id = 6 LIMIT 1));\n"

        q += f"INSERT INTO organism(organism_name, taxonomy_id) VALUES ('{m}', (SELECT taxonomy_id FROM taxonomy WHERE name = '{t_species}' AND taxonomy_level_id = 7 LIMIT 1));\n\n"

    fout.write(q)


'''
{
  "antimicrobial_susceptibility": null,
  "microbe_id": 5753,
  "antimicrobial_susceptibility_citation": null,
  "spore_forming_citation": null,
  "kingdom": "Bacteria",
  "biofilm_forming_citation": null,
  "plant_pathogen": null,
  "species": "Selenomonas bovis",
  "optimal_ph": 7.1,
  "optimal_temperature": 39,
  "phylum": "Firmicutes",
  "order": "Selenomonadales",
  "extreme_environment": 0,
  "biofilm_forming": null,
  "gram_stain": 0,
  "class": "Negativicutes",
  "microbiome_location": 0,
  "spore_forming": 0,
  "gram_stain_citation": null,
  "microbiome_location_citation": null,
  "optimal_ph_citation": null,
  "animal_pathogen": null,
  "genus": "Selenomonas",
  "plant_pathogen_citation": null,
  "pathogenicity_citation": null,
  "extreme_environment_citation": null,
  "family": "Veillonellaceae",
  "pathogenicity": null,
  "animal_pathogen_citation": null,
  "optimal_temperature_citation": null
}
'''





