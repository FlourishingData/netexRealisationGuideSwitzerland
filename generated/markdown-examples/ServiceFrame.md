# ServiceFrame

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | frames | ignored | 1..1 | unknown |  |  |
| > | ServiceFrame | ignored | 1..1 | unknown | TODO how would we describe additional id and which ones are mandatory? | TODO how would we describe additional id and which ones are mandatory? |
| >> | connections | ignored | 1..1 | unknown |  |  |
| >> | destinationDisplays | ignored | 1..1 | unknown | We only allow fully formed content of destinationDisplays | We only allow fully formed content of destinationDisplays |
| >> | directions | forbidden | 1..1 | unknown | We don't use directions, but only direction type | We don't use directions, but only direction type |
| >> | groupsOfLines | forbidden | 1..1 | unknown |  |  |
| >> | lines | mandatory | 1..1 | unknown | Only Line is used and not FlexibleLine | Only Line is used and not FlexibleLine |
| >> | notices | ignored | 1..1 | unknown | notices may be present or not | notices may be present or not |
| >> | scheduledStopPoints | ignored | 1..1 | unknown | Swiss ScheduledStopPoint are using the sloid in the id, when possible. | Swiss ScheduledStopPoint are using the sloid in the id, when possible. |
| >> | stopAssignments | ignored | 1..1 | unknown |  |  |
| >>> | Access | forbidden | 1..1 | unknown |  |  |
| <>>> | [Connection](Connection.md) | ignored | 1..1 | unknown | Connection is used only used in the site file | Connection is used only used in the site file |
| <>>> | [DefaultConnection](DefaultConnection.md) | ignored | 1..1 | unknown | DefaultConnection is only used in the site file | DefaultConnection is only used in the site file |
| <>>> | [DestinationDisplay](DestinationDisplay.md) | ignored | 1..1 | unknown | We only allow fully formed content of destinationDisplays | We only allow fully formed content of destinationDisplays |
| >>> | Direction | forbidden | 1..1 | unknown |  |  |
| >>> | FlexibleLine | forbidden | 1..1 | unknown | We work with Line only. | We work with Line only. |
| >>> | GroupOfLines | forbidden | 1..1 | unknown |  |  |
| <>>> | [Line](Line.md) | mandatory | 1..1 | unknown |  |  |
| <>>> | [Notice](Notice.md) | ignored | 1..1 | unknown | if notices are present, one Notice must be. | if notices are present, one Notice must be. |
| <>>> | [PassengerStopAssignment](PassengerStopAssignment.md) | ignored | 1..1 | unknown | are only ued in a special PSA file in the export. | are only ued in a special PSA file in the export. |
| >>> | ScheduledStopPoint | ignored | 1..1 | unknown | TODO full or not | TODO full or not |
| <>>> | [SiteConnection](SiteConnection.md) | ignored | 1..1 | unknown | SiteConnection are used only in the main file and not in timetable files. | SiteConnection are used only in the main file and not in timetable files. |
| >>>> | From | ignored | 1..1 | unknown |  |  |
| >>>> | Name | ignored | 1..1 | unknown |  |  |
| >>>> | To | ignored | 1..1 | unknown |  |  |
