# SiteFrame

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | SiteFrame | expected | 1..1 | unknown |  | **TODO** most documenation from the RG is missing here. Pls note that with expection from ch-start and ch-stop. All other annotations are to be put within the element |
| + | topographicPlaces | optional | 1..1 | unknown |  |  |
| ln++ | [TopographicPlace](TopographicPlace.md) | expected | 1..1 | unknown |  |  |
| + | stopPlaces | mandatory | 1..1 | unknown |  |  |
| ln++ | [StopPlace](StopPlace.md) | mandatory | 1..1 | unknown |  |  |
| + | siteFacilitySets | optional | 1..1 | unknown |  |  |
| ln++ | [SiteFacilitySet](SiteFacilitySet.md) | optional | 1..1 | unknown |  |  |
