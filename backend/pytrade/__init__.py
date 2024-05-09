import os
from uuid import uuid4

from flask_migrate import Migrate
from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, mapped_column
from flask_sqlalchemy import SQLAlchemy

class Base(DeclarativeBase,MappedAsDataclass):
    id = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    created_at = mapped_column(
        DateTime,
        default=func.now(),
    )

    updated_at = mapped_column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    )



db = SQLAlchemy(model_class=Base)
migrate = Migrate()


