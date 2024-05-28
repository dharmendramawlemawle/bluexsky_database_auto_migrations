import os
from alembic.config import Config
from alembic.migration import MigrationContext
from alembic import command
from database import engine, DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError


def run_migrations():
     try:
          engine = create_engine(DATABASE_URL)
          with engine.connect() as connection:
               alembic_cfg = Config("alembic.ini")
               alembic_cfg.set_main_option('sqlalchemy.url', DATABASE_URL)
               alembic_cfg.attributes['connection'] = connection
               
               # Check the current version
               context = MigrationContext.configure(connection)
               current_rev = context.get_current_revision()
               # import pdb;pdb.set_trace()
               
               print(f"Current database version: {current_rev}")

               # Run the upgrade to the latest version
               command.upgrade(alembic_cfg, "head")
               
               # Verify the new version
               new_rev = context.get_current_revision()
               print(f"Database upgraded to version: {new_rev}")
     except OperationalError as e:
          print(f"Database connection error: {e}")
     except Exception as e:
          print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_migrations()
