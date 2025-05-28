from app.core.database import engine
from app.models.base import Base
from app.models import sale  # make sure all models are imported

# This will create all tables defined using Base
Base.metadata.create_all(bind=engine)
