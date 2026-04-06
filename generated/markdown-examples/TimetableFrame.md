# TimetableFrame

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | frames | ignored | 1..1 | unknown |  |  |
| > | TimetableFrame | ignored | 1..1 | unknown |  |  |
| >> | trainNumbers | ignored | 1..1 | unknown |  |  |
| >> | typesOfService | ignored | 1..1 | unknown |  |  |
| >> | vehicleJourneys | ignored | 1..1 | unknown |  |  |
| <>>> | [TemplateServiceJourney](TemplateServiceJourney.md) | ignored | 1..1 | unknown |  |  |
| >>> | TemplateServiceJourney | ignored | 1..1 | unknown |  |  |
| <>>> | [TrainNumber](TrainNumber.md) | ignored | 1..1 | unknown |  |  |
| >>> | TypeOfService | ignored | 1..1 | unknown | This is exactly how the TypeOfService should be defined for Switzerland. Attention: Only once per file. | This is exactly how the TypeOfService should be defined for Switzerland. Attention: Only once per file. |
| <>>> | [VehicleJourney](VehicleJourney.md) | ignored | 1..1 | unknown |  |  |
| >>>> | Name | ignored | 1..1 | unknown |  |  |
| >>>> | PrivateCode | ignored | 1..1 | unknown |  |  |
| >>>> | ShortName | ignored | 1..1 | unknown |  |  |
