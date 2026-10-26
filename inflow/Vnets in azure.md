First, let's quickly adjust the math on the host bits. An IPv4 address is exactly 32 bits long. If your mask is `/26`, that means 26 bits are locked in for the network, leaving **6 bits** (not 8) for the host addresses ($32 - 26 = 6$). A `/24` mask would leave 8 bits.

  

With 6 bits, a `/26` subnet gives you 64 total IP addresses ($2^6 = 64$).

  

If you want to use VLSM to divide that `10.12.0.0/26` block further into `/28` subnets, you are borrowing 2 more bits for the network ($28 - 26 = 2$). This divides your original block into four smaller subnets of 16 IPs each ($2^4 = 16$):

  

- **Subnet 1:** 10.12.0.0/28 (IPs 0 to 15)
    
      
    
- **Subnet 2:** 10.12.0.16/28 (IPs 16 to 31)
    
      
    
- **Subnet 3:** 10.12.0.32/28 (IPs 32 to 47)
    
      
    
- **Subnet 4:** 10.12.0.48/28 (IPs 48 to 63)
    
      
    

### How Networking Understands This: Longest Prefix Match

In traditional networking, routers understand these divisions using a rule called **Longest Prefix Match (LPM)**.

  

When a router receives a packet destined for an IP address, it looks at its routing table. If a packet is trying to reach `10.12.0.20`, it might technically fall under a broad `/16` route, a narrower `/26` route, and a highly specific `/28` route. The router will always choose the most specific path—the one with the "longest prefix" (the highest slash number). It will route the packet directly to the `10.12.0.16/28` network.

  

### How Azure Applies This

Azure applies the same Longest Prefix Match logic under the hood, but it enforces a specific flat structure for how you build it:

  

1. **No Subnet Nesting:** In Azure, you cannot create a `/26` subnet and then create `/28` subnets _inside_ of it. Azure requires a flat hierarchy.
    
      
    
2. **VNet is the Master Block:** You assign the broad address space to the Virtual Network (e.g., `10.12.0.0/16`).
    
      
    
3. **Subnets are Chiseled Directly from the VNet:** You carve your subnets directly out of that VNet address space. You can create one subnet as a `/24`, the next as a `/26`, and the next as a `/28`, as long as none of their specific IP ranges overlap with each other.
    
      
    
4. **Automatic Routing:** Azure automatically creates system routes behind the scenes so that all subnets within a VNet can talk to each other directly by default, using that Longest Prefix Match logic to ensure packets go to the exact right subnet.