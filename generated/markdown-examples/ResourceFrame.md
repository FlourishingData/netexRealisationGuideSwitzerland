# ResourceFrame

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | frames | ignored | 1..1 | unknown |  |  |
| > | ResourceFrame | ignored | 1..1 | unknown |  |  |
| >> | organisations | ignored | 1..1 | unknown |  |  |
| >> | responsibilitySets | mandatory | 1..1 | unknown |  |  |
| >> | serviceFacilitySets | ignored | 1..1 | unknown |  |  |
| >> | siteFacilitySets | ignored | 1..1 | unknown |  |  |
| >> | typesOfValue | mandatory | 1..1 | unknown |  |  |
| <>>> | [Operator](Operator.md) | mandatory | 1..1 | unknown | We will use this organisation also in AuthorityRef. The problem is that the sboid can be used only once. | We will use this organisation also in AuthorityRef. The problem is that the sboid can be used only once. |
| <>>> | [ResponsibilitySet](ResponsibilitySet.md) | mandatory | 1..1 | unknown | Each combination of Authority and Operator needs a ResponsibilitySet. | Each combination of Authority and Operator needs a ResponsibilitySet. |
| <>>> | [ServiceFacilitySet](ServiceFacilitySet.md) | ignored | 1..1 | unknown |  |  |
| <>>> | [SiteFacilitySet](SiteFacilitySet.md) | ignored | 1..1 | unknown |  |  |
| >>> | ValueSet | mandatory | 1..1 | unknown |  |  |
| >>> | ValueSet | ignored | 1..1 | unknown |  |  |
| >>>> | values | mandatory | 1..1 | unknown |  |  |
| >>>>> | TypeOfNotice | ignored | 1..1 | unknown |  |  |
| >>>>> | TypeOfNotice | ignored | 1..1 | unknown |  |  |
| >>>>> | TypeOfNotice | ignored | 1..1 | unknown |  |  |
| >>>>> | TypeOfNotice | ignored | 1..1 | unknown |  |  |
| >>>>> | TypeOfNotice | ignored | 1..1 | unknown |  |  |
| >>>>>> | Name | ignored | 1..1 | unknown |  |  |
| >>>>>> | PrivateCode | ignored | 1..1 | unknown |  |  |
