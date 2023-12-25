from dataclasses import dataclass, field
from datetime import date
from pydantic import BaseModel, Field
from typing import Optional


class ApartTransactionResponse(BaseModel):
    거래금액: str
    거래유형: str
    건축년도: str
    년: str
    도로명: str
    도로명건물본번호코드: str
    도로명건물부번호코드: str
    도로명시군구코드: str
    도로명일련번호코드: str
    도로명지상지하코드: str
    도로명코드: str
    등기일자: Optional[str] = Field(null=True)
    법정동: str
    법정동본번코드: str
    법정동부번코드: str
    법정동시군구코드: str
    법정동읍면동코드: str
    법정동지번코드: str
    아파트: str
    월: int
    일: int
    일련번호: str
    전용면적: str
    중개사소재지: str
    지번: str
    지역코드: str
    층: str
    해제사유발생일: str
    해제여부: str

