<?xml version="1.0" encoding="UTF-8"?>
<schema xmlns="http://purl.oclc.org/dsdl/schematron">
	<title>Generated schematron from template</title>
	<pattern id="p1">
		<rule context=".//ServiceFrame">
			<assert test="count(stopAssignments) &amp;gt; 0">stopAssignments must be present</assert>
		</rule>
		<rule context=".//PassengerStopAssignment">
			<assert test="count(ScheduledStopPointRef) &amp;gt; 0">ScheduledStopPointRef must be present</assert>
		</rule>
		<rule context=".//PassengerStopAssignment">
			<assert test="count(StopPlaceRef) &amp;gt; 0">StopPlaceRef must be present</assert>
		</rule>
	</pattern>
</schema>