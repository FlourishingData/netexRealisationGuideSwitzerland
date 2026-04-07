# Common elements

## id/versions and other attributes

* `version` is generelly always set to `"1"`
* We use `responsibilitySetRef` in the following elements xxx
* We use `nameOfClass` in the XXXRef elements.

## MultilingualString
NeTEx uses the type “MultilingualString” for descriptive text elements (e.g. Notice text, Name, ShortName etc.).
However, only one language can be set for a given element (`<MultilingualString lang=”xx”>`). 
Additional languages are introduced through the `AlternativeName` and `AlternativeText` object described in tbd and tbd.

For the organisations e.g. there are all languages present.

## IDs
It is important to note that internal or artificially generated IDs should not be used to extract content whenever business keys and attributes are available. For readability and easy refer-encing, we will use the following principles:
•	We will use attributes to build the technical IDs.
•	The class of the object is the beginning of the technical ID in general.
•	Where there is a compelling need for global stability, the ID will be a global ID. This in-formation will be also transmitted separately in a KeyList. 

ID must be globally unique during importation. 
IDs may also be partially or completely artificially generated. The persistence of ID between exports is then usually not guaranteed. Important business level keys are stored in ele-ments not in IDs (PublicKey, PrivateKey, KeyList). They must be communicated as attrib-ute in the elements.
