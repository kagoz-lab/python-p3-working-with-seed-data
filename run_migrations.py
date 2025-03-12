
import sys
import os
from alembic.config import Config
from alembic import command

# Set the PYTHONPATH to include the parent directory of 'lib'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'lib')))

# Create an Alembic configuration object
alembic_cfg = Config("alembic.ini")

# Run the Alembic upgrade command
command.upgrade(alembic_cfg, "head")
