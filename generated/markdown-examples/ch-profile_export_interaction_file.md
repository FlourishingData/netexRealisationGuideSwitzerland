# ch-profile_export_interaction_file

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
| + | ParticipantRef | mandatory | 1..1 | siri:ParticipantCodeType | Identifier of system requesting Data. |  |
| + | PublicationTimestamp | mandatory | 1..1 | xsd:dateTime | Time of output of data. |  |
| + | dataObjects | mandatory | 1..1 | unknown |  |  |
| ++ | CompositeFrame | mandatory | 1..1 | unknown |  |  |
| +++ | frames | mandatory | 1..1 | unknown |  |  |
| ++++ | TimetableFrame | mandatory | 1..1 | unknown |  |  |
| +++++ | interchangeRules | expected | 1..1 | unknown |  |  |
| +++++ | journeyMeetings | optional | 1..1 | unknown |  |  |
| ln++++++ | [JourneyMeeting](JourneyMeeting.md) | expected | 1..1 | unknown |  |  |
