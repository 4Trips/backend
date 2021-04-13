"""empty message

Revision ID: c5c4e390a891
Revises: 
Create Date: 2021-04-08 08:20:18.494971

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5c4e390a891'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('traveler',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=15), nullable=False),
    sa.Column('email', sa.String(length=40), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.Column('avatar', sa.String(length=180), nullable=True),
    sa.Column('rol', sa.String(length=10), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('fecha_registro', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('userpro',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=35), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('url', sa.String(length=120), nullable=True),
    sa.Column('location', sa.String(length=40), nullable=False),
    sa.Column('direction', sa.String(length=40), nullable=False),
    sa.Column('vat_number', sa.String(length=20), nullable=True),
    sa.Column('social_reason', sa.String(length=20), nullable=True),
    sa.Column('avatar', sa.String(length=120), nullable=False),
    sa.Column('photos', sa.Text(), nullable=True),
    sa.Column('registr_date', sa.DateTime(), nullable=False),
    sa.Column('rol', sa.String(length=30), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('percent_reviews', sa.Float(), nullable=False),
    sa.Column('total_reviews', sa.Float(), nullable=True),
    sa.Column('sum_reviews', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('user_name')
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_traveler', sa.Integer(), nullable=False),
    sa.Column('id_pro', sa.Integer(), nullable=False),
    sa.Column('id_users', sa.String(length=20), nullable=False),
    sa.Column('value', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_pro'], ['userpro.id'], ),
    sa.ForeignKeyConstraint(['id_traveler'], ['traveler.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id_users')
    )
    op.create_table('trip',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_traveler', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('post_date', sa.DateTime(), nullable=False),
    sa.Column('needs_trip', sa.String(length=60), nullable=False),
    sa.Column('destination', sa.String(length=200), nullable=False),
    sa.Column('first_day', sa.Date(), nullable=False),
    sa.Column('last_day', sa.Date(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('receiving_offers', sa.Boolean(), nullable=False),
    sa.Column('counter', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_traveler'], ['traveler.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('offers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_pro', sa.Integer(), nullable=False),
    sa.Column('id_trip', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('attached', sa.String(length=120), nullable=True),
    sa.ForeignKeyConstraint(['id_pro'], ['userpro.id'], ),
    sa.ForeignKeyConstraint(['id_trip'], ['trip.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_traveler', sa.Integer(), nullable=True),
    sa.Column('id_pro', sa.Integer(), nullable=True),
    sa.Column('id_offer', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('attached', sa.String(length=120), nullable=True),
    sa.ForeignKeyConstraint(['id_offer'], ['offers.id'], ),
    sa.ForeignKeyConstraint(['id_pro'], ['userpro.id'], ),
    sa.ForeignKeyConstraint(['id_traveler'], ['traveler.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    op.drop_table('offers')
    op.drop_table('trip')
    op.drop_table('reviews')
    op.drop_table('userpro')
    op.drop_table('traveler')
    # ### end Alembic commands ###
