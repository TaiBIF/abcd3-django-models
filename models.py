from django.db import models


class AccessionNamesType_model(models.Model):
    AccessionName = models.CharField(max_length=1000, )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class AccessionType_model(models.Model):
    AccessionDate = models.CharField(max_length=1000, blank=True, null=True)
    AccessionCatalogue = models.CharField(max_length=1000, blank=True, null=True)
    AccessionNumber = models.CharField(max_length=1000, blank=True, null=True)
    AccessionURI = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class AccessionsType_model(models.Model):
    Accession = models.ForeignKey(
        "AccessionType_model",
        on_delete=models.CASCADE,
        related_name="AccessionsType_Accession_AccessionType",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class AcknowledgementsType_model(models.Model):
    Acknowledgement = models.ForeignKey(
        "LegalStatement_model",
        on_delete=models.CASCADE,
        related_name="AcknowledgementsType_Acknowledgement_LegalStatement",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class AcquisitionType_model(models.Model):
    AcquisitionType = models.ForeignKey(
        "AcquisitionType_model",
        on_delete=models.CASCADE,
        related_name="AcquisitionType_AcquisitionType_AcquisitionType",
        blank=True, null=True,
    )
    Date = models.CharField(max_length=1000, blank=True, null=True)
    AcquiredFrom = models.ForeignKey(
        "Contact_model",
        on_delete=models.CASCADE,
        related_name="AcquisitionType_AcquiredFrom_Contact",
        blank=True, null=True,
    )
    AcquisitionSourceText = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="AcquisitionType_AcquisitionSourceText_StringL",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class AddressesType_model(models.Model):
    Address = models.ForeignKey(
        "StringLP_model",
        on_delete=models.CASCADE,
        related_name="AddressesType_Address_StringLP",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class AnnotationType_model(models.Model):
    Text = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="AnnotationType_Text_StringL",
    )
    Annotator = models.ForeignKey(
        "Contact_model",
        on_delete=models.CASCADE,
        related_name="AnnotationType_Annotator_Contact",
        blank=True, null=True,
    )
    Date = models.ForeignKey(
        "DateTime_model",
        on_delete=models.CASCADE,
        related_name="AnnotationType_Date_DateTime",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class AnnotationsType_model(models.Model):
    Annotation = models.ForeignKey(
        "AnnotationType_model",
        on_delete=models.CASCADE,
        related_name="AnnotationsType_Annotation_AnnotationType",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class AssemblageType_model(models.Model):
    ID = models.CharField(max_length=1000, )
    AssemblageName = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="AssemblageType_AssemblageName_StringL",
        blank=True, null=True,
    )
    ResourceURIs = models.ForeignKey(
        "ResourceURIsType7_model",
        on_delete=models.CASCADE,
        related_name="AssemblageType_ResourceURIs_ResourceURIsType7",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class AssemblagesType_model(models.Model):
    Assemblage = models.ForeignKey(
        "AssemblageType_model",
        on_delete=models.CASCADE,
        related_name="AssemblagesType_Assemblage_AssemblageType",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class AssociatedTaxaType_model(models.Model):
    AssociatedTaxon = models.ForeignKey(
        "TaxonIdentified_model",
        on_delete=models.CASCADE,
        related_name="AssociatedTaxaType_AssociatedTaxon_TaxonIdentified",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class AssociationType_model(models.Model):
    GUID = models.CharField(max_length=1000, blank=True, null=True)
    ID = models.CharField(max_length=1000, )
    SourceID = models.CharField(max_length=1000, )
    SourceInstitutionID = models.CharField(max_length=1000, )
    KindOfUnit = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="AssociationType_KindOfUnit_StringL",
        blank=True, null=True,
    )
    AssociationType = models.ForeignKey(
        "AssociationType_model",
        on_delete=models.CASCADE,
        related_name="AssociationType_AssociationType_AssociationType",
    )
    DirectAccessURL = models.CharField(max_length=1000, blank=True, null=True)
    Notes = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="AssociationType_Notes_StringL",
        blank=True, null=True,
    )
    ResourceURIs = models.ForeignKey(
        "ResourceURIsType6_model",
        on_delete=models.CASCADE,
        related_name="AssociationType_ResourceURIs_ResourceURIsType6",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class AssociationsType_model(models.Model):
    Association = models.ForeignKey(
        "AssociationType_model",
        on_delete=models.CASCADE,
        related_name="AssociationsType_Association_AssociationType",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class AtomizedNameType_model(models.Model):
    InheritedName = models.CharField(max_length=1000, )
    Prefix = models.CharField(max_length=1000, blank=True, null=True)
    Suffix = models.CharField(max_length=1000, blank=True, null=True)
    GivenNames = models.CharField(max_length=1000, blank=True, null=True)
    PreferredName = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class AudioType_model(models.Model):
    Microphone = models.CharField(max_length=1000, blank=True, null=True)
    AudioChannel = models.CharField(max_length=1000, blank=True, null=True)
    DurationTimeCode = models.CharField(max_length=1000, blank=True, null=True)
    CodecName = models.CharField(max_length=1000, blank=True, null=True)
    CodecQuality = models.CharField(max_length=1000, blank=True, null=True)
    AudioEncoding = models.CharField(max_length=1000, blank=True, null=True)
    SamplingRate = models.FloatField(blank=True, null=True)
    AudioBitrate = models.CharField(max_length=1000, blank=True, null=True)
    Parabola = models.CharField(max_length=1000, blank=True, null=True)
    CarrierFrequency = models.CharField(max_length=1000, blank=True, null=True)
    PulseRepetitionRate = models.CharField(max_length=1000, blank=True, null=True)
    PulseLength = models.CharField(max_length=1000, blank=True, null=True)
    PulseFrequencyContour = models.CharField(max_length=1000, blank=True, null=True)
    PulseEnergyContour = models.CharField(max_length=1000, blank=True, null=True)
    PulseTimeEncodedSignal = models.CharField(max_length=1000, blank=True, null=True)
    PulseMaximumAmplitude = models.CharField(max_length=1000, blank=True, null=True)
    PulseFrequencyModulations = models.CharField(max_length=1000, blank=True, null=True)
    PulseDistanceRegularity = models.CharField(max_length=1000, blank=True, null=True)
    PulseGrouping = models.CharField(max_length=1000, blank=True, null=True)
    Speed = models.FloatField(blank=True, null=True)
    Pitch = models.CharField(max_length=1000, blank=True, null=True)
    Volume = models.CharField(max_length=1000, blank=True, null=True)
    CallType = models.CharField(max_length=1000, blank=True, null=True)
    NumberOfNotes = models.CharField(max_length=1000, blank=True, null=True)
    Chapters = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class BiostratigraphicTermsType_model(models.Model):
    BiostratigraphicTerm = models.ForeignKey(
        "StratigraphicTermL_model",
        on_delete=models.CASCADE,
        related_name="BiostratigraphicTermsType_BiostratigraphicTerm_StratigraphicTermL",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class BiotopeType_model(models.Model):
    ClassificationScheme = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="BiotopeType_ClassificationScheme_StringL",
        blank=True, null=True,
    )
    Name = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="BiotopeType_Name_StringL",
        blank=True, null=True,
    )
    Text = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="BiotopeType_Text_StringL",
        blank=True, null=True,
    )
    MeasurementsOrFacts = models.ForeignKey(
        "MeasurementsOrFactsType_model",
        on_delete=models.CASCADE,
        related_name="BiotopeType_MeasurementsOrFacts_MeasurementsOrFactsType",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class BotanicalGardenUnit_model(models.Model):
    AccessionSpecimenNumbers = models.IntegerField(blank=True, null=True)
    LocationInGarden = models.CharField(max_length=1000, blank=True, null=True)
    AccessionMaterialType = models.CharField(max_length=1000, blank=True, null=True)
    Hardiness = models.NullBooleanField(blank=True, null=True)
    ProvenanceCategory = models.CharField(max_length=1000, blank=True, null=True)
    PropagationHistoryCode = models.CharField(max_length=1000, blank=True, null=True)
    AccessionLineage = models.CharField(max_length=1000, blank=True, null=True)
    Cultivation = models.CharField(max_length=1000, blank=True, null=True)
    PlantingDate = models.CharField(max_length=1000, blank=True, null=True)
    Propagation = models.CharField(max_length=1000, blank=True, null=True)
    Perennation = models.CharField(max_length=1000, blank=True, null=True)
    BreedingSystem = models.CharField(max_length=1000, blank=True, null=True)
    IPEN = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class ChronostratigraphicTermsType_model(models.Model):
    ChronostratigraphicTerm = models.ForeignKey(
        "StratigraphicTermL_model",
        on_delete=models.CASCADE,
        related_name="ChronostratigraphicTermsType_ChronostratigraphicTerm_StratigraphicTermL",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class Contact_model(models.Model):
    UnformattedValue = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="Contact_UnformattedValue_StringL",
        blank=True, null=True,
    )
    Organization = models.ForeignKey(
        "Organization_model",
        on_delete=models.CASCADE,
        related_name="Contact_Organization_Organization",
        blank=True, null=True,
    )
    Person = models.ForeignKey(
        "PersonName_model",
        on_delete=models.CASCADE,
        related_name="Contact_Person_PersonName",
        blank=True, null=True,
    )
    Roles = models.ForeignKey(
        "RolesType_model",
        on_delete=models.CASCADE,
        related_name="Contact_Roles_RolesType",
        blank=True, null=True,
    )
    Addresses = models.ForeignKey(
        "AddressesType_model",
        on_delete=models.CASCADE,
        related_name="Contact_Addresses_AddressesType",
        blank=True, null=True,
    )
    TelephoneNumbers = models.ForeignKey(
        "TelephoneNumbersType_model",
        on_delete=models.CASCADE,
        related_name="Contact_TelephoneNumbers_TelephoneNumbersType",
        blank=True, null=True,
    )
    EmailAddresses = models.ForeignKey(
        "EmailAddressesType_model",
        on_delete=models.CASCADE,
        related_name="Contact_EmailAddresses_EmailAddressesType",
        blank=True, null=True,
    )
    WebsiteURL = models.CharField(max_length=1000, blank=True, null=True)
    ResourceURIs = models.ForeignKey(
        "ResourceURIsType11_model",
        on_delete=models.CASCADE,
        related_name="Contact_ResourceURIs_ResourceURIsType11",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class ContactP_model(models.Model):
    Contact = models.ForeignKey(
        "Contact_model",
        on_delete=models.CASCADE,
    )
    preferred = models.NullBooleanField(blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class ContentContactType_model(models.Model):
    Contact = models.ForeignKey(
        "Contact_model",
        on_delete=models.CASCADE,
    )
    preferred = models.NullBooleanField(blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class ContentContactsType_model(models.Model):
    ContentContact = models.ForeignKey(
        "ContactP_model",
        on_delete=models.CASCADE,
        related_name="ContentContactsType_ContentContact_ContactP",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class ContentContactsType3_model(models.Model):
    ContentContact = models.ForeignKey(
        "ContentContactType_model",
        on_delete=models.CASCADE,
        related_name="ContentContactsType3_ContentContact_ContentContactType",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class ContentMetadata_model(models.Model):
    Description = models.ForeignKey(
        "DescriptionType_model",
        on_delete=models.CASCADE,
        related_name="ContentMetadata_Description_DescriptionType",
    )
    LogoURL = models.CharField(max_length=1000, blank=True, null=True)
    Scope = models.ForeignKey(
        "ScopeType_model",
        on_delete=models.CASCADE,
        related_name="ContentMetadata_Scope_ScopeType",
        blank=True, null=True,
    )
    Version = models.ForeignKey(
        "VersionType_model",
        on_delete=models.CASCADE,
        related_name="ContentMetadata_Version_VersionType",
        blank=True, null=True,
    )
    RevisionData = models.ForeignKey(
        "RevisionData_model",
        on_delete=models.CASCADE,
        related_name="ContentMetadata_RevisionData_RevisionData",
    )
    Owners = models.ForeignKey(
        "OwnersType_model",
        on_delete=models.CASCADE,
        related_name="ContentMetadata_Owners_OwnersType",
        blank=True, null=True,
    )
    LegalStatements = models.ForeignKey(
        "LegalStatements_model",
        on_delete=models.CASCADE,
        related_name="ContentMetadata_LegalStatements_LegalStatements",
        blank=True, null=True,
    )
    InformationWithheld = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="ContentMetadata_InformationWithheld_StringL",
        blank=True, null=True,
    )
    DirectAccessURL = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class CoordinateSetType_model(models.Model):
    original = models.NullBooleanField(blank=True, null=True)
    begin = models.NullBooleanField(blank=True, null=True)
    end = models.NullBooleanField(blank=True, null=True)
    Method = models.CharField(max_length=1000, blank=True, null=True)
    References = models.ForeignKey(
        "ReferencesType_model",
        on_delete=models.CASCADE,
        related_name="CoordinateSetType_References_ReferencesType",
        blank=True, null=True,
    )
    VerificationStatus = models.CharField(max_length=1000, blank=True, null=True)
    Notes = models.CharField(max_length=1000, blank=True, null=True)
    CoordinatesUTM = models.ForeignKey(
        "CoordinatesUTMType_model",
        on_delete=models.CASCADE,
        related_name="CoordinateSetType_CoordinatesUTM_CoordinatesUTMType",
        blank=True, null=True,
    )
    CoordinatesGrid = models.ForeignKey(
        "CoordinatesGridType_model",
        on_delete=models.CASCADE,
        related_name="CoordinateSetType_CoordinatesGrid_CoordinatesGridType",
        blank=True, null=True,
    )
    CoordinatesLatLong = models.ForeignKey(
        "CoordinatesLatLongType_model",
        on_delete=models.CASCADE,
        related_name="CoordinateSetType_CoordinatesLatLong_CoordinatesLatLongType",
        blank=True, null=True,
    )
    EPSGID = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class CoordinateSetsType_model(models.Model):
    CoordinateSet = models.ForeignKey(
        "CoordinateSetType_model",
        on_delete=models.CASCADE,
        related_name="CoordinateSetsType_CoordinateSet_CoordinateSetType",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class CoordinatesGridType_model(models.Model):
    GridCellSystem = models.CharField(max_length=1000, )
    GridCellCode = models.CharField(max_length=1000, )
    GridQualifier = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class CoordinatesLatLongType_model(models.Model):
    LongitudeDecimal = models.FloatField(blank=True, null=True)
    VerbatimLongitude = models.CharField(max_length=1000, blank=True, null=True)
    LatitudeDecimal = models.FloatField(blank=True, null=True)
    VerbatimLatitude = models.CharField(max_length=1000, blank=True, null=True)
    SpatialDatum = models.CharField(max_length=1000, blank=True, null=True)
    Accuracy = models.CharField(max_length=1000, blank=True, null=True)
    ErrorDistanceInMeters = models.FloatField(blank=True, null=True)
    ErrorMethod = models.CharField(max_length=1000, blank=True, null=True)
    PointRadiusSpatialFit = models.CharField(max_length=1000, blank=True, null=True)
    CoordinatesText = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class CoordinatesUTMType_model(models.Model):
    UTMZone = models.IntegerField(blank=True, null=True)
    UTMSubzone = models.CharField(max_length=1000, blank=True, null=True)
    UTMNS = models.CharField(max_length=1000, blank=True, null=True)
    UTMZoneFull = models.CharField(max_length=1000, blank=True, null=True)
    UTMEasting = models.CharField(max_length=1000, blank=True, null=True)
    UTMNorthing = models.CharField(max_length=1000, blank=True, null=True)
    UTMDatum = models.CharField(max_length=1000, blank=True, null=True)
    UTMText = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class Country_model(models.Model):
    Name = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="Country_Name_StringL",
        blank=True, null=True,
    )
    DerivedFlag = models.NullBooleanField(blank=True, null=True)
    ISO3166Code = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class CreatorsType_model(models.Model):
    Creator = models.CharField(max_length=1000, )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class CultureCollectionUnit_model(models.Model):
    OrganismType = models.CharField(max_length=1000, blank=True, null=True)
    InfrasubspecificName = models.CharField(max_length=1000, blank=True, null=True)
    CultureNames = models.ForeignKey(
        "CultureNamesType_model",
        on_delete=models.CASCADE,
        related_name="CultureCollectionUnit_CultureNames_CultureNamesType",
        blank=True, null=True,
    )
    Strain = models.CharField(max_length=1000, blank=True, null=True)
    SerovarOrSerotype = models.CharField(max_length=1000, blank=True, null=True)
    Pathovar = models.CharField(max_length=1000, blank=True, null=True)
    Mutant = models.CharField(max_length=1000, blank=True, null=True)
    Genotype = models.CharField(max_length=1000, blank=True, null=True)
    GrowthConditions = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="CultureCollectionUnit_GrowthConditions_StringL",
        blank=True, null=True,
    )
    GrowthConditionsAtomized = models.ForeignKey(
        "GrowthConditionsAtomizedType_model",
        on_delete=models.CASCADE,
        related_name="CultureCollectionUnit_GrowthConditionsAtomized_GrowthConditionsAtomizedType",
        blank=True, null=True,
    )
    References = models.ForeignKey(
        "ReferencesType12_model",
        on_delete=models.CASCADE,
        related_name="CultureCollectionUnit_References_ReferencesType12",
        blank=True, null=True,
    )
    FormOfSupply = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="CultureCollectionUnit_FormOfSupply_StringL",
        blank=True, null=True,
    )
    Applications = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="CultureCollectionUnit_Applications_StringL",
        blank=True, null=True,
    )
    Hazard = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="CultureCollectionUnit_Hazard_StringL",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class CultureNamesType_model(models.Model):
    CultureName = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="CultureNamesType_CultureName_StringL",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class DataSetType_model(models.Model):
    GUID = models.CharField(max_length=1000, blank=True, null=True)
    ID = models.CharField(max_length=1000, blank=True, null=True)
    ResourceURIs = models.ForeignKey(
        "ResourceURIsType_model",
        on_delete=models.CASCADE,
        related_name="DataSetType_ResourceURIs_ResourceURIsType",
        blank=True, null=True,
    )
    TechnicalContacts = models.ForeignKey(
        "TechnicalContactsType_model",
        on_delete=models.CASCADE,
        related_name="DataSetType_TechnicalContacts_TechnicalContactsType",
        blank=True, null=True,
    )
    ContentContacts = models.ForeignKey(
        "ContentContactsType_model",
        on_delete=models.CASCADE,
        related_name="DataSetType_ContentContacts_ContentContactsType",
    )
    DataCenter = models.CharField(max_length=1000, blank=True, null=True)
    OtherProviders = models.ForeignKey(
        "OtherProvidersType_model",
        on_delete=models.CASCADE,
        related_name="DataSetType_OtherProviders_OtherProvidersType",
        blank=True, null=True,
    )
    Metadata = models.ForeignKey(
        "ContentMetadata_model",
        on_delete=models.CASCADE,
        related_name="DataSetType_Metadata_ContentMetadata",
    )
    Units = models.ForeignKey(
        "UnitsType_model",
        on_delete=models.CASCADE,
        related_name="DataSetType_Units_UnitsType",
    )
    DataSetExtension = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class DataSets_model(models.Model):
    DataSet = models.ForeignKey(
        "DataSetType_model",
        on_delete=models.CASCADE,
        related_name="DataSets_DataSet_DataSetType",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class DateTime_model(models.Model):
    DateText = models.CharField(max_length=1000, blank=True, null=True)
    TimeZone = models.CharField(max_length=1000, blank=True, null=True)
    ISODateTimeBegin = models.CharField(max_length=1000, blank=True, null=True)
    TimeOfDayBegin = models.TimeField(blank=True, null=True)
    ISODateTimeEnd = models.CharField(max_length=1000, blank=True, null=True)
    TimeOfDayEnd = models.TimeField(blank=True, null=True)
    PeriodExplicit = models.NullBooleanField(blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class DescriptionType_model(models.Model):
    Representation = models.ForeignKey(
        "MetadataDescriptionRepr_model",
        on_delete=models.CASCADE,
        related_name="DescriptionType_Representation_MetadataDescriptionRepr",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class DivisionsType_model(models.Model):
    Division = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="DivisionsType_Division_StringL",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class EmailAddressesType_model(models.Model):
    EmailAddress = models.ForeignKey(
        "StringP255_model",
        on_delete=models.CASCADE,
        related_name="EmailAddressesType_EmailAddress_StringP255",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class FieldNotesReferencesType_model(models.Model):
    FieldNotesReference = models.ForeignKey(
        "Reference_model",
        on_delete=models.CASCADE,
        related_name="FieldNotesReferencesType_FieldNotesReference_Reference",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class FieldNumberType_model(models.Model):
    ID = models.CharField(max_length=1000, )
    CollectorName = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class FieldNumbersType_model(models.Model):
    FieldNumber = models.ForeignKey(
        "FieldNumberType_model",
        on_delete=models.CASCADE,
        related_name="FieldNumbersType_FieldNumber_FieldNumberType",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class Gathering_model(models.Model):
    ID = models.CharField(max_length=1000, blank=True, null=True)
    Date = models.ForeignKey(
        "DateTime_model",
        on_delete=models.CASCADE,
        related_name="Gathering_Date_DateTime",
        blank=True, null=True,
    )
    GatheringAgents = models.ForeignKey(
        "GatheringAgentsType_model",
        on_delete=models.CASCADE,
        related_name="Gathering_GatheringAgents_GatheringAgentsType",
        blank=True, null=True,
    )
    GatheringAgentsText = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="Gathering_GatheringAgentsText_StringL",
        blank=True, null=True,
    )
    Permits = models.ForeignKey(
        "PermitsType_model",
        on_delete=models.CASCADE,
        related_name="Gathering_Permits_PermitsType",
        blank=True, null=True,
    )
    Project = models.ForeignKey(
        "ProjectType_model",
        on_delete=models.CASCADE,
        related_name="Gathering_Project_ProjectType",
        blank=True, null=True,
    )
    PlatformName = models.CharField(max_length=1000, blank=True, null=True)
    Method = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="Gathering_Method_StringL",
        blank=True, null=True,
    )
    ValidDistributionFlag = models.NullBooleanField(blank=True, null=True)
    EstablishmentMeans = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="Gathering_EstablishmentMeans_StringL",
        blank=True, null=True,
    )
    LocalityText = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="Gathering_LocalityText_StringL",
        blank=True, null=True,
    )
    Country = models.ForeignKey(
        "Country_model",
        on_delete=models.CASCADE,
        related_name="Gathering_Country_Country",
        blank=True, null=True,
    )
    NamedAreas = models.ForeignKey(
        "NamedAreasType_model",
        on_delete=models.CASCADE,
        related_name="Gathering_NamedAreas_NamedAreasType",
        blank=True, null=True,
    )
    NamedPlaceRelations = models.ForeignKey(
        "NamedPlaceRelationsType_model",
        on_delete=models.CASCADE,
        related_name="Gathering_NamedPlaceRelations_NamedPlaceRelationsType",
        blank=True, null=True,
    )
    Details = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="Gathering_Details_StringL",
        blank=True, null=True,
    )
    GML = models.CharField(max_length=1000, blank=True, null=True)
    WFS = models.CharField(max_length=1000, blank=True, null=True)
    WMSURL = models.CharField(max_length=1000, blank=True, null=True)
    CoordinateSets = models.ForeignKey(
        "CoordinateSetsType_model",
        on_delete=models.CASCADE,
        related_name="Gathering_CoordinateSets_CoordinateSetsType",
        blank=True, null=True,
    )
    Altitude = models.ForeignKey(
        "MeasurementOrFact_model",
        on_delete=models.CASCADE,
        related_name="Gathering_Altitude_MeasurementOrFact",
        blank=True, null=True,
    )
    Depth = models.ForeignKey(
        "MeasurementOrFact_model",
        on_delete=models.CASCADE,
        related_name="Gathering_Depth_MeasurementOrFact",
        blank=True, null=True,
    )
    Height = models.ForeignKey(
        "MeasurementOrFact_model",
        on_delete=models.CASCADE,
        related_name="Gathering_Height_MeasurementOrFact",
        blank=True, null=True,
    )
    Aspect = models.ForeignKey(
        "MeasurementOrFact_model",
        on_delete=models.CASCADE,
        related_name="Gathering_Aspect_MeasurementOrFact",
        blank=True, null=True,
    )
    OtherMeasurementsOrFacts = models.ForeignKey(
        "OtherMeasurementsOrFactsType_model",
        on_delete=models.CASCADE,
        related_name="Gathering_OtherMeasurementsOrFacts_OtherMeasurementsOrFactsType",
        blank=True, null=True,
    )
    MultimediaObjects = models.ForeignKey(
        "MultimediaObjectsType_model",
        on_delete=models.CASCADE,
        related_name="Gathering_MultimediaObjects_MultimediaObjectsType",
        blank=True, null=True,
    )
    Stratigraphy = models.ForeignKey(
        "Stratigraphy_model",
        on_delete=models.CASCADE,
        related_name="Gathering_Stratigraphy_Stratigraphy",
        blank=True, null=True,
    )
    Biotope = models.ForeignKey(
        "BiotopeType_model",
        on_delete=models.CASCADE,
        related_name="Gathering_Biotope_BiotopeType",
        blank=True, null=True,
    )
    Synecology = models.ForeignKey(
        "SynecologyType_model",
        on_delete=models.CASCADE,
        related_name="Gathering_Synecology_SynecologyType",
        blank=True, null=True,
    )
    Notes = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="Gathering_Notes_StringL",
        blank=True, null=True,
    )
    FootprintWKT = models.CharField(max_length=1000, blank=True, null=True)
    FootprintSpatialFit = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class GatheringAgentType_model(models.Model):
    Contact = models.ForeignKey(
        "Contact_model",
        on_delete=models.CASCADE,
    )
    sequence = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class GatheringAgentsType_model(models.Model):
    GatheringAgent = models.ForeignKey(
        "GatheringAgentType_model",
        on_delete=models.CASCADE,
        related_name="GatheringAgentsType_GatheringAgent_GatheringAgentType",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class GeoecologicalTermsType_model(models.Model):
    GeoecologicalTerm = models.ForeignKey(
        "StringL255_model",
        on_delete=models.CASCADE,
        related_name="GeoecologicalTermsType_GeoecologicalTerm_StringL255",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class GrowthConditionAtomized_model(models.Model):
    CultureMedium = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="GrowthConditionAtomized_CultureMedium_StringL",
        blank=True, null=True,
    )
    Aerobicity = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="GrowthConditionAtomized_Aerobicity_StringL",
        blank=True, null=True,
    )
    Temperature = models.ForeignKey(
        "Temperature_model",
        on_delete=models.CASCADE,
        related_name="GrowthConditionAtomized_Temperature_Temperature",
        blank=True, null=True,
    )
    References = models.ForeignKey(
        "ReferencesType13_model",
        on_delete=models.CASCADE,
        related_name="GrowthConditionAtomized_References_ReferencesType13",
        blank=True, null=True,
    )
    GrowthConditionsMeasurementsOrFacts = models.ForeignKey(
        "GrowthConditionsMeasurementsOrFactsType_model",
        on_delete=models.CASCADE,
        related_name="GrowthConditionAtomized_GrowthConditionsMeasurementsOrFacts_GrowthConditionsMeasurementsOrFactsType",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class GrowthConditionsAtomizedType_model(models.Model):
    GrowthConditionAtomized = models.ForeignKey(
        "GrowthConditionAtomized_model",
        on_delete=models.CASCADE,
        related_name="GrowthConditionsAtomizedType_GrowthConditionAtomized_GrowthConditionAtomized",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class GrowthConditionsMeasurementsOrFactsType_model(models.Model):
    GrowthConditionsMeasurementOrFact = models.ForeignKey(
        "MeasurementOrFact_model",
        on_delete=models.CASCADE,
        related_name="GrowthConditionsMeasurementsOrFactsType_GrowthConditionsMeasurementOrFact_MeasurementOrFact",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class HerbariumUnit_model(models.Model):
    Exsiccatum = models.CharField(max_length=1000, blank=True, null=True)
    LoanID = models.CharField(max_length=1000, blank=True, null=True)
    LoanSequenceNumber = models.IntegerField(blank=True, null=True)
    LoanDestination = models.CharField(max_length=1000, blank=True, null=True)
    LoanForBotanist = models.CharField(max_length=1000, blank=True, null=True)
    LoanDispatchMethod = models.CharField(max_length=1000, blank=True, null=True)
    LoanDate = models.DateField(blank=True, null=True)
    LoanReturnDate = models.DateField(blank=True, null=True)
    NaturalOccurrence = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="HerbariumUnit_NaturalOccurrence_StringL",
        blank=True, null=True,
    )
    CultivatedOccurrence = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="HerbariumUnit_CultivatedOccurrence_StringL",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class HigherTaxaType_model(models.Model):
    HigherTaxon = models.ForeignKey(
        "HigherTaxon_model",
        on_delete=models.CASCADE,
        related_name="HigherTaxaType_HigherTaxon_HigherTaxon",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class HigherTaxon_model(models.Model):
    HigherTaxonName = models.CharField(max_length=1000, )
    HigherTaxonRank = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class HybridFlagType_model(models.Model):
    insertionpoint = models.IntegerField(blank=True, null=True)
    valueOf_x = models.CharField(max_length=1000, )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class Identification_model(models.Model):
    Result = models.ForeignKey(
        "ResultType_model",
        on_delete=models.CASCADE,
        related_name="Identification_Result_ResultType",
    )
    PreferredFlag = models.NullBooleanField(blank=True, null=True)
    NegativeIdentificationFlag = models.NullBooleanField(blank=True, null=True)
    StoredUnderFlag = models.NullBooleanField(blank=True, null=True)
    ResultRole = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="Identification_ResultRole_StringL",
        blank=True, null=True,
    )
    Identifiers = models.ForeignKey(
        "IdentifiersType_model",
        on_delete=models.CASCADE,
        related_name="Identification_Identifiers_IdentifiersType",
        blank=True, null=True,
    )
    IdentifierRole = models.CharField(max_length=1000, blank=True, null=True)
    IdentificationSource = models.ForeignKey(
        "Reference_model",
        on_delete=models.CASCADE,
        related_name="Identification_IdentificationSource_Reference",
        blank=True, null=True,
    )
    References = models.ForeignKey(
        "ReferencesType2_model",
        on_delete=models.CASCADE,
        related_name="Identification_References_ReferencesType2",
        blank=True, null=True,
    )
    Date = models.ForeignKey(
        "DateTime_model",
        on_delete=models.CASCADE,
        related_name="Identification_Date_DateTime",
        blank=True, null=True,
    )
    Method = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="Identification_Method_StringL",
        blank=True, null=True,
    )
    Notes = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="Identification_Notes_StringL",
        blank=True, null=True,
    )
    VerificationLevel = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class IdentificationQualifierType_model(models.Model):
    insertionpoint = models.IntegerField(blank=True, null=True)
    valueOf_x = models.CharField(max_length=1000, )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class IdentificationsType_model(models.Model):
    Identification = models.ForeignKey(
        "Identification_model",
        on_delete=models.CASCADE,
        related_name="IdentificationsType_Identification_Identification",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class IdentifiersType_model(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    Identifier = models.ForeignKey(
        "Contact_model",
        on_delete=models.CASCADE,
        related_name="IdentifiersType_Identifier_Contact",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class ImageType_model(models.Model):
    LensModel = models.CharField(max_length=1000, blank=True, null=True)
    FNumber = models.FloatField(blank=True, null=True)
    FocalLength = models.FloatField(blank=True, null=True)
    FocalLengthIn35mmFilm = models.FloatField(blank=True, null=True)
    LightSource = models.CharField(max_length=1000, blank=True, null=True)
    Flash = models.CharField(max_length=1000, blank=True, null=True)
    FlashEnergy = models.CharField(max_length=1000, blank=True, null=True)
    WhiteBalance = models.CharField(max_length=1000, blank=True, null=True)
    DigitalZoomRatio = models.CharField(max_length=1000, blank=True, null=True)
    Contrast = models.CharField(max_length=1000, blank=True, null=True)
    Saturation = models.CharField(max_length=1000, blank=True, null=True)
    Sharpness = models.CharField(max_length=1000, blank=True, null=True)
    Gamma = models.CharField(max_length=1000, blank=True, null=True)
    ColorSpace = models.CharField(max_length=1000, blank=True, null=True)
    ImageSize = models.ForeignKey(
        "imageSize_model",
        on_delete=models.CASCADE,
        related_name="ImageType_ImageSize_imageSize",
        blank=True, null=True,
    )
    ImageResolution = models.IntegerField(blank=True, null=True)
    ExposureTime = models.CharField(max_length=1000, blank=True, null=True)
    ExposureMode = models.CharField(max_length=1000, blank=True, null=True)
    SpectralSensitivity = models.CharField(max_length=1000, blank=True, null=True)
    PhotographicSensitivity = models.CharField(max_length=1000, blank=True, null=True)
    ISOSpeed = models.CharField(max_length=1000, blank=True, null=True)
    ShutterSpeed = models.IntegerField(blank=True, null=True)
    Brightness = models.CharField(max_length=1000, blank=True, null=True)
    Color = models.CharField(max_length=1000, blank=True, null=True)
    ThumbnailURL = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class ImagesType_model(models.Model):
    ImageID = models.CharField(max_length=1000, )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class Label_model(models.Model):
    Representation = models.ForeignKey(
        "RepresentationType_model",
        on_delete=models.CASCADE,
        related_name="Label_Representation_RepresentationType",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class LabelRepr_model(models.Model):
    language = models.CharField(max_length=1000, )
    Text = models.CharField(max_length=1000, )
    Abbreviation = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class LegalStatement_model(models.Model):
    language = models.CharField(max_length=1000, )
    Text = models.CharField(max_length=1000, )
    Details = models.CharField(max_length=1000, blank=True, null=True)
    WebsiteURL = models.CharField(max_length=1000, blank=True, null=True)
    ResourceURI = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class LegalStatements_model(models.Model):
    Licenses = models.ForeignKey(
        "LicensesType_model",
        on_delete=models.CASCADE,
        related_name="LegalStatements_Licenses_LicensesType",
        blank=True, null=True,
    )
    Acknowledgements = models.ForeignKey(
        "AcknowledgementsType_model",
        on_delete=models.CASCADE,
        related_name="LegalStatements_Acknowledgements_AcknowledgementsType",
        blank=True, null=True,
    )
    SuggestedCitations = models.ForeignKey(
        "SuggestedCitationsType_model",
        on_delete=models.CASCADE,
        related_name="LegalStatements_SuggestedCitations_SuggestedCitationsType",
        blank=True, null=True,
    )
    OtherLegalStatements = models.ForeignKey(
        "OtherLegalStatementsType_model",
        on_delete=models.CASCADE,
        related_name="LegalStatements_OtherLegalStatements_OtherLegalStatementsType",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class LicensesType_model(models.Model):
    License = models.ForeignKey(
        "LegalStatement_model",
        on_delete=models.CASCADE,
        related_name="LicensesType_License_LegalStatement",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class LithostratigraphicTermsType_model(models.Model):
    LithostratigraphicTerm = models.ForeignKey(
        "StratigraphicTermL_model",
        on_delete=models.CASCADE,
        related_name="LithostratigraphicTermsType_LithostratigraphicTerm_StratigraphicTermL",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class LoanRestrictionsType_model(models.Model):
    BlockedUntil = models.CharField(max_length=1000, blank=True, null=True)
    Blocked = models.NullBooleanField(blank=True, null=True)
    LoanConditions = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class MarkType_model(models.Model):
    MarkType = models.ForeignKey(
        "MarkType_model",
        on_delete=models.CASCADE,
        related_name="MarkType_MarkType_MarkType",
        blank=True, null=True,
    )
    MarkText = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="MarkType_MarkText_StringL",
        blank=True, null=True,
    )
    PositionOnObject = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="MarkType_PositionOnObject_StringL",
        blank=True, null=True,
    )
    MarkAuthor = models.CharField(max_length=1000, blank=True, null=True)
    MarkComment = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="MarkType_MarkComment_StringL",
        blank=True, null=True,
    )
    Images = models.ForeignKey(
        "ImagesType_model",
        on_delete=models.CASCADE,
        related_name="MarkType_Images_ImagesType",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class MarksType_model(models.Model):
    Mark = models.ForeignKey(
        "MarkType_model",
        on_delete=models.CASCADE,
        related_name="MarksType_Mark_MarkType",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class MeasurementOrFact_model(models.Model):
    MeasurementOrFactAtomized = models.ForeignKey(
        "MeasurementOrFactAtomizedType_model",
        on_delete=models.CASCADE,
        related_name="MeasurementOrFact_MeasurementOrFactAtomized_MeasurementOrFactAtomizedType",
        blank=True, null=True,
    )
    MeasurementOrFactText = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="MeasurementOrFact_MeasurementOrFactText_StringL",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class MeasurementOrFactAtomizedType_model(models.Model):
    MeasuredBy = models.CharField(max_length=1000, blank=True, null=True)
    MeasurementDateTime = models.CharField(max_length=1000, blank=True, null=True)
    Duration = models.CharField(max_length=1000, blank=True, null=True)
    Method = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="MeasurementOrFactAtomizedType_Method_StringL",
        blank=True, null=True,
    )
    Parameter = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="MeasurementOrFactAtomizedType_Parameter_StringL",
        blank=True, null=True,
    )
    AppliesTo = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="MeasurementOrFactAtomizedType_AppliesTo_StringL",
        blank=True, null=True,
    )
    LowerValue = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="MeasurementOrFactAtomizedType_LowerValue_StringL",
    )
    UpperValue = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="MeasurementOrFactAtomizedType_UpperValue_StringL",
        blank=True, null=True,
    )
    UnitOfMeasurement = models.CharField(max_length=1000, blank=True, null=True)
    Accuracy = models.CharField(max_length=1000, blank=True, null=True)
    MeasurementOrFactReference = models.ForeignKey(
        "Reference_model",
        on_delete=models.CASCADE,
        related_name="MeasurementOrFactAtomizedType_MeasurementOrFactReference_Reference",
        blank=True, null=True,
    )
    IsQuantitative = models.NullBooleanField(blank=True, null=True)
    ReferenceSystem = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class MeasurementsOrFactsType_model(models.Model):
    MeasurementOrFact = models.ForeignKey(
        "MeasurementOrFact_model",
        on_delete=models.CASCADE,
        related_name="MeasurementsOrFactsType_MeasurementOrFact_MeasurementOrFact",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class MeasurementsOrFactsType8_model(models.Model):
    MeasurementOrFact = models.ForeignKey(
        "MeasurementOrFact_model",
        on_delete=models.CASCADE,
        related_name="MeasurementsOrFactsType8_MeasurementOrFact_MeasurementOrFact",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class MetadataDescriptionRepr_model(models.Model):
    language = models.CharField(max_length=1000, )
    Title = models.CharField(max_length=1000, )
    Details = models.CharField(max_length=1000, blank=True, null=True)
    Coverage = models.CharField(max_length=1000, blank=True, null=True)
    WebsiteURL = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class MultimediaObject_model(models.Model):
    ID = models.CharField(max_length=1000, blank=True, null=True)
    Type = models.CharField(max_length=1000, blank=True, null=True)
    Title = models.CharField(max_length=1000, blank=True, null=True)
    IDofContainingCollection = models.CharField(max_length=1000, blank=True, null=True)
    Source = models.ForeignKey(
        "Reference_model",
        on_delete=models.CASCADE,
        related_name="MultimediaObject_Source_Reference",
        blank=True, null=True,
    )
    Provider = models.CharField(max_length=1000, blank=True, null=True)
    FileURL = models.CharField(max_length=1000, )
    ProductURL = models.CharField(max_length=1000, blank=True, null=True)
    Context = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="MultimediaObject_Context_StringL",
        blank=True, null=True,
    )
    Tags = models.ForeignKey(
        "TagsType_model",
        on_delete=models.CASCADE,
        related_name="MultimediaObject_Tags_TagsType",
        blank=True, null=True,
    )
    Ratings = models.ForeignKey(
        "RatingsType_model",
        on_delete=models.CASCADE,
        related_name="MultimediaObject_Ratings_RatingsType",
        blank=True, null=True,
    )
    FileFormat = models.CharField(max_length=1000, blank=True, null=True)
    FileFormatVersion = models.CharField(max_length=1000, blank=True, null=True)
    FileSize = models.CharField(max_length=1000, blank=True, null=True)
    PhysicalFormat = models.CharField(max_length=1000, blank=True, null=True)
    PhysicalObjectID = models.CharField(max_length=1000, blank=True, null=True)
    DateCreated = models.CharField(max_length=1000, blank=True, null=True)
    Creators = models.ForeignKey(
        "CreatorsType_model",
        on_delete=models.CASCADE,
        related_name="MultimediaObject_Creators_CreatorsType",
        blank=True, null=True,
    )
    Modified = models.CharField(max_length=1000, blank=True, null=True)
    LegalStatements = models.ForeignKey(
        "LegalStatements_model",
        on_delete=models.CASCADE,
        related_name="MultimediaObject_LegalStatements_LegalStatements",
        blank=True, null=True,
    )
    Notes = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="MultimediaObject_Notes_StringL",
        blank=True, null=True,
    )
    Sex = models.CharField(max_length=1000, blank=True, null=True)
    LifeStage = models.CharField(max_length=1000, blank=True, null=True)
    SubjectPart = models.CharField(max_length=1000, blank=True, null=True)
    SubjectOrientation = models.CharField(max_length=1000, blank=True, null=True)
    SubjectDistance = models.CharField(max_length=1000, blank=True, null=True)
    TaxaInBackground = models.ForeignKey(
        "TaxaInBackgroundType_model",
        on_delete=models.CASCADE,
        related_name="MultimediaObject_TaxaInBackground_TaxaInBackgroundType",
        blank=True, null=True,
    )
    RecordingEnvironment = models.CharField(max_length=1000, blank=True, null=True)
    Temperature = models.ForeignKey(
        "Temperature_model",
        on_delete=models.CASCADE,
        related_name="MultimediaObject_Temperature_Temperature",
        blank=True, null=True,
    )
    LightCondition = models.CharField(max_length=1000, blank=True, null=True)
    PlaybackUsed = models.NullBooleanField(blank=True, null=True)
    CaptureEquipment = models.CharField(max_length=1000, blank=True, null=True)
    Counter = models.CharField(max_length=1000, blank=True, null=True)
    FilterUsedForRecording = models.CharField(max_length=1000, blank=True, null=True)
    MakerNote = models.CharField(max_length=1000, blank=True, null=True)
    Audio = models.ForeignKey(
        "AudioType_model",
        on_delete=models.CASCADE,
        related_name="MultimediaObject_Audio_AudioType",
        blank=True, null=True,
    )
    Video = models.ForeignKey(
        "VideoType_model",
        on_delete=models.CASCADE,
        related_name="MultimediaObject_Video_VideoType",
        blank=True, null=True,
    )
    Image = models.ForeignKey(
        "ImageType_model",
        on_delete=models.CASCADE,
        related_name="MultimediaObject_Image_ImageType",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class MultimediaObjectsType_model(models.Model):
    MultimediaObject = models.ForeignKey(
        "MultimediaObject_model",
        on_delete=models.CASCADE,
        related_name="MultimediaObjectsType_MultimediaObject_MultimediaObject",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class MultimediaObjectsType5_model(models.Model):
    MultimediaObject = models.ForeignKey(
        "MultimediaObject_model",
        on_delete=models.CASCADE,
        related_name="MultimediaObjectsType5_MultimediaObject_MultimediaObject",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class MycologicalLiveStagesType_model(models.Model):
    MycologicalLiveStage = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="MycologicalLiveStagesType_MycologicalLiveStage_StringL",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class MycologicalUnit_model(models.Model):
    LichenMorphotype = models.CharField(max_length=1000, blank=True, null=True)
    MycologicalSexualStage = models.CharField(max_length=1000, blank=True, null=True)
    MycologicalLiveStages = models.ForeignKey(
        "MycologicalLiveStagesType_model",
        on_delete=models.CASCADE,
        related_name="MycologicalUnit_MycologicalLiveStages_MycologicalLiveStagesType",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class NameAtomizedType_model(models.Model):
    Bacterial = models.ForeignKey(
        "NameBacterial_model",
        on_delete=models.CASCADE,
        related_name="NameAtomizedType_Bacterial_NameBacterial",
        blank=True, null=True,
    )
    Botanical = models.ForeignKey(
        "NameBotanical_model",
        on_delete=models.CASCADE,
        related_name="NameAtomizedType_Botanical_NameBotanical",
        blank=True, null=True,
    )
    Zoological = models.ForeignKey(
        "NameZoological_model",
        on_delete=models.CASCADE,
        related_name="NameAtomizedType_Zoological_NameZoological",
        blank=True, null=True,
    )
    Viral = models.ForeignKey(
        "NameViral_model",
        on_delete=models.CASCADE,
        related_name="NameAtomizedType_Viral_NameViral",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class NameBacterial_model(models.Model):
    GenusOrMonomial = models.CharField(max_length=1000, blank=True, null=True)
    Subgenus = models.CharField(max_length=1000, blank=True, null=True)
    SubgenusAuthorAndYear = models.CharField(max_length=1000, blank=True, null=True)
    SpeciesEpithet = models.CharField(max_length=1000, blank=True, null=True)
    SubspeciesEpithet = models.CharField(max_length=1000, blank=True, null=True)
    ParentheticalAuthorTeamAndYear = models.CharField(max_length=1000, blank=True, null=True)
    AuthorTeamAndYear = models.CharField(max_length=1000, blank=True, null=True)
    NameApprobation = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class NameBotanical_model(models.Model):
    GenusOrMonomial = models.CharField(max_length=1000, blank=True, null=True)
    FirstEpithet = models.CharField(max_length=1000, blank=True, null=True)
    InfraspecificEpithet = models.CharField(max_length=1000, blank=True, null=True)
    Rank = models.CharField(max_length=1000, blank=True, null=True)
    HybridFlag = models.ForeignKey(
        "HybridFlagType_model",
        on_delete=models.CASCADE,
        related_name="NameBotanical_HybridFlag_HybridFlagType",
        blank=True, null=True,
    )
    AuthorTeamParenthesis = models.CharField(max_length=1000, blank=True, null=True)
    AuthorTeam = models.CharField(max_length=1000, blank=True, null=True)
    CultivarGroupName = models.CharField(max_length=1000, blank=True, null=True)
    CultivarName = models.CharField(max_length=1000, blank=True, null=True)
    TradeDesignationNames = models.ForeignKey(
        "TradeDesignationNamesType_model",
        on_delete=models.CASCADE,
        related_name="NameBotanical_TradeDesignationNames_TradeDesignationNamesType",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class NameViral_model(models.Model):
    GenusOrMonomial = models.CharField(max_length=1000, blank=True, null=True)
    ViralSpeciesDesignation = models.CharField(max_length=1000, blank=True, null=True)
    Acronym = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class NameZoological_model(models.Model):
    GenusOrMonomial = models.CharField(max_length=1000, blank=True, null=True)
    Subgenus = models.CharField(max_length=1000, blank=True, null=True)
    SpeciesEpithet = models.CharField(max_length=1000, blank=True, null=True)
    SubspeciesEpithet = models.CharField(max_length=1000, blank=True, null=True)
    AuthorTeamOriginalAndYear = models.CharField(max_length=1000, blank=True, null=True)
    AuthorTeamParenthesisAndYear = models.CharField(max_length=1000, blank=True, null=True)
    CombinationAuthorTeamAndYear = models.CharField(max_length=1000, blank=True, null=True)
    Breed = models.CharField(max_length=1000, blank=True, null=True)
    NamedIndividual = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class NamedArea_model(models.Model):
    AreaClass = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="NamedArea_AreaClass_StringL",
        blank=True, null=True,
    )
    Name = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="NamedArea_Name_StringL",
        blank=True, null=True,
    )
    CodeStandard = models.CharField(max_length=1000, blank=True, null=True)
    Code = models.CharField(max_length=1000, blank=True, null=True)
    Reference = models.ForeignKey(
        "Reference_model",
        on_delete=models.CASCADE,
        related_name="NamedArea_Reference_Reference",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class NamedAreaType_model(models.Model):
    NamedArea = models.ForeignKey(
        "NamedArea_model",
        on_delete=models.CASCADE,
    )
    sequence = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class NamedAreasType_model(models.Model):
    NamedArea = models.ForeignKey(
        "NamedArea_model",
        on_delete=models.CASCADE,
        related_name="NamedAreasType_NamedArea_NamedArea",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class NamedCollectionsOrSurveysType_model(models.Model):
    NamedCollectionOrSurvey = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="NamedCollectionsOrSurveysType_NamedCollectionOrSurvey_StringL",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class NamedPlaceRelationType_model(models.Model):
    NearbyPlaceName = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="NamedPlaceRelationType_NearbyPlaceName_StringL",
        blank=True, null=True,
    )
    NearbyPlaceRelation = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="NamedPlaceRelationType_NearbyPlaceRelation_StringL",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class NamedPlaceRelationsType_model(models.Model):
    NamedPlaceRelation = models.ForeignKey(
        "NamedPlaceRelationType_model",
        on_delete=models.CASCADE,
        related_name="NamedPlaceRelationsType_NamedPlaceRelation_NamedPlaceRelationType",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class NomenclaturalTypeDesignationType_model(models.Model):
    TypifiedName = models.ForeignKey(
        "ScientificName_model",
        on_delete=models.CASCADE,
        related_name="NomenclaturalTypeDesignationType_TypifiedName_ScientificName",
        blank=True, null=True,
    )
    NomenclaturalReference = models.ForeignKey(
        "Reference_model",
        on_delete=models.CASCADE,
        related_name="NomenclaturalTypeDesignationType_NomenclaturalReference_Reference",
        blank=True, null=True,
    )
    TypeStatus = models.CharField(max_length=1000, blank=True, null=True)
    CodeAssessment = models.CharField(max_length=1000, blank=True, null=True)
    DoubtfulFlag = models.NullBooleanField(blank=True, null=True)
    Verifier = models.ForeignKey(
        "PersonName_model",
        on_delete=models.CASCADE,
        related_name="NomenclaturalTypeDesignationType_Verifier_PersonName",
        blank=True, null=True,
    )
    VerificationDate = models.DateField(blank=True, null=True)
    VerificationNotes = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="NomenclaturalTypeDesignationType_VerificationNotes_StringL",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class NomenclaturalTypeDesignationsType_model(models.Model):
    NomenclaturalTypeDesignation = models.ForeignKey(
        "NomenclaturalTypeDesignationType_model",
        on_delete=models.CASCADE,
        related_name="NomenclaturalTypeDesignationsType_NomenclaturalTypeDesignation_NomenclaturalTypeDesignationType",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class ObservationUnitIDsType_model(models.Model):
    ObservationUnitID = models.ForeignKey(
        "StringP_model",
        on_delete=models.CASCADE,
        related_name="ObservationUnitIDsType_ObservationUnitID_StringP",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class ObservationUnitType_model(models.Model):
    ObservationUnitIDs = models.ForeignKey(
        "ObservationUnitIDsType_model",
        on_delete=models.CASCADE,
        related_name="ObservationUnitType_ObservationUnitIDs_ObservationUnitIDsType",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class Organization_model(models.Model):
    GUID = models.CharField(max_length=1000, blank=True, null=True)
    Name = models.ForeignKey(
        "Label_model",
        on_delete=models.CASCADE,
        related_name="Organization_Name_Label",
    )
    LogoURL = models.CharField(max_length=1000, blank=True, null=True)
    Divisions = models.ForeignKey(
        "DivisionsType_model",
        on_delete=models.CASCADE,
        related_name="Organization_Divisions_DivisionsType",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class OtherLegalStatementsType_model(models.Model):
    OtherLegalStatement = models.ForeignKey(
        "LegalStatement_model",
        on_delete=models.CASCADE,
        related_name="OtherLegalStatementsType_OtherLegalStatement_LegalStatement",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class OtherMeasurementsOrFactsType_model(models.Model):
    OtherMeasurementOrFact = models.ForeignKey(
        "MeasurementOrFact_model",
        on_delete=models.CASCADE,
        related_name="OtherMeasurementsOrFactsType_OtherMeasurementOrFact_MeasurementOrFact",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class OtherProvidersType_model(models.Model):
    OtherProvider = models.CharField(max_length=1000, )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class OwnersType_model(models.Model):
    Owner = models.ForeignKey(
        "Contact_model",
        on_delete=models.CASCADE,
        related_name="OwnersType_Owner_Contact",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class PGRUnit_model(models.Model):
    NationalInventoryCode = models.CharField(max_length=1000, blank=True, null=True)
    BreedingCountryCode = models.CharField(max_length=1000, blank=True, null=True)
    BreedingInstitutionCode = models.CharField(max_length=1000, blank=True, null=True)
    DecodedBreedingInstitute = models.CharField(max_length=1000, blank=True, null=True)
    GatheringInstitutionCode = models.CharField(max_length=1000, blank=True, null=True)
    DecodedGatheringInstitute = models.CharField(max_length=1000, blank=True, null=True)
    BiologicalStatus = models.IntegerField(blank=True, null=True)
    AncestralData = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="PGRUnit_AncestralData_StringL",
        blank=True, null=True,
    )
    CollectingAcquisitionSource = models.IntegerField(blank=True, null=True)
    OtherIdentification = models.CharField(max_length=1000, blank=True, null=True)
    LocationSafetyDuplicates = models.CharField(max_length=1000, blank=True, null=True)
    DecodedLocationSafetyDuplicates = models.CharField(max_length=1000, blank=True, null=True)
    TypeGermplasmStorage = models.IntegerField(blank=True, null=True)
    AccessionNames = models.ForeignKey(
        "AccessionNamesType_model",
        on_delete=models.CASCADE,
        related_name="PGRUnit_AccessionNames_AccessionNamesType",
        blank=True, null=True,
    )
    AccessionNameText = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class PaleontologicalUnit_model(models.Model):
    Preservation = models.ForeignKey(
        "PreservationType14_model",
        on_delete=models.CASCADE,
        related_name="PaleontologicalUnit_Preservation_PreservationType14",
        blank=True, null=True,
    )
    TimeRange = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class Permit_model(models.Model):
    Type = models.CharField(max_length=1000, )
    Status = models.CharField(max_length=1000, )
    Details = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="Permit_Details_StringL",
        blank=True, null=True,
    )
    ResourceURI = models.CharField(max_length=1000, blank=True, null=True)
    WebsiteURL = models.CharField(max_length=1000, blank=True, null=True)
    Text = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="Permit_Text_StringL",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class PermitsType_model(models.Model):
    Permit = models.ForeignKey(
        "Permit_model",
        on_delete=models.CASCADE,
        related_name="PermitsType_Permit_Permit",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class PersonName_model(models.Model):
    FullName = models.CharField(max_length=1000, )
    SortingName = models.CharField(max_length=1000, blank=True, null=True)
    AtomizedName = models.ForeignKey(
        "AtomizedNameType_model",
        on_delete=models.CASCADE,
        related_name="PersonName_AtomizedName_AtomizedNameType",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class PhasesOrStagesType_model(models.Model):
    PhaseOrStage = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="PhasesOrStagesType_PhaseOrStage_StringL",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class PreparationType_model(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    PreparationType = models.ForeignKey(
        "PreparationType_model",
        on_delete=models.CASCADE,
        related_name="PreparationType_PreparationType_PreparationType",
        blank=True, null=True,
    )
    PreparationMethod = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="PreparationType_PreparationMethod_StringL",
        blank=True, null=True,
    )
    PreparationMaterials = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="PreparationType_PreparationMaterials_StringL",
        blank=True, null=True,
    )
    PreparationAgent = models.ForeignKey(
        "Contact_model",
        on_delete=models.CASCADE,
        related_name="PreparationType_PreparationAgent_Contact",
        blank=True, null=True,
    )
    PreparationDate = models.CharField(max_length=1000, blank=True, null=True)
    SampleSize = models.CharField(max_length=1000, blank=True, null=True)
    Sieving = models.CharField(max_length=1000, blank=True, null=True)
    SampleDesignations = models.ForeignKey(
        "SampleDesignationsType_model",
        on_delete=models.CASCADE,
        related_name="PreparationType_SampleDesignations_SampleDesignationsType",
        blank=True, null=True,
    )
    References = models.ForeignKey(
        "ReferencesType4_model",
        on_delete=models.CASCADE,
        related_name="PreparationType_References_ReferencesType4",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class PreparationsType_model(models.Model):
    Preparation = models.ForeignKey(
        "PreparationType_model",
        on_delete=models.CASCADE,
        related_name="PreparationsType_Preparation_PreparationType",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class PreservationType_model(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    PreservationType = models.ForeignKey(
        "PreservationType_model",
        on_delete=models.CASCADE,
        related_name="PreservationType_PreservationType_PreservationType",
        blank=True, null=True,
    )
    PreservationTemperature = models.ForeignKey(
        "Temperature_model",
        on_delete=models.CASCADE,
        related_name="PreservationType_PreservationTemperature_Temperature",
        blank=True, null=True,
    )
    PreservationDateBegin = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class PreservationType14_model(models.Model):
    Completeness = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="PreservationType14_Completeness_StringL",
        blank=True, null=True,
    )
    Form = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="PreservationType14_Form_StringL",
        blank=True, null=True,
    )
    Matrix = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="PreservationType14_Matrix_StringL",
        blank=True, null=True,
    )
    Mineralization = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="PreservationType14_Mineralization_StringL",
        blank=True, null=True,
    )
    Taphonomy = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="PreservationType14_Taphonomy_StringL",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class PreservationsType_model(models.Model):
    Preservation = models.ForeignKey(
        "PreservationType_model",
        on_delete=models.CASCADE,
        related_name="PreservationsType_Preservation_PreservationType",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class PreviousUnitType_model(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    PreviousUnitGUID = models.CharField(max_length=1000, blank=True, null=True)
    PreviousSourceInstitutionID = models.CharField(max_length=1000, blank=True, null=True)
    PreviousSourceID = models.CharField(max_length=1000, blank=True, null=True)
    PreviousUnitID = models.CharField(max_length=1000, blank=True, null=True)
    Date = models.ForeignKey(
        "DateTime_model",
        on_delete=models.CASCADE,
        related_name="PreviousUnitType_Date_DateTime",
        blank=True, null=True,
    )
    Notes = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="PreviousUnitType_Notes_StringL",
        blank=True, null=True,
    )
    PreviousUnitText = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="PreviousUnitType_PreviousUnitText_StringL",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class PreviousUnitsType_model(models.Model):
    PreviousUnit = models.ForeignKey(
        "PreviousUnitType_model",
        on_delete=models.CASCADE,
        related_name="PreviousUnitsType_PreviousUnit_PreviousUnitType",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class ProjectType_model(models.Model):
    Title = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="ProjectType_Title_StringL",
        blank=True, null=True,
    )
    ResourceURIs = models.ForeignKey(
        "ResourceURIsType1_model",
        on_delete=models.CASCADE,
        related_name="ProjectType_ResourceURIs_ResourceURIsType1",
        blank=True, null=True,
    )
    WebsiteURL = models.CharField(max_length=1000, blank=True, null=True)
    Contact = models.ForeignKey(
        "Contact_model",
        on_delete=models.CASCADE,
        related_name="ProjectType_Contact_Contact",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class RatingsType_model(models.Model):
    Rating = models.CharField(max_length=1000, )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class Reference_model(models.Model):
    GUID = models.CharField(max_length=1000, blank=True, null=True)
    Text = models.CharField(max_length=1000, )
    Details = models.CharField(max_length=1000, blank=True, null=True)
    WebsiteURL = models.CharField(max_length=1000, blank=True, null=True)
    ResourceURIs = models.ForeignKey(
        "ResourceURIsType10_model",
        on_delete=models.CASCADE,
        related_name="Reference_ResourceURIs_ResourceURIsType10",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class ReferencesType_model(models.Model):
    Reference = models.ForeignKey(
        "Reference_model",
        on_delete=models.CASCADE,
        related_name="ReferencesType_Reference_Reference",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class ReferencesType12_model(models.Model):
    Reference = models.ForeignKey(
        "Reference_model",
        on_delete=models.CASCADE,
        related_name="ReferencesType12_Reference_Reference",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class ReferencesType13_model(models.Model):
    Reference = models.ForeignKey(
        "Reference_model",
        on_delete=models.CASCADE,
        related_name="ReferencesType13_Reference_Reference",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class ReferencesType2_model(models.Model):
    Reference = models.ForeignKey(
        "Reference_model",
        on_delete=models.CASCADE,
        related_name="ReferencesType2_Reference_Reference",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class ReferencesType4_model(models.Model):
    Reference = models.ForeignKey(
        "Reference_model",
        on_delete=models.CASCADE,
        related_name="ReferencesType4_Reference_Reference",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class RepresentationType_model(models.Model):
    LabelRepr = models.ForeignKey(
        "LabelRepr_model",
        on_delete=models.CASCADE,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class ResourceURIsType_model(models.Model):
    ResourceURI = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class ResourceURIsType1_model(models.Model):
    ResourceURI = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class ResourceURIsType10_model(models.Model):
    ResourceURI = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class ResourceURIsType11_model(models.Model):
    ResourceURI = models.CharField(max_length=1000, )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class ResourceURIsType6_model(models.Model):
    ResourceURI = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class ResourceURIsType7_model(models.Model):
    ResourceURI = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class ResourceURIsType9_model(models.Model):
    ResourceURI = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class ResultType_model(models.Model):
    TaxonIdentified = models.ForeignKey(
        "TaxonIdentified_model",
        on_delete=models.CASCADE,
        related_name="ResultType_TaxonIdentified_TaxonIdentified",
        blank=True, null=True,
    )
    MaterialIdentified = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="ResultType_MaterialIdentified_StringL",
        blank=True, null=True,
    )
    Extension = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class RevisionData_model(models.Model):
    Creators = models.CharField(max_length=1000, blank=True, null=True)
    Contributors = models.CharField(max_length=1000, blank=True, null=True)
    DateCreated = models.CharField(max_length=1000, blank=True, null=True)
    DateModified = models.CharField(max_length=1000, )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class RolesType_model(models.Model):
    Role = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="RolesType_Role_StringL",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class SampleDesignationsType_model(models.Model):
    SampleDesignation = models.CharField(max_length=1000, )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class ScientificName_model(models.Model):
    FullScientificName = models.CharField(max_length=1000, )
    NameAtomized = models.ForeignKey(
        "NameAtomizedType_model",
        on_delete=models.CASCADE,
        related_name="ScientificName_NameAtomized_NameAtomizedType",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class ScientificNameIdentified_model(models.Model):
    ScientificName = models.ForeignKey(
        "ScientificName_model",
        on_delete=models.CASCADE,
    )
    IdentificationQualifier = models.ForeignKey(
        "IdentificationQualifierType_model",
        on_delete=models.CASCADE,
        related_name="ScientificNameIdentified_IdentificationQualifier_IdentificationQualifierType",
        blank=True, null=True,
    )
    NameAddendum = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class ScopeType_model(models.Model):
    GeoecologicalTerms = models.ForeignKey(
        "GeoecologicalTermsType_model",
        on_delete=models.CASCADE,
        related_name="ScopeType_GeoecologicalTerms_GeoecologicalTermsType",
        blank=True, null=True,
    )
    TaxonomicTerms = models.ForeignKey(
        "TaxonomicTermsType_model",
        on_delete=models.CASCADE,
        related_name="ScopeType_TaxonomicTerms_TaxonomicTermsType",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class Sequence_model(models.Model):
    SequenceDatabase = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="Sequence_SequenceDatabase_StringL",
    )
    ID = models.CharField(max_length=1000, )
    Method = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="Sequence_Method_StringL",
        blank=True, null=True,
    )
    SequencedPart = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="Sequence_SequencedPart_StringL",
        blank=True, null=True,
    )
    Reference = models.ForeignKey(
        "Reference_model",
        on_delete=models.CASCADE,
        related_name="Sequence_Reference_Reference",
        blank=True, null=True,
    )
    SequencingAgent = models.ForeignKey(
        "Contact_model",
        on_delete=models.CASCADE,
        related_name="Sequence_SequencingAgent_Contact",
        blank=True, null=True,
    )
    SequenceLength = models.IntegerField(blank=True, null=True)
    DirectAccessURL = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class SequencesType_model(models.Model):
    Sequence = models.ForeignKey(
        "Sequence_model",
        on_delete=models.CASCADE,
        related_name="SequencesType_Sequence_Sequence",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class SpecimenMeasurementsOrFactsType_model(models.Model):
    SpecimenMeasurementOrFact = models.ForeignKey(
        "MeasurementOrFact_model",
        on_delete=models.CASCADE,
        related_name="SpecimenMeasurementsOrFactsType_SpecimenMeasurementOrFact_MeasurementOrFact",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class SpecimenUnitType_model(models.Model):
    Owner = models.ForeignKey(
        "Contact_model",
        on_delete=models.CASCADE,
        related_name="SpecimenUnitType_Owner_Contact",
        blank=True, null=True,
    )
    LoanRestrictions = models.ForeignKey(
        "LoanRestrictionsType_model",
        on_delete=models.CASCADE,
        related_name="SpecimenUnitType_LoanRestrictions_LoanRestrictionsType",
        blank=True, null=True,
    )
    Acquisition = models.ForeignKey(
        "AcquisitionType_model",
        on_delete=models.CASCADE,
        related_name="SpecimenUnitType_Acquisition_AcquisitionType",
        blank=True, null=True,
    )
    Accessions = models.ForeignKey(
        "AccessionsType_model",
        on_delete=models.CASCADE,
        related_name="SpecimenUnitType_Accessions_AccessionsType",
        blank=True, null=True,
    )
    Preparations = models.ForeignKey(
        "PreparationsType_model",
        on_delete=models.CASCADE,
        related_name="SpecimenUnitType_Preparations_PreparationsType",
        blank=True, null=True,
    )
    PreparationsText = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="SpecimenUnitType_PreparationsText_StringL",
        blank=True, null=True,
    )
    Preservations = models.ForeignKey(
        "PreservationsType_model",
        on_delete=models.CASCADE,
        related_name="SpecimenUnitType_Preservations_PreservationsType",
        blank=True, null=True,
    )
    Marks = models.ForeignKey(
        "MarksType_model",
        on_delete=models.CASCADE,
        related_name="SpecimenUnitType_Marks_MarksType",
        blank=True, null=True,
    )
    PreviousUnits = models.ForeignKey(
        "PreviousUnitsType_model",
        on_delete=models.CASCADE,
        related_name="SpecimenUnitType_PreviousUnits_PreviousUnitsType",
        blank=True, null=True,
    )
    PreviousUnitsText = models.CharField(max_length=1000, blank=True, null=True)
    NomenclaturalTypeDesignations = models.ForeignKey(
        "NomenclaturalTypeDesignationsType_model",
        on_delete=models.CASCADE,
        related_name="SpecimenUnitType_NomenclaturalTypeDesignations_NomenclaturalTypeDesignationsType",
        blank=True, null=True,
    )
    NomenclaturalTypeText = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="SpecimenUnitType_NomenclaturalTypeText_StringL",
        blank=True, null=True,
    )
    DuplicatesDistributedTo = models.CharField(max_length=1000, blank=True, null=True)
    Disposition = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="SpecimenUnitType_Disposition_StringL",
        blank=True, null=True,
    )
    SpecimenMeasurementsOrFacts = models.ForeignKey(
        "SpecimenMeasurementsOrFactsType_model",
        on_delete=models.CASCADE,
        related_name="SpecimenUnitType_SpecimenMeasurementsOrFacts_SpecimenMeasurementsOrFactsType",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class StratigraphicTerm_model(models.Model):
    Domain = models.CharField(max_length=1000, blank=True, null=True)
    Term = models.CharField(max_length=1000, )
    Source = models.ForeignKey(
        "Reference_model",
        on_delete=models.CASCADE,
        related_name="StratigraphicTerm_Source_Reference",
        blank=True, null=True,
    )
    Comment = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class StratigraphicTermL_model(models.Model):
    StratigraphicTerm = models.ForeignKey(
        "StratigraphicTerm_model",
        on_delete=models.CASCADE,
    )
    language = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class Stratigraphy_model(models.Model):
    ChronostratigraphicTerms = models.ForeignKey(
        "ChronostratigraphicTermsType_model",
        on_delete=models.CASCADE,
        related_name="Stratigraphy_ChronostratigraphicTerms_ChronostratigraphicTermsType",
        blank=True, null=True,
    )
    BiostratigraphicTerms = models.ForeignKey(
        "BiostratigraphicTermsType_model",
        on_delete=models.CASCADE,
        related_name="Stratigraphy_BiostratigraphicTerms_BiostratigraphicTermsType",
        blank=True, null=True,
    )
    LithostratigraphicTerms = models.ForeignKey(
        "LithostratigraphicTermsType_model",
        on_delete=models.CASCADE,
        related_name="Stratigraphy_LithostratigraphicTerms_LithostratigraphicTermsType",
        blank=True, null=True,
    )
    StratigraphyText = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="Stratigraphy_StratigraphyText_StringL",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class StringL_model(models.Model):
    language = models.CharField(max_length=1000, blank=True, null=True)
    valueOf_x = models.CharField(max_length=1000, )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class StringL255_model(models.Model):
    language = models.CharField(max_length=1000, blank=True, null=True)
    valueOf_x = models.CharField(max_length=1000, )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class StringLP_model(models.Model):
    language = models.CharField(max_length=1000, blank=True, null=True)
    preferred = models.NullBooleanField(blank=True, null=True)
    valueOf_x = models.CharField(max_length=1000, )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class StringLP255_model(models.Model):
    language = models.CharField(max_length=1000, blank=True, null=True)
    preferred = models.NullBooleanField(blank=True, null=True)
    valueOf_x = models.CharField(max_length=1000, )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class StringP_model(models.Model):
    preferred = models.NullBooleanField(blank=True, null=True)
    valueOf_x = models.CharField(max_length=1000, )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class StringP255_model(models.Model):
    preferred = models.NullBooleanField(blank=True, null=True)
    valueOf_x = models.CharField(max_length=1000, )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class SuggestedCitationsType_model(models.Model):
    SuggestedCitation = models.ForeignKey(
        "LegalStatement_model",
        on_delete=models.CASCADE,
        related_name="SuggestedCitationsType_SuggestedCitation_LegalStatement",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class SynecologyType_model(models.Model):
    Syntaxon = models.CharField(max_length=1000, blank=True, null=True)
    Notes = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="SynecologyType_Notes_StringL",
        blank=True, null=True,
    )
    AssociatedTaxa = models.ForeignKey(
        "AssociatedTaxaType_model",
        on_delete=models.CASCADE,
        related_name="SynecologyType_AssociatedTaxa_AssociatedTaxaType",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class TagsType_model(models.Model):
    Tag = models.CharField(max_length=1000, )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class TaxaInBackgroundType_model(models.Model):
    TaxonInBackground = models.ForeignKey(
        "TaxonIdentified_model",
        on_delete=models.CASCADE,
        related_name="TaxaInBackgroundType_TaxonInBackground_TaxonIdentified",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class TaxonIdentified_model(models.Model):
    HigherTaxa = models.ForeignKey(
        "HigherTaxaType_model",
        on_delete=models.CASCADE,
        related_name="TaxonIdentified_HigherTaxa_HigherTaxaType",
        blank=True, null=True,
    )
    ScientificName = models.ForeignKey(
        "ScientificName_model",
        on_delete=models.CASCADE,
        related_name="TaxonIdentified_ScientificName_ScientificName",
        blank=True, null=True,
    )
    InformalName = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="TaxonIdentified_InformalName_StringL",
        blank=True, null=True,
    )
    NameComments = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="TaxonIdentified_NameComments_StringL",
        blank=True, null=True,
    )
    Code = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class TaxonomicTermsType_model(models.Model):
    TaxonomicTerm = models.ForeignKey(
        "StringL255_model",
        on_delete=models.CASCADE,
        related_name="TaxonomicTermsType_TaxonomicTerm_StringL255",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class TechnicalContactsType_model(models.Model):
    TechnicalContact = models.ForeignKey(
        "ContactP_model",
        on_delete=models.CASCADE,
        related_name="TechnicalContactsType_TechnicalContact_ContactP",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class TelephoneNumbersType_model(models.Model):
    TelephoneNumber = models.ForeignKey(
        "StringP255_model",
        on_delete=models.CASCADE,
        related_name="TelephoneNumbersType_TelephoneNumber_StringP255",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class Temperature_model(models.Model):
    scale = models.CharField(max_length=1000, blank=True, null=True)
    valueOf_x = models.CharField(max_length=1000, )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class TradeDesignationNamesType_model(models.Model):
    TradeDesignationName = models.CharField(max_length=1000, )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class Unit_model(models.Model):
    GUID = models.CharField(max_length=1000, blank=True, null=True)
    SourceInstitutionID = models.CharField(max_length=1000, )
    SourceID = models.CharField(max_length=1000, )
    ID = models.CharField(max_length=1000, )
    NumericID = models.IntegerField(blank=True, null=True)
    LastEditor = models.ForeignKey(
        "Contact_model",
        on_delete=models.CASCADE,
        related_name="Unit_LastEditor_Contact",
        blank=True, null=True,
    )
    DateModified = models.CharField(max_length=1000, blank=True, null=True)
    Owner = models.ForeignKey(
        "Contact_model",
        on_delete=models.CASCADE,
        related_name="Unit_Owner_Contact",
        blank=True, null=True,
    )
    LegalStatements = models.ForeignKey(
        "LegalStatements_model",
        on_delete=models.CASCADE,
        related_name="Unit_LegalStatements_LegalStatements",
        blank=True, null=True,
    )
    ContentContacts = models.ForeignKey(
        "ContentContactsType3_model",
        on_delete=models.CASCADE,
        related_name="Unit_ContentContacts_ContentContactsType3",
        blank=True, null=True,
    )
    InformationWithheld = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="Unit_InformationWithheld_StringL",
        blank=True, null=True,
    )
    SourceReference = models.ForeignKey(
        "Reference_model",
        on_delete=models.CASCADE,
        related_name="Unit_SourceReference_Reference",
        blank=True, null=True,
    )
    UnitReferences = models.ForeignKey(
        "UnitReferencesType_model",
        on_delete=models.CASCADE,
        related_name="Unit_UnitReferences_UnitReferencesType",
        blank=True, null=True,
    )
    Identifications = models.ForeignKey(
        "IdentificationsType_model",
        on_delete=models.CASCADE,
        related_name="Unit_Identifications_IdentificationsType",
        blank=True, null=True,
    )
    IdentificationHistory = models.CharField(max_length=1000, blank=True, null=True)
    RecordBasis = models.CharField(max_length=1000, blank=True, null=True)
    KindOfUnit = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="Unit_KindOfUnit_StringL",
        blank=True, null=True,
    )
    SpecimenUnit = models.ForeignKey(
        "SpecimenUnitType_model",
        on_delete=models.CASCADE,
        related_name="Unit_SpecimenUnit_SpecimenUnitType",
        blank=True, null=True,
    )
    ObservationUnit = models.ForeignKey(
        "ObservationUnitType_model",
        on_delete=models.CASCADE,
        related_name="Unit_ObservationUnit_ObservationUnitType",
        blank=True, null=True,
    )
    CultureCollectionUnit = models.ForeignKey(
        "CultureCollectionUnit_model",
        on_delete=models.CASCADE,
        related_name="Unit_CultureCollectionUnit_CultureCollectionUnit",
        blank=True, null=True,
    )
    MycologicalUnit = models.ForeignKey(
        "MycologicalUnit_model",
        on_delete=models.CASCADE,
        related_name="Unit_MycologicalUnit_MycologicalUnit",
        blank=True, null=True,
    )
    HerbariumUnit = models.ForeignKey(
        "HerbariumUnit_model",
        on_delete=models.CASCADE,
        related_name="Unit_HerbariumUnit_HerbariumUnit",
        blank=True, null=True,
    )
    BotanicalGardenUnit = models.ForeignKey(
        "BotanicalGardenUnit_model",
        on_delete=models.CASCADE,
        related_name="Unit_BotanicalGardenUnit_BotanicalGardenUnit",
        blank=True, null=True,
    )
    PlantGeneticResourcesUnit = models.ForeignKey(
        "PGRUnit_model",
        on_delete=models.CASCADE,
        related_name="Unit_PlantGeneticResourcesUnit_PGRUnit",
        blank=True, null=True,
    )
    ZoologicalUnit = models.ForeignKey(
        "ZoologicalUnit_model",
        on_delete=models.CASCADE,
        related_name="Unit_ZoologicalUnit_ZoologicalUnit",
        blank=True, null=True,
    )
    PaleontologicalUnit = models.ForeignKey(
        "PaleontologicalUnit_model",
        on_delete=models.CASCADE,
        related_name="Unit_PaleontologicalUnit_PaleontologicalUnit",
        blank=True, null=True,
    )
    MultimediaObjects = models.ForeignKey(
        "MultimediaObjectsType5_model",
        on_delete=models.CASCADE,
        related_name="Unit_MultimediaObjects_MultimediaObjectsType5",
        blank=True, null=True,
    )
    Associations = models.ForeignKey(
        "AssociationsType_model",
        on_delete=models.CASCADE,
        related_name="Unit_Associations_AssociationsType",
        blank=True, null=True,
    )
    Assemblages = models.ForeignKey(
        "AssemblagesType_model",
        on_delete=models.CASCADE,
        related_name="Unit_Assemblages_AssemblagesType",
        blank=True, null=True,
    )
    NamedCollectionsOrSurveys = models.ForeignKey(
        "NamedCollectionsOrSurveysType_model",
        on_delete=models.CASCADE,
        related_name="Unit_NamedCollectionsOrSurveys_NamedCollectionsOrSurveysType",
        blank=True, null=True,
    )
    Gathering = models.ForeignKey(
        "Gathering_model",
        on_delete=models.CASCADE,
        related_name="Unit_Gathering_Gathering",
        blank=True, null=True,
    )
    FieldNumbers = models.ForeignKey(
        "FieldNumbersType_model",
        on_delete=models.CASCADE,
        related_name="Unit_FieldNumbers_FieldNumbersType",
        blank=True, null=True,
    )
    FieldNotes = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="Unit_FieldNotes_StringL",
        blank=True, null=True,
    )
    FieldNotesReferences = models.ForeignKey(
        "FieldNotesReferencesType_model",
        on_delete=models.CASCADE,
        related_name="Unit_FieldNotesReferences_FieldNotesReferencesType",
        blank=True, null=True,
    )
    MeasurementsOrFacts = models.ForeignKey(
        "MeasurementsOrFactsType8_model",
        on_delete=models.CASCADE,
        related_name="Unit_MeasurementsOrFacts_MeasurementsOrFactsType8",
        blank=True, null=True,
    )
    Sex = models.CharField(max_length=1000, blank=True, null=True)
    Age = models.CharField(max_length=1000, blank=True, null=True)
    Sequences = models.ForeignKey(
        "SequencesType_model",
        on_delete=models.CASCADE,
        related_name="Unit_Sequences_SequencesType",
        blank=True, null=True,
    )
    Notes = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="Unit_Notes_StringL",
        blank=True, null=True,
    )
    WebsiteURL = models.CharField(max_length=1000, blank=True, null=True)
    Annotations = models.ForeignKey(
        "AnnotationsType_model",
        on_delete=models.CASCADE,
        related_name="Unit_Annotations_AnnotationsType",
        blank=True, null=True,
    )
    UnitExtensions = models.ForeignKey(
        "UnitExtensionsType_model",
        on_delete=models.CASCADE,
        related_name="Unit_UnitExtensions_UnitExtensionsType",
        blank=True, null=True,
    )
    ResourceURIs = models.ForeignKey(
        "ResourceURIsType9_model",
        on_delete=models.CASCADE,
        related_name="Unit_ResourceURIs_ResourceURIsType9",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class UnitExtensionsType_model(models.Model):
    UnitExtension = models.CharField(max_length=1000, )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class UnitReferencesType_model(models.Model):
    UnitReference = models.ForeignKey(
        "Reference_model",
        on_delete=models.CASCADE,
        related_name="UnitReferencesType_UnitReference_Reference",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class UnitsType_model(models.Model):
    Unit = models.ForeignKey(
        "Unit_model",
        on_delete=models.CASCADE,
        related_name="UnitsType_Unit_Unit",
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class VersionType_model(models.Model):
    Major = models.IntegerField()
    Minor = models.IntegerField(blank=True, null=True)
    Modifier = models.CharField(max_length=1000, blank=True, null=True)
    DateCreated = models.CharField(max_length=1000, blank=True, null=True)
    VersionText = models.ForeignKey(
        "StringL_model",
        on_delete=models.CASCADE,
        related_name="VersionType_VersionText_StringL",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class VideoType_model(models.Model):
    Microphone = models.CharField(max_length=1000, blank=True, null=True)
    LensModel = models.CharField(max_length=1000, blank=True, null=True)
    LightSource = models.CharField(max_length=1000, blank=True, null=True)
    AudioChannel = models.CharField(max_length=1000, blank=True, null=True)
    DurationTimeCode = models.CharField(max_length=1000, blank=True, null=True)
    AudioEncoding = models.CharField(max_length=1000, blank=True, null=True)
    AudioBitrate = models.CharField(max_length=1000, blank=True, null=True)
    AspectRatio = models.CharField(max_length=1000, blank=True, null=True)
    VideoEncoding = models.CharField(max_length=1000, blank=True, null=True)
    VideoBitrate = models.CharField(max_length=1000, blank=True, null=True)
    Framerate = models.CharField(max_length=1000, blank=True, null=True)
    CaptureFramerate = models.CharField(max_length=1000, blank=True, null=True)
    Color = models.CharField(max_length=1000, blank=True, null=True)
    ThumbnailURL = models.CharField(max_length=1000, blank=True, null=True)
    ImageSize = models.ForeignKey(
        "imageSize_model",
        on_delete=models.CASCADE,
        related_name="VideoType_ImageSize_imageSize",
        blank=True, null=True,
    )
    CallType = models.CharField(max_length=1000, blank=True, null=True)
    NumberOfNotes = models.CharField(max_length=1000, blank=True, null=True)
    Subtitles = models.CharField(max_length=1000, blank=True, null=True)
    SubtitlesFormat = models.CharField(max_length=1000, blank=True, null=True)
    Chapters = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "id: %s" % (self.id, )


class ZoologicalUnit_model(models.Model):
    PhasesOrStages = models.ForeignKey(
        "PhasesOrStagesType_model",
        on_delete=models.CASCADE,
        related_name="ZoologicalUnit_PhasesOrStages_PhasesOrStagesType",
        blank=True, null=True,
    )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class anyUriP_model(models.Model):
    preferred = models.NullBooleanField(blank=True, null=True)
    valueOf_x = models.CharField(max_length=1000, )

    def __unicode__(self):
        return "id: %s" % (self.id, )


class imageSize_model(models.Model):
    Width = models.IntegerField()
    Height = models.IntegerField()

    def __unicode__(self):
        return "id: %s" % (self.id, )

