from django import forms


class AccessionNamesType_form(forms.Form):
    AccessionName = forms.CharField(max_length=1000, )

class AccessionType_form(forms.Form):
    AccessionDate = forms.CharField(max_length=1000, blank=True, null=True)
    AccessionCatalogue = forms.CharField(max_length=1000, blank=True, null=True)
    AccessionNumber = forms.CharField(max_length=1000, blank=True, null=True)
    AccessionURI = forms.CharField(max_length=1000, blank=True, null=True)

class AccessionsType_form(forms.Form):
    Accession = forms.MultipleChoiceField(AccessionType_model.objects.all())

class AcknowledgementsType_form(forms.Form):
    Acknowledgement = forms.MultipleChoiceField(LegalStatement_model.objects.all())

class AcquisitionType_form(forms.Form):
    AcquisitionType = forms.MultipleChoiceField(AcquisitionType_model.objects.all())
    Date = forms.CharField(max_length=1000, blank=True, null=True)
    AcquiredFrom = forms.MultipleChoiceField(Contact_model.objects.all())
    AcquisitionSourceText = forms.MultipleChoiceField(StringL_model.objects.all())

class AddressesType_form(forms.Form):
    Address = forms.MultipleChoiceField(StringLP_model.objects.all())

class AnnotationType_form(forms.Form):
    Text = forms.MultipleChoiceField(StringL_model.objects.all())
    Annotator = forms.MultipleChoiceField(Contact_model.objects.all())
    Date = forms.MultipleChoiceField(DateTime_model.objects.all())

class AnnotationsType_form(forms.Form):
    Annotation = forms.MultipleChoiceField(AnnotationType_model.objects.all())

class AssemblageType_form(forms.Form):
    ID = forms.CharField(max_length=1000, )
    AssemblageName = forms.MultipleChoiceField(StringL_model.objects.all())
    ResourceURIs = forms.MultipleChoiceField(ResourceURIsType7_model.objects.all())

class AssemblagesType_form(forms.Form):
    Assemblage = forms.MultipleChoiceField(AssemblageType_model.objects.all())

class AssociatedTaxaType_form(forms.Form):
    AssociatedTaxon = forms.MultipleChoiceField(TaxonIdentified_model.objects.all())

class AssociationType_form(forms.Form):
    GUID = forms.CharField(max_length=1000, blank=True, null=True)
    ID = forms.CharField(max_length=1000, )
    SourceID = forms.CharField(max_length=1000, )
    SourceInstitutionID = forms.CharField(max_length=1000, )
    KindOfUnit = forms.MultipleChoiceField(StringL_model.objects.all())
    AssociationType = forms.MultipleChoiceField(AssociationType_model.objects.all())
    DirectAccessURL = forms.CharField(max_length=1000, blank=True, null=True)
    Notes = forms.MultipleChoiceField(StringL_model.objects.all())
    ResourceURIs = forms.MultipleChoiceField(ResourceURIsType6_model.objects.all())

class AssociationsType_form(forms.Form):
    Association = forms.MultipleChoiceField(AssociationType_model.objects.all())

class AtomizedNameType_form(forms.Form):
    InheritedName = forms.CharField(max_length=1000, )
    Prefix = forms.CharField(max_length=1000, blank=True, null=True)
    Suffix = forms.CharField(max_length=1000, blank=True, null=True)
    GivenNames = forms.CharField(max_length=1000, blank=True, null=True)
    PreferredName = forms.CharField(max_length=1000, blank=True, null=True)

class AudioType_form(forms.Form):
    Microphone = forms.CharField(max_length=1000, blank=True, null=True)
    AudioChannel = forms.CharField(max_length=1000, blank=True, null=True)
    DurationTimeCode = forms.CharField(max_length=1000, blank=True, null=True)
    CodecName = forms.CharField(max_length=1000, blank=True, null=True)
    CodecQuality = forms.CharField(max_length=1000, blank=True, null=True)
    AudioEncoding = forms.CharField(max_length=1000, blank=True, null=True)
    SamplingRate = forms.FloatField(blank=True, null=True)
    AudioBitrate = forms.CharField(max_length=1000, blank=True, null=True)
    Parabola = forms.CharField(max_length=1000, blank=True, null=True)
    CarrierFrequency = forms.CharField(max_length=1000, blank=True, null=True)
    PulseRepetitionRate = forms.CharField(max_length=1000, blank=True, null=True)
    PulseLength = forms.CharField(max_length=1000, blank=True, null=True)
    PulseFrequencyContour = forms.CharField(max_length=1000, blank=True, null=True)
    PulseEnergyContour = forms.CharField(max_length=1000, blank=True, null=True)
    PulseTimeEncodedSignal = forms.CharField(max_length=1000, blank=True, null=True)
    PulseMaximumAmplitude = forms.CharField(max_length=1000, blank=True, null=True)
    PulseFrequencyModulations = forms.CharField(max_length=1000, blank=True, null=True)
    PulseDistanceRegularity = forms.CharField(max_length=1000, blank=True, null=True)
    PulseGrouping = forms.CharField(max_length=1000, blank=True, null=True)
    Speed = forms.FloatField(blank=True, null=True)
    Pitch = forms.CharField(max_length=1000, blank=True, null=True)
    Volume = forms.CharField(max_length=1000, blank=True, null=True)
    CallType = forms.CharField(max_length=1000, blank=True, null=True)
    NumberOfNotes = forms.CharField(max_length=1000, blank=True, null=True)
    Chapters = forms.CharField(max_length=1000, blank=True, null=True)

class BiostratigraphicTermsType_form(forms.Form):
    BiostratigraphicTerm = forms.MultipleChoiceField(StratigraphicTermL_model.objects.all())

class BiotopeType_form(forms.Form):
    ClassificationScheme = forms.MultipleChoiceField(StringL_model.objects.all())
    Name = forms.MultipleChoiceField(StringL_model.objects.all())
    Text = forms.MultipleChoiceField(StringL_model.objects.all())
    MeasurementsOrFacts = forms.MultipleChoiceField(MeasurementsOrFactsType_model.objects.all())

class BotanicalGardenUnit_form(forms.Form):
    AccessionSpecimenNumbers = forms.IntegerField(blank=True, null=True)
    LocationInGarden = forms.CharField(max_length=1000, blank=True, null=True)
    AccessionMaterialType = forms.CharField(max_length=1000, blank=True, null=True)
    Hardiness = forms.NullBooleanField(blank=True, null=True)
    ProvenanceCategory = forms.CharField(max_length=1000, blank=True, null=True)
    PropagationHistoryCode = forms.CharField(max_length=1000, blank=True, null=True)
    AccessionLineage = forms.CharField(max_length=1000, blank=True, null=True)
    Cultivation = forms.CharField(max_length=1000, blank=True, null=True)
    PlantingDate = forms.CharField(max_length=1000, blank=True, null=True)
    Propagation = forms.CharField(max_length=1000, blank=True, null=True)
    Perennation = forms.CharField(max_length=1000, blank=True, null=True)
    BreedingSystem = forms.CharField(max_length=1000, blank=True, null=True)
    IPEN = forms.CharField(max_length=1000, blank=True, null=True)

class ChronostratigraphicTermsType_form(forms.Form):
    ChronostratigraphicTerm = forms.MultipleChoiceField(StratigraphicTermL_model.objects.all())

class Contact_form(forms.Form):
    UnformattedValue = forms.MultipleChoiceField(StringL_model.objects.all())
    Organization = forms.MultipleChoiceField(Organization_model.objects.all())
    Person = forms.MultipleChoiceField(PersonName_model.objects.all())
    Roles = forms.MultipleChoiceField(RolesType_model.objects.all())
    Addresses = forms.MultipleChoiceField(AddressesType_model.objects.all())
    TelephoneNumbers = forms.MultipleChoiceField(TelephoneNumbersType_model.objects.all())
    EmailAddresses = forms.MultipleChoiceField(EmailAddressesType_model.objects.all())
    WebsiteURL = forms.CharField(max_length=1000, blank=True, null=True)
    ResourceURIs = forms.MultipleChoiceField(ResourceURIsType11_model.objects.all())

class ContactP_form(forms.Form):
    preferred = forms.NullBooleanField(blank=True, null=True)

class ContentContactType_form(forms.Form):
    preferred = forms.NullBooleanField(blank=True, null=True)

class ContentContactsType_form(forms.Form):
    ContentContact = forms.MultipleChoiceField(ContactP_model.objects.all())

class ContentContactsType3_form(forms.Form):
    ContentContact = forms.MultipleChoiceField(ContentContactType_model.objects.all())

class ContentMetadata_form(forms.Form):
    Description = forms.MultipleChoiceField(DescriptionType_model.objects.all())
    LogoURL = forms.CharField(max_length=1000, blank=True, null=True)
    Scope = forms.MultipleChoiceField(ScopeType_model.objects.all())
    Version = forms.MultipleChoiceField(VersionType_model.objects.all())
    RevisionData = forms.MultipleChoiceField(RevisionData_model.objects.all())
    Owners = forms.MultipleChoiceField(OwnersType_model.objects.all())
    LegalStatements = forms.MultipleChoiceField(LegalStatements_model.objects.all())
    InformationWithheld = forms.MultipleChoiceField(StringL_model.objects.all())
    DirectAccessURL = forms.CharField(max_length=1000, blank=True, null=True)

class CoordinateSetType_form(forms.Form):
    original = forms.NullBooleanField(blank=True, null=True)
    begin = forms.NullBooleanField(blank=True, null=True)
    end = forms.NullBooleanField(blank=True, null=True)
    Method = forms.CharField(max_length=1000, blank=True, null=True)
    References = forms.MultipleChoiceField(ReferencesType_model.objects.all())
    VerificationStatus = forms.CharField(max_length=1000, blank=True, null=True)
    Notes = forms.CharField(max_length=1000, blank=True, null=True)
    CoordinatesUTM = forms.MultipleChoiceField(CoordinatesUTMType_model.objects.all())
    CoordinatesGrid = forms.MultipleChoiceField(CoordinatesGridType_model.objects.all())
    CoordinatesLatLong = forms.MultipleChoiceField(CoordinatesLatLongType_model.objects.all())
    EPSGID = forms.IntegerField(blank=True, null=True)

class CoordinateSetsType_form(forms.Form):
    CoordinateSet = forms.MultipleChoiceField(CoordinateSetType_model.objects.all())

class CoordinatesGridType_form(forms.Form):
    GridCellSystem = forms.CharField(max_length=1000, )
    GridCellCode = forms.CharField(max_length=1000, )
    GridQualifier = forms.CharField(max_length=1000, blank=True, null=True)

class CoordinatesLatLongType_form(forms.Form):
    LongitudeDecimal = forms.FloatField(blank=True, null=True)
    VerbatimLongitude = forms.CharField(max_length=1000, blank=True, null=True)
    LatitudeDecimal = forms.FloatField(blank=True, null=True)
    VerbatimLatitude = forms.CharField(max_length=1000, blank=True, null=True)
    SpatialDatum = forms.CharField(max_length=1000, blank=True, null=True)
    Accuracy = forms.CharField(max_length=1000, blank=True, null=True)
    ErrorDistanceInMeters = forms.FloatField(blank=True, null=True)
    ErrorMethod = forms.CharField(max_length=1000, blank=True, null=True)
    PointRadiusSpatialFit = forms.CharField(max_length=1000, blank=True, null=True)
    CoordinatesText = forms.CharField(max_length=1000, blank=True, null=True)

class CoordinatesUTMType_form(forms.Form):
    UTMZone = forms.IntegerField(blank=True, null=True)
    UTMSubzone = forms.CharField(max_length=1000, blank=True, null=True)
    UTMNS = forms.CharField(max_length=1000, blank=True, null=True)
    UTMZoneFull = forms.CharField(max_length=1000, blank=True, null=True)
    UTMEasting = forms.CharField(max_length=1000, blank=True, null=True)
    UTMNorthing = forms.CharField(max_length=1000, blank=True, null=True)
    UTMDatum = forms.CharField(max_length=1000, blank=True, null=True)
    UTMText = forms.CharField(max_length=1000, blank=True, null=True)

class Country_form(forms.Form):
    Name = forms.MultipleChoiceField(StringL_model.objects.all())
    DerivedFlag = forms.NullBooleanField(blank=True, null=True)
    ISO3166Code = forms.CharField(max_length=1000, blank=True, null=True)

class CreatorsType_form(forms.Form):
    Creator = forms.CharField(max_length=1000, )

class CultureCollectionUnit_form(forms.Form):
    OrganismType = forms.CharField(max_length=1000, blank=True, null=True)
    InfrasubspecificName = forms.CharField(max_length=1000, blank=True, null=True)
    CultureNames = forms.MultipleChoiceField(CultureNamesType_model.objects.all())
    Strain = forms.CharField(max_length=1000, blank=True, null=True)
    SerovarOrSerotype = forms.CharField(max_length=1000, blank=True, null=True)
    Pathovar = forms.CharField(max_length=1000, blank=True, null=True)
    Mutant = forms.CharField(max_length=1000, blank=True, null=True)
    Genotype = forms.CharField(max_length=1000, blank=True, null=True)
    GrowthConditions = forms.MultipleChoiceField(StringL_model.objects.all())
    GrowthConditionsAtomized = forms.MultipleChoiceField(GrowthConditionsAtomizedType_model.objects.all())
    References = forms.MultipleChoiceField(ReferencesType12_model.objects.all())
    FormOfSupply = forms.MultipleChoiceField(StringL_model.objects.all())
    Applications = forms.MultipleChoiceField(StringL_model.objects.all())
    Hazard = forms.MultipleChoiceField(StringL_model.objects.all())

class CultureNamesType_form(forms.Form):
    CultureName = forms.MultipleChoiceField(StringL_model.objects.all())

class DataSetType_form(forms.Form):
    GUID = forms.CharField(max_length=1000, blank=True, null=True)
    ID = forms.CharField(max_length=1000, blank=True, null=True)
    ResourceURIs = forms.MultipleChoiceField(ResourceURIsType_model.objects.all())
    TechnicalContacts = forms.MultipleChoiceField(TechnicalContactsType_model.objects.all())
    ContentContacts = forms.MultipleChoiceField(ContentContactsType_model.objects.all())
    DataCenter = forms.CharField(max_length=1000, blank=True, null=True)
    OtherProviders = forms.MultipleChoiceField(OtherProvidersType_model.objects.all())
    Metadata = forms.MultipleChoiceField(ContentMetadata_model.objects.all())
    Units = forms.MultipleChoiceField(UnitsType_model.objects.all())
    DataSetExtension = forms.CharField(max_length=1000, blank=True, null=True)

class DataSets_form(forms.Form):
    DataSet = forms.MultipleChoiceField(DataSetType_model.objects.all())

class DateTime_form(forms.Form):
    DateText = forms.CharField(max_length=1000, blank=True, null=True)
    TimeZone = forms.CharField(max_length=1000, blank=True, null=True)
    ISODateTimeBegin = forms.CharField(max_length=1000, blank=True, null=True)
    TimeOfDayBegin = forms.TimeField(blank=True, null=True)
    ISODateTimeEnd = forms.CharField(max_length=1000, blank=True, null=True)
    TimeOfDayEnd = forms.TimeField(blank=True, null=True)
    PeriodExplicit = forms.NullBooleanField(blank=True, null=True)

class DescriptionType_form(forms.Form):
    Representation = forms.MultipleChoiceField(MetadataDescriptionRepr_model.objects.all())

class DivisionsType_form(forms.Form):
    Division = forms.MultipleChoiceField(StringL_model.objects.all())

class EmailAddressesType_form(forms.Form):
    EmailAddress = forms.MultipleChoiceField(StringP255_model.objects.all())

class FieldNotesReferencesType_form(forms.Form):
    FieldNotesReference = forms.MultipleChoiceField(Reference_model.objects.all())

class FieldNumberType_form(forms.Form):
    ID = forms.CharField(max_length=1000, )
    CollectorName = forms.CharField(max_length=1000, blank=True, null=True)

class FieldNumbersType_form(forms.Form):
    FieldNumber = forms.MultipleChoiceField(FieldNumberType_model.objects.all())

class Gathering_form(forms.Form):
    ID = forms.CharField(max_length=1000, blank=True, null=True)
    Date = forms.MultipleChoiceField(DateTime_model.objects.all())
    GatheringAgents = forms.MultipleChoiceField(GatheringAgentsType_model.objects.all())
    GatheringAgentsText = forms.MultipleChoiceField(StringL_model.objects.all())
    Permits = forms.MultipleChoiceField(PermitsType_model.objects.all())
    Project = forms.MultipleChoiceField(ProjectType_model.objects.all())
    PlatformName = forms.CharField(max_length=1000, blank=True, null=True)
    Method = forms.MultipleChoiceField(StringL_model.objects.all())
    ValidDistributionFlag = forms.NullBooleanField(blank=True, null=True)
    EstablishmentMeans = forms.MultipleChoiceField(StringL_model.objects.all())
    LocalityText = forms.MultipleChoiceField(StringL_model.objects.all())
    Country = forms.MultipleChoiceField(Country_model.objects.all())
    NamedAreas = forms.MultipleChoiceField(NamedAreasType_model.objects.all())
    NamedPlaceRelations = forms.MultipleChoiceField(NamedPlaceRelationsType_model.objects.all())
    Details = forms.MultipleChoiceField(StringL_model.objects.all())
    GML = forms.CharField(max_length=1000, blank=True, null=True)
    WFS = forms.CharField(max_length=1000, blank=True, null=True)
    WMSURL = forms.CharField(max_length=1000, blank=True, null=True)
    CoordinateSets = forms.MultipleChoiceField(CoordinateSetsType_model.objects.all())
    Altitude = forms.MultipleChoiceField(MeasurementOrFact_model.objects.all())
    Depth = forms.MultipleChoiceField(MeasurementOrFact_model.objects.all())
    Height = forms.MultipleChoiceField(MeasurementOrFact_model.objects.all())
    Aspect = forms.MultipleChoiceField(MeasurementOrFact_model.objects.all())
    OtherMeasurementsOrFacts = forms.MultipleChoiceField(OtherMeasurementsOrFactsType_model.objects.all())
    MultimediaObjects = forms.MultipleChoiceField(MultimediaObjectsType_model.objects.all())
    Stratigraphy = forms.MultipleChoiceField(Stratigraphy_model.objects.all())
    Biotope = forms.MultipleChoiceField(BiotopeType_model.objects.all())
    Synecology = forms.MultipleChoiceField(SynecologyType_model.objects.all())
    Notes = forms.MultipleChoiceField(StringL_model.objects.all())
    FootprintWKT = forms.CharField(max_length=1000, blank=True, null=True)
    FootprintSpatialFit = forms.CharField(max_length=1000, blank=True, null=True)

class GatheringAgentType_form(forms.Form):
    sequence = forms.IntegerField(blank=True, null=True)

class GatheringAgentsType_form(forms.Form):
    GatheringAgent = forms.MultipleChoiceField(GatheringAgentType_model.objects.all())

class GeoecologicalTermsType_form(forms.Form):
    GeoecologicalTerm = forms.MultipleChoiceField(StringL255_model.objects.all())

class GrowthConditionAtomized_form(forms.Form):
    CultureMedium = forms.MultipleChoiceField(StringL_model.objects.all())
    Aerobicity = forms.MultipleChoiceField(StringL_model.objects.all())
    Temperature = forms.MultipleChoiceField(Temperature_model.objects.all())
    References = forms.MultipleChoiceField(ReferencesType13_model.objects.all())
    GrowthConditionsMeasurementsOrFacts = forms.MultipleChoiceField(GrowthConditionsMeasurementsOrFactsType_model.objects.all())

class GrowthConditionsAtomizedType_form(forms.Form):
    GrowthConditionAtomized = forms.MultipleChoiceField(GrowthConditionAtomized_model.objects.all())

class GrowthConditionsMeasurementsOrFactsType_form(forms.Form):
    GrowthConditionsMeasurementOrFact = forms.MultipleChoiceField(MeasurementOrFact_model.objects.all())

class HerbariumUnit_form(forms.Form):
    Exsiccatum = forms.CharField(max_length=1000, blank=True, null=True)
    LoanID = forms.CharField(max_length=1000, blank=True, null=True)
    LoanSequenceNumber = forms.IntegerField(blank=True, null=True)
    LoanDestination = forms.CharField(max_length=1000, blank=True, null=True)
    LoanForBotanist = forms.CharField(max_length=1000, blank=True, null=True)
    LoanDispatchMethod = forms.CharField(max_length=1000, blank=True, null=True)
    LoanDate = forms.DateField(blank=True, null=True)
    LoanReturnDate = forms.DateField(blank=True, null=True)
    NaturalOccurrence = forms.MultipleChoiceField(StringL_model.objects.all())
    CultivatedOccurrence = forms.MultipleChoiceField(StringL_model.objects.all())

class HigherTaxaType_form(forms.Form):
    HigherTaxon = forms.MultipleChoiceField(HigherTaxon_model.objects.all())

class HigherTaxon_form(forms.Form):
    HigherTaxonName = forms.CharField(max_length=1000, )
    HigherTaxonRank = forms.CharField(max_length=1000, blank=True, null=True)

class HybridFlagType_form(forms.Form):
    insertionpoint = forms.IntegerField(blank=True, null=True)
    valueOf_x = forms.CharField(max_length=1000, )

class Identification_form(forms.Form):
    Result = forms.MultipleChoiceField(ResultType_model.objects.all())
    PreferredFlag = forms.NullBooleanField(blank=True, null=True)
    NegativeIdentificationFlag = forms.NullBooleanField(blank=True, null=True)
    StoredUnderFlag = forms.NullBooleanField(blank=True, null=True)
    ResultRole = forms.MultipleChoiceField(StringL_model.objects.all())
    Identifiers = forms.MultipleChoiceField(IdentifiersType_model.objects.all())
    IdentifierRole = forms.CharField(max_length=1000, blank=True, null=True)
    IdentificationSource = forms.MultipleChoiceField(Reference_model.objects.all())
    References = forms.MultipleChoiceField(ReferencesType2_model.objects.all())
    Date = forms.MultipleChoiceField(DateTime_model.objects.all())
    Method = forms.MultipleChoiceField(StringL_model.objects.all())
    Notes = forms.MultipleChoiceField(StringL_model.objects.all())
    VerificationLevel = forms.CharField(max_length=1000, blank=True, null=True)

class IdentificationQualifierType_form(forms.Form):
    insertionpoint = forms.IntegerField(blank=True, null=True)
    valueOf_x = forms.CharField(max_length=1000, )

class IdentificationsType_form(forms.Form):
    Identification = forms.MultipleChoiceField(Identification_model.objects.all())

class IdentifiersType_form(forms.Form):
    sequence = forms.IntegerField(blank=True, null=True)
    Identifier = forms.MultipleChoiceField(Contact_model.objects.all())

class ImageType_form(forms.Form):
    LensModel = forms.CharField(max_length=1000, blank=True, null=True)
    FNumber = forms.FloatField(blank=True, null=True)
    FocalLength = forms.FloatField(blank=True, null=True)
    FocalLengthIn35mmFilm = forms.FloatField(blank=True, null=True)
    LightSource = forms.CharField(max_length=1000, blank=True, null=True)
    Flash = forms.CharField(max_length=1000, blank=True, null=True)
    FlashEnergy = forms.CharField(max_length=1000, blank=True, null=True)
    WhiteBalance = forms.CharField(max_length=1000, blank=True, null=True)
    DigitalZoomRatio = forms.CharField(max_length=1000, blank=True, null=True)
    Contrast = forms.CharField(max_length=1000, blank=True, null=True)
    Saturation = forms.CharField(max_length=1000, blank=True, null=True)
    Sharpness = forms.CharField(max_length=1000, blank=True, null=True)
    Gamma = forms.CharField(max_length=1000, blank=True, null=True)
    ColorSpace = forms.CharField(max_length=1000, blank=True, null=True)
    ImageSize = forms.MultipleChoiceField(imageSize_model.objects.all())
    ImageResolution = forms.IntegerField(blank=True, null=True)
    ExposureTime = forms.CharField(max_length=1000, blank=True, null=True)
    ExposureMode = forms.CharField(max_length=1000, blank=True, null=True)
    SpectralSensitivity = forms.CharField(max_length=1000, blank=True, null=True)
    PhotographicSensitivity = forms.CharField(max_length=1000, blank=True, null=True)
    ISOSpeed = forms.CharField(max_length=1000, blank=True, null=True)
    ShutterSpeed = forms.IntegerField(blank=True, null=True)
    Brightness = forms.CharField(max_length=1000, blank=True, null=True)
    Color = forms.CharField(max_length=1000, blank=True, null=True)
    ThumbnailURL = forms.CharField(max_length=1000, blank=True, null=True)

class ImagesType_form(forms.Form):
    ImageID = forms.CharField(max_length=1000, )

class Label_form(forms.Form):
    Representation = forms.MultipleChoiceField(RepresentationType_model.objects.all())

class LabelRepr_form(forms.Form):
    language = forms.CharField(max_length=1000, )
    Text = forms.CharField(max_length=1000, )
    Abbreviation = forms.CharField(max_length=1000, blank=True, null=True)

class LegalStatement_form(forms.Form):
    language = forms.CharField(max_length=1000, )
    Text = forms.CharField(max_length=1000, )
    Details = forms.CharField(max_length=1000, blank=True, null=True)
    WebsiteURL = forms.CharField(max_length=1000, blank=True, null=True)
    ResourceURI = forms.CharField(max_length=1000, blank=True, null=True)

class LegalStatements_form(forms.Form):
    Licenses = forms.MultipleChoiceField(LicensesType_model.objects.all())
    Acknowledgements = forms.MultipleChoiceField(AcknowledgementsType_model.objects.all())
    SuggestedCitations = forms.MultipleChoiceField(SuggestedCitationsType_model.objects.all())
    OtherLegalStatements = forms.MultipleChoiceField(OtherLegalStatementsType_model.objects.all())

class LicensesType_form(forms.Form):
    License = forms.MultipleChoiceField(LegalStatement_model.objects.all())

class LithostratigraphicTermsType_form(forms.Form):
    LithostratigraphicTerm = forms.MultipleChoiceField(StratigraphicTermL_model.objects.all())

class LoanRestrictionsType_form(forms.Form):
    BlockedUntil = forms.CharField(max_length=1000, blank=True, null=True)
    Blocked = forms.NullBooleanField(blank=True, null=True)
    LoanConditions = forms.CharField(max_length=1000, blank=True, null=True)

class MarkType_form(forms.Form):
    MarkType = forms.MultipleChoiceField(MarkType_model.objects.all())
    MarkText = forms.MultipleChoiceField(StringL_model.objects.all())
    PositionOnObject = forms.MultipleChoiceField(StringL_model.objects.all())
    MarkAuthor = forms.CharField(max_length=1000, blank=True, null=True)
    MarkComment = forms.MultipleChoiceField(StringL_model.objects.all())
    Images = forms.MultipleChoiceField(ImagesType_model.objects.all())

class MarksType_form(forms.Form):
    Mark = forms.MultipleChoiceField(MarkType_model.objects.all())

class MeasurementOrFact_form(forms.Form):
    MeasurementOrFactAtomized = forms.MultipleChoiceField(MeasurementOrFactAtomizedType_model.objects.all())
    MeasurementOrFactText = forms.MultipleChoiceField(StringL_model.objects.all())

class MeasurementOrFactAtomizedType_form(forms.Form):
    MeasuredBy = forms.CharField(max_length=1000, blank=True, null=True)
    MeasurementDateTime = forms.CharField(max_length=1000, blank=True, null=True)
    Duration = forms.CharField(max_length=1000, blank=True, null=True)
    Method = forms.MultipleChoiceField(StringL_model.objects.all())
    Parameter = forms.MultipleChoiceField(StringL_model.objects.all())
    AppliesTo = forms.MultipleChoiceField(StringL_model.objects.all())
    LowerValue = forms.MultipleChoiceField(StringL_model.objects.all())
    UpperValue = forms.MultipleChoiceField(StringL_model.objects.all())
    UnitOfMeasurement = forms.CharField(max_length=1000, blank=True, null=True)
    Accuracy = forms.CharField(max_length=1000, blank=True, null=True)
    MeasurementOrFactReference = forms.MultipleChoiceField(Reference_model.objects.all())
    IsQuantitative = forms.NullBooleanField(blank=True, null=True)
    ReferenceSystem = forms.CharField(max_length=1000, blank=True, null=True)

class MeasurementsOrFactsType_form(forms.Form):
    MeasurementOrFact = forms.MultipleChoiceField(MeasurementOrFact_model.objects.all())

class MeasurementsOrFactsType8_form(forms.Form):
    MeasurementOrFact = forms.MultipleChoiceField(MeasurementOrFact_model.objects.all())

class MetadataDescriptionRepr_form(forms.Form):
    language = forms.CharField(max_length=1000, )
    Title = forms.CharField(max_length=1000, )
    Details = forms.CharField(max_length=1000, blank=True, null=True)
    Coverage = forms.CharField(max_length=1000, blank=True, null=True)
    WebsiteURL = forms.CharField(max_length=1000, blank=True, null=True)

class MultimediaObject_form(forms.Form):
    ID = forms.CharField(max_length=1000, blank=True, null=True)
    Type = forms.CharField(max_length=1000, blank=True, null=True)
    Title = forms.CharField(max_length=1000, blank=True, null=True)
    IDofContainingCollection = forms.CharField(max_length=1000, blank=True, null=True)
    Source = forms.MultipleChoiceField(Reference_model.objects.all())
    Provider = forms.CharField(max_length=1000, blank=True, null=True)
    FileURL = forms.CharField(max_length=1000, )
    ProductURL = forms.CharField(max_length=1000, blank=True, null=True)
    Context = forms.MultipleChoiceField(StringL_model.objects.all())
    Tags = forms.MultipleChoiceField(TagsType_model.objects.all())
    Ratings = forms.MultipleChoiceField(RatingsType_model.objects.all())
    FileFormat = forms.CharField(max_length=1000, blank=True, null=True)
    FileFormatVersion = forms.CharField(max_length=1000, blank=True, null=True)
    FileSize = forms.CharField(max_length=1000, blank=True, null=True)
    PhysicalFormat = forms.CharField(max_length=1000, blank=True, null=True)
    PhysicalObjectID = forms.CharField(max_length=1000, blank=True, null=True)
    DateCreated = forms.CharField(max_length=1000, blank=True, null=True)
    Creators = forms.MultipleChoiceField(CreatorsType_model.objects.all())
    Modified = forms.CharField(max_length=1000, blank=True, null=True)
    LegalStatements = forms.MultipleChoiceField(LegalStatements_model.objects.all())
    Notes = forms.MultipleChoiceField(StringL_model.objects.all())
    Sex = forms.CharField(max_length=1000, blank=True, null=True)
    LifeStage = forms.CharField(max_length=1000, blank=True, null=True)
    SubjectPart = forms.CharField(max_length=1000, blank=True, null=True)
    SubjectOrientation = forms.CharField(max_length=1000, blank=True, null=True)
    SubjectDistance = forms.CharField(max_length=1000, blank=True, null=True)
    TaxaInBackground = forms.MultipleChoiceField(TaxaInBackgroundType_model.objects.all())
    RecordingEnvironment = forms.CharField(max_length=1000, blank=True, null=True)
    Temperature = forms.MultipleChoiceField(Temperature_model.objects.all())
    LightCondition = forms.CharField(max_length=1000, blank=True, null=True)
    PlaybackUsed = forms.NullBooleanField(blank=True, null=True)
    CaptureEquipment = forms.CharField(max_length=1000, blank=True, null=True)
    Counter = forms.CharField(max_length=1000, blank=True, null=True)
    FilterUsedForRecording = forms.CharField(max_length=1000, blank=True, null=True)
    MakerNote = forms.CharField(max_length=1000, blank=True, null=True)
    Audio = forms.MultipleChoiceField(AudioType_model.objects.all())
    Video = forms.MultipleChoiceField(VideoType_model.objects.all())
    Image = forms.MultipleChoiceField(ImageType_model.objects.all())

class MultimediaObjectsType_form(forms.Form):
    MultimediaObject = forms.MultipleChoiceField(MultimediaObject_model.objects.all())

class MultimediaObjectsType5_form(forms.Form):
    MultimediaObject = forms.MultipleChoiceField(MultimediaObject_model.objects.all())

class MycologicalLiveStagesType_form(forms.Form):
    MycologicalLiveStage = forms.MultipleChoiceField(StringL_model.objects.all())

class MycologicalUnit_form(forms.Form):
    LichenMorphotype = forms.CharField(max_length=1000, blank=True, null=True)
    MycologicalSexualStage = forms.CharField(max_length=1000, blank=True, null=True)
    MycologicalLiveStages = forms.MultipleChoiceField(MycologicalLiveStagesType_model.objects.all())

class NameAtomizedType_form(forms.Form):
    Bacterial = forms.MultipleChoiceField(NameBacterial_model.objects.all())
    Botanical = forms.MultipleChoiceField(NameBotanical_model.objects.all())
    Zoological = forms.MultipleChoiceField(NameZoological_model.objects.all())
    Viral = forms.MultipleChoiceField(NameViral_model.objects.all())

class NameBacterial_form(forms.Form):
    GenusOrMonomial = forms.CharField(max_length=1000, blank=True, null=True)
    Subgenus = forms.CharField(max_length=1000, blank=True, null=True)
    SubgenusAuthorAndYear = forms.CharField(max_length=1000, blank=True, null=True)
    SpeciesEpithet = forms.CharField(max_length=1000, blank=True, null=True)
    SubspeciesEpithet = forms.CharField(max_length=1000, blank=True, null=True)
    ParentheticalAuthorTeamAndYear = forms.CharField(max_length=1000, blank=True, null=True)
    AuthorTeamAndYear = forms.CharField(max_length=1000, blank=True, null=True)
    NameApprobation = forms.CharField(max_length=1000, blank=True, null=True)

class NameBotanical_form(forms.Form):
    GenusOrMonomial = forms.CharField(max_length=1000, blank=True, null=True)
    FirstEpithet = forms.CharField(max_length=1000, blank=True, null=True)
    InfraspecificEpithet = forms.CharField(max_length=1000, blank=True, null=True)
    Rank = forms.CharField(max_length=1000, blank=True, null=True)
    HybridFlag = forms.MultipleChoiceField(HybridFlagType_model.objects.all())
    AuthorTeamParenthesis = forms.CharField(max_length=1000, blank=True, null=True)
    AuthorTeam = forms.CharField(max_length=1000, blank=True, null=True)
    CultivarGroupName = forms.CharField(max_length=1000, blank=True, null=True)
    CultivarName = forms.CharField(max_length=1000, blank=True, null=True)
    TradeDesignationNames = forms.MultipleChoiceField(TradeDesignationNamesType_model.objects.all())

class NameViral_form(forms.Form):
    GenusOrMonomial = forms.CharField(max_length=1000, blank=True, null=True)
    ViralSpeciesDesignation = forms.CharField(max_length=1000, blank=True, null=True)
    Acronym = forms.CharField(max_length=1000, blank=True, null=True)

class NameZoological_form(forms.Form):
    GenusOrMonomial = forms.CharField(max_length=1000, blank=True, null=True)
    Subgenus = forms.CharField(max_length=1000, blank=True, null=True)
    SpeciesEpithet = forms.CharField(max_length=1000, blank=True, null=True)
    SubspeciesEpithet = forms.CharField(max_length=1000, blank=True, null=True)
    AuthorTeamOriginalAndYear = forms.CharField(max_length=1000, blank=True, null=True)
    AuthorTeamParenthesisAndYear = forms.CharField(max_length=1000, blank=True, null=True)
    CombinationAuthorTeamAndYear = forms.CharField(max_length=1000, blank=True, null=True)
    Breed = forms.CharField(max_length=1000, blank=True, null=True)
    NamedIndividual = forms.CharField(max_length=1000, blank=True, null=True)

class NamedArea_form(forms.Form):
    AreaClass = forms.MultipleChoiceField(StringL_model.objects.all())
    Name = forms.MultipleChoiceField(StringL_model.objects.all())
    CodeStandard = forms.CharField(max_length=1000, blank=True, null=True)
    Code = forms.CharField(max_length=1000, blank=True, null=True)
    Reference = forms.MultipleChoiceField(Reference_model.objects.all())

class NamedAreaType_form(forms.Form):
    sequence = forms.IntegerField(blank=True, null=True)

class NamedAreasType_form(forms.Form):
    NamedArea = forms.MultipleChoiceField(NamedArea_model.objects.all())

class NamedCollectionsOrSurveysType_form(forms.Form):
    NamedCollectionOrSurvey = forms.MultipleChoiceField(StringL_model.objects.all())

class NamedPlaceRelationType_form(forms.Form):
    NearbyPlaceName = forms.MultipleChoiceField(StringL_model.objects.all())
    NearbyPlaceRelation = forms.MultipleChoiceField(StringL_model.objects.all())

class NamedPlaceRelationsType_form(forms.Form):
    NamedPlaceRelation = forms.MultipleChoiceField(NamedPlaceRelationType_model.objects.all())

class NomenclaturalTypeDesignationType_form(forms.Form):
    TypifiedName = forms.MultipleChoiceField(ScientificName_model.objects.all())
    NomenclaturalReference = forms.MultipleChoiceField(Reference_model.objects.all())
    TypeStatus = forms.CharField(max_length=1000, blank=True, null=True)
    CodeAssessment = forms.CharField(max_length=1000, blank=True, null=True)
    DoubtfulFlag = forms.NullBooleanField(blank=True, null=True)
    Verifier = forms.MultipleChoiceField(PersonName_model.objects.all())
    VerificationDate = forms.DateField(blank=True, null=True)
    VerificationNotes = forms.MultipleChoiceField(StringL_model.objects.all())

class NomenclaturalTypeDesignationsType_form(forms.Form):
    NomenclaturalTypeDesignation = forms.MultipleChoiceField(NomenclaturalTypeDesignationType_model.objects.all())

class ObservationUnitIDsType_form(forms.Form):
    ObservationUnitID = forms.MultipleChoiceField(StringP_model.objects.all())

class ObservationUnitType_form(forms.Form):
    ObservationUnitIDs = forms.MultipleChoiceField(ObservationUnitIDsType_model.objects.all())

class Organization_form(forms.Form):
    GUID = forms.CharField(max_length=1000, blank=True, null=True)
    Name = forms.MultipleChoiceField(Label_model.objects.all())
    LogoURL = forms.CharField(max_length=1000, blank=True, null=True)
    Divisions = forms.MultipleChoiceField(DivisionsType_model.objects.all())

class OtherLegalStatementsType_form(forms.Form):
    OtherLegalStatement = forms.MultipleChoiceField(LegalStatement_model.objects.all())

class OtherMeasurementsOrFactsType_form(forms.Form):
    OtherMeasurementOrFact = forms.MultipleChoiceField(MeasurementOrFact_model.objects.all())

class OtherProvidersType_form(forms.Form):
    OtherProvider = forms.CharField(max_length=1000, )

class OwnersType_form(forms.Form):
    Owner = forms.MultipleChoiceField(Contact_model.objects.all())

class PGRUnit_form(forms.Form):
    NationalInventoryCode = forms.CharField(max_length=1000, blank=True, null=True)
    BreedingCountryCode = forms.CharField(max_length=1000, blank=True, null=True)
    BreedingInstitutionCode = forms.CharField(max_length=1000, blank=True, null=True)
    DecodedBreedingInstitute = forms.CharField(max_length=1000, blank=True, null=True)
    GatheringInstitutionCode = forms.CharField(max_length=1000, blank=True, null=True)
    DecodedGatheringInstitute = forms.CharField(max_length=1000, blank=True, null=True)
    BiologicalStatus = forms.IntegerField(blank=True, null=True)
    AncestralData = forms.MultipleChoiceField(StringL_model.objects.all())
    CollectingAcquisitionSource = forms.IntegerField(blank=True, null=True)
    OtherIdentification = forms.CharField(max_length=1000, blank=True, null=True)
    LocationSafetyDuplicates = forms.CharField(max_length=1000, blank=True, null=True)
    DecodedLocationSafetyDuplicates = forms.CharField(max_length=1000, blank=True, null=True)
    TypeGermplasmStorage = forms.IntegerField(blank=True, null=True)
    AccessionNames = forms.MultipleChoiceField(AccessionNamesType_model.objects.all())
    AccessionNameText = forms.CharField(max_length=1000, blank=True, null=True)

class PaleontologicalUnit_form(forms.Form):
    Preservation = forms.MultipleChoiceField(PreservationType14_model.objects.all())
    TimeRange = forms.CharField(max_length=1000, blank=True, null=True)

class Permit_form(forms.Form):
    Type = forms.CharField(max_length=1000, )
    Status = forms.CharField(max_length=1000, )
    Details = forms.MultipleChoiceField(StringL_model.objects.all())
    ResourceURI = forms.CharField(max_length=1000, blank=True, null=True)
    WebsiteURL = forms.CharField(max_length=1000, blank=True, null=True)
    Text = forms.MultipleChoiceField(StringL_model.objects.all())

class PermitsType_form(forms.Form):
    Permit = forms.MultipleChoiceField(Permit_model.objects.all())

class PersonName_form(forms.Form):
    FullName = forms.CharField(max_length=1000, )
    SortingName = forms.CharField(max_length=1000, blank=True, null=True)
    AtomizedName = forms.MultipleChoiceField(AtomizedNameType_model.objects.all())

class PhasesOrStagesType_form(forms.Form):
    PhaseOrStage = forms.MultipleChoiceField(StringL_model.objects.all())

class PreparationType_form(forms.Form):
    sequence = forms.IntegerField(blank=True, null=True)
    PreparationType = forms.MultipleChoiceField(PreparationType_model.objects.all())
    PreparationMethod = forms.MultipleChoiceField(StringL_model.objects.all())
    PreparationMaterials = forms.MultipleChoiceField(StringL_model.objects.all())
    PreparationAgent = forms.MultipleChoiceField(Contact_model.objects.all())
    PreparationDate = forms.CharField(max_length=1000, blank=True, null=True)
    SampleSize = forms.CharField(max_length=1000, blank=True, null=True)
    Sieving = forms.CharField(max_length=1000, blank=True, null=True)
    SampleDesignations = forms.MultipleChoiceField(SampleDesignationsType_model.objects.all())
    References = forms.MultipleChoiceField(ReferencesType4_model.objects.all())

class PreparationsType_form(forms.Form):
    Preparation = forms.MultipleChoiceField(PreparationType_model.objects.all())

class PreservationType_form(forms.Form):
    sequence = forms.IntegerField(blank=True, null=True)
    PreservationType = forms.MultipleChoiceField(PreservationType_model.objects.all())
    PreservationTemperature = forms.MultipleChoiceField(Temperature_model.objects.all())
    PreservationDateBegin = forms.CharField(max_length=1000, blank=True, null=True)

class PreservationType14_form(forms.Form):
    Completeness = forms.MultipleChoiceField(StringL_model.objects.all())
    Form = forms.MultipleChoiceField(StringL_model.objects.all())
    Matrix = forms.MultipleChoiceField(StringL_model.objects.all())
    Mineralization = forms.MultipleChoiceField(StringL_model.objects.all())
    Taphonomy = forms.MultipleChoiceField(StringL_model.objects.all())

class PreservationsType_form(forms.Form):
    Preservation = forms.MultipleChoiceField(PreservationType_model.objects.all())

class PreviousUnitType_form(forms.Form):
    sequence = forms.IntegerField(blank=True, null=True)
    PreviousUnitGUID = forms.CharField(max_length=1000, blank=True, null=True)
    PreviousSourceInstitutionID = forms.CharField(max_length=1000, blank=True, null=True)
    PreviousSourceID = forms.CharField(max_length=1000, blank=True, null=True)
    PreviousUnitID = forms.CharField(max_length=1000, blank=True, null=True)
    Date = forms.MultipleChoiceField(DateTime_model.objects.all())
    Notes = forms.MultipleChoiceField(StringL_model.objects.all())
    PreviousUnitText = forms.MultipleChoiceField(StringL_model.objects.all())

class PreviousUnitsType_form(forms.Form):
    PreviousUnit = forms.MultipleChoiceField(PreviousUnitType_model.objects.all())

class ProjectType_form(forms.Form):
    Title = forms.MultipleChoiceField(StringL_model.objects.all())
    ResourceURIs = forms.MultipleChoiceField(ResourceURIsType1_model.objects.all())
    WebsiteURL = forms.CharField(max_length=1000, blank=True, null=True)
    Contact = forms.MultipleChoiceField(Contact_model.objects.all())

class RatingsType_form(forms.Form):
    Rating = forms.CharField(max_length=1000, )

class Reference_form(forms.Form):
    GUID = forms.CharField(max_length=1000, blank=True, null=True)
    Text = forms.CharField(max_length=1000, )
    Details = forms.CharField(max_length=1000, blank=True, null=True)
    WebsiteURL = forms.CharField(max_length=1000, blank=True, null=True)
    ResourceURIs = forms.MultipleChoiceField(ResourceURIsType10_model.objects.all())

class ReferencesType_form(forms.Form):
    Reference = forms.MultipleChoiceField(Reference_model.objects.all())

class ReferencesType12_form(forms.Form):
    Reference = forms.MultipleChoiceField(Reference_model.objects.all())

class ReferencesType13_form(forms.Form):
    Reference = forms.MultipleChoiceField(Reference_model.objects.all())

class ReferencesType2_form(forms.Form):
    Reference = forms.MultipleChoiceField(Reference_model.objects.all())

class ReferencesType4_form(forms.Form):
    Reference = forms.MultipleChoiceField(Reference_model.objects.all())

class RepresentationType_form(forms.Form):

class ResourceURIsType_form(forms.Form):
    ResourceURI = forms.CharField(max_length=1000, blank=True, null=True)

class ResourceURIsType1_form(forms.Form):
    ResourceURI = forms.CharField(max_length=1000, blank=True, null=True)

class ResourceURIsType10_form(forms.Form):
    ResourceURI = forms.CharField(max_length=1000, blank=True, null=True)

class ResourceURIsType11_form(forms.Form):
    ResourceURI = forms.CharField(max_length=1000, )

class ResourceURIsType6_form(forms.Form):
    ResourceURI = forms.CharField(max_length=1000, blank=True, null=True)

class ResourceURIsType7_form(forms.Form):
    ResourceURI = forms.CharField(max_length=1000, blank=True, null=True)

class ResourceURIsType9_form(forms.Form):
    ResourceURI = forms.CharField(max_length=1000, blank=True, null=True)

class ResultType_form(forms.Form):
    TaxonIdentified = forms.MultipleChoiceField(TaxonIdentified_model.objects.all())
    MaterialIdentified = forms.MultipleChoiceField(StringL_model.objects.all())
    Extension = forms.CharField(max_length=1000, blank=True, null=True)

class RevisionData_form(forms.Form):
    Creators = forms.CharField(max_length=1000, blank=True, null=True)
    Contributors = forms.CharField(max_length=1000, blank=True, null=True)
    DateCreated = forms.CharField(max_length=1000, blank=True, null=True)
    DateModified = forms.CharField(max_length=1000, )

class RolesType_form(forms.Form):
    Role = forms.MultipleChoiceField(StringL_model.objects.all())

class SampleDesignationsType_form(forms.Form):
    SampleDesignation = forms.CharField(max_length=1000, )

class ScientificName_form(forms.Form):
    FullScientificName = forms.CharField(max_length=1000, )
    NameAtomized = forms.MultipleChoiceField(NameAtomizedType_model.objects.all())

class ScientificNameIdentified_form(forms.Form):
    IdentificationQualifier = forms.MultipleChoiceField(IdentificationQualifierType_model.objects.all())
    NameAddendum = forms.CharField(max_length=1000, blank=True, null=True)

class ScopeType_form(forms.Form):
    GeoecologicalTerms = forms.MultipleChoiceField(GeoecologicalTermsType_model.objects.all())
    TaxonomicTerms = forms.MultipleChoiceField(TaxonomicTermsType_model.objects.all())

class Sequence_form(forms.Form):
    SequenceDatabase = forms.MultipleChoiceField(StringL_model.objects.all())
    ID = forms.CharField(max_length=1000, )
    Method = forms.MultipleChoiceField(StringL_model.objects.all())
    SequencedPart = forms.MultipleChoiceField(StringL_model.objects.all())
    Reference = forms.MultipleChoiceField(Reference_model.objects.all())
    SequencingAgent = forms.MultipleChoiceField(Contact_model.objects.all())
    SequenceLength = forms.IntegerField(blank=True, null=True)
    DirectAccessURL = forms.CharField(max_length=1000, blank=True, null=True)

class SequencesType_form(forms.Form):
    Sequence = forms.MultipleChoiceField(Sequence_model.objects.all())

class SpecimenMeasurementsOrFactsType_form(forms.Form):
    SpecimenMeasurementOrFact = forms.MultipleChoiceField(MeasurementOrFact_model.objects.all())

class SpecimenUnitType_form(forms.Form):
    Owner = forms.MultipleChoiceField(Contact_model.objects.all())
    LoanRestrictions = forms.MultipleChoiceField(LoanRestrictionsType_model.objects.all())
    Acquisition = forms.MultipleChoiceField(AcquisitionType_model.objects.all())
    Accessions = forms.MultipleChoiceField(AccessionsType_model.objects.all())
    Preparations = forms.MultipleChoiceField(PreparationsType_model.objects.all())
    PreparationsText = forms.MultipleChoiceField(StringL_model.objects.all())
    Preservations = forms.MultipleChoiceField(PreservationsType_model.objects.all())
    Marks = forms.MultipleChoiceField(MarksType_model.objects.all())
    PreviousUnits = forms.MultipleChoiceField(PreviousUnitsType_model.objects.all())
    PreviousUnitsText = forms.CharField(max_length=1000, blank=True, null=True)
    NomenclaturalTypeDesignations = forms.MultipleChoiceField(NomenclaturalTypeDesignationsType_model.objects.all())
    NomenclaturalTypeText = forms.MultipleChoiceField(StringL_model.objects.all())
    DuplicatesDistributedTo = forms.CharField(max_length=1000, blank=True, null=True)
    Disposition = forms.MultipleChoiceField(StringL_model.objects.all())
    SpecimenMeasurementsOrFacts = forms.MultipleChoiceField(SpecimenMeasurementsOrFactsType_model.objects.all())

class StratigraphicTerm_form(forms.Form):
    Domain = forms.CharField(max_length=1000, blank=True, null=True)
    Term = forms.CharField(max_length=1000, )
    Source = forms.MultipleChoiceField(Reference_model.objects.all())
    Comment = forms.CharField(max_length=1000, blank=True, null=True)

class StratigraphicTermL_form(forms.Form):
    language = forms.CharField(max_length=1000, blank=True, null=True)

class Stratigraphy_form(forms.Form):
    ChronostratigraphicTerms = forms.MultipleChoiceField(ChronostratigraphicTermsType_model.objects.all())
    BiostratigraphicTerms = forms.MultipleChoiceField(BiostratigraphicTermsType_model.objects.all())
    LithostratigraphicTerms = forms.MultipleChoiceField(LithostratigraphicTermsType_model.objects.all())
    StratigraphyText = forms.MultipleChoiceField(StringL_model.objects.all())

class StringL_form(forms.Form):
    language = forms.CharField(max_length=1000, blank=True, null=True)
    valueOf_x = forms.CharField(max_length=1000, )

class StringL255_form(forms.Form):
    language = forms.CharField(max_length=1000, blank=True, null=True)
    valueOf_x = forms.CharField(max_length=1000, )

class StringLP_form(forms.Form):
    language = forms.CharField(max_length=1000, blank=True, null=True)
    preferred = forms.NullBooleanField(blank=True, null=True)
    valueOf_x = forms.CharField(max_length=1000, )

class StringLP255_form(forms.Form):
    language = forms.CharField(max_length=1000, blank=True, null=True)
    preferred = forms.NullBooleanField(blank=True, null=True)
    valueOf_x = forms.CharField(max_length=1000, )

class StringP_form(forms.Form):
    preferred = forms.NullBooleanField(blank=True, null=True)
    valueOf_x = forms.CharField(max_length=1000, )

class StringP255_form(forms.Form):
    preferred = forms.NullBooleanField(blank=True, null=True)
    valueOf_x = forms.CharField(max_length=1000, )

class SuggestedCitationsType_form(forms.Form):
    SuggestedCitation = forms.MultipleChoiceField(LegalStatement_model.objects.all())

class SynecologyType_form(forms.Form):
    Syntaxon = forms.CharField(max_length=1000, blank=True, null=True)
    Notes = forms.MultipleChoiceField(StringL_model.objects.all())
    AssociatedTaxa = forms.MultipleChoiceField(AssociatedTaxaType_model.objects.all())

class TagsType_form(forms.Form):
    Tag = forms.CharField(max_length=1000, )

class TaxaInBackgroundType_form(forms.Form):
    TaxonInBackground = forms.MultipleChoiceField(TaxonIdentified_model.objects.all())

class TaxonIdentified_form(forms.Form):
    HigherTaxa = forms.MultipleChoiceField(HigherTaxaType_model.objects.all())
    ScientificName = forms.MultipleChoiceField(ScientificName_model.objects.all())
    InformalName = forms.MultipleChoiceField(StringL_model.objects.all())
    NameComments = forms.MultipleChoiceField(StringL_model.objects.all())
    Code = forms.CharField(max_length=1000, blank=True, null=True)

class TaxonomicTermsType_form(forms.Form):
    TaxonomicTerm = forms.MultipleChoiceField(StringL255_model.objects.all())

class TechnicalContactsType_form(forms.Form):
    TechnicalContact = forms.MultipleChoiceField(ContactP_model.objects.all())

class TelephoneNumbersType_form(forms.Form):
    TelephoneNumber = forms.MultipleChoiceField(StringP255_model.objects.all())

class Temperature_form(forms.Form):
    scale = forms.CharField(max_length=1000, blank=True, null=True)
    valueOf_x = forms.CharField(max_length=1000, )

class TradeDesignationNamesType_form(forms.Form):
    TradeDesignationName = forms.CharField(max_length=1000, )

class Unit_form(forms.Form):
    GUID = forms.CharField(max_length=1000, blank=True, null=True)
    SourceInstitutionID = forms.CharField(max_length=1000, )
    SourceID = forms.CharField(max_length=1000, )
    ID = forms.CharField(max_length=1000, )
    NumericID = forms.IntegerField(blank=True, null=True)
    LastEditor = forms.MultipleChoiceField(Contact_model.objects.all())
    DateModified = forms.CharField(max_length=1000, blank=True, null=True)
    Owner = forms.MultipleChoiceField(Contact_model.objects.all())
    LegalStatements = forms.MultipleChoiceField(LegalStatements_model.objects.all())
    ContentContacts = forms.MultipleChoiceField(ContentContactsType3_model.objects.all())
    InformationWithheld = forms.MultipleChoiceField(StringL_model.objects.all())
    SourceReference = forms.MultipleChoiceField(Reference_model.objects.all())
    UnitReferences = forms.MultipleChoiceField(UnitReferencesType_model.objects.all())
    Identifications = forms.MultipleChoiceField(IdentificationsType_model.objects.all())
    IdentificationHistory = forms.CharField(max_length=1000, blank=True, null=True)
    RecordBasis = forms.CharField(max_length=1000, blank=True, null=True)
    KindOfUnit = forms.MultipleChoiceField(StringL_model.objects.all())
    SpecimenUnit = forms.MultipleChoiceField(SpecimenUnitType_model.objects.all())
    ObservationUnit = forms.MultipleChoiceField(ObservationUnitType_model.objects.all())
    CultureCollectionUnit = forms.MultipleChoiceField(CultureCollectionUnit_model.objects.all())
    MycologicalUnit = forms.MultipleChoiceField(MycologicalUnit_model.objects.all())
    HerbariumUnit = forms.MultipleChoiceField(HerbariumUnit_model.objects.all())
    BotanicalGardenUnit = forms.MultipleChoiceField(BotanicalGardenUnit_model.objects.all())
    PlantGeneticResourcesUnit = forms.MultipleChoiceField(PGRUnit_model.objects.all())
    ZoologicalUnit = forms.MultipleChoiceField(ZoologicalUnit_model.objects.all())
    PaleontologicalUnit = forms.MultipleChoiceField(PaleontologicalUnit_model.objects.all())
    MultimediaObjects = forms.MultipleChoiceField(MultimediaObjectsType5_model.objects.all())
    Associations = forms.MultipleChoiceField(AssociationsType_model.objects.all())
    Assemblages = forms.MultipleChoiceField(AssemblagesType_model.objects.all())
    NamedCollectionsOrSurveys = forms.MultipleChoiceField(NamedCollectionsOrSurveysType_model.objects.all())
    Gathering = forms.MultipleChoiceField(Gathering_model.objects.all())
    FieldNumbers = forms.MultipleChoiceField(FieldNumbersType_model.objects.all())
    FieldNotes = forms.MultipleChoiceField(StringL_model.objects.all())
    FieldNotesReferences = forms.MultipleChoiceField(FieldNotesReferencesType_model.objects.all())
    MeasurementsOrFacts = forms.MultipleChoiceField(MeasurementsOrFactsType8_model.objects.all())
    Sex = forms.CharField(max_length=1000, blank=True, null=True)
    Age = forms.CharField(max_length=1000, blank=True, null=True)
    Sequences = forms.MultipleChoiceField(SequencesType_model.objects.all())
    Notes = forms.MultipleChoiceField(StringL_model.objects.all())
    WebsiteURL = forms.CharField(max_length=1000, blank=True, null=True)
    Annotations = forms.MultipleChoiceField(AnnotationsType_model.objects.all())
    UnitExtensions = forms.MultipleChoiceField(UnitExtensionsType_model.objects.all())
    ResourceURIs = forms.MultipleChoiceField(ResourceURIsType9_model.objects.all())

class UnitExtensionsType_form(forms.Form):
    UnitExtension = forms.CharField(max_length=1000, )

class UnitReferencesType_form(forms.Form):
    UnitReference = forms.MultipleChoiceField(Reference_model.objects.all())

class UnitsType_form(forms.Form):
    Unit = forms.MultipleChoiceField(Unit_model.objects.all())

class VersionType_form(forms.Form):
    Major = forms.IntegerField()
    Minor = forms.IntegerField(blank=True, null=True)
    Modifier = forms.CharField(max_length=1000, blank=True, null=True)
    DateCreated = forms.CharField(max_length=1000, blank=True, null=True)
    VersionText = forms.MultipleChoiceField(StringL_model.objects.all())

class VideoType_form(forms.Form):
    Microphone = forms.CharField(max_length=1000, blank=True, null=True)
    LensModel = forms.CharField(max_length=1000, blank=True, null=True)
    LightSource = forms.CharField(max_length=1000, blank=True, null=True)
    AudioChannel = forms.CharField(max_length=1000, blank=True, null=True)
    DurationTimeCode = forms.CharField(max_length=1000, blank=True, null=True)
    AudioEncoding = forms.CharField(max_length=1000, blank=True, null=True)
    AudioBitrate = forms.CharField(max_length=1000, blank=True, null=True)
    AspectRatio = forms.CharField(max_length=1000, blank=True, null=True)
    VideoEncoding = forms.CharField(max_length=1000, blank=True, null=True)
    VideoBitrate = forms.CharField(max_length=1000, blank=True, null=True)
    Framerate = forms.CharField(max_length=1000, blank=True, null=True)
    CaptureFramerate = forms.CharField(max_length=1000, blank=True, null=True)
    Color = forms.CharField(max_length=1000, blank=True, null=True)
    ThumbnailURL = forms.CharField(max_length=1000, blank=True, null=True)
    ImageSize = forms.MultipleChoiceField(imageSize_model.objects.all())
    CallType = forms.CharField(max_length=1000, blank=True, null=True)
    NumberOfNotes = forms.CharField(max_length=1000, blank=True, null=True)
    Subtitles = forms.CharField(max_length=1000, blank=True, null=True)
    SubtitlesFormat = forms.CharField(max_length=1000, blank=True, null=True)
    Chapters = forms.CharField(max_length=1000, blank=True, null=True)

class ZoologicalUnit_form(forms.Form):
    PhasesOrStages = forms.MultipleChoiceField(PhasesOrStagesType_model.objects.all())

class anyUriP_form(forms.Form):
    preferred = forms.NullBooleanField(blank=True, null=True)
    valueOf_x = forms.CharField(max_length=1000, )

class imageSize_form(forms.Form):
    Width = forms.IntegerField()
    Height = forms.IntegerField()
