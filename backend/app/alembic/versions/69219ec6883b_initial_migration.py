"""Initial migration	

Revision ID: 69219ec6883b	
Revises: 	
Create Date: 2024-09-15 19:59:28.847793+10:00	

"""	
from alembic import op	
import sqlalchemy as sa	
	

# revision identifiers, used by Alembic.	
revision = '69219ec6883b'	
down_revision = None	
branch_labels = None	
depends_on = None	


def upgrade():	
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('date_creation', sa.String(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('markdown', sa.String(), nullable=False),
    sa.Column('thumbnail', sa.String(), nullable=False),
    sa.Column('color', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_article_date_creation'), 'article', ['date_creation'], unique=True)
    op.create_index(op.f('ix_article_id'), 'article', ['id'], unique=False)
    # ### end Alembic commands ###	


def downgrade():	
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_article_id'), table_name='article')
    op.drop_index(op.f('ix_article_date_creation'), table_name='article')
    op.drop_table('article')
    # ### end Alembic commands ###