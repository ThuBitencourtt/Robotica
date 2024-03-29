"""empty message

Revision ID: 2887d9479642
Revises: e83d91893afa
Create Date: 2019-11-24 14:01:45.022427

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2887d9479642'
down_revision = 'e83d91893afa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Equipes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(), nullable=True),
    sa.Column('lastname', sa.String(), nullable=True),
    sa.Column('slogan', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('site', sa.String(), nullable=True),
    sa.Column('país', sa.String(), nullable=True),
    sa.Column('estado', sa.String(), nullable=True),
    sa.Column('cidade', sa.String(), nullable=True),
    sa.Column('instituicao', sa.String(), nullable=True),
    sa.Column('capitao', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('firstname'),
    sa.UniqueConstraint('lastname'),
    sa.UniqueConstraint('site'),
    sa.UniqueConstraint('slogan')
    )
    op.create_table('Pessoas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('idade', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name')
    )
    op.create_table('Robos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('categoria', sa.String(), nullable=True),
    sa.Column('peso', sa.String(), nullable=True),
    sa.Column('responsavel', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('Robos')
    op.drop_table('Pessoas')
    op.drop_table('Equipes')
    # ### end Alembic commands ###
