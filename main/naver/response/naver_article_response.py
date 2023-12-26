from pydantic import BaseModel
from typing import List


class NaverArticleResponse(BaseModel):
    articleNo: str
    articleName: str
    articleStatus: str
    realEstateTypeCode: str
    realEstateTypeName: str
    articleRealEstateTypeCode: str
    articleRealEstateTypeName: str
    tradeTypeCode: str
    tradeTypeName: str
    verificationTypeCode: str
    floorInfo: str
    priceChangeState: str
    isPriceModification: bool
    dealOrWarrantPrc: str
    areaName: str
    area1: int
    area2: int
    direction: str
    articleConfirmYmd: str
    siteImageCount: int
    articleFeatureDesc: str
    tagList: List[str]
    buildingName: str
    sameAddrCnt: int
    sameAddrDirectCnt: int
    sameAddrMaxPrc: str
    sameAddrMinPrc: str
    cpid: str
    cpName: str
    cpPcArticleUrl: str
    cpPcArticleBridgeUrl: str
    cpPcArticleLinkUseAtArticleTitleYn: bool
    cpPcArticleLinkUseAtCpNameYn: bool
    cpMobileArticleUrl: str
    cpMobileArticleLinkUseAtArticleTitleYn: bool
    cpMobileArticleLinkUseAtCpNameYn: bool
    latitude: str
    longitude: str
    isLocationShow: bool
    realtorName: str
    realtorId: str
    tradeCheckedByOwner: bool
    isDirectTrade: bool
    isInterest: bool
    isComplex: bool
    detailAddress: str
    detailAddressYn: str

