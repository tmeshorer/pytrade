from typing import Optional, List, Any
from . import db, Base
from .models import Account, Bar, Company, FinanicalStatement, Instrument, Order, Position


class BaseRepository(object):


    def find_by(self, *, entity_class: Any, entity_param: Any, variable: Any) -> Optional[Any]:
        return db.session.query(entity_class).filter(entity_param == variable).first()

    def find_all(self, *, entity_class: Any, skip=0, limit=100) -> List[Optional[Any]]:
        return db.session.query(entity_class).offset(skip).limit(limit).all()

    def save(self, entity: Any) -> Any:
        db.session.add(entity)
        db.session.commit()
        db.session.refresh(entity)

        return entity

    def delete(self, entity: Any):
        db.session.delete(entity)
        db.session.commit()


class AccountRepository(BaseRepository):
    def find_by_id(self, *, entity_class=Account, entity_param=Account.id, variable: Any) -> Optional[Account]:
        return super().find_by(entity_class=entity_class, entity_param=entity_param, variable=variable)

    def find_all(self, *, entity_class=Account, skip=0, limit=100) -> List[Optional[Account]]:
        return super().find_all(entity_class=entity_class)


class BarRepository(BaseRepository):
    def find_by_id(self, *, entity_class=Bar, entity_param=Bar.id, variable: Any) -> Optional[Bar]:
        return super().find_by(entity_class=entity_class, entity_param=entity_param, variable=variable)

    def find_all(self, *, entity_class=Bar, skip=0, limit=100) -> List[Optional[Bar]]:
        return super().find_all(entity_class=entity_class)

class CompanyRepository(BaseRepository):
    def find_by_id(self, *, entity_class=Company, entity_param=Company.id, variable: Any) -> Optional[Company]:
        return super().find_by(entity_class=entity_class, entity_param=entity_param, variable=variable)

    def find_all(self, *, entity_class=Company, skip=0, limit=100) -> List[Optional[Company]]:
        return super().find_all(entity_class=entity_class)

class FinancialStatmentRepository(BaseRepository):
    def find_by_id(self, *, entity_class=FinanicalStatement, entity_param=FinanicalStatement.id, variable: Any) -> Optional[FinanicalStatement]:
        return super().find_by(entity_class=entity_class, entity_param=entity_param, variable=variable)

    def find_all(self, *, entity_class=FinanicalStatement, skip=0, limit=100) -> List[Optional[FinanicalStatement]]:
        return super().find_all(entity_class=entity_class)

class IndicatorRepository(BaseRepository):
    def find_by_id(self, *, entity_class=Instrument, entity_param=Instrument.id, variable: Any) -> Optional[Instrument]:
        return super().find_by(entity_class=entity_class, entity_param=entity_param, variable=variable)

    def find_all(self, *, entity_class=Instrument, skip=0, limit=100) -> List[Optional[Instrument]]:
        return super().find_all(entity_class=entity_class)

class OrderRepository(BaseRepository):
    def find_by_id(self, *, entity_class=Order, entity_param=Order.id, variable: Any) -> Optional[Order]:
        return super().find_by(entity_class=entity_class, entity_param=entity_param, variable=variable)

    def find_all(self, *, entity_class=Order, skip=0, limit=100) -> List[Optional[Order]]:
        return super().find_all(entity_class=entity_class)

class PositionRepository(BaseRepository):
    def find_by_id(self, *, entity_class=Position, entity_param=Position.id, variable: Any) -> Optional[Position]:
        return super().find_by(entity_class=entity_class, entity_param=entity_param, variable=variable)

    def find_all(self, *, entity_class=Position, skip=0, limit=100) -> List[Optional[Position]]:
        return super().find_all(entity_class=entity_class)