
# Building the profile checker and most documentation tables from templates
First thoughts based on the idea that XML examples could be used as a scaffold for a 
documentation of the profile:
* **Principle:** An XML example/template is annotated with comments that contain all necessary information allowing (a) to derive the Swiss profile from the NeTEx schema, and (b) to provide useful profile-specific documentation.
* **Machinery:** Software made by SBB and by Hans-Jürgen Rennau is likely capable of generating documentation tables for each XML example/template, as well a a complete xsd for the Swiss profile. 


**Advantages:**
- Profile specification attached to XML example/template is quite easily readable and maintainable.
- Minimal effort when NeTEx changes
- XML examples/templates can be copy-pasted by users and the comments help understanding and adhering to the profile.

## Processes

The templates are used in three ways:
- generate example xml files with elements to be used directly
- markdown tables for documentation
- schematron files

### Possible markdown result: StopPlace
The following shows the idea of and output table we want to have:

| Sub   | Element             | Usage     | Card | Type                     | Description                                                                                                                           | Note                                                                                                                                                                                                                                                                                                                                                                        |
| ----- | ------------------- | --------- |------| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <<    | ValidBetween        | mandatory | 1..1 | ValidBetweenType         | Validity of the StopPlace                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                             |
|       | alternativeTexts    | mandatory | 0..1 | AlternativeTextType[]    | Alternative texts for the StopPlace                                                                                                   | Abbreviation of the STOP PLACE.                                                                                                                                                                                                                                                                                                                                             |
| >>    | AlternativeText     | mandatory | 1..* | AlternativeTextType      | ALTERNATIVE TEXTs associated with ENTITY.                                                                                             | Variant for de is always required. Further languages fr, it, en only necessary if different from de.                                                                                                                                                                                                                                                                        |
| >>>>  | Text                | mandatory | 1..1 | MultilingualString       | Variant of the text in the specified language.                                                                                        | Name of the StopPlace in a defined language                                                                                                                                                                                                                                                                                                                                 |
| <<    | keyList             | mandatory | 0..1 | KeyListType              |                                                                                                                                       | KEY LIST with the KEY VALUEs related to the STOP PLACE. SKI use KeyValues: one for the Didok number one for the SLOID For delivery to SKI only one Value is necessary.                                                                                                                                                                                                      |
|       | Extensions          | mandatory | 1..1 | ExtensionsType           | See description of extensions                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                             |
| >>    | HafasPriority       | mandatory | 1..1 | ValueType                |                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                             |
| >>>>  | Value               | mandatory | 1..1 | xsd:nonNegativeInteger   |                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                             |
| >>    | HafasKMInfo         | expected  | 0..1 | ValueType                |                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                             |
| >>>>  | Value               | mandatory | 1..1 | xsd:nonNegativeInteger   |                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                             |
|       | Name                | mandatory | 1..1 | MultilingualString       | The name of the StopPlace                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                             |
|       | ShortName           | expected  | 0..1 | MultilingualString       | Description of TYPE OF VALUE.                                                                                                         | Is used to transmit the abbreviation of the StopPlace. There is not one abbreviation for all StopPlaces                                                                                                                                                                                                                                                                     |
|       | PrivateCode         | mandatory | 1..1 | xsd:string               | Private Code of STOP PLACE.                                                                                                           | Field **must be filled**. In Switzerland it is the **DiDok** number.                                                                                                                                                                                                                                                                                                        |
| <<    | Centroid            | expected  | 0..1 | CentroidType             | Global or national location of STOP PLACE.                                                                                            |                                                                                                                                                                                                                                                                                                                                                                             |
|       | alternativeNames    | expected  | 0..1 | AlternativeNameType[]    | Alternative names for SITE ELEMENT.                                                                                                   | We will also use these for synonyms. From INFO+ the synonyms are used on the StopPlace.                                                                                                                                                                                                                                                                                     |
| >> << | AlternativeName     | expected  | 0..* | AlternativNameType       |                                                                                                                                       | **Use NameType alias, TypeOfName official.**                                                                                                                                                                                                                                                                                                                                |
|       | TopographicPlaceRef | expected  | 0..1 | TopographicPlaceRefType  | Reference to TopographicPlace. Link to TopographicPlace of type county or country                                                     |                                                                                                                                                                                                                                                                                                                                                                             |
|       | Weighting           | optional  | 0..1 | InterchangeWeightingEnum | STOP PLACEs can be classified for their relative desirability (weighting) as an interchange.                                          | Default relative weighting to be used for stop place. The STOP PLACE element WEIGHTING basically accomplishes this feature but only allows the following values: noInterchange interchangeAllowed recommendedInterchange preferredInterchange. To incorporate the desired value range, we will add an EXTENSION element “HafasPriority” that contains the full information. |
|       | quays               | expected  | 0..1 | QuayType[]               | The QUAYs contained in the STOP PLACE, that is platforms, jetties, bays, taxi ranks, and other points of physical access to VEHICLEs. |                                                                                                                                                                                                                                                                                                                                                                             |
| >> << | Quay                | expected  | 0..* | QuayType                 |                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                             |

### Legend
* Sub:
  * Identiation rule "<<" mean referenced, ">>" indentation
  * source: Template
* Element:
  * The relevant XML element
  * source: Template
* Usage:
  * How the Swiss profile will use it: mandatory | forbidden
  * source: Template
* Card:
  * Cardinality of the element in NeTEx
  * source: XSD
* Type:
  * the type of the element
  * source: XSD
* Description:
  * The original description from the XSD.
  * source: XSD
* Notes:
  * Notes from the Swiss profile
  * source: Template

## Templates are valid NeTEx XML file
Each template is a valid XML file itself. So one can also study them directly.
Everything is done with annotations in comments below/within the elements.

e.g.
```commandline
<ResponsibilitySet id="ch:1:ResponsbilitySet-gen" version="1">
	<!-- ch-note: Each combination of Authority and Operator needs a ResponsibilitySet. -->
	<!-- ch-usage: mandatory -->
	<!-- ch-referenced -->
```
We have two snippets that say where the relevant part of the template start (the part that defines the thing we want to process afterwards):
* `<!-- ch-start: Example starts here -->`
* `<!-- ch-stop: Example stops here -->`

For the top level templates only the first line `<?xml version="1.0" encoding="UTF-8"?>
` is not in scope.
For the others it is the element that needs to be processed (e.g. `StopPlace` in `StopPlace.xml`).

It is also shown that multiple annotations can be used for one element.

## Annotations in the templates and what they do achieve

The document https://github.com/openTdataCH/netexRealisationGuideSwitzerland/blob/main/mgmt/Changes_in_profile.md describes the changes we might want to apply to the standard NeTEx schema in order to obtain the profile. 
Here we describe, what we realised so far and what is planned.

Important behaviour for the markdown: 
**Only elements having one of the `<!-- ch-<annotation> -->` will be shown in the tables.**


### Add description
The profile wants to add a more specialised description. Below the begin tag of the element there a comment is added:
`<!-- ch-note: <Text> -->` and `<!-- ch-notice: <Text> -->`

Output:
* schematron: In the schematron this will result in a comment. 
* markdown: This will be used in the note part of the table.
* xml: This will remain as a comment without the the starting **Swiss profile**.

### Change usage
The profile wants to make elements mandatory ord forbidden.  
`<!-- ch-usage: <mandatory|forbidden|optional|ignored|expected> -->`

Output:
* schematron: forbidden and mandatory result in rules.
* markdown: will be used for the usage column.
* xml: `forbidden` and `ignored` are removed


### Restricted choice
In some cases only a subset of choices is allowed.
If only one choice is allowed - simple: the template XML shows only the allowed variant. 
If multiple choices are allowed - the template XML could be extended with additonal variants (thereby violating the xsd) and marking all elements affected by the choices.

**Note: We did not implement this. In many cases having forbidden/mandatory is enough.**

### Deprecated
Perhaps some elements are still used, but will be deprecated. This is marked with this flag:
`<!-- ch-deprecated -->`

* schematron: warning (report) is produced.
* markdown: tbd
* xml: not used anymore.

### Restrict an enumeration in a given element
We might want to restrict some enumerations and allow only some variants.
Certainly a notice can be made.

The improved element needs testing, when we see a first example:

**NOTE: TBD **

### Restrict strings, integers etc
We won't do this currently.
e.g. only values between-5 and 5.

### Restrict the allowed types in a container
Certainly a notice helps.
With `ch-usage: forbidden` and `ch-usage: mandatory` this can be modeled.
We will often simplify containers to make the processing easier.

e.g. no `QuayRef` in quays only `Quay`

### Extension in extension point
Extensions are explicit in the template XML, must be marked with `ch-usage` when thea are to be used.


### Restrict to a subset of substitutionGroup
Restrictions on elements that are inherited or part of a subgroup is straightforward since they appear explicitely in the template XML and can be marked as necessary. 
This is also done with `ch-usage`.

### Attribute handling
In the NeTEx specification and most profiles a lot is said about attributes too.
For NeTEx 2.0 `id` and `version` are now mandatory, `order' is no longer important.

We will use `responsibilitySetRef` in many cases and want it there. For this we needed a new annotation.

**NOTE: We use `versionRef` sometimes in the template. This allows us to minimize the templates. `versionRef` blocks the XSD validation of the ref-id relationship.
`versionRef` is intended to be used, when the reference is not in the same file.
In all the output form the template processing the `versionRef` is replaced with `version`. 
We will rather have some files that don't validate (`PassengerStopAssinments`, `JourneyMeeting`, `InterchangeRule` etc), than to deal with `versionRef` in our profile. So that's the only part where the templates cannot be taken litterally.**

We have not yet implemented the annotation for the attributes, but it will look like this:

```commandline
<!-- ch-attrs: id version responsibilitySetRef -->
```
If nothing is mentioned, it is only id and version that we want to see.

Other attributes will be ignored by our profile.

### Referencing
When we use `<!-- ch-referenced -->` we express that there is a template with the same name as the element (e.g. `StopPlace` --> `StopPlace.xml`).
In some cases two different types of StopPlace may be needed (e.g. the full version for the site model and the minimal version of the importation from a operator)

Then `<!-- ch-referenced: <alternativefilename> -->` can be used. 

The full version should always be in the "normal" version (here `StopPlace.xml` should contain the full StopPlace as needed for the site model).

With referencing we will do a lot of reuse of elements. So design them carefully.

## Top-level templates
We have in this profile different files. Which then use different schematrons for the different files.

* ch-profile_import:
* ch-simplified_import: later
* ch-profile_resource_file.xml:
* ch-profile_site_file.xml:
* ch-profile_service_file.xml:
* ch-profile_timetable_file.xml:
* ch-profile_psa_file.xml: All PassengerStopAssignments: won't validate
* ch-profile_interactions_file.xml: JourneyMeetings, InterchangeRules: won't validate

## 