from django.contrib import admin
from .models import \
    AccessionNamesType_model, \
    AccessionType_model, \
    AccessionsType_model, \
    AcknowledgementsType_model, \
    AcquisitionType_model, \
    AddressesType_model, \
    AnnotationType_model, \
    AnnotationsType_model, \
    AssemblageType_model, \
    AssemblagesType_model, \
    AssociatedTaxaType_model, \
    AssociationType_model, \
    AssociationsType_model, \
    AtomizedNameType_model, \
    AudioType_model, \
    BiostratigraphicTermsType_model, \
    BiotopeType_model, \
    BotanicalGardenUnit_model, \
    ChronostratigraphicTermsType_model, \
    Contact_model, \
    ContactP_model, \
    ContentContactType_model, \
    ContentContactsType_model, \
    ContentContactsType3_model, \
    ContentMetadata_model, \
    CoordinateSetType_model, \
    CoordinateSetsType_model, \
    CoordinatesGridType_model, \
    CoordinatesLatLongType_model, \
    CoordinatesUTMType_model, \
    Country_model, \
    CreatorsType_model, \
    CultureCollectionUnit_model, \
    CultureNamesType_model, \
    DataSetType_model, \
    DataSets_model, \
    DateTime_model, \
    DescriptionType_model, \
    DivisionsType_model, \
    EmailAddressesType_model, \
    FieldNotesReferencesType_model, \
    FieldNumberType_model, \
    FieldNumbersType_model, \
    Gathering_model, \
    GatheringAgentType_model, \
    GatheringAgentsType_model, \
    GeoecologicalTermsType_model, \
    GrowthConditionAtomized_model, \
    GrowthConditionsAtomizedType_model, \
    GrowthConditionsMeasurementsOrFactsType_model, \
    HerbariumUnit_model, \
    HigherTaxaType_model, \
    HigherTaxon_model, \
    HybridFlagType_model, \
    Identification_model, \
    IdentificationQualifierType_model, \
    IdentificationsType_model, \
    IdentifiersType_model, \
    ImageType_model, \
    ImagesType_model, \
    Label_model, \
    LabelRepr_model, \
    LegalStatement_model, \
    LegalStatements_model, \
    LicensesType_model, \
    LithostratigraphicTermsType_model, \
    LoanRestrictionsType_model, \
    MarkType_model, \
    MarksType_model, \
    MeasurementOrFact_model, \
    MeasurementOrFactAtomizedType_model, \
    MeasurementsOrFactsType_model, \
    MeasurementsOrFactsType8_model, \
    MetadataDescriptionRepr_model, \
    MultimediaObject_model, \
    MultimediaObjectsType_model, \
    MultimediaObjectsType5_model, \
    MycologicalLiveStagesType_model, \
    MycologicalUnit_model, \
    NameAtomizedType_model, \
    NameBacterial_model, \
    NameBotanical_model, \
    NameViral_model, \
    NameZoological_model, \
    NamedArea_model, \
    NamedAreaType_model, \
    NamedAreasType_model, \
    NamedCollectionsOrSurveysType_model, \
    NamedPlaceRelationType_model, \
    NamedPlaceRelationsType_model, \
    NomenclaturalTypeDesignationType_model, \
    NomenclaturalTypeDesignationsType_model, \
    ObservationUnitIDsType_model, \
    ObservationUnitType_model, \
    Organization_model, \
    OtherLegalStatementsType_model, \
    OtherMeasurementsOrFactsType_model, \
    OtherProvidersType_model, \
    OwnersType_model, \
    PGRUnit_model, \
    PaleontologicalUnit_model, \
    Permit_model, \
    PermitsType_model, \
    PersonName_model, \
    PhasesOrStagesType_model, \
    PreparationType_model, \
    PreparationsType_model, \
    PreservationType_model, \
    PreservationType14_model, \
    PreservationsType_model, \
    PreviousUnitType_model, \
    PreviousUnitsType_model, \
    ProjectType_model, \
    RatingsType_model, \
    Reference_model, \
    ReferencesType_model, \
    ReferencesType12_model, \
    ReferencesType13_model, \
    ReferencesType2_model, \
    ReferencesType4_model, \
    RepresentationType_model, \
    ResourceURIsType_model, \
    ResourceURIsType1_model, \
    ResourceURIsType10_model, \
    ResourceURIsType11_model, \
    ResourceURIsType6_model, \
    ResourceURIsType7_model, \
    ResourceURIsType9_model, \
    ResultType_model, \
    RevisionData_model, \
    RolesType_model, \
    SampleDesignationsType_model, \
    ScientificName_model, \
    ScientificNameIdentified_model, \
    ScopeType_model, \
    Sequence_model, \
    SequencesType_model, \
    SpecimenMeasurementsOrFactsType_model, \
    SpecimenUnitType_model, \
    StratigraphicTerm_model, \
    StratigraphicTermL_model, \
    Stratigraphy_model, \
    StringL_model, \
    StringL255_model, \
    StringLP_model, \
    StringLP255_model, \
    StringP_model, \
    StringP255_model, \
    SuggestedCitationsType_model, \
    SynecologyType_model, \
    TagsType_model, \
    TaxaInBackgroundType_model, \
    TaxonIdentified_model, \
    TaxonomicTermsType_model, \
    TechnicalContactsType_model, \
    TelephoneNumbersType_model, \
    Temperature_model, \
    TradeDesignationNamesType_model, \
    Unit_model, \
    UnitExtensionsType_model, \
    UnitReferencesType_model, \
    UnitsType_model, \
    VersionType_model, \
    VideoType_model, \
    ZoologicalUnit_model, \
    anyUriP_model, \
    imageSize_model

admin.site.register(AccessionNamesType_model)
admin.site.register(AccessionType_model)
admin.site.register(AccessionsType_model)
admin.site.register(AcknowledgementsType_model)
admin.site.register(AcquisitionType_model)
admin.site.register(AddressesType_model)
admin.site.register(AnnotationType_model)
admin.site.register(AnnotationsType_model)
admin.site.register(AssemblageType_model)
admin.site.register(AssemblagesType_model)
admin.site.register(AssociatedTaxaType_model)
admin.site.register(AssociationType_model)
admin.site.register(AssociationsType_model)
admin.site.register(AtomizedNameType_model)
admin.site.register(AudioType_model)
admin.site.register(BiostratigraphicTermsType_model)
admin.site.register(BiotopeType_model)
admin.site.register(BotanicalGardenUnit_model)
admin.site.register(ChronostratigraphicTermsType_model)
admin.site.register(Contact_model)
admin.site.register(ContactP_model)
admin.site.register(ContentContactType_model)
admin.site.register(ContentContactsType_model)
admin.site.register(ContentContactsType3_model)
admin.site.register(ContentMetadata_model)
admin.site.register(CoordinateSetType_model)
admin.site.register(CoordinateSetsType_model)
admin.site.register(CoordinatesGridType_model)
admin.site.register(CoordinatesLatLongType_model)
admin.site.register(CoordinatesUTMType_model)
admin.site.register(Country_model)
admin.site.register(CreatorsType_model)
admin.site.register(CultureCollectionUnit_model)
admin.site.register(CultureNamesType_model)
admin.site.register(DataSetType_model)
admin.site.register(DataSets_model)
admin.site.register(DateTime_model)
admin.site.register(DescriptionType_model)
admin.site.register(DivisionsType_model)
admin.site.register(EmailAddressesType_model)
admin.site.register(FieldNotesReferencesType_model)
admin.site.register(FieldNumberType_model)
admin.site.register(FieldNumbersType_model)
admin.site.register(Gathering_model)
admin.site.register(GatheringAgentType_model)
admin.site.register(GatheringAgentsType_model)
admin.site.register(GeoecologicalTermsType_model)
admin.site.register(GrowthConditionAtomized_model)
admin.site.register(GrowthConditionsAtomizedType_model)
admin.site.register(GrowthConditionsMeasurementsOrFactsType_model)
admin.site.register(HerbariumUnit_model)
admin.site.register(HigherTaxaType_model)
admin.site.register(HigherTaxon_model)
admin.site.register(HybridFlagType_model)
admin.site.register(Identification_model)
admin.site.register(IdentificationQualifierType_model)
admin.site.register(IdentificationsType_model)
admin.site.register(IdentifiersType_model)
admin.site.register(ImageType_model)
admin.site.register(ImagesType_model)
admin.site.register(Label_model)
admin.site.register(LabelRepr_model)
admin.site.register(LegalStatement_model)
admin.site.register(LegalStatements_model)
admin.site.register(LicensesType_model)
admin.site.register(LithostratigraphicTermsType_model)
admin.site.register(LoanRestrictionsType_model)
admin.site.register(MarkType_model)
admin.site.register(MarksType_model)
admin.site.register(MeasurementOrFact_model)
admin.site.register(MeasurementOrFactAtomizedType_model)
admin.site.register(MeasurementsOrFactsType_model)
admin.site.register(MeasurementsOrFactsType8_model)
admin.site.register(MetadataDescriptionRepr_model)
admin.site.register(MultimediaObject_model)
admin.site.register(MultimediaObjectsType_model)
admin.site.register(MultimediaObjectsType5_model)
admin.site.register(MycologicalLiveStagesType_model)
admin.site.register(MycologicalUnit_model)
admin.site.register(NameAtomizedType_model)
admin.site.register(NameBacterial_model)
admin.site.register(NameBotanical_model)
admin.site.register(NameViral_model)
admin.site.register(NameZoological_model)
admin.site.register(NamedArea_model)
admin.site.register(NamedAreaType_model)
admin.site.register(NamedAreasType_model)
admin.site.register(NamedCollectionsOrSurveysType_model)
admin.site.register(NamedPlaceRelationType_model)
admin.site.register(NamedPlaceRelationsType_model)
admin.site.register(NomenclaturalTypeDesignationType_model)
admin.site.register(NomenclaturalTypeDesignationsType_model)
admin.site.register(ObservationUnitIDsType_model)
admin.site.register(ObservationUnitType_model)
admin.site.register(Organization_model)
admin.site.register(OtherLegalStatementsType_model)
admin.site.register(OtherMeasurementsOrFactsType_model)
admin.site.register(OtherProvidersType_model)
admin.site.register(OwnersType_model)
admin.site.register(PGRUnit_model)
admin.site.register(PaleontologicalUnit_model)
admin.site.register(Permit_model)
admin.site.register(PermitsType_model)
admin.site.register(PersonName_model)
admin.site.register(PhasesOrStagesType_model)
admin.site.register(PreparationType_model)
admin.site.register(PreparationsType_model)
admin.site.register(PreservationType_model)
admin.site.register(PreservationType14_model)
admin.site.register(PreservationsType_model)
admin.site.register(PreviousUnitType_model)
admin.site.register(PreviousUnitsType_model)
admin.site.register(ProjectType_model)
admin.site.register(RatingsType_model)
admin.site.register(Reference_model)
admin.site.register(ReferencesType_model)
admin.site.register(ReferencesType12_model)
admin.site.register(ReferencesType13_model)
admin.site.register(ReferencesType2_model)
admin.site.register(ReferencesType4_model)
admin.site.register(RepresentationType_model)
admin.site.register(ResourceURIsType_model)
admin.site.register(ResourceURIsType1_model)
admin.site.register(ResourceURIsType10_model)
admin.site.register(ResourceURIsType11_model)
admin.site.register(ResourceURIsType6_model)
admin.site.register(ResourceURIsType7_model)
admin.site.register(ResourceURIsType9_model)
admin.site.register(ResultType_model)
admin.site.register(RevisionData_model)
admin.site.register(RolesType_model)
admin.site.register(SampleDesignationsType_model)
admin.site.register(ScientificName_model)
admin.site.register(ScientificNameIdentified_model)
admin.site.register(ScopeType_model)
admin.site.register(Sequence_model)
admin.site.register(SequencesType_model)
admin.site.register(SpecimenMeasurementsOrFactsType_model)
admin.site.register(SpecimenUnitType_model)
admin.site.register(StratigraphicTerm_model)
admin.site.register(StratigraphicTermL_model)
admin.site.register(Stratigraphy_model)
admin.site.register(StringL_model)
admin.site.register(StringL255_model)
admin.site.register(StringLP_model)
admin.site.register(StringLP255_model)
admin.site.register(StringP_model)
admin.site.register(StringP255_model)
admin.site.register(SuggestedCitationsType_model)
admin.site.register(SynecologyType_model)
admin.site.register(TagsType_model)
admin.site.register(TaxaInBackgroundType_model)
admin.site.register(TaxonIdentified_model)
admin.site.register(TaxonomicTermsType_model)
admin.site.register(TechnicalContactsType_model)
admin.site.register(TelephoneNumbersType_model)
admin.site.register(Temperature_model)
admin.site.register(TradeDesignationNamesType_model)
admin.site.register(Unit_model)
admin.site.register(UnitExtensionsType_model)
admin.site.register(UnitReferencesType_model)
admin.site.register(UnitsType_model)
admin.site.register(VersionType_model)
admin.site.register(VideoType_model)
admin.site.register(ZoologicalUnit_model)
admin.site.register(anyUriP_model)
admin.site.register(imageSize_model)

