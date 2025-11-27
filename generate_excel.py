import pandas as pd

data = [
    {
        "Manufacturer Name": "Hyundai Motor Company",
        "Country": "Korea",
        "Production Date": "2025/01",
        "Model Year": "2025",
        "Max Weight": "2000",
        "Max Weight Per Axle": "",
        "Compliance Note": "Matches Iraqi Standards",
        "VIN": "KMHGN41EBU123456",
        "Classification": "Passenger Car",
        "Engine": "Gasoline 2.0L",
        "Model": "Sonata",
        "Factory": "Ulsan Plant"
    },
    {
        "Manufacturer Name": "Kia Corporation",
        "Country": "Slovakia",
        "Production Date": "2024/12",
        "Model Year": "2025",
        "Max Weight": "1800",
        "Max Weight Per Axle": "",
        "Compliance Note": "Matches Iraqi Standards",
        "VIN": "U5YHN41EBU654321",
        "Classification": "SUV",
        "Engine": "Diesel 2.2L",
        "Model": "Sportage",
        "Factory": "Zilina Plant"
    },
    {
        "Manufacturer Name": "Toyota Motor Corporation",
        "Country": "Japan",
        "Production Date": "2025/02",
        "Model Year": "2025",
        "Max Weight": "2500",
        "Max Weight Per Axle": "",
        "Compliance Note": "Matches Iraqi Standards",
        "VIN": "JTDGN41EBU987654",
        "Classification": "SUV",
        "Engine": "Hybrid 2.5L",
        "Model": "RAV4",
        "Factory": "Takaoka Plant"
    },
    {
        "Manufacturer Name": "BMW AG",
        "Country": "Germany",
        "Production Date": "2025/03",
        "Model Year": "2025",
        "Max Weight": "2200",
        "Max Weight Per Axle": "",
        "Compliance Note": "Matches Iraqi Standards",
        "VIN": "WBAHN41EBU456789",
        "Classification": "Sedan",
        "Engine": "Gasoline 3.0L",
        "Model": "5 Series",
        "Factory": "Dingolfing Plant"
    },
    {
        "Manufacturer Name": "Mercedes-Benz AG",
        "Country": "Germany",
        "Production Date": "2025/01",
        "Model Year": "2025",
        "Max Weight": "2400",
        "Max Weight Per Axle": "",
        "Compliance Note": "Matches Iraqi Standards",
        "VIN": "WDDHN41EBU112233",
        "Classification": "Sedan",
        "Engine": "Gasoline 2.0L",
        "Model": "E-Class",
        "Factory": "Sindelfingen Plant"
    }
]

df = pd.DataFrame(data)
df.to_excel("e:/xampp/htdocs/car-label/car-label-test.xlsx", index=False)
print("Excel file created successfully.")
