# ServiceJourney

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
| + | validityConditions | expected | 1..1 | unknown |  |  |
| ln++ | [AvailabilityCondition](AvailabilityCondition.md) | expected | 1..1 | unknown |  |  |
| + | keyList | mandatory | 1..1 | unknown |  |  |
| ++ | KeyValue | mandatory | 1..1 | unknown |  |  |
| +++ | Key | mandatory | 1..1 | unknown |  |  |
| +++ | Value | mandatory | 1..1 | unknown |  |  |
| + | Extensions | optional | 1..1 | unknown |  |  |
| ++ | facilities | optional | 1..1 | unknown |  |  |
| ln+++ | [Facility](Facility.md) | optional | 1..1 | unknown |  |  |
| + | PrivateCode | optional | 1..1 | unknown |  |  |
| + | TransportMode | optional | 1..1 | unknown |  |  |
| + | TypeOfProductCategoryRef | expected | 1..1 | unknown |  |  |
| + | TypeOfServiceRef | optional | 1..1 | unknown |  |  |
| + | noticeAssignments | optional | 1..1 | unknown |  |  |
| ln++ | [NoticeAssignment](NoticeAssignment.md) | optional | 1..1 | unknown |  |  |
| + | occupancies | optional | 1..1 | unknown |  |  |
| ln++ | [OccupancyView](OccupancyView.md) | optional | 1..1 | unknown |  |  |
| + | ServiceAlteration | optional | 1..1 | unknown |  |  |
| + | DepartureTime | expected | 1..1 | unknown |  |  |
| + | DepartureTimeOffset | optional | 1..1 | unknown |  |  |
| + | LineRef | mandatory | 1..1 | unknown |  |  |
| + | DirectionType | optional | 1..1 | unknown |  |  |
| + | trainNumbers | mandatory | 1..1 | unknown |  |  |
| ++ | TrainNumberRef | mandatory | 1..1 | unknown |  |  |
| + | passingTimes | mandatory | 1..1 | unknown |  |  |
| ln++ | [TimetabledPassingTime](TimetabledPassingTime.md) | expected | 1..1 | unknown |  |  |
