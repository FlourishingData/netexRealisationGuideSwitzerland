# ServiceFacilitySet

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | serviceFacilitySets | ignored | 1..1 | unknown |  |  |
| > | ServiceFacilitySet | ignored | 1..1 | unknown | List of ServiceFacility. Be careful: not all are supported. Consult profile. Make sure to not generate identical ServiceFacilitySets. Reuse them. | List of ServiceFacility. Be careful: not all are supported. Consult profile. Make sure to not generate identical ServiceFacilitySets. Reuse them. |
| >> | CouchetteFacilityList | ignored | 1..1 | unknown |  |  |
| >> | GroupBookingFacility | ignored | 1..1 | unknown |  |  |
| >> | NuisanceFacilityList | ignored | 1..1 | unknown |  |  |
| >> | SanitaryFacilityList | ignored | 1..1 | unknown |  |  |
| >> | accommodations | ignored | 1..1 | unknown |  |  |
| >>> | AccommodationRef | ignored | 1..1 | unknown |  |  |
