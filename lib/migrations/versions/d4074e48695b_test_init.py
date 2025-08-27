"""Test Init

Revision ID: d4074e48695b
Revises: a0b234bd62d8
Create Date: 2025-08-27 13:17:16.539452

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd4074e48695b'
down_revision: Union[str, Sequence[str], None] = 'a0b234bd62d8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
