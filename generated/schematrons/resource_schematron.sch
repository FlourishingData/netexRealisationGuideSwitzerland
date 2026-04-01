<?xml version="1.0" encoding="UTF-8"?>
<schema xmlns="http://purl.oclc.org/dsdl/schematron">
	<title>Generated schematron from template</title>
	<pattern id="p1">
		<rule context=".//ResourceFrame">
			<assert test="count(responsibilitySets) &amp;gt; 0">responsibilitySets must be present</assert>
		</rule>
		<rule context=".//responsibilitySets">
			<assert test="count(ResponsibilitySet) &amp;gt; 0">ResponsibilitySet must be present</assert>
		</rule>
		<rule context=".//values">
			<assert test="count(TypeOfProductCategory) &amp;gt; 0">TypeOfProductCategory must be present</assert>
		</rule>
		<rule context=".//Operator">
			<assert test="count(Operator) &amp;gt; 0">Operator must be present</assert>
		</rule>
		<rule context=".//keyList">
			<assert test="count(KeyValue) &amp;gt; 0">KeyValue must be present</assert>
		</rule>
		<rule context=".//organisations">
			<assert test="count(Operator) &amp;gt; 0">Operator must be present</assert>
		</rule>
		<rule context=".//ServiceFrame">
			<assert test="count(directions) = 0">directions must NOT be present</assert>
		</rule>
		<rule context=".//directions">
			<assert test="count(Direction) = 0">Direction must NOT be present</assert>
		</rule>
		<rule context=".//ServiceFrame">
			<assert test="count(lines) &amp;gt; 0">lines must be present</assert>
		</rule>
		<rule context=".//lines">
			<assert test="count(Line) &amp;gt; 0">Line must be present</assert>
		</rule>
		<rule context=".//lines">
			<assert test="count(FlexibleLine) = 0">FlexibleLine must NOT be present</assert>
		</rule>
		<rule context=".//ServiceFrame">
			<assert test="count(groupsOfLines) = 0">groupsOfLines must NOT be present</assert>
		</rule>
		<rule context=".//groupsOfLines">
			<assert test="count(GroupOfLines) = 0">GroupOfLines must NOT be present</assert>
		</rule>
		<rule context=".//connections">
			<assert test="count(Access) = 0">Access must NOT be present</assert>
		</rule>
		<rule context=".//PassengerStopAssignment">
			<assert test="count(ScheduledStopPointRef) &amp;gt; 0">ScheduledStopPointRef must be present</assert>
		</rule>
		<rule context=".//PassengerStopAssignment">
			<assert test="count(StopPlaceRef) &amp;gt; 0">StopPlaceRef must be present</assert>
		</rule>
		<rule context=".//stopAssignments">
			<assert test="count(DeckEntranceAssignment) = 0">DeckEntranceAssignment must NOT be present</assert>
		</rule>
		<rule context=".//stopAssignments">
			<assert test="count(NavigationPathAssignment) = 0">NavigationPathAssignment must NOT be present</assert>
		</rule>
	</pattern>
</schema>