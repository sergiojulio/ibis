import ibis

con = ibis.duckdb.connect("palmer_penguins.ddb")

penguins = con.table("penguins")

rows = penguins.filter(penguins.species == "Adelie")

print(rows)