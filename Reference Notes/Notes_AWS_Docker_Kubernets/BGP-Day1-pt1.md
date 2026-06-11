## TOPIC Name
BGP- Basics 
BGP- The difference between EBGP IBGP
BGP- Redistribution (Injecting routes)
BGP- Origin Code 
BGP- LB & Redundancy between AS
BGP- Changing Default peering parameter (TTL, Connected check)
BGP- Authentication 
## Course Name
CCNP ENARSI 

## Summary 
Border Gateway Protocol (BGP) is the protocol that connects different autonomous systems (AS) on the internet. It is path-vector based, relies on TCP (port 179), and makes routing decisions using attributes such as AS-PATH, NEXT-HOP Origin Code. BGP is designed for scalability, stability.

## What did I learn
 - BGP operates on port 179 TCP connection 
 - In BGP Neighbors(peers) are defined manually
 - BGP has 4 messages 
	 - Open (Initiate BGP session)
	 - keep alive (Maintain BGP session)
	 - Update (new routes added or deleting existing routes)
	 - Notification ( its an error message )
 - BGP states
	 - Idle (process started or error in link )
	 - connect (TCP establishment, send open message if TCP is successful)
	 - Open sent (waiting for ACK after sending open message in connect)
	 - open confirm (ACK received and BGP confirms the session )
	 - establishment (router start exchanging routes) 
	 - Active (if connect phase was not successful it returns to idle to re-initiate TCP and that state only appears in event debugger)
 - BGP  has two flavors EBGP (AD:20)and IBGP (AD:200)
 - EBGP has TTL = 1 so it requires its neighbors to be directly connected ( on same subnet) used in connection AS with each other
 - BGP Counts best path with respect to least number of AS hops 
 - Origin code (i) and (?)
	 - (i) means its a network added to the route table of the router 
	 - (?) means its an injected network (redistribution)
	 - (i) has the highest priority 
	 - origin code can be changed for any network..
 - Its best practice for BGP network to be defined with its mask, if mask not defined BGP will assume default network class which may lead to ignoring some network entries...
 - IBGP is used because it can handle large number of routes & maintain the BGP attributes as      AS path attribute 
 - IBGP is used along side an IGP protocol inside an Autonomous group 
 - LB and Redundancy between two AS (EBGP) on two links 
	 - Issue
		 - In this case 2 sessions will be established one on each link 
		 - 2 updates will be shared on each link 
	 - Solution (Assuming there is reachability between the routers)
		 - Using loopback interface as source instead of the physical interface
		 - changing TTL (ebgp-multihop) which also disables connected check

 - We can also disable the neighbor check only without changing TTL if the two interfaces are not on the same subnet but assuming there is reachability between them like defining a static route 
 
 

