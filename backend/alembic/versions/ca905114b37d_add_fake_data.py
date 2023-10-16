"""add_fake_data

Revision ID: ca905114b37d
Revises: f013ae44ffb7
Create Date: 2023-10-09 12:24:41.811039

"""

import random

from faker import Faker

from alembic import op
from src.models.todos import Todo
from src.schemas.todos import TodoPriority

# revision identifiers, used by Alembic.
revision = "ca905114b37d"
down_revision = "f013ae44ffb7"
branch_labels = None
depends_on = None


def upgrade():
    fake = Faker()
    op.bulk_insert(
        Todo.__table__,
        [
            {
                "title": fake.sentence(nb_words=random.randint(3, 10)),
                "description": fake.paragraph(nb_sentences=random.randint(1, 6))
                if fake.boolean()
                else None,
                "priority": random.choice(list(TodoPriority)),
                "created_at": fake.date_time_this_month(),
                "updated_at": fake.date_time_this_month(),
            }
            for _ in range(random.randint(10, 16))
        ],
    )


def downgrade():
    op.execute("TRUNCATE TABLE todo")
