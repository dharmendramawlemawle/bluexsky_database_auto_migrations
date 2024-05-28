from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from graphviz import Digraph

# Database URL
DATABASE_URL = "sqlite:///./test.db"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Reflect the existing database into a new model
metadata = MetaData()
metadata.reflect(engine, only=['user', 'post', 'comment', 'category', 'post_category'])

# Produce a set of mappings from the database tables
Base = automap_base(metadata=metadata)
Base.prepare()

# Create a graph object
dot = Digraph()

# Add nodes for each table
for table_name, table in metadata.tables.items():
    dot.node(table_name, table_name)
    for column in table.columns:
        dot.node(f'{table_name}.{column.name}', f'{column.name}: {column.type}')
        dot.edge(table_name, f'{table_name}.{column.name}')

# Add edges for foreign key relationships
for table_name, table in metadata.tables.items():
    for column in table.columns:
        for fk in column.foreign_keys:
            dot.edge(f'{table_name}.{column.name}', f'{fk.column.table.name}.{fk.column.name}')

# Save the diagram to a file
dot.render('erd_from_sqlalchemy', format='png')
