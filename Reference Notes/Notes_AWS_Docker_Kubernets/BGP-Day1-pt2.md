## TOPIC Name
BGP- Redundant IBGP (IGP ensures reachability)
BGP- Nexthop-self (Split horizon)
BGP- IBGP Full Mesh
BGP- Route Reflector
BGP- Route Reflector (PR-inline) 
## Course Name
CCNP ENARSI 

## Summary 
Redundant iBGP relies on the IGP for next-hop reachability, while `next-hop-self` fixes external next-hop issues caused by the iBGP split-horizon rule. iBGP full mesh is the default requirement, but Route Reflectors — including PR-Inline designs — remove the need for full meshing and improve scalability and convergence within large autonomous systems.

## What did I learn
- when receiving updates from EBGP to IBGP the next hop is not changed unless next-hop-self(attribute) is used when defining a neighbor   
- routes learned from IBGP neighbor can't be advertised to other IBGP neighbors(Split horizon blocks **iBGP-learned routes** from being sent to other iBGP peers.)
- to solve this issue we either use full mesh connection which is not very practical not scalable requires lots of configuration and very very complex
- other approach is Route Reflector which is centralized router that defines its neighbors with `route-reflector-client` so any update is learned by it then it redistribute it to other routers to the ibgp split horizon is not a problem any more 
- since IGP is used it chooses the best path for traffic and sometimes we need to for the path to be through the (route reflector router) the centralized router in this case I will either apply 
	- Route filters (ACL)
	- Monitoring  