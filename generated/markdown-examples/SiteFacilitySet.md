# SiteFacilitySet

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | SiteFacilitySet | mandatory | 1..1 | unknown |  | List of SiteFacility. Be careful: not all are supported. Consult profile. Make sure to not generate identical SiteFacilitySets. Reuse them. |
| + | validityConditions | optional | 1..1 | unknown |  |  |
| ln++ | [AvailabilityCondition](AvailabilityCondition.md) | mandatory | 1..1 | unknown |  |  |
| + | FareClasses | optional | 1..1 | unknown |  |  |
| + | SanitaryFacilityList | optional | 1..1 | unknown |  |  |
| + | TicketingServiceFacilityList | optional | 1..1 | unknown |  |  |
| + | LuggageLockerFacilityList | optional | 1..1 | unknown |  |  |
