from enum import Enum


class TradeType(Enum):
    매매 = "A1"
    전세 = "B1"
    월세 = "B2"


class PriceOrder(Enum):
    낮은가격순 = "prc"
    높은가격순 = "prcDesc"


