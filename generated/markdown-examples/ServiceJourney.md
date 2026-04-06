# ServiceJourney

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | vehicleJourneys | ignored | 1..1 | unknown |  |  |
| > | ServiceJourney | ignored | 1..1 | unknown |  |  |
| >> | DepartureTime | ignored | 1..1 | unknown |  |  |
| >> | DirectionType | ignored | 1..1 | unknown |  |  |
| >> | Extensions | ignored | 1..1 | unknown |  |  |
| >> | LineRef | mandatory | 1..1 | unknown |  |  |
| >> | PrivateCode | ignored | 1..1 | unknown |  |  |
| >> | ServiceAlteration | ignored | 1..1 | unknown |  |  |
| >> | TransportMode | ignored | 1..1 | unknown |  |  |
| >> | TypeOfProductCategoryRef | ignored | 1..1 | unknown |  |  |
| >> | TypeOfServiceRef | ignored | 1..1 | unknown |  |  |
| >> | keyList | ignored | 1..1 | unknown |  |  |
| >> | noticeAssignments | ignored | 1..1 | unknown |  |  |
| >> | passingTimes | ignored | 1..1 | unknown |  |  |
| >> | trainNumbers | ignored | 1..1 | unknown |  |  |
| >> | validityConditions | ignored | 1..1 | unknown |  |  |
| >>> | AvailabilityCondition | ignored | 1..1 | unknown |  |  |
| >>> | KeyValue | ignored | 1..1 | unknown |  |  |
| <>>> | [NoticeAssignment](NoticeAssignment.md) | ignored | 1..1 | unknown |  |  |
| <>>> | [TimetabledPassingTime](TimetabledPassingTime.md) | ignored | 1..1 | unknown |  |  |
| >>> | TrainNumberRef | mandatory | 1..1 | unknown |  |  |
| >>> | facilities | ignored | 1..1 | unknown |  |  |
| >>>> | Facility | ignored | 1..1 | unknown |  |  |
| >>>> | FromDate | mandatory | 1..1 | unknown |  |  |
| >>>> | Key | ignored | 1..1 | unknown |  |  |
| >>>> | ToDate | mandatory | 1..1 | unknown |  |  |
| >>>> | ValidDayBits | mandatory | 1..1 | unknown |  |  |
| >>>> | Value | ignored | 1..1 | unknown |  |  |
| >>>> | timebands | ignored | 1..1 | unknown |  |  |
| >>>>> | ServiceFacilitySetRef | ignored | 1..1 | unknown |  |  |
| <>>>>> | [Timeband](Timeband.md) | ignored | 1..1 | unknown |  |  |
