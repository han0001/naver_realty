from dataclasses import dataclass, field


@dataclass
class Article:
    articleNo: str
    articleName: str
    articleStatus: str
    realEstateTypeCode: str
    realEstateTypeName: str
    articleRealEstateTypeCode: str
    articleRealEstateTypeName: str
    tradeTypeCode: str
    tradeTypeName: str = field(default=None)
    verificationTypeCode: str = field(default=None)
    floorInfo: str = field(default=None)
    priceChangeState: str = field(default=None)
    isPriceModification: str = field(default=None)
    dealOrWarrantPrc: str = field(default=None)
    areaName: str = field(default=None)
    area1: str = field(default=None)
    area2: str = field(default=None)
    direction: str = field(default=None)
    articleConfirmYmd: str = field(default=None)
    siteImageCount: str = field(default=None)
    articleFeatureDesc: str = field(default=None)
    tagList: list = field(default=None)
    buildingName: str = field(default=None)
    sameAddrCnt: str = field(default=None)
    sameAddrDirectCnt: str = field(default=None)
    sameAddrMaxPrc: str = field(default=None)
    sameAddrMinPrc: str = field(default=None)
    cpid: str = field(default=None)
    cpName: str = field(default=None)
    cpPcArticleUrl: str = field(default=None)
    cpPcArticleBridgeUrl: str = field(default=None)
    cpPcArticleLinkUseAtArticleTitleYn: str = field(default=None)
    cpPcArticleLinkUseAtCpNameYn: str = field(default=None)
    cpMobileArticleUrl: str = field(default=None)
    cpMobileArticleLinkUseAtArticleTitleYn: str = field(default=None)
    cpMobileArticleLinkUseAtCpNameYn: str = field(default=None)
    latitude: str = field(default=None)
    longitude: str = field(default=None)
    isLocationShow: str = field(default=None)
    realtorName: str = field(default=None)
    tradeCheckedByOwner: str = field(default=None)
    isDirectTrade: str = field(default=None)
    isInterest: str = field(default=None)
    isComplex: str = field(default=None)
    detailAddress: str = field(default=None)
    detailAddressYn: str = field(default=None)
    realtorId: str = field(default=None)

