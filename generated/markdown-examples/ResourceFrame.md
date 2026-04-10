# ResourceFrame

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | ResourceFrame | mandatory | 1..1 | unknown |  |  |
| + | responsibilitySets | mandatory | 1..1 | unknown |  |  |
| ln++ | [ResponsibilitySet](ResponsibilitySet.md) | mandatory | 1..1 | unknown |  |  |
| + | typesOfValue | mandatory | 1..1 | unknown |  |  |
| ++ | ValueSet | mandatory | 1..1 | unknown |  |  |
| + | organisations | mandatory | 1..1 | unknown |  |  |
| ln++ | [Operator](Operator.md) | mandatory | 1..1 | unknown |  |  |
| + | siteFacilitySets | optional | 1..1 | unknown |  |  |
| ln++ | [SiteFacilitySet](SiteFacilitySet.md) | optional | 1..1 | unknown |  |  |
| ln++ | [ServiceFacilitySet](ServiceFacilitySet.md) | optional | 1..1 | unknown |  |  |
