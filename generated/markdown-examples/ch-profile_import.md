# ch-profile_import

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | PublicationDelivery | mandatory | 1..1 | PublicationDeliveryStructure | A set of NeTEx objects as assembled by a publication request or other service. Provides a general purpose wrapper for NeTEx data content. |  |
| + | PublicationTimestamp | mandatory | 1..1 | xsd:dateTime | Time of output of data. |  |
| + | ParticipantRef | mandatory | 1..1 | siri:ParticipantCodeType | Identifier of system requesting Data. |  |
| + | dataObjects | mandatory | 1..1 | unknown |  |  |
| ++ | CompositeFrame | mandatory | 1..1 | unknown |  |  |
| +++ | frames | mandatory | 1..1 | unknown |  |  |
| ln++++ | [ResourceFrame](ResourceFrame.md) | mandatory | 1..1 | unknown |  |  |
| ln++++ | [ServiceFrame](ServiceFrame.md) | mandatory | 1..1 | unknown |  |  |
| ln++++ | [ServiceCalendarFrame](ServiceCalendarFrame.md) | mandatory | 1..1 | unknown |  |  |
| ln++++ | [TimetableFrame](TimetableFrame.md) | mandatory | 1..1 | unknown |  |  |
