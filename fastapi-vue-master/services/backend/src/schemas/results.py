from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Results


ResultInSchema = pydantic_model_creator(
    Registrations, name="ResultIn", exclude=["author_id"], exclude_readonly=True)
ResultOutSchema = pydantic_model_creator(
    Registrations, name="Result", exclude =[
      "modified_at", "author.password", "author.created_at", "author.modified_at"
    ]
)


class UpdateResult(BaseModel):
    patient: Optional[str]
    result: Optional[str]
    gen: Optional[str]
