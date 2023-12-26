from pydantic import BaseModel, Field
from typing import Optional


class LawDongResponse(BaseModel):
    과거법정동코드: int
    리명: str
    법정동코드: int
    삭제일자: str
    생성일자: str
    순위: int
    시군구명: str
    시도명: str
    읍면동명: str

