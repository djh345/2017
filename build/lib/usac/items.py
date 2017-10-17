# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UsacItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    FRN = scrapy.Field()
    FRNNickname = scrapy.Field()
    FRNStatus = scrapy.Field()
    FourSeventyOneApplicationNumber = scrapy.Field()
    FourSeventyOneNickName = scrapy.Field()
    FourSeventyOneApplicationStatus = scrapy.Field()
    FourSeventyOneReviewStatus = scrapy.Field()
    EstablishingFCCFormFourSeventyNumber = scrapy.Field()
    EstablishingFCCFormFourSeventyStatus = scrapy.Field()
    UserEnteredEstablishingFCCFormFourSeventyNumber = scrapy.Field()
    BEN = scrapy.Field()
    BilledEntityName = scrapy.Field()
    ApplicantType = scrapy.Field()
    ApplicantStreetAddressOne = scrapy.Field()
    ApplicantStreetAddressTwo = scrapy.Field()
    ApplicantCity = scrapy.Field()
    ApplicantState = scrapy.Field()
    ApplicantZipCode = scrapy.Field()
    FourSeventyOneContactName = scrapy.Field()
    FourSeventyOneContactEmail = scrapy.Field()
    BENUrbanRuralStatus = scrapy.Field()
    BENAccountAdministrator = scrapy.Field()
    BENAccountAdministratorEmail = scrapy.Field()
    StateLEACode = scrapy.Field()
    StateSchoolCode = scrapy.Field()
    LibraryLocaleCode = scrapy.Field()
    LibraryFSCSKey = scrapy.Field()
    LibrarySquareFootage = scrapy.Field()
    LibraryFSCSSEQ = scrapy.Field()
    FourSeventyOneConsultantRegistrationNumber = scrapy.Field()
    FourSeventyOneConsultingFirmName = scrapy.Field()
    ServiceProviderName = scrapy.Field()
    SPIN = scrapy.Field()
    SPACFiled = scrapy.Field()
    FundYear = scrapy.Field()
    FourEightySixServiceStartDate = scrapy.Field()
    ContractAwardDate = scrapy.Field()
    ContractExpOrSvcEndDate = scrapy.Field()
    RemainingContractExtensions = scrapy.Field()
    LastDatetoInvoice = scrapy.Field()
    OrigRMonthlyCost = scrapy.Field()
    CmtdRMonthlyCost = scrapy.Field()
    OrigRIneligibleCost = scrapy.Field()
    CmtdRIneligibleCost = scrapy.Field()
    OrigREligibleCost = scrapy.Field()
    CmtdREligibleCost = scrapy.Field()
    OrigRMonthsofService = scrapy.Field()
    CmtdRMonthsofService = scrapy.Field()
    OrigRAnnualCost = scrapy.Field()
    CmtdRAnnualCost = scrapy.Field()
    OrigNRCost = scrapy.Field()
    CmtdNRCost = scrapy.Field()
    OrigNRIneligibleCost = scrapy.Field()
    CmtdNRIneligibleCost = scrapy.Field()
    OrigNREligibleCost = scrapy.Field()
    CmtdNREligibleCost = scrapy.Field()
    OrigTotalCost = scrapy.Field()
    CmtdTotalCost = scrapy.Field()
    OrigDiscount = scrapy.Field()
    CmtdDiscount = scrapy.Field()
    OrigFundingRequest = scrapy.Field()
    CmtdFundingRequest = scrapy.Field()
    OrigFRNServiceType = scrapy.Field()
    CmtdFRNServiceType = scrapy.Field()
    OrigFourSeventyOneSSD = scrapy.Field()
    CmtdFourSeventyOneSSD = scrapy.Field()
    WaveNumber = scrapy.Field()
    FCDLDate = scrapy.Field()
    DateUserGeneratedFCDL = scrapy.Field()
    FCDLCommentforFourSeventyOneApplication = scrapy.Field()
    FCDLCommentforFRN = scrapy.Field()
    AppealWaveNumber = scrapy.Field()
    RevisedFCDLDate = scrapy.Field()
    FRNCommittedAmount = scrapy.Field()
    InvoicingMode = scrapy.Field()
    TotalAuthorizedDisbursement = scrapy.Field()

