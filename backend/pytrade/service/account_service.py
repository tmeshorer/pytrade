import attr
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from injector import inject
from pytrade.repository.account_repository import AccountRepository


@inject
@attr.s(auto_attribs=True)
@attr.dataclass
class AccountService:
    _repository: AccountRepository

    def create(self, *, request: AccountCreate) -> AccountDTO:
        request_data = jsonable_encoder(request)
        account = Account(**request_data)

        Account = self._repository.save(Account)

        return AccountDTO(id=Account.id, title=Account.title, description=Account.description)

    def update(self, *, Account_id: int, request: AccountUpdate) -> AccountDTO:
        Account: Account = self._repository.find_by_id(variable=Account_id)

        if not Account:
            raise HTTPException(status_code=400, detail="Account not found")

        Account_data = jsonable_encoder(Account)
        update_data = request.dict(skip_defaults=True)

        for field in Account_data:
            if field in update_data:
                setattr(Account, field, update_data[field])

        Account = self._repository.save(Account)

        return AccountDTO(id=Account.id, title=Account.title, description=Account.description)

    def remove(self, *, Account_id: int):
        Account = self._repository.find_by_id(variable=Account_id)

        if not Account:
            raise HTTPException(status_code=404, detail="Account not found")

        return self._repository.delete(Account)