from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
Post = Table('Post', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('body', String(length=1200)),
    Column('timestamp', DATETIME),
    Column('user_id', Integer),
)

User = Table('User', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=32)),
    Column('password_hash', String(length=128)),
    Column('email', String(length=120)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['Post'].create()
    post_meta.tables['User'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['Post'].drop()
    post_meta.tables['User'].drop()
