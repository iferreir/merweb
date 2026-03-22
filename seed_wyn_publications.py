import datetime

import pandas as pd
from app.db.database import SessionLocal, engine
from app.db import models

# Make sure tables exist
models.Base.metadata.create_all(bind=engine)

EXCEL_FILE = "EPS-Publications-1-Aug-24-to-31-Jul-25.xlsx"

def seed_wyn():
    df = pd.read_excel(EXCEL_FILE)

    # Filter rows where Internal Author(s) contains "Williams, Wyn"
    mask = df["Internal Author(s)"].astype(str).str.contains("Williams, Wyn", na=False)
    wyn_df = df[mask]

    db = SessionLocal()
    try:
        for _, row in wyn_df.iterrows():
            title = str(row["Title"]).strip()
            journal = str(row["Journal title"]).strip()
            doi = str(row["DOIs (Digital Object Identifiers)"]).strip()
            year = None

            # Try to get year from Published column
            pub_date = row.get("Published")
            if isinstance(pub_date, (datetime.date, datetime.datetime)):
                year = pub_date.year

            # Avoid inserting duplicates (by title + year)
            existing = (
                db.query(models.Publication)
                .filter(models.Publication.title == title)
                .first()
            )
            if existing:
                continue

            link = ""
            if doi and doi.lower().startswith("10."):
                link = f"https://doi.org/{doi}"
            elif doi.startswith("http"):
                link = doi

            pub = models.Publication(
                title=title,
                authors=str(row["Internal Author(s)"]),
                year=year if year is not None else 0,
                journal=journal,
                link=link,
                notes="Imported from EPS spreadsheet for Wyn Williams.",
            )
            db.add(pub)

        db.commit()
        print("Wyn Williams publications seeded.")
    finally:
        db.close()

if __name__ == "__main__":
    seed_wyn()

