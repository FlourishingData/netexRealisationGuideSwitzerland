# ch-profile_export-timetable_file

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
| + | PublicationTimestamp | mandatory | 1..1 | xsd:dateTime | Time of output of data. |  |
| + | ParticipantRef | mandatory | 1..1 | siri:ParticipantCodeType | Identifier of system requesting Data. |  |
| + | dataObjects | mandatory | 1..1 | unknown |  |  |
| ++ | CompositeFrame | mandatory | 1..1 | unknown |  |  |
| +++ | frames | mandatory | 1..1 | unknown |  |  |
| ln++++ | [ResourceFrame](ResourceFrame.md) | expected | 1..1 | unknown |  |  |
| ln++++ | [ServiceFrame](ServiceFrame.md) | expected | 1..1 | unknown |  |  |
| ln++++ | [ServiceCalendarFrame](ServiceCalendarFrame.md) | expected | 1..1 | unknown |  |  |
| ln++++ | [TimetableFrame](TimetableFrame.md) | mandatory | 1..1 | unknown |  |  |
