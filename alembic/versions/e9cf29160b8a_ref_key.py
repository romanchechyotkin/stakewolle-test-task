"""“ref_key”

Revision ID: e9cf29160b8a
Revises: 9e33e2364fbf
Create Date: 2024-02-09 18:01:21.692843

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e9cf29160b8a'
down_revision: Union[str, None] = '9e33e2364fbf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('users_referral_fkey', 'users', type_='foreignkey')
    op.create_foreign_key(op.f('users_referral_fkey'), 'users', 'referral_codes', ['referral'], ['code'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('users_referral_fkey'), 'users', type_='foreignkey')
    op.create_foreign_key('users_referral_fkey', 'users', 'referral_codes', ['referral'], ['code'], ondelete='CASCADE')
    # ### end Alembic commands ###