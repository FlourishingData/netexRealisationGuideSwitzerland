# TimetableFrame

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
| + | vehicleJourneys | expected | 1..1 | unknown |  |  |
| ln++ | [ServiceJourney](ServiceJourney.md) | expected | 1..1 | unknown |  |  |
| ln++ | [TemplateServiceJourney](TemplateServiceJourney.md) | expected | 1..1 | unknown |  |  |
| + | trainNumbers | expected | 1..1 | unknown |  |  |
| ln++ | [TrainNumber](TrainNumber.md) | mandatory | 1..1 | unknown |  |  |
| + | serviceFacilitySets | optional | 1..1 | unknown |  |  |
| ln++ | [ServiceFacilitySet](ServiceFacilitySet.md) | expected | 1..1 | unknown |  |  |
| + | typesOfService | expected | 1..1 | unknown |  |  |
| ++ | TypeOfService | optional | 1..1 | unknown |  |  |
| + | journeyMeetings | optional | 1..1 | unknown |  |  |
| ln++ | [JourneyMeeting](JourneyMeeting.md) | optional | 1..1 | unknown |  |  |
| + | interchangeRules | expected | 1..1 | unknown |  |  |
| ln++ | [InterchangeRule](InterchangeRule.md) | expected | 1..1 | unknown |  |  |
