# ServiceFrame

The service related elements of the Network Description model can be grouped into a SER-VICE FRAME which holds a coherent set of elements for data exchange.

The Service Frame model comprises among others:
-	Route model: fixed LINEs and ROUTEs of a transport network.
-	Flexible Network model: flexible LINEs and ROUTEs of a demand responsive transport network.
-	Line Network model: overall topology of the LINEs and LINE SECTIONs that make up a transport network.
-	Service Pattern model: SCHEDULED STOP POINTs and SERVICE LINKs, i.e., points and links referenced by schedules.

Other important classes of the SERVICE FRAME include:
-	PASSENGER STOP ASSIGNMENTs and TRAIN STOP ASSIGNMENTs which model the relationship between stops in the timetable and the physical platforms of an actual station or other stop.
-	CONNECTIONs as the topological model of INTERCHANGES. They model the possi-bility of a transfer between two SCHEDULED STOP POINTs.
-	NOTICEs which are then assigned to JOURNEYs and CALLs of the TIMETABLE FRAME through NOTICE ASSIGNMENTs. They model the association of footnotes and passenger information content such as stop announcements and the network.

See the following class diagram for the most important objects of the RESOURCE FRAME and their relationships to the other frames.
<img width="604" height="434" alt="ServiceModel" src="media/ServiceModel.png" />


