#!/usr/bin/env python3

from faker import Faker
import logging
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Game

fake = Faker()

def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

if __name__ == '__main__':
    main()
    engine = create_engine('sqlite:///seed_db.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Clear existing records
    session.query(Game).delete()
    session.commit()

    # Add a console message to indicate seeding has started
    logger.info("Seeding games...")

    # Generate random game data
    games = [
        Game(
            title=fake.catch_phrase(),
            genre=fake.word(),
            platform=fake.word(),
            price=random.randint(0, 60),
            description=fake.text(),
            release_date=fake.date_between(start_date='-2y', end_date='today')
        )
        for _ in range(50)
    ]

    # Bulk save new records
    try:
        session.bulk_save_objects(games)
        session.commit()
    except Exception as e:
        logger.error(f"Error occurred while seeding: {e}")
    session.commit()
