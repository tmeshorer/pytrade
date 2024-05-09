from pydantic import BaseModel, ConfigDict
class AccountDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    provider_account_id: str
    broker: str
    currency: str
    account_type: str


class AccountCreate(AccountDTO):
    pass

class AccountUpdate(AccountDTO):
    pass
