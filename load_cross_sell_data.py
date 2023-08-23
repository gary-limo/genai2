# Load cross sell data into the CrossSellData table

import os
import django

# Set the environment variable to your Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hello.settings")
django.setup()

from hello.models import CrossSellData

cross_sell_data = [
    ("C1", "Rios Tina Rhodes", 1, "Yes", "NA"),
    ("C2", "Smith Noah Rios", 2, "Yes", "NA"),
    ("C3", "Valencia Richard Smith", 3, "Yes", "NA"),
    ("C4", "Lowe Kaitlyn Valencia", 4, "Yes", "NA"),
    ("C5", "Wilson Rachel Lowe", 5, "No", "Daughter"),
    ("C6", "Davis Austin Wilson", 6, "No", "Daughter"),
    ("C7", "Warren Karen Davis", 7, "No", "Son"),
    ("C8", "Richardson Sean Warren", 8, "No", "Son"),
    ("C9", "Anderson Laura Richardson", 9, "No", "Son"),
    ("C10", "Garcia Lisa Anderson", 1, "No", "Son"),
    ("C11", "Mendez Shannon Garcia", 2, "No", "Son"),
    ("C12", "Rodgers Gary Mendez", 3, "No", "Son"),
    ("C13", "Reed Jillian Rodgers", 4, "No", "Son"),
    ("C14", "Newman Jeffrey Reed", 5, "No", "Husband"),
    ("C15", "Blake Donna Newman", 15, "No", "Husband"),
    ("C16", "Young Rachel Blake", 16, "No", "Husband"),
    ("C17", "Hawkins Kimberly Young", 17, "No", "Husband"),
    ("C18", "Green Robert Hawkins", 18, "No", "Husband"),
    ("C19", "Smith Briana Green", 19, "No", "Husband"),
    ("C20", "Barnes Joseph Smith", 20, "No", "Husband"),
    ("C21", "Silva Michelle Barnes", 21, "No", "Husband"),
    ("C22", "Joseph Mr. Silva", 22, "No", "Wife"),
    ("C23", "Hart Trevor Joseph", 23, "No", "Wife"),
    ("C24", "Koch Sarah Hart", 15, "No", "Wife"),
    ("C25", "Lawrence Kelly Koch", 16, "No", "Wife"),
    ("C26", "Harrington Catherine Lawrence", 17, "No", "Wife"),
    ("C27", "Mathis Janet Harrington", 18, "No", "Wife"),
    ("C28", "Davenport Ethan Mathis", 19, "No", "Husband"),
    ("C29", "Garcia Amber Davenport", 20, "No", "Wife"),
    ("C30", "Carlson Maureen Garcia", 21, "No", "Husband"),
]


for data in cross_sell_data:
    customer_id, customer_name, agent_id, speciality, households_with_vehicles = data
    entry = CrossSellData(
        customer_id=int(customer_id[1:]),  # Extract and convert the numeric part
        customer_name=customer_name,
        agent_id=agent_id,
        speciality=speciality,
        additional_households_with_vehicles=households_with_vehicles
    )
    entry.save()
    print(f"Inserted: {entry}")

print("Data insertion completed.")
