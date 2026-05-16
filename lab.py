from pymongo import MongoClient, ASCENDING

def setup_catalog_and_queries():
    client = MongoClient('localhost', 27017)
    db = client['Catalog']
    db.drop_collection('PC_components')
    comps = db['PC_components']

    components = [
        {"Production": "MSI", "Model": "B450 TOMAHAWK", "Price": 120,
         "Category": {"Type": "материнская плата", "Description": "AM4, ATX", "format": "ATX", "socket": "AM4"}},
        {"Production": "ASUS", "Model": "ROG STRIX B550-F", "Price": 180,
         "Category": {"Type": "материнская плата", "Description": "AM4, ATX", "format": "ATX", "socket": "AM4"}},
        {"Production": "Gigabyte", "Model": "B450M DS3H", "Price": 80,
         "Category": {"Type": "материнская плата", "Description": "AM4, mATX", "format": "mATX", "socket": "AM4"}},
        {"Production": "ASRock", "Model": "A520M-HDV", "Price": 70,
         "Category": {"Type": "материнская плата", "Description": "AM4, mATX", "format": "mATX", "socket": "AM4"}},
        {"Production": "MSI", "Model": "Z490-A PRO", "Price": 160,
         "Category": {"Type": "материнская плата", "Description": "LGA1200, ATX", "format": "ATX", "socket": "LGA1200"}},
        {"Production": "Gigabyte", "Model": "Z590 AORUS ELITE", "Price": 220,
         "Category": {"Type": "материнская плата", "Description": "LGA1200, ATX", "format": "ATX", "socket": "LGA1200"}},
        {"Production": "ASUS", "Model": "TUF GAMING B660M-PLUS", "Price": 150,
         "Category": {"Type": "материнская плата", "Description": "LGA1700, mATX", "format": "mATX", "socket": "LGA1700"}},

        {"Production": "AMD", "Model": "Ryzen 5 5600X", "Price": 200,
         "Category": {"Type": "процессор", "Description": "AM4, 3.7 GHz", "socket": "AM4", "frequency": 3.7}},
        {"Production": "AMD", "Model": "Ryzen 7 5800X", "Price": 350,
         "Category": {"Type": "процессор", "Description": "AM4, 3.8 GHz", "socket": "AM4", "frequency": 3.8}},
        {"Production": "AMD", "Model": "Ryzen 5 3600", "Price": 130,
         "Category": {"Type": "процессор", "Description": "AM4, 3.6 GHz", "socket": "AM4", "frequency": 3.6}},
        {"Production": "Intel", "Model": "Core i5-11400F", "Price": 170,
         "Category": {"Type": "процессор", "Description": "LGA1200, 2.6 GHz", "socket": "LGA1200", "frequency": 2.6}},
        {"Production": "Intel", "Model": "Core i7-11700K", "Price": 320,
         "Category": {"Type": "процессор", "Description": "LGA1200, 3.6 GHz", "socket": "LGA1200", "frequency": 3.6}},
        {"Production": "Intel", "Model": "Core i5-12400F", "Price": 190,
         "Category": {"Type": "процессор", "Description": "LGA1700, 2.5 GHz", "socket": "LGA1700", "frequency": 2.5}},
        {"Production": "Intel", "Model": "Core i9-12900K", "Price": 550,
         "Category": {"Type": "процессор", "Description": "LGA1700, 3.2 GHz", "socket": "LGA1700", "frequency": 3.2}},

        {"Production": "Corsair", "Model": "Vengeance LPX 16GB", "Price": 70,
         "Category": {"Type": "ОЗУ", "Description": "DDR4 3200 MHz", "frequency": 3200, "capacity": 16}},
        {"Production": "Kingston", "Model": "FURY Beast 8GB", "Price": 40,
         "Category": {"Type": "ОЗУ", "Description": "DDR4 2666 MHz", "frequency": 2666, "capacity": 8}},
        {"Production": "Crucial", "Model": "Ballistix 32GB", "Price": 130,
         "Category": {"Type": "ОЗУ", "Description": "DDR4 3600 MHz", "frequency": 3600, "capacity": 32}},
        {"Production": "G.Skill", "Model": "Trident Z RGB 16GB", "Price": 100,
         "Category": {"Type": "ОЗУ", "Description": "DDR4 4000 MHz", "frequency": 4000, "capacity": 16}},
        {"Production": "Corsair", "Model": "Dominator Platinum 64GB", "Price": 300,
         "Category": {"Type": "ОЗУ", "Description": "DDR4 3200 MHz", "frequency": 3200, "capacity": 64}},
        {"Production": "Samsung", "Model": "DDR5 4800 32GB", "Price": 200,
         "Category": {"Type": "ОЗУ", "Description": "DDR5 4800 MHz", "frequency": 4800, "capacity": 32}},

        {"Production": "Samsung", "Model": "870 EVO 1TB", "Price": 100,
         "Category": {"Type": "ПЗУ", "Description": "SATA SSD 2.5\"", "form_factor": "2.5\"", "capacity": 1024}},
        {"Production": "WD", "Model": "Black SN850 1TB", "Price": 140,
         "Category": {"Type": "ПЗУ", "Description": "NVMe SSD M.2", "form_factor": "M.2", "capacity": 1024}},
        {"Production": "Seagate", "Model": "BarraCuda 2TB", "Price": 55,
         "Category": {"Type": "ПЗУ", "Description": "HDD 3.5\"", "form_factor": "3.5\"", "capacity": 2048}},
        {"Production": "Crucial", "Model": "MX500 500GB", "Price": 55,
         "Category": {"Type": "ПЗУ", "Description": "SATA SSD 2.5\"", "form_factor": "2.5\"", "capacity": 512}},
        {"Production": "Samsung", "Model": "980 Pro 2TB", "Price": 250,
         "Category": {"Type": "ПЗУ", "Description": "NVMe SSD M.2", "form_factor": "M.2", "capacity": 2048}},
        {"Production": "Kingston", "Model": "A400 240GB", "Price": 25,
         "Category": {"Type": "ПЗУ", "Description": "SATA SSD 2.5\"", "form_factor": "2.5\"", "capacity": 240}},

        {"Production": "NVIDIA", "Model": "RTX 3060", "Price": 350,
         "Category": {"Type": "видеокарта", "Description": "12GB GDDR6", "memory": 12, "ports": ["HDMI", "3xDP"]}},
        {"Production": "NVIDIA", "Model": "RTX 3070", "Price": 550,
         "Category": {"Type": "видеокарта", "Description": "8GB GDDR6", "memory": 8, "ports": ["HDMI", "3xDP"]}},
        {"Production": "AMD", "Model": "Radeon RX 6800", "Price": 600,
         "Category": {"Type": "видеокарта", "Description": "16GB GDDR6", "memory": 16, "ports": ["HDMI", "2xDP", "USB-C"]}},
        {"Production": "NVIDIA", "Model": "GTX 1650", "Price": 200,
         "Category": {"Type": "видеокарта", "Description": "4GB GDDR5", "memory": 4, "ports": ["HDMI", "DP", "DVI"]}},
        {"Production": "AMD", "Model": "Radeon RX 6600", "Price": 320,
         "Category": {"Type": "видеокарта", "Description": "8GB GDDR6", "memory": 8, "ports": ["HDMI", "3xDP"]}},
        {"Production": "NVIDIA", "Model": "RTX 3080", "Price": 750,
         "Category": {"Type": "видеокарта", "Description": "10GB GDDR6X", "memory": 10, "ports": ["HDMI", "3xDP"]}},
    ]
    comps.insert_many(components)
    print("Коллекция PC_components заполнена.")

    sockets = comps.distinct("Category.socket", {"Category.Type": "материнская плата"})
    min_ram = comps.find_one({"Category.Type": "ОЗУ"}, sort=[("Price", 1)])
    max_ram = comps.find_one({"Category.Type": "ОЗУ"}, sort=[("Price", -1)])
    min_storage = comps.find_one({"Category.Type": "ПЗУ"}, sort=[("Price", 1)])
    max_storage = comps.find_one({"Category.Type": "ПЗУ"}, sort=[("Price", -1)])
    min_gpu = comps.find_one({"Category.Type": "видеокарта"}, sort=[("Price", 1)])
    max_gpu = comps.find_one({"Category.Type": "видеокарта"}, sort=[("Price", -1)])

    cheap_builds = []
    expensive_builds = []
    for sock in sockets:
        cheap_mb = comps.find_one({"Category.Type": "материнская плата", "Category.socket": sock},
                                  sort=[("Price", 1)])
        cheap_cpu = comps.find_one({"Category.Type": "процессор", "Category.socket": sock},
                                   sort=[("Price", 1)])
        if cheap_mb and cheap_cpu:
            cheap_builds.append({
                "motherboard": cheap_mb["Model"], "cpu": cheap_cpu["Model"],
                "ram": min_ram["Model"], "storage": min_storage["Model"], "gpu": min_gpu["Model"],
                "total": cheap_mb["Price"] + cheap_cpu["Price"] + min_ram["Price"] + min_storage["Price"] + min_gpu["Price"]
            })
        exp_mb = comps.find_one({"Category.Type": "материнская плата", "Category.socket": sock},
                                sort=[("Price", -1)])
        exp_cpu = comps.find_one({"Category.Type": "процессор", "Category.socket": sock},
                                 sort=[("Price", -1)])
        if exp_mb and exp_cpu:
            expensive_builds.append({
                "motherboard": exp_mb["Model"], "cpu": exp_cpu["Model"],
                "ram": max_ram["Model"], "storage": max_storage["Model"], "gpu": max_gpu["Model"],
                "total": exp_mb["Price"] + exp_cpu["Price"] + max_ram["Price"] + max_storage["Price"] + max_gpu["Price"]
            })

    print("\nСамая дешёвая сборка")
    for b in cheap_builds:
        print(b)
    print("\nСамая дорогая сборка (по сокетам)")
    for b in expensive_builds:
        print(b)

    print("\n3-й и 5-й по стоимости")
    for cat_type in ["материнская плата", "процессор", "ОЗУ", "ПЗУ", "видеокарта"]:
        items = list(comps.find({"Category.Type": cat_type}).sort("Price", ASCENDING))
        if len(items) >= 5:
            third, fifth = items[2], items[4]
            print(f"{cat_type}: 3-й = {third['Model']} ({third['Price']}р.), 5-й = {fifth['Model']} ({fifth['Price']}р.)")
        else:
            print(f"{cat_type}: недостаточно элементов (всего {len(items)})")

    am4_mb = list(comps.find({"Category.Type": "материнская плата", "Category.socket": "AM4"}))
    am4_cpu = list(comps.find({"Category.Type": "процессор", "Category.socket": "AM4"}))
    rams = list(comps.find({"Category.Type": "ОЗУ"}))
    storages = list(comps.find({"Category.Type": "ПЗУ"}))
    gpus = list(comps.find({"Category.Type": "видеокарта"}))

    am4_builds = []
    for mb in am4_mb:
        for cpu in am4_cpu:
            for ram in rams:
                for st in storages:
                    for gpu in gpus:
                        am4_builds.append({
                            "motherboard": mb["Model"], "cpu": cpu["Model"],
                            "ram": ram["Model"], "storage": st["Model"], "gpu": gpu["Model"],
                            "total": mb["Price"] + cpu["Price"] + ram["Price"] + st["Price"] + gpu["Price"]
                        })
    print(f"\nВсего AM4-сборок: {len(am4_builds)}")
    for i, b in enumerate(am4_builds[:5], 1):
        print(f"{i}: {b}")

    client.close()

if __name__ == "__main__":
    setup_catalog_and_queries()
