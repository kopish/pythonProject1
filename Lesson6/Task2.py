def rest_ethanol(total_mass, warehouse):
   ethanol = total_mass*83/100
   warehouse -= ethanol
   print('Остаток этанола на складе:', warehouse)
   return warehouse

warehouse = 1000
mass = int(input('Масса готового антисептика (г):'))
warehouse = rest_ethanol(mass, warehouse)
mass = int(input('Масса готового антисептика (г):'))
warehouse = rest_ethanol(mass, warehouse)
