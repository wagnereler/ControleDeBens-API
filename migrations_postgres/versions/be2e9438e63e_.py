"""empty message

Revision ID: be2e9438e63e
Revises: 55e3c808dff8
Create Date: 2024-01-19 17:51:48.387617

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be2e9438e63e'
down_revision = '55e3c808dff8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('log_acesso',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_usuario', sa.Integer(), nullable=False),
    sa.Column('id_empresa', sa.Integer(), nullable=False),
    sa.Column('data_acesso', sa.Date(), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_empresa'], ['empresa.id'], ),
    sa.ForeignKeyConstraint(['id_usuario'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('log_acess')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('log_acess',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('id_usuario', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('id_empresa', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('data_acesso', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('status', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['id_empresa'], ['empresa.id'], name='log_acess_id_empresa_fkey'),
    sa.ForeignKeyConstraint(['id_usuario'], ['usuario.id'], name='log_acess_id_usuario_fkey'),
    sa.PrimaryKeyConstraint('id', name='log_acess_pkey')
    )
    op.drop_table('log_acesso')
    # ### end Alembic commands ###