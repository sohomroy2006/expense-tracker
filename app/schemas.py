from datetime import date
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    password: str = Field(min_length=6, max_length=72)  # bcrypt limit is 72 bytes


class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr

    model_config = {"from_attributes": True}


class Token(BaseModel):
    access_token: str
    token_type: str



class CategoryCreate(BaseModel):
    name: str = Field(min_length=1, max_length=50)


class CategoryOut(BaseModel):
    id: int
    name: str

    model_config = {"from_attributes": True}


class ExpenseCreate(BaseModel):
    category_id: int
    amount: Decimal = Field(gt=0, max_digits=10, decimal_places=2)
    description: Optional[str] = Field(default=None, max_length=255)
    expense_date: date


class ExpenseUpdate(BaseModel):
    # every field optional, so you can change just one thing
    category_id: Optional[int] = None
    amount: Optional[Decimal] = Field(default=None, gt=0, max_digits=10, decimal_places=2)
    description: Optional[str] = Field(default=None, max_length=255)
    expense_date: Optional[date] = None


class ExpenseOut(BaseModel):
    id: int
    amount: Decimal
    description: Optional[str]
    expense_date: date
    category: CategoryOut

    model_config = {"from_attributes": True}