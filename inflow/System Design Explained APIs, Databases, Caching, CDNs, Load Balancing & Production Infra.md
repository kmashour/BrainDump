---
title: "System Design Explained: APIs, Databases, Caching, CDNs, Load Balancing & Production Infra"
source: "https://www.youtube.com/watch?v=oYxTTirKY8M"
author:
  - "[[Hayk Simonyan]]"
published: 2026-05-26
created: 2026-06-07
description: "Become a senior software engineer with a job guarantee: https://go.hayksimonyan.com/168-sd-courseMaster the exact system design and architectural skills required to break out of the mid-level and ac"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=oYxTTirKY8M)

Become a senior software engineer with a job guarantee: https://go.hayksimonyan.com/168-sd-course  
  
Master the exact system design and architectural skills required to break out of the mid-level and accelerate your career to a high-paying senior engineer role.  
  
Timestamps:  
0:00:00 Introduction  
0:02:13 Single Server Setup  
0:06:20 Databases: SQL, NoSQL, Graph  
0:12:40 Vertical vs Horizontal Scaling  
0:16:50 Load Balancing  
0:23:18 Health Checks  
0:26:10 Single Point of Failure (SPOF)  
0:29:50 API Design  
0:46:06 API Protocols  
0:57:59 Transport Layer: TCP, UDP  
1:03:11 RESTful APIs  
1:17:53 GraphQL  
1:23:41 Authentication  
1:44:40 Authorization  
1:55:51 Security  
2:03:30 What's next

## Transcript

### Introduction

**0:00** · AI is quickly changing software engineering. Almost every engineer nowadays uses AI to write the code implementation, and we're moving towards agentic development. And companies also know this, which is why they are now prioritizing different skills in interviews, not only whether you can write the code implementation, but whether you understand the system and trade-offs at the high level, which is why the best skill you can learn nowadays is system design, how all these components talk to each other high level, how to design them from scratch.

**0:32** · So, in almost every tech interview, now there is a system design round where they are testing your understanding on how systems actually work at the high level, and whether you can make architectural decisions at scale and articulate the trade-offs in systems you have built or worked on.

**0:49** · And this is not only for interviews, even if you're not the one making all these decisions in your current role that you're working at, you still need to understand how the overall system functions, explain how components fit together in the system, and explain the trade-offs that were made while building the project. And that's exactly what we're going to cover in this full course. We're going to cover the skills that are proven at the senior level and beyond.

**1:16** · These are the exact skills and concepts that got me into senior and to lead engineer position, and also helped many engineers pass interviews at senior and staff level and land new roles. So, we're going to cover this in five steps.

**1:33** · First, we'll start with the foundations, which are the core concepts every engineer should know. Then we'll get into API design, how to come up with contracts, versioning, and communication patterns, and design APIs from scratch.

**1:46** · Then we'll get into databases, storage patterns, consistency, and when to use which type of database. Then we'll get into scaling, performance, caching, reliability, and handling points of failure in the system. And lastly, we'll cover interviews on how to pass these system design interviews that are coming up at almost every position that you apply nowadays, and how to prepare for those. Let's get started. Designing a system to support millions of users is challenging, but every complex system starts with something simple.

### Single Server Setup

**2:17** · That's why in this lesson, we'll build a basic setup that supports just one single user, and then we'll gradually expand it as we go. Because starting small allows us to understand each core component before adding more complexity. So, let's start with the first step and build a single server setup. Imagine that we're setting up a system for a small user base. This means that everything runs on one single server. The web application, the database, the cache, and also the other components.

**2:46** · And this setup allows us to visualize the core workings without added complexity. Now, let's break down how this single server setup handles the user requests. We have some users who are trying to access our website or our API on the server. They can be either using the web browser or a mobile app to access our server. And on the other hand, we have our server, which has the necessary files to serve to the web browsers and also the necessary API endpoints to serve to the mobile app. And it is hosted on this example IP address.

**3:18** · Initially, our users don't have this IP address. They have the domain which they're trying to access. Let's say it's app.demo.com.

**3:27** · So, if they just type this domain name and hit enter, their web browser, for example, will contact a DNS, which stands for domain name system. This is a provider which maps the domains to the IP addresses. And in our case, let's say our domain name is mapped to the IP address, which is the server's IP address that we have. So, now this DNS provider will send the IP address back to the web browser or to the mobile app to our clients. And this IP address is our server's IP address. So, now they have the location where they are trying to send requests.

**3:59** · So, with this IP address in hand, the user's device sends an HTTP request to our server asking for specific data. And then our server processes this request and sends back the requested data. This might be an HTML page for a browser or a JSON response for the app depending on the request type. In this setup, traffic usually originates from two main sources. The first one is the web applications and the second one is the mobile applications that are trying to access our server.

**4:29** · For our web users, the server handles the business logic, data storage, and also presentation using HTML, CSS, and JavaScript. And for mobile users, communication typically happens over HTTP. These mobile apps request data from the server using API calls, and JSON is often used for responses because it's lightweight and easy for mobile devices to interpret.

**4:54** · Here is an example API request that we can receive for our server. It can be a get request to our domain {slash} product {slash} the ID of that product.

**5:03** · And for this endpoint, we need to retrieve the details of a product. And here is an example response that we might send back to the client. This is a JSON response which contains the product ID. It contains the name of this product, some description, the price of the product, and some other metadata is useful for the client. And then this will be used by the mobile app or by the web browser to display this product on the screen. And as we continue, our goal will be to identify areas where a single server might not be enough for the user demand.

**5:35** · For now, this setup is ideal for small user bases, but it may struggle under heavy traffic. So, next we'll explore ways to scale each part of the system to support more users effectively. Some key takeaways that we can have from this is that we need to start small. We need to begin with a straightforward single server setup to understand the essential components of system architecture. Now, we also understand how these requests flow through your system, which is fundamental for building more scalable systems.

**6:05** · And we also recognize the unique demands for web and mobile applications and how they interact with your server.

**6:13** · And in the next lessons, we'll start looking at strategies for optimizing and scaling this setup. As our user base grows, a single server isn't enough to handle the increased demand. And to accommodate more users, we can separate our web tier, which is handling the web and mobile traffic, and the data tier, which is managing the database. This setup enables us to scale each server based on its specific load. But when it comes to choosing the right database, how do we know which specific database is the best for our specific application?

### Databases: SQL, NoSQL, Graph

**6:44** · When it comes to database selection, there are two main options.

**6:48** · The first option is relational databases or RDBMS, which are structured in tables and rows. Some popular examples are PostgreSQL, MySQL, Oracle database, or SQLite. On the other hand, we have non-relational or NoSQL databases. These are suited for applications that require flexibility and fast access to large volumes of unstructured data. Some examples are Cassandra, MongoDB, Redis, or Neo4j. Let's start by exploring the relational databases.

**7:17** · These databases use structured query language or SQL for finding and manipulating data. The data here is structured in tables, which are the fundamental building blocks of SQL databases. And these are similar to spreadsheets. Each table consists of columns, which can be thought as the fields or attributes of the table. And it also consists of rows, which are single records within this table. For example, if you imagine a customer's table, within this table we can have columns like ID, name, age, and email.

**7:50** · And for each rows, we can have specific customers like the ID of 123, and the name will be John, and the age will be 40, and so on. But what are the advantages of using an SQL database?

**8:02** · First of all, they support complex join operations across multiple tables. For example, if you imagine we have a customer's table and also a product table. And now we want to create a separate table that will connect the customers and the products that they have ordered. With SQL, you can join these two tables together into an orders table, and this will hold the information about the customer IDs who have this order, and also the product IDs which this customer has ordered.

**8:29** · And this process of combining two or more tables into one table are called join operations in SQL. And the other big advantage is they provide robust data consistency and integrity, especially for transactions. Transactions in SQL are a sequence of one or more SQL operations that are performed as a single atomic unit, and each transaction in SQL follows the ACID acronym. You can think of a transaction example like a bank transfer.

**8:58** · So first of all, all of the transactions are atomic, which means that the entire transaction is treated as a single unit, which either completely succeeds or completely fails.

**9:09** · Each transaction is also consistent, which means that it transforms the database from one valid state to another valid state. And they also come with isolation, which means that modifications made by concurrent transactions are isolated from one another, and they don't interfere with each other. And lastly, they come with durability, which means even if the system fails or the database server fails, the data will still remain there.

**9:34** · And now let's have a look at non-relational databases. Non-relational databases can be in different forms. For example, we have document stores like MongoDB, or you can use wide column stores like Cassandra, key-value stores like Redis, and graph stores like Neo4j.

**9:50** · Let's have a look at each of these types separately, and let's start with the document stores. MongoDB is the most popular example of a document store, and the data here is stored in JSON-like documents, which allows us to have complex data structures within a single record. Next, we have wide column stores, where data is stored in tables, rows, and dynamic columns. Some examples here are Cassandra or Cosmos DB. The main advantage of these databases is they can handle massive scales and are very good for many write operations.

**10:19** · The other option is graph databases, which focus on storing the entities and their relationships as graphs. An example of a graph database is Neo4j. For example, in Amazon, they use the Neptune graph database, which helps them to make you product recommendations based on your previous orders. And the other popular type is key-value stores. Here, data is stored in key-value pairs. The biggest advantage of key-value stores is their simplicity and speed.

**10:47** · Since they are primarily stored in RAM, reading and writing to these databases is extremely fast compared to other databases. Some examples of key-value stores are Memcached or Redis. So, that's the main four types of NoSQL databases. Now, let's have a look at the advantages of these NoSQL databases. If you have a look at the same example that we had for the SQL databases, where we have customers and products, and we want to join them in orders.

**11:15** · For example, in MongoDB, you could have this as a single document, so you could store all of the user data, also the orders and products in a single document. And because of this structure, the NoSQL databases can handle highly dynamic and large data sets without the structure imposed by relational databases. And also, they are optimized for low latency and scalability. So, when should you use relational versus non-relational databases? Here is a quick comparison of both.

**11:44** · If your application data is well-structured with clear relationships, then you should use SQL databases. For example, if you have an e-commerce application tracking customers and orders, that's a good use case of using an SQL database. Next, need strong consistency and transactional integrity. For example, if you have a financial application or banking system, then you should use the SQL databases. However, if your app demands super low latency for quick responses, then you should go with non-relational databases.

**12:15** · Or if the data is unstructured or semi-structured like JSON objects and the relationships aren't that crucial, then you should also go with no SQL databases. And lastly, if your application requires flexible and scalable storage for massive data volumes. For example, a recommendation engine storing user activity data and key value format, then you should also go with no SQL databases. Let's explore the two primary approaches to scaling, which are vertical and horizontal ways of scaling.

### Vertical vs Horizontal Scaling

**12:47** · And we'll also see why horizontal scaling is generally more suitable for high traffic applications. First, we have the vertical scaling or sometimes it's also called scale up. This just means that we are adding more resources to our existing server, meaning RAM, CPU, or any other resources that might help us to handle more traffic. And this approach is simple and works well for applications that have low or moderate traffic. However, it comes with its limitations, which are firstly, resource limits.

**13:18** · There is a hard cap on how much you can add to a single server. And eventually, you will reach a limit on how much you can upgrade your new server. And the second reason is lack of redundancy, meaning if this server goes down, you don't have any other servers to serve your users, which means that your whole application goes down with your single server.

**13:40** · On the other hand, we have horizontal scaling, which is also sometimes called scale out. In case of horizontal scaling, we are just adding more servers to share the load. So, instead of having the single server, we might replicate and have three of that same server. And now we can share that load between these servers instead of handling all of them in a single server. Generally, this is more suitable for large-scale applications, as it comes with higher fault tolerance.

**14:07** · And higher fault tolerance means if one of our servers goes down, we still have two servers available, so these two servers can continue serving our users while the second server recovers from the failure.

**14:20** · And it also comes with better scalability, because you can just add more servers as needed. Instead of having three, you might introduce a fourth one, which will handle the new incoming traffic. But how do we implement the horizontal scaling? In case of a single server, we know that all of our client requests went to the single server, whether it's from mobile app or from the desktop. But what if now we have three servers to handle all the load? How do we distribute the client requests? Let's say our mobile app makes a request. How do we know where this request should go?

**14:52** · Whether it should go to the server one or server two or to server three? And seems like we need to have something in the middle, which will direct the traffic to the appropriate servers. And that part in the middle is called a load balancer. We use load balancers to distribute the traffic across multiple servers. For example, here we have three servers, server one, two, and three.

**15:17** · Whenever we have a new request from the clients, the load balancer decides where we have the least load and then it redirects the traffic to that server.

**15:26** · And it also controls the fault tolerance, meaning if one of our server goes down, like the server free, it will stop sending traffic to the first server since it's not available anymore and it will send all of the traffic to server two and one until the server free is available again. And it also can make our app more scalable because we can introduce a new fourth server and any other servers that we want and this load balancer will ensure that all of the traffic is distributed evenly.

**15:54** · So, that's the two main approaches of scaling, which are vertical and horizontal ways of scaling. In case of vertical scaling, we are just adding more resources to our same server, but in case of horizontal scaling, we are adding more users to our server base and then we use a load balancer which distributes the traffic across multiple servers. But right now this load balancer is kind of a black box for us because we don't understand how does it work, how does it take the requests and how does it distribute the traffic.

**16:25** · So, let's explore that in the next lesson and let's see how this exactly works and what are the strategies that we use in load balancing. Load balancers distribute the incoming traffic across multiple servers while also ensuring that no single server bears too much load, but how does it actually happen and how does the logic work of distributing the incoming traffic? To understand load balancers better, let's explore seven strategies and algorithms that are commonly used in load balancing.

### Load Balancing

**16:58** · Let's start with round robin, which is one of the most popular algorithms.

**17:02** · That's mainly because it's the simplest form of load balancing where each servers in the pool gets a request in sequential rotating order, which basically means that the first request that it receives, it directs it to the first server and the next request will go to the second server, and the third one will go to the fourth server.

**17:23** · And once the last server is reached, in this case it's the server three, it redirects it back to the first server, and then again to the second server, and so on.

**17:33** · This works well for servers with similar specifications, meaning if all of our three servers have the same capability, then round robin will be a good choice here.

**17:44** · Next option is the least connections algorithm. It directs traffic to the server with the fewest active connections. For example, if we have 10 active connections on the server one, we have nine active connections on the server two, and we have 30 active connections on the server three.

**18:02** · If it receives a new request from the client, it will direct it to the server two because it has the least active connections at the moment. So, now it will have one more connection. And this is particularly useful for applications where you have sessions of variable lengths, meaning that one of your sessions might last 10 minutes, the other one might last one minute, and so on. And in this case, the load balancer will take that into account, and it will send the traffic to the least connection server. The third option is least response time.

**18:34** · This algorithm is more focused on responsiveness of the servers.

**18:38** · Let's say your first server is highly responsive, the second one is low responsiveness, and the third one is medium responsiveness.

**18:46** · In that case, the load balancer chooses the lowest response time, and with the fewest active connections. Meaning first it will try to send as many connections to the high responsive server as possible, but it also takes into account the active connections. Let's say this server reaches 40 active connections, then it will switch to the third server because this is the medium responsiveness server, and it will send some traffic, let's 20 other requests to the medium responsiveness server.

**19:13** · And after that, it will switch to the second server, and it might send another 10 requests to this fourth server until it redirects them back to the first server.

**19:25** · This is effective when the goal is to provide the fastest response time to requests, and you also have different servers with different capabilities.

**19:34** · The fourth option is the IP hash algorithm, which determines which server receives the request based on the hash of the client's IP address. This is useful when you want your clients to consistently connect to the same server.

**19:47** · Let's say client one makes a request to your load balancer.

**19:51** · The load balancer will use the client's IP address, and based on this, it will hash it and send it to appropriate server, let's say server two. And all of the future requests of the client one will go to the load balancer, and it will use the same IP hashing algorithm, and based on this IP address, it will again redirect the user one requests to the server two. This is useful if it's important for a client to consistently connect to the same application.

**20:19** · If every of your server has some information about the clients that are connected to it, in that case, the IP hashing is a good choice.

**20:27** · Then, there are also weighted algorithms. These are variants of the above methods that can be also weighted.

**20:33** · For example, you can have a weighted round robin or weighted least connections.

**20:38** · In this case, servers are assigned two weights, typically based on their capacity and performance metrics.

**20:45** · For example, if the first server has 16 gigs of RAM, the second one has 32, and the third one has 64, based on the server RAM and other metrics, they are assigned two weights, and the load balancer takes that into account when redirecting the traffic.

**21:01** · First, it will try to send as many connections to the first server as possible because it's more weighted, meaning it has more performance, and then it will try to send the other traffic to server two, and then the last and small portion will go to server one.

**21:17** · There are also geographical algorithms, which are location-based algorithms that direct requests to the server geographically closest to the user.

**21:26** · Let's say this application is for US users, so mostly users are connecting to this application from US, but we also have some part of the users who are connecting from Europe. And in our pool of servers, we can have one server that is located in US East, another server that is located in US West, and the last server can be located somewhere in Europe for the small base of users who are located in Europe. So, if a user comes from Europe and makes a request to this load balancer, it will redirect this user to the server in Europe.

**21:57** · Or if a user comes from your US and makes a request to this load balancer, it will check the location of this US user based on its IP address, and then it will redirect either to the US East or US West. This type of load balancing is useful for global services where latency reduction is important. And the last most popular type is consistent hashing.

**22:22** · In this case, we use a hash function to distribute data across various nodes.

**22:27** · We have a hash function inside of a load balancer, and we usually imagine a hash space along with this that forms a hash ring, like a circle.

**22:36** · This hash function forms a circle where we have the servers, for example, the server one, two, and three, which are located in front of this load balancer.

**22:46** · So, whenever a new request comes from a user, this hash function takes the IP address of that user, and then based on that, it locates this user on this hash ring. Let's say it locates it somewhere here, and then depending to which server this point is closest to, for example, in this case this is closer to server two, it redirects the traffic to that server.

**23:08** · This is a bit more complicated way of load balancing, but it also ensures that the same client consistently connects to the same server like in case of IP hashing.

### Health Checks

**23:18** · We also talked about that whenever a server goes down, this load balancer ensures that traffic is not redirected to that server.

**23:26** · But how does it know in the first place that this server is not available? For that most load balancers come with health check features, which means that they are consistently monitoring the servers by sending a health check requests to all of these servers, and they have the information about which servers are online. Let's say the first three servers are available, and which ones are offline, which means the fourth server, which is offline.

**23:51** · So whenever it detects a failure in the health check, it knows that this fourth server is not available anymore, and based on that information, if the next request comes from the client, it won't redirect them to the fourth server until the health check again succeeds, and it knows that the fourth server is back online.

**24:11** · And now let's see some load balancer examples, and what are these actually?

**24:15** · How do we implement them? First we have software load balancers. For example, Nginx is probably the most common type of the software load balancer.

**24:25** · It has other features, and it's also used as a web server, but it also offers the functionality of balancer.

**24:32** · Typically you install this Nginx on your server, and then configure the servers that should be load balanced, and also the algorithm. And as you can see it also comes with health checks, which I mentioned. So you can set up health checks among your servers, and then this will consistently monitor your servers, and whenever one of your server goes down, it won't redirect traffic to that server.

**24:55** · Another example of a software load balancer is HAProxy, which is an open source software that again you can install on your server and configure as you want. But apart from software load balancers, we also have hardware load balancers. For example, we have the F5 load balancer, which is a widely used hardware load balancer known for its high performance and feature set.

**25:18** · Next, we have Citrix, which also comes with load balancing functionality. And again, this is a hardware type of load balancer.

**25:26** · But if you don't want to configure all of that yourself on your server or as a hardware, then the easier solutions are cloud-based load balancers. For example, AWS comes with elastic load balancing.

**25:38** · And if you have your servers also set up in AWS, then it's pretty easy to configure this with your servers. And you can also see it in the benefits that it automatically comes with security, automatic scaling, meaning that it will automatically add new servers to the pool if the demand increases of your application. And it also comes with monitoring, which is the same as health checks. So you don't have to set it up yourself. And other examples similar to AWS are Azure's load balancer and Google Cloud's load balancing.

**26:07** · Now, let's talk about the concept which is called a single point of failure in system design. This is one part of your whole system that whenever it fails, it will bring the entire system down with it. So to put it simply, it is any component that could cause the whole system to fail whenever it stops working.

### Single Point of Failure (SPOF)

**26:27** · For example, if you imagine this setup when the clients connect to our load balancer and then load balancer distributes them to the APIs, and then we have a single database which is used for all API servers. Database here is one example of a single point of failure.

**26:46** · Whenever this database goes down, all of these APIs won't be able to connect to the database and because of that all of these also won't function properly and our clients won't be able to receive any response from the servers. So, having single points of failures in your system is problematic because they can create vulnerabilities.

**27:09** · The first obvious downside is the reliability because a single failure like the failure of this database can take the entire system down which could mean business losses because users are not able to access our platform. Maybe they are also not able to access the checkout page or any other parts of the system which can bring losses in the business.

**27:31** · It is also an issue for scalability because systems that have single point of failures like this can often struggle to scale as each component will add a risk of failing this single part.

**27:43** · And the last part it also brings a security issue because if you have a single point of failure in your system like the load balancer, attackers can compromise this point by sending huge traffic to it and if this fails, the whole system will go down.

**27:58** · We will talk about how to avoid the database single points of failure in the databases section, but in this section we can have a look at how to avoid the load balancers to become a single point of failure because right now we have only one load balancer setup. And if this load balancer goes down, then all of our users won't be able to access this point and they will also not be able to access to our APIs.

**28:24** · The first strategy is adding redundancy to our system. This means that we can use more than one load balancer and for example, if the second load balancer goes down, users won't be able to connect to this load balancer, but in that case we can redirect all of the traffic to the first one and then this first load balancer will balance the load between those servers and we will

**28:47** · monitor the health of the second load balancer and whenever it's back online and it's again available, we will also redirect 50% of the traffic to the second load balancer.

**28:59** · Another strategy is to use health checks and monitoring for load balancers themselves. As we saw load balancer can do health checks for the servers and check whenever our servers are online or offline. We can do the same strategy for load balancers and we can check their health continuously and whenever one of our load balancer goes down, we will know that we shouldn't redirect any traffic to this load balancer until it is back online.

**29:24** · And the third common type is self-healing systems, which means that we again monitor the health of our load balancer and if at any point we detect that it goes down, we will replace this with a new load balancer, which is basically an instance of the same load balancer and this way we won't cause any interruptions and our clients will be able to connect to this new load balancer.

**29:49** · Welcome to this section where you will learn the fundamental principles of API design, which will enable you to create efficient, scalable and also maintainable interfaces between software systems. Here is what we're going to cover in this lesson. We'll start from what APIs are and what is their role in system architecture. Then we'll cover the three most commonly used API styles, which are REST, GraphQL and gRPC.

### API Design

**30:16** · We'll discuss the four essential design principles that make great APIs and also how application protocols influence the API design decisions.

**30:27** · We'll also cover the API design process, so starting from the design phase to development phase to deployment, so we'll see how that process looks like.

**30:37** · So let's start by understanding what is an API. API stands for application programming interface, which defines how software components should interact with each other.

**30:47** · Let's say on one side you have the client, which is either the mobile phone or the browser of this user, and on the other side you have the server, which will be responding to the requests.

**30:57** · So, API here is just a contract that defines these terms, which are what requests can be made. So, it provides us with an interface on how to make these requests, meaning what endpoints do we have, what methods can we use, and so on. Also, what responses can we expect from the server for a specific endpoint.

**31:18** · So, first of all, it is an abstraction mechanism because it hides the implementation details while exposing the functionality. For example, we can make a request to save a user data in this server, but we don't care at all about how the logic applies behind the scenes inside of this server. So, we only care about the interface that is provided through this API, and we only use that endpoint, and we store the user without even knowing about the implementation details.

**31:45** · And it also sets the service boundaries because it defines clear interfaces between systems and components. So, this allows us to have multiple servers. We can have one server that is responsible for managing the users. We can have another one that is responsible for some other records, let's say for managing the posts, and so on.

**32:08** · So, this allows different systems to communicate regardless of their underlying implementation, like client browsers with servers or servers with another servers, and so on.

**32:19** · Now, let's focus on the most important API styles you will encounter during the design phase. These are RESTful, GraphQL, and gRPC. The most common one out of these is REST, which stands for representational state transfer. These type of APIs use resource-based approach by using the HTTP methods as a protocol.

**32:41** · One of the advantages of REST APIs is that they are stateless, meaning that each request contains all of the information needed to process it, and we don't need any prior requests to be able to process the current request. And it uses the standard methods on HTTP protocol, which are get for fetching data, post for storing data, put or patch for updating data, and delete for deleting data.

**33:07** · So, based on its characteristics, the REST is most commonly used in web and mobile applications. Next, we have GraphQL, which is the second most common API style after the REST APIs. GraphQL is a query language that allows clients to request exactly what they need. This means that it comes with a single endpoint for all of the operations, and we can choose what we are expecting to receive from this API by providing the payload in the request.

**33:36** · And the operations here are called query whenever we are retrieving data, or mutation whenever we are updating data.

**33:44** · So, this is the equivalent in put or patch or post in the RESTful APIs. And there is also a subscription in operations, which is for real-time communication. The advantage of GraphQL APIs is that it allows us to have minimal round trips. Let's say we need some data that in RESTful APIs we will need to make three requests to get all of this data.

**34:07** · In GraphQL case, we can make a single request and get all of this data, avoiding the unnecessary two requests that we will otherwise have to make in RESTful.

**34:17** · And because of that, this is the recommended option for complex UIs. So, wherever you have some complex UIs where on one page you might need different data, on another page you might need some other complex nested data. In these cases, GraphQL is the better choice over RESTful APIs.

**34:34** · And the last option is gRPC. I would say this is the least common one out of these three.

**34:40** · gRPC is a high-performance RPC framework, which is using protocol buffers for communication.

**34:47** · The methods in gRPC are defined as RPCs in the proto files, and it supports streaming and bidirectional communication. This is an excellent approach for microservices especially and internal system communication, as it is more efficient when you're working between servers compared to GraphQL or compared to RESTful APIs.

**35:10** · So, the difference between REST, GraphQL, and gRPC APIs is kind of clear, but let's also clarify the real difference between REST and GraphQL APIs on examples.

**35:21** · So, as you saw, REST comes with resource-based endpoints. For example, here, if we take a look at these requests, you can see that the resource here is users. So, you always expect to see some users endpoint or some followers endpoint or, let's say, posts endpoint. So, it is resource-based.

**35:39** · And sometimes we might need to make multiple requests for getting the related data. As you can see here, we need, let's say, the user details, but we also need the user posts and followers. So, in this case, we need to make three requests to get all of these data.

**35:54** · And it uses HTTP methods to define operations. As you can see, these are HTTP endpoints, and we are using the get method specifically. And the response structures are fixed, meaning if you got one response for this specific user, next time you can expect to have exactly the same response structure. Maybe some data will be modified, but the structure always remains the same. And it also provides explicit versioning. So, as you can see, it comes with V1 for the V1 API.

**36:23** · Then later, if it got a major upgrade, then this will become V2, and so on. And you can use the headers on the requests to leverage the HTTP caching on RESTful APIs. Now, if we compare that to GraphQL APIs, it comes with a single endpoint for all operations. So, mostly it is {slash} GraphQL or {slash} some API endpoint that is commonly used for all operations. And in this case, we will use a single request to get the precise data that we need, and we will use the query language of GraphQL.

**36:57** · This is what the query language looks like. As you can see, we start with a query, and then we define what we need.

**37:03** · For example, we need the user with ID 123. Then we need the name of the user, the posts, and then we define whatever we need from the posts. Maybe we need only title and content, and nothing more. And also the followers, and what we need from followers, maybe only names. So, this allows us to be more efficient in our requests compared to RESTful APIs, where we will need to make three requests for this same data.

**37:30** · This means that client needs to specify the response structure. And in this case, the schema evolution is without versioning. So, here as you saw, it is with V1, V2, and so on. In this case, the schema usually evolves without versioning, but there is also a common pattern to start versioning the fields.

**37:49** · For example, you can have followers V2, and that will be the second type of followers schema. But you can also go without versioning, so you can just start modifying the followers or posts if you are sure that there are no other clients using your old API.

**38:07** · And in this case, you can leverage the application-level caching instead of the HTTP caching.

**38:13** · Now, let's discuss the major design principles that will allow us to create consistent, simple, secure, and also performant APIs.

**38:22** · Ultimately, the best API is the one that we can use without even reading the documentation. For example, if you saw the previous endpoints in the users, you see that we have {slash} users {slash} 123, and obviously we are expecting to get the user details of this specific user.

**38:40** · And if you make a request, for example, to that endpoint to fetch user details, but then you find out that it also update some followers or something while making this request, then obviously that is a very bad type of API as we didn't expect it to do such operations.

**38:57** · So, first of all, the good API should be consistent, meaning it should use the consistent naming, casing, and patterns.

**39:05** · For example, if you use camel case in one of the endpoints, let's say you have user details, and you do this in camel case, but in another case you do it with a snake case like user {slash} details, then this is not common and this is not consistent.

**39:22** · The second key principle is to keep it very simple and focus on core use cases and intuitive design.

**39:29** · So, you should minimize complexity and aim for designs that developers can understand quickly without even maybe reading the documentation. And simplicity again comes down to this, which is the best API is one that developers can use without even reading the documentation.

**39:47** · Next, obviously it has to be secure, so you have to have some sort of authentication and authorization between users. Also, if you have inputs, then you need to make sure that these are validated, and you should also apply rate limiting. So, these are the most basic things that you have to do to keep your APIs secure.

**40:06** · And the last pillar is performance, so you should design for efficiency with appropriate caching strategies, with pagination. If you have a large amount of data, let's say thousands of posts, you don't want to retrieve all of these whenever they make a request to get the posts. So, you should always have pagination with some limit and offset.

**40:27** · Also, the payloads, meaning the data that you will send back, should be minimized. And also, whenever possible, you should reduce the round trips. So, if you have the opportunity to send some small data along with the request of one of the endpoints, then it's better to do this if you know that you're going to use it instead of making another endpoint for making a request to get the same data.

**40:51** · Now, each of these APIs use different protocols, and we will learn more about these in the next lesson. But, basically, your protocol choice will fundamentally shape your API design options. For example, the features of HTTP protocol directly enable RESTful capabilities. So, it makes more sense to use HTTP along with RESTful APIs because it also provides you with status codes, and these are great to be used with CRUD operations that you will have in RESTful APIs.

**41:22** · On the other hand, WebSockets, which is another type of protocol, enable real-time data and also enable bidirectional APIs. So, these can be used along with real-time APIs wherever you need some chat application or some video streaming. This is a good use case of WebSocket APIs.

**41:41** · In case of GraphQL APIs, you again will use the HTTP protocol instead of WebSockets or gRPC.

**41:48** · gRPC, on the other hand, can be used among with microservices in your architecture to make it faster compared to HTTP.

**41:57** · So, your protocol choice will affect the API structure and also the performance and capabilities.

**42:04** · Therefore, you should choose it based on its limitations and strengths, and the one that makes more sense in the type of API that you'll be developing.

**42:14** · Now, let's discuss the API design process. It all starts with understanding the requirements, which is identifying core use cases and user stories that you will need to develop.

**42:25** · Also, defining the scope and boundaries because if it's a huge API, then you probably won't develop all of the features at once. So, you should scope it to some specific features that you'll be developing and also what are out of scope for now. Then you should determine the performance requirements and specifically in your API case, what will be the bottlenecks and where you need to make sure that it's performant.

**42:51** · And you should also not overlook the security constraints. So, you should implement all of the basic features like authentication, authorization, the rate limiting, but maybe some more stuff depending on the API that you'll develop. When it comes to design approaches, there are couple of ways to go about it. The first one is top-down approach, which is you start with high-level requirements and workflows.

**43:15** · This is more common in interviews where they give you the requirements on what the API will be about, and then you start defining what the endpoints will be, what the operations will be, and so on. But there is also the bottom-up approach, which is if you have existing data models and capabilities, then you should design the API based on this. So, this is more common when you're working in a company and they already have their data models and capabilities of their APIs. So, you should take that into account when designing the API.

**43:49** · And we also have contract first approach, which is you define the API contract before implementation, meaning what the requests should look like and what the responses should look like. And this is more similar to top-down approach and this is also commonly used in interviews.

**44:06** · When it comes to life cycle management of APIs, it starts with the design phase where you design the API, discuss the requirements, and the expected outcomes of the API. And only after that you can start the development and maybe local testing of your API.

**44:24** · After that, you usually deploy and monitor it, so you do some more testing, but now on staging or on production.

**44:31** · But then it also comes the maintenance phase, and this is why it's important to develop it with keeping the simplicity in place, so it will be easier for you to maintain or for other developers to maintain in the future.

**44:45** · And lastly, APIs also go through deprecation and retirement phase. So, some APIs eventually get deprecated because there might come up with a new version of the API that you should use, or let's say you are transitioning from V1 to V2 API. So, that's also the deprecation phase of the V1 API.

**45:05** · So, developing APIs is not only in the development phase, as you might assume.

**45:10** · It's not just coding. So, the big part of it is designing it, and also keeping it maintainable, and also eventually you might need to retire it at the end.

**45:21** · So, let's recap and see what our next steps are. We learned what APIs are and about the most dominant three type of API styles, which are RESTful, GraphQL, and gRPC.

**45:33** · We've covered the four key principles that will guide us when creating API designs effectively. And you now also understand how the design choice of your protocol will influence the design of your API, and also the whole API design process from start to finish.

**45:51** · But we didn't discuss the limitations and strengths of these API protocols.

**45:56** · So, that's why in the next lesson, we will learn all about the API protocols that we can use with API design and which one we should choose based on the requirements of our API. Choosing the wrong protocol for our API can lead to performance bottlenecks and also limitations in functionality. That's why we need to first understand these protocols which will allow us to build APIs that meet our specific user requirements for latency, throughput, and also interaction patterns.

### API Protocols

**46:23** · That's why in this lesson we'll cover the role of API protocols in the network stack, the two fundamental protocols which are HTTP and HTTPS, and also their relationship to APIs.

**46:38** · Also, another common type of protocol which is WebSocket for real-time communication. We'll also cover advanced message queuing protocol which is commonly used for asynchronous communication. And lastly, we'll cover the gRPC which is Google's remote procedure call and it is also another common type of protocol used commonly within servers. Let's start by understanding the application protocols in network stack.

**47:03** · Application layer protocols sit at the top of network stack building on top of protocols like TCP and UDP which are at the transport layer. These protocols at application layer define the message formats and structures, also the request response patterns, and management of the connections and error handling.

**47:26** · Now, below that we have many other layers like the network layer or data link layer or even physical layers, but when building APIs, we are mostly concerned with the API layer protocols which are HTTP, HTTPS, WebSockets, and so on. The most common type of protocol and also the foundation of web APIs is HTTP which stands for Hypertext Transfer Protocol. This is the typical interaction between client and server when they are interacting over HTTP.

**47:54** · As you can see, client always sends a request and they define the method which can be get, post, or other methods and they define the resource URL which can be at {slash} API {slash} products.

**48:08** · Let's say they are requesting data for this specific ID of the product and they also define the version of the HTTP protocol that they are using. They also define the host which is the domain of your server where the information is accessed and usually they also authenticate before accessing any resources. So, it can be either a bearer token or a basic authentication, OAuth, and so on. So, once the request is authenticated in the server, it receives the response which is in similar format and it's in HTTP response.

**48:39** · So, you get the HTTP version which is again the same as you requested with and the status code which can be 200 if it was successful or it can be 400 if the client was error or 500 if the error happened in server and so on. You receive the content type which can be usually application JSON, but it can also be a static web page or something else.

**49:04** · And there are many other headers that you can control like controlling cache, you can use the cache control header or some other properties, but these are the main things that you would notice in HTTP request response cycles.

**49:18** · Now, when it comes to methods, you have get for retrieving data, post for creating data in the server, put or patch for updating data partially or fully, and delete for removing data from the server. And when it comes to status codes which are received by the server, so you have 200 series which are successful cases.

**49:37** · You have 300 for redirection. 400 means that client made an error in the request, so this is an issue from client side or 500 which means that server made an error or like some error happened in the server which means that this is the issue in this server. And And these are the common headers like content type, which is defined by the server usually, but also from the client, authorization for making a request and authorizing to the server, accept headers, cache control, user agent, and there are more headers, but these are the common ones.

**50:09** · Then we also have HTTPS, which is basically the same HTTP protocol, but with some sort of TLS or SSL encryption, which means that our data is now protected in transit when we are making requests. So it adds a security layer through these TLS or SSL certificates and encryption, so and it protects data in the transit.

**50:33** · And benefits of HTTPS is obviously your data is encrypted in the transit, it comes with data integrity, and you also authenticate users before providing any data, and it also adds SEO benefits, and you have many risks when you are using HTTP only without any encryption. So the golden standard is to always use HTTPS in servers.

**50:55** · The next type of protocols are web sockets. While we have HTTP, which is very good at request-response patterns, sometimes HTTP has limitations. For example, let's say you're polling some data. Let's say this is a user chat, so you have the client and server. On the client side, you have the user chat, and on the server, you have the messages between two users.

**51:16** · When one of the users messages the other, it sends a request to the server to notify that a message has been sent, and it receives a response from the server, maybe the messages from the other users, if there are any. And then next time, if you need to know if you have new messages, you need to make again another request to the server, and maybe you don't have any new messages, so you will receive an empty response with no new data.

**51:41** · So this was basically a unnecessary request-response cycle, and you might request from some other time, let's say from 1 minute and receive a response. Now you have some messages, but it can be also empty again. So, this way is not ideal for real-time communication. As you can see, you get increased latency, you waste some bandwidth with making requests that are empty, and you also use the server resources without the need of making requests to the server.

**52:09** · And for such cases, we have WebSockets, which solve this issue. So, in WebSocket, you have usually a handshake that is happening within the first request and now you have both like two-side communication between client and the server, which means that once the handshake has been made, the server can independently decide to push data to the client. Let's say now you have two new messages on the server. So, server can decide to send these messages to the client without even client requesting for it.

**52:39** · But, client can still request data. So, if client needs some external data or more data from the server, it can still make requests, but server is now also able to independently push data to the client.

**52:55** · So, this is what unlocks the real-time data with minimal latency. As soon as you have some new data in the server, it pushes the new data to the client and it also reduces the bandwidth usage by allowing bidirectional communication. In client-server model with HTTP, you would make, let's say, new requests per 5 seconds or 10 seconds to see if there are any new data in the server. But, in this scenario, you don't make any more requests other than the first one. And now, whenever there are new data, server will push it.

**53:26** · And whenever there are no data to be requested, then you don't need to make unnecessary requests to the server.

**53:34** · The next very common type of protocol is Advanced Message Queuing Protocol, which is an enterprise messaging protocol used for message queuing and guaranteeing delivery. In this setup, you usually have the producer, which can be either a web service or payment system or something like that. And on the other side, you have the consumer, which can be the processor of the payments or notification systems and stuff like that.

**54:01** · So, a producer publishes messages to the message broker, and here is where you have the advanced message queuing protocol. You have queues in the middle.

**54:11** · Let's say one of these queues is for order processing. So, whenever a new order has been placed, producer publishes a message to this queue. And then whenever this consumer is free, it can pull messages from this queue and start updating the inventory and data in the database. This allows the consumer to only pull data from here whenever it has capacity.

**54:32** · And whenever this consumer is busy with some other tasks, it leaves the message in the queue and then later on, whenever it has some free capacity, it will pull the message and start updating the data. And when it comes to exchange types, you have direct one-on-one exchange or fan out or topic-based communication. And we will explore these more when we come to the message queuing section.

**54:58** · The other common type of protocol is gRPC, which works with protocol buffers.

**55:04** · This is a high-performance RPC framework invented by Google, and it uses HTTP 2 for transport, meaning the second version of the HTTP. This means that clients should support HTTP 2, otherwise this can't be used between client and server. But that's why this is most commonly used between servers. So, usually the client is another server, and we have some other microservices communicating with each other with this gRPC framework.

**55:30** · It mainly uses protocol buffers, and it also comes with built-in streaming capacities because it uses HTTP 2. So, these are the most common types of API protocols. There are many more, but usually in 90% of cases you would see only these protocols. And when choosing the right one, you should mainly consider the interaction patterns.

**55:53** · Usually by default you go with HTTP if it's just a request-response cycle, but if you're building something like real-time chat or some real-time communication, then you would need to go with WebSockets. The choice also depends from the performance requirements. So, if you have multiple servers, microservices communicating with each other, and there is an opportunity to use gRPC, for example, then you can go with it to increase the performance and speed of the communication. But it also comes down to client compatibility.

**56:22** · For example, most browsers don't support the latest version of the HTTP. That's why gRPC isn't that very common for browser-server communication.

**56:34** · It also comes down to the payload size, meaning the volume of the data and encoding, security needs based on the authentication, encryption, and so on, and also the developer experience, so the tooling and documentation. And it also comes down to the developer experience because you're mostly going to work with this API, and it needs to have good documentation and tooling for you to fully work with this type of API protocol.

**57:00** · So, to recap, we have explored the role of application protocols in network the HTTP and HTTPS, which are the most fundamental types of protocols, WebSockets for real-time communication, AMQP, which stands for Advanced Message Queuing Protocol, which allows us to have asynchronous communication and adding message queues between the consumer and producer, and also gRPC, which stands for Google Remote Procedure Call, and the main advantage of this is is it's high-performance RPC framework, which uses HTTP/2 for transport.

**57:35** · So, we discussed the application layer, which includes these protocols that we usually use for building APIs, but we don't know yet about this transport layer, which includes the TCP and UDP.

**57:47** · So, in the next lesson, we are going to discuss this layer and understand which of these transport layers, whether TCP or UDP, are the best choice depending on the API that we are building. Most developers work APIs, but never think about what's actually delivering those packets. Like, how does it happen that the request is being made from client to server, and how does this request go through the internet? That's where the second layer comes in in the OSI model, which is the transport layer that has the TCP and UDP inside of it.

### Transport Layer: TCP, UDP

**58:22** · These are both transport layer protocols, meaning they handle how data moves from one machine to another over the network. But, both are doing it very differently.

**58:33** · In this lesson, we'll learn about these transport layer protocols. We'll start with TCP, which is the reliable but slower version. Then, we'll learn about the UDP, which is In short, it's faster and unreliable version of TCP. And, we'll compare both of them and decide which one we need to choose based on the API requirements.

**58:54** · Let's start with TCP, which stands for Transmission Control Protocol. Think of it like sending a packet with a receipt, tracking, and also signature that is required. So, when you send some packets over the internet, you usually don't send all of it at once. Sometimes, the data is larger. Let's say it's divided in three chunks, so you need to send them separately. The first chunk, the second chunk, and also the third chunk.

**59:20** · So, in this case, TCP guarantees delivery of all of these three chunks.

**59:25** · If one of these packets is lost or arrives out of order, TCP will resend or reorder it.

**59:32** · It's also connection-based, which means that before sending any data, it performs a three-way handshake, which is establishing the connection between client and server.

**59:43** · It also orders these packets. Let's say the client receives the first packet first, then the third packet, then the second packet. It makes sure that it's reordered to first, second, and third.

**59:55** · This, of course, adds overhead, but it ensures that it's accurate and reliable.

**1:00:01** · That's why APIs that involve payments, authentication, or user data always use TCP. On the other hand, we have UDP, which stands for User Datagram Protocol.

**1:00:11** · It's fast and efficient, but the downside of this is that it doesn't guarantee that all of the packets will arrive. For example, if you're sending four packets from the server to the client, one of these packets might be lost, and it won't be pushed to the client, and UDP won't make sure that this eventually gets delivered. So, there is no delivery guarantee. There is also no handshake or connection or any sort of tracking.

**1:00:37** · But because of these tradeoffs, it is faster transmission, and it comes with less overhead as it doesn't need to make sure that all of the packets are delivered or in the correct order. For example, in video calls, UDP can be the best protocol because if some information was cut in the middle, or let's say you're in a call with someone and their internet connection lags, you don't need to receive that old connection or the old data on what they said because you are in the call right now.

**1:01:07** · So, UDP is the go-to for video calls, online games, or live streams because if one of these packets drops, it's still fine, and you don't need to go back and resend this packet. You can just move on and send the next packets.

**1:01:23** · This is what the three-step handshake looks like in TCP. As you can see, the first step is that client sends a request to the server. In the second step, server syncs and acknowledges the request. And in the first step, the client acknowledges the server. And this is where the connection is established between the client and server. And now they can start sending data back and forth on top of this TCP protocol.

**1:01:49** · So, in short, TCP is the safer and reliable version of UDP, but it is slower. And on the other hand, UDP is faster and lightweight, but it is risky.

**1:02:00** · For example, if one of the packets in between the source and destination is lost, it doesn't resend it, so there is no guaranteed delivery. But on the other hand, if in TCP one of the packets is lost, after some timeout, it still resends the third packets. And this way, it guarantees that all data will be delivered compared to UDP, where some data might be lost, but it will still keep going. And when choosing between those two, these are the main things that you need to look for. If you need the connection to be safe and reliable, then you need to go with TCP.

**1:02:32** · Or if you need it to be fast, lightweight, but some data loss might be acceptable, then you will need to go with UDP. For example, it is best for using TCP in bankings, emails, payments, and so on.

**1:02:47** · And on the other hand, UDP is mostly used in video streaming, streaming, gaming, and so on.

**1:02:53** · These are the main things that you need to know about the application and transport layers. And these are the only layers that will need to be used to building APIs. And in the next lesson, we will learn about RESTful APIs and how we usually design APIs in RESTful format. RESTful APIs let different parts of a system talk to each other using the standard HTTP methods. they are the most common way developers build and consume APIs today.

### RESTful APIs

**1:03:21** · And in this video, you'll learn how to design clean REST APIs by following the proven best practices so that you avoid creating messy and inconsistent patterns that make the APIs hard to use and maintain. We'll start by learning about the architectural principles and constraints of RESTful APIs, about the resource modeling and URL design, also the status codes and the error handling as well as filtering, sorting, and so on.

**1:03:52** · And we'll learn the best practices when using and developing RESTful APIs.

**1:03:57** · Let's start from the resource modeling.

**1:03:59** · Resources are the core concepts in REST.

**1:04:02** · Let's say you have the business domain which consists of the products, orders, and reviews. When modeling these to a RESTful API, you usually convert these into nouns and not verbs, meaning that the product becomes products, order becomes orders, and same for the reviews. These can be collections or individual items. For example, this first request, which is to {slash} API {slash} products, will return you the collection of products, not a single product.

**1:04:31** · But on the other hand, you could have {slash} products and {slash} specific ID of a product, which will return you the individual item. And notice that we are using {slash} products when retrieving the collection of products, and we are not using something like get products, which will be not a best practice in RESTful APIs.

**1:04:53** · As I mentioned, we are using nouns here and not verbs. So, to fetch orders, for example, you don't define the URL as get orders. You just define it as {slash} orders, and depending on the method that we'll use, let's say it's a get method, then you will retrieve the orders. If it's a post method, then you will create an order, and so on. So, all the resources should be clearly identifiable through the URLs. For instance, this is an example of getting a collection. This is an example of getting a specific item.

**1:05:24** · And also, nested resources should be clearly defined. For example, if you want to retrieve reviews for some specific product, then we would assume that if you make a request to {slash} products {slash} ID of that product, and then {slash} reviews, you would get the reviews for that specific product. But, in real-world APIs, you rarely want to return all the results at once. That's why we usually incorporate filtering, sorting, and pagination in APIs. So, let's start from the filtering.

**1:05:54** · For example, if you make a request to get all the products, you usually add some query parameter, which in this case you can see it's category. So, you're first of all filtering them by category. And then also, with the end sign, you add that they should be in stock. So, the in stock should be true. And this way, you are only returning the items that you're going to display on the UI.

**1:06:17** · And you're not making some requests that will waste the bandwidth of this API, and also, it will be a huge response for you in the front-end side. Next, we also have sorting. In this case, again, it's controlled through the query parameters.

**1:06:34** · And query parameters are anything that start after the question mark in the URL. So, in this case, you usually pass the sort attribute. And this can be, for example, ascending by price, or ascending by reviews, or it can be also the descending order. So, based on this, you will get the response from the API in a sorted order. Because if you, for example, have 1,000 items in the back-end, in the database, you don't want to retrieve all of these in unsorted order to the front-end.

**1:07:06** · Because, let's say the front end now needs to sort them by the price ascending. This means that it needs to make request to get all of the products, which are these thousand items that you have in the database. So, that will be very inefficient. That's why we do the sorting in the back end instead. So, your back end should support sorting functionality. This way the front end can just make a request to your back end and pass this sort query parameter and then that way it will get the sorted products to be displayed on the screen.

**1:07:39** · And next we also have pagination. Again, with a query parameter, you usually pass the page which you want to retrieve and also the limit because if you don't pass the limit, then again it will give you all of the products starting from the page two till the end, which can be a lot of items. So, you also pass some sort of limit and that limit is whatever you're going to display on the front end. And then based on that, you will get the response and here let's say you fetched 10 items.

**1:08:05** · So, you're going to display those 10 on the UI and then once they click on the next page, you will make another request to the page three this time and you will get the next items from the server.

**1:08:19** · Now, usually we use page for pagination, but there is another common attribute that is offset. So, some APIs use offset instead of the page and they use this in combination with limit, which basically means if you have thousand items. So, offset will tell the API from where to start counting these thousand items and then limit is the same as you have it here. So, it's basically limiting the number of items that you are getting from this offset to retrieve to the front end.

**1:08:49** · And the last option, you can also have this cursor based. So, instead of page and limit, you would pass a cursor, which will be the hash of the page you want to retrieve.

**1:08:59** · So, this approach of adding filtering, sorting, and pagination comes with benefits. So, first of all, it saves the bandwidth of your server. It also improves the performance both in the server side and on the front end side.

**1:09:12** · And it also gives the front end more flexibility because now you can fetch only the things that you need and not some unnecessary data from the database.

**1:09:22** · Now, let's come to the HTTP methods that REST APIs use because they rely on HTTP protocol and hence they are using the HTTP methods, especially for CRUD operations. So, these are the most common types of CRUD operations you would see in REST APIs. First of all, we have the GET method, which is used for reading data from the API. So, this is for retrieving resources, as you saw, like retrieving the products, retrieving the reviews, and so on. And the URL usually looks like this.

**1:09:53** · You make a GET request to the /api/version of the API/the resource name. And these type of requests are both safe and idempotent, which basically means if you make a request to /products two or three times, you expect to receive the exact same output every time unless some new products obviously have been added to the database. Next, we have the POST method. This is usually when you're creating a resource in your server.

**1:10:21** · The common example is again, you will make the request to exact same endpoint as you have it for the GET to create a collection. But in this case, instead of GET, you are using POST method. And this tells the API that you need to create a resource in the products and not retrieve them.

**1:10:42** · These type of requests change the state of the server. They are adding a new item and also they are not idempotent, which means that they are creating a resource. So, the first time you create a resource, you will get the ID of the first item that you created. The second time you created you will get the ID of the second one and so on. Next we have the put and patch methods which are very similar but they are updating resources in your API. But they do it a bit differently.

**1:11:11** · The put method replaces the whole resource whereas the patch method partially updates the resource in your API. Now you can see that the request URL is exactly the same in both of their cases so it's tool {slash} products {slash} ID of a product you want to modify. Just in case of the put request it will take this whole product with the ID of 123 and it will basically replace it with the new one that is coming from the front end.

**1:11:39** · Whereas in case of the patch it will again take this item from the database with ID 123 but it will update it partially. Let's say you just updated the title from the front end and you made the request with patch method.

**1:11:54** · So this will only update the title of this product and it will leave the other parts other properties unchanged.

**1:12:02** · And the last crowd operation is delete and we use delete method in this case and obviously as the name tells it deletes the resource from the database.

**1:12:11** · So again the URL is exactly the same as you have for modifying items. It's tool {slash} products {slash} ID of the resource and in this case you are not passing anything in the request body so you are just making a delete request to this item and you are removing this from the database. And each of these operations return you different status codes depending on how the request went whether it was successful or not. For that we have status codes and error handling in restful APIs.

**1:12:42** · So you should use the appropriate status codes when working with rest APIs. For example the 200 series are for successful requests. For example 200 is okay, 201 is resource has been created, 204 is there is no content here.

**1:12:59** · Let's say you made a request, the previous request we were talking about to {slash} products {slash} some ID of a product, and you successfully retrieved this item. This means that you also need to set the status code to 200 because the request has been successful. In the other case where you're creating a product and you're making a post request to {slash} products, this time you shouldn't respond with the same 200 code because 200 generally means that the status was okay.

**1:13:26** · But in 201 case, it means that the resource has been created. And in this case, since you're creating a new product, you should obviously respond with the 201 status code, meaning resource has been created.

**1:13:40** · You also have 300 series, which are for redirection. Let's say you make a request to a URL, and now this URL has been moved to somewhere else. So, it will respond with a 300 series, and it will redirect you to the new URL. In 400 series, we have the client errors. So, this is whenever your front end made a bad request or the user made a bad request. For example, 400 is a generic bad request.

**1:14:05** · In 401, we have unauthorized requests, meaning the user is not authenticated to make this request. For 404, we have not found. So, generally when you visit some URL or you make a request for some specific resource that doesn't exist, you would get this 404 status code.

**1:14:25** · So, for 400 case, let's say you made a request with invalid parameters or some wrong JSON format. In this case, you would get a generic 400 bad request. But if a user makes a request to to get some product, which is let's say the product with this ID, and it doesn't exist in the database after querying it, then you should respond with the 404 status code, meaning that the resource has not been found.

**1:14:52** · And lastly, we have 500 series. These are things when error happens in your server, so you don't know the exact reason, and it's also not a client error, meaning client requested everything properly. And in this case, we throw unexpected server-side errors.

**1:15:08** · You generally respond with a server error message, and you return the 500 status code along with it.

**1:15:15** · When it comes to best practices of RESTful APIs, first of all, notice that we are using plural nouns for all of the resources. So, instead of {slash} product, we are using {slash} products for retrieving the products collection.

**1:15:30** · So, you should always use the plural in this case. Also, in the CRUD operations, we use the proper HTTP methods. For example, when making a request to delete users, we expect to make a request to users {slash} ID of a user, and not some post request to {slash} users {slash} ID. So, first of all, the HTTP methods needs to be properly set up, and also the URL. We don't expect some random things like {slash} delete to delete a resource from the database.

**1:16:00** · As you saw, we also support filtering, sorting, and pagination in good REST APIs. Not only pagination. For example, in this case, we only have the page three, but we cannot limit the amount of products that we want to retrieve.

**1:16:15** · Whereas in this case, we can fully control what we want to get from the API. We want to get the items from page three. We want this number of limit to be applied on the products. And we also want to apply some sort, like sorting, to sort the price or sort by ratings, and so on. And also, versionings in the RESTful APIs. As you noticed in all of these requests, they all come with a prefix, which is {slash} API, and then {slash} the ID of the API, which is either V1, V2, V3, and so on.

**1:16:44** · Let's let's say in the future you migrate your API and you start using bunch of new features, but you also break something in the previous version one, then if you use the versioning, you won't break it on the front end because they can use the old version of your API and still use the old features and functionalities while you continue to develop the new version, let's say version three, and you support new features here and you might have broken something here, but

**1:17:15** · they are still using the old API, so this doesn't impact the end users.

**1:17:20** · So, to recap, we learned about the REST architectural principles and constraints, also about the resource modeling and URL design, and how we model the business domain into the RESTful API domain, also the status codes, error handling, and the proper methods to be used with the basic CRUD operations.

**1:17:41** · And lastly, we covered the best practices for RESTful APIs that you should use to keep your APIs consistent and also predictable for other developers who are using it. Traditional RESTful APIs often return too much or too little data, which requires us to do multiple requests for a single view to get all the data that we need. GraphQL solves this issue by giving clients exactly what they requested for, but designing GraphQL APIs is different from designing RESTful APIs.

### GraphQL

**1:18:10** · That's why in this video we'll cover the core concepts of GraphQL and why it exists, the schema design and type system of GraphQL, queries and mutations, error handling, and also best practices for designing GraphQL APIs. Let's start by understanding why GraphQL exists in the first place. It was created by Facebook to solve a very specific pain, which is clients needing to make multiple API calls and still not getting the exact data that they needed.

**1:18:39** · For example, if we imagine we have the Facebook APIs like user API, post API, comments, and likes for the Facebook page. Most of the times client can make requests to all of these APIs separately and still not get all the data that it needs, which will require it to do multiple requests to the same API. This, of course, adds up to the overall latency of the page because page is still not loaded until all of these requests are made and the data is fetched.

**1:19:09** · But, in case of GraphQL APIs, you have a single GraphQL endpoint. So, the client specifies the shape of the response and this one endpoint handles all of the data interactions.

**1:19:22** · It is still an HTTP request, but as you can see, we can specify the exact data that we need. For example, we need the user with ID 123 and we need only the name of the user, also posts, and from the posts, we can specify only title, so we don't need the images for this view.

**1:19:38** · And again, with the comments, you can specify the exact data that you need within the object so that you are not doing over fetching of the data.

**1:19:46** · Now, let's see the schema design and type system of GraphQL and how it's different from RESTful APIs.

**1:19:52** · The schema in this case is a contract between the client and server. In schema, first of all, you have types, which can be, for example, user type that you specify and you specify all the fields that exist on this user type, which are ID, name, posts, and so on.

**1:20:08** · And as you can see, if the type is not a primitive type like posts, then you can specify another type of post array, and then this post type can be defined separately.

**1:20:18** · Next, we have queries to read data. So, this is the equivalent of doing get requests in RESTful API. You specify the query and the function of this query.

**1:20:29** · This can be the user query, which fetches the user with specific ID, and also the return type of this query, which in this case is the user type that we defined above.

**1:20:40** · And GraphQL also come with mutations.

**1:20:42** · You can think of this as the equivalent to post, put, patch, and delete methods in restful APIs. So, anytime you are mutating a data in the database, you are making a mutation query.

**1:20:55** · Here, as you can see, we have an example of create user method, which accepts name and of course many things in real world, and then it returns the user type that we have defined above.

**1:21:05** · So, if you have good schema design in GraphQL, it should mirror your domain model, and it should be intuitive and flexible.

**1:21:12** · Next, once you define the schema design and type system, you can start querying and mutating data with this GraphQL API.

**1:21:20** · For that, we have queries for fetching data. Again, this is like the get requests in restful APIs, and here you can specify exactly what you need from the user. This is the same user method that we defined there in the schema. So, here you can also specify the exact attributes, like the name, posts, and from posts you need the title only. And this will make a request to your GraphQL API and return the exact data that you requested.

**1:21:46** · Similarly, you can also use the mutations that you defined. For example, if you have a create post method defined as a mutation, you can use this to mutate the post, for example, setting the title and body of the post, and then you also specify what data you need to retrieve after this post is created, which is ID and title. When it comes to error handling in GraphQL APIs, this is a bit different than in restful APIs, since GraphQL always returns 200 OK status for all responses, even if there was an error.

**1:22:17** · In this case, we have to return errors field in the response, which will indicate that there was an error. So, partial data can still be returned with errors, like in this case we have the user, which is null, and then we have the errors field, which indicates that you have the status code 404, message not found, and path, which is the user in your schema. As you can see in this case, you can specify the status code in the errors array.

**1:22:40** · Since we are returning 200 status codes for all GraphQL requests, that's why we have the status code specifically mentioned in the errors, so that we know what kind of error this is, which is user not found. There are also best practices that we normally follow when designing GraphQL APIs. First of all, the schemas that we saw, it's a good practice to keep them small and modular. Also, we should avoid deeply nested queries.

**1:23:05** · For example, you can have a user and then nested post, and then within the post you can have a comment, so this can be infinitely nested. And to avoid that, we usually implement query limits depths, which is how deep you can go, like how many layers nested you can have in your data. So, you specify something like six or seven layers deep. You also use meaningful naming for types and fields, so that it also makes from the client side, because they both are going to use the same schema.

**1:23:36** · And when mutating data, we always use the input types for mutations.

### Authentication

**1:23:42** · Before a system can authorize or restrict anything, it first needs to know the identity of the requester, whether it's a user accessing our service through a browser or through mobile app, or it's a third-party service trying to access our system.

**1:23:59** · That's what authentication does. It verifies that user or service trying to access our system is who they claim to be. But here is where most software engineers confuse or mix up concepts.

**1:24:12** · They mix up authentication methods with authorization frameworks. They treat JWT as an authentication method when in reality it's just a token format. They also confuse the bearer authentication with JWT. They sometimes call OAuth 2 an authentication method when in reality, it's actually an authorization framework. And they mix up single sign-on with authentication methods when it's really a user experience pattern.

**1:24:40** · In this video, we're going to fix all of that by covering, first of all, what authentication is and then all the major types of authentication starting from basic to digest authentication to API keys, sessions, and cookies, bearer authentication, and JWT tokens. What are access and refresh tokens? Also, we'll cover OAuth 2, OpenID Connect, also single sign-on and identity protocols, and understand what each one actually is and where this all fits.

**1:25:11** · Let's first understand what is authentication, and then we'll get into the different authentication methods.

**1:25:17** · So, authentication really answers one simple question, which is who the user is, whoever is trying to access our system. Let's say you have your system like your API gateway, the layer of APIs, then your service layer, and also the data storage. Before anyone can make requests to your API gateway and start accessing services and data, they first need to be authenticated. That is where they send a login request. This comes either from a user or another service.

**1:25:50** · This is where we confirm their identity if it's valid and grant access to our system, to our API gateway, and all the other services. Or if the identity is not confirmed, then we reject it with a 401 unauthorized response. This is the first step before they will get into the authorization, which is what they can access and what they can do once they can sign in to your system, but that's a separate discussion in itself.

**1:26:16** · So in this one we are primarily focusing on the authentication and different authentication methods that we can use to verify the user's identity. Now let's see the different authentication methods that we have to verify the identity of the requester and let's start with the basic authentication methods. These are the basic of digest authentication, API keys and session based authentication.

**1:26:43** · Let's start with the very first one on the list which is the basic authentication flow. This is the simplest form of authentication. Let's say you're making a request to the server to access some resource like API/users to retrieve the user data. You will first receive an unauthorized response because you didn't provide the credentials. So we prompt the user or the service to provide credentials before accessing any resource in the server.

**1:27:10** · So in the upcoming request to the same resource they also provide the authorization header and this header contains the base 64 encoded version of the username and password for this user.

**1:27:26** · This is where we verify it on the server side. If the credentials are valid then we respond with 200 OK status with the user data returned in the body or we unauthorized it again marking this as credentials invalid. The problem with this method is that base 64 is easily reversible.

**1:27:46** · So this is an insecure method unless it is wrapped with HTTPS protocol and even then it's rarely used nowadays in production outside of the internal tools because you're sending the credentials with every request and you're sending the base 64 encoded version which is not that secure. That's why we also have a digest authentication which is slightly better and it uses the MD5 hashing. So, this method works similar to the authentication with basic version.

**1:28:19** · So, you are let's say trying to access the same resource like the users.

**1:28:24** · It will first respond with 401 unauthorized prompting you to include the credentials and then you'll make the same request but with the hashed response and that will also contain the MD5 hash version instead of the plain password and username. And same process as the previous one. If the credentials are invalid, you will receive 401 unauthorized. Otherwise, you will receive the successful response with the user data in the request body.

**1:28:54** · This is slightly better than the basic off as it uses the MD5 hashing, but it's still outdated and rarely used today because we have better options as you will see soon. And if you're wondering how do we set these options in the authorization, for instance, if you're making the request from Postman or if you're doing this from the code, then you'll include it as the header in the request.

**1:29:17** · This is where you can set the authentication type and you will notice the things that we're discussing here like the basic authentication, which was the first version, or digest authentication, which is the second version, and you will see the other methods available here, also the API key option.

**1:29:34** · And Postman calls all of these authentication types to just keep it simple on the interface, but that's also one of the reasons why developers get confused and they think that all of these are authentication types when some of them are authentication methods, some of them are authorization frameworks.

**1:29:53** · Next, we have API key authentication.

**1:29:56** · This is where you generate a unique key for each client and then they send it with each request to access the resources. So, for the same request as we discussed, the comes to your API server first and it will include either authorization header or X-API-Key and that will include the API key that you generated for the user. These API keys are typically stored in a database with key hash and also the scopes for the API key.

**1:30:26** · And for instance, if you ever tried to access APIs by generating a key on the dashboard and then it gives you the key back which you can attach to the requests. That is where you already used the API key of that service to access the data. So, if you included that key in the request, then the server will first do an API key lookup in the permissions or users table.

**1:30:50** · And if it's able to verify that the API key is valid, then we will authorize the request and send the successful response with the data in the response body.

**1:31:02** · Otherwise, the user will get a 401 unauthorized response.

**1:31:07** · And if the key is missing overall, like the authorization header or X-API-Key, then we just return a 400 bad request because the API key is required to access this type of system.

**1:31:20** · One issue with API keys is that if the key ever leaks, then anyone can use it and start accessing the resources on your behalf with your API key and there is no built-in expiration unless you implement it yourself. Another thing is that this might seem similar to JSON web tokens, but API keys are just random strings with no embedded information while in JWT, we can store also information as you will see shortly.

**1:31:47** · So, the server here has no way to know who owns the key or what permissions they have without looking it up in the database.

**1:31:58** · Next, we have the traditional web approach which is the session-based authentication. This is where a user logs in with their credentials, and then we create a session in some sort of session storage. This session storage can be as simple as just in memory, like just a variable, but the problem here is that we will lose it once the server restarts or crashes.

**1:32:20** · The other option is we can use tools like Redis, which is one of the most common ones in production because it's fast and it supports expiration for the sessions, or we can use a dedicated database here, like SQL type of database. Another option, which is very rare, is to use the file system of the server that you're using. The problem with this one is that it's not scalable, and overall Redis is usually the go-to for production because it's fast and has built-in key expiration.

**1:32:52** · So, with the first request, we are fetching the session ID, and then we set the session cookie on the client side. Then for any other upcoming requests that contain this cookie, we look up the session in the session storage here, and then if the session is valid, we will get back the user data, and we will send it with authorized response. Otherwise, if it's not found, if we can't find the session, then this user is not authenticated, so we send them an unauthorized response.

**1:33:22** · One challenge with session-based authentications is that it is stateful, which means that the server must remember the sessions. We need to have some sort of session storage here, and it works great for traditional web apps, but cannot scale as easily for APIs or distributed systems. Now, let's look at token-based authentication. We'll cover bearer authentication, JWT tokens, access and refresh tokens, and how this compares to the session-based authentication. Instead of sessions, modern applications usually use tokens.

**1:33:56** · So, the client sends a token with each request. For example, we have a login with credentials, where user will include their credentials in the authorization header, which will include the type of authentication, which is bearer, and also the token, which we will validate on the server side. One thing developers confuse here is the bearer token and JSON web tokens. Bearer token just means whoever has this token gets access. So, it's a pattern, but not a specific method.

**1:34:26** · And the most common type of bearer token is JWT, JSON web token.

**1:34:33** · It's basically a signed JSON object that contains the user ID or email for us to validate the user, also expiration time, and other claims as we need to store them, like roles, permissions, and so on. So, what we do on the authentication server is we validate the credentials once we receive that authorization header. And it is stateless, meaning that we don't need a database here to look up, and that is why it's also scalable compared to the session-based authentication.

**1:35:04** · Before the JWT, let's say revolution, a token was just a string with no information. And that token was sent, and then this was looked up in some sort of database, and only then we could verify that the user has access. The downside of that was that, of course, it's still stateful, because we need the database access or cache, which is required every time the token is used.

**1:35:31** · With JSON web tokens, now we can encode and verify via signing their own claims.

**1:35:37** · And this is what now allows us to issue a short-lived JWT tokens that are stateless, meaning they are self-contained, and they don't depend on anybody else. They do not need to hit the database, and this reduces the databases load and it also simplifies the authentication process for the server. So the first time you will receive the credentials and validate the user and if it is valid we will generate the JSON web token and send it to the client.

**1:36:07** · From this point forward the client can make requests and include this better token which is this authorization header that contains the better authentication with the token.

**1:36:20** · And that token is most cases it is a JSON web token. We verify that signature locally without needing to hit the database and if the token is valid we return the requested data otherwise we return an unauthorized response.

**1:36:36** · Modern systems also use two types of tokens. One of them is the access token and the other one is the refresh tokens.

**1:36:45** · The reason we need two tokens here is that access tokens are short-lived and they are used for API calls to the server while the refresh tokens are long-lived and they are used to get new access tokens basically to renew the access token.

**1:37:01** · Whenever user sends a login request and signs in they get both of these tokens.

**1:37:07** · We generate an access token that's valid for 15 minutes to 1 hour and we generate a refresh token that can last for days or even weeks.

**1:37:17** · Client now will use the access token to access the API and make the requests and it also stores the refresh tokens. One important note here is that we never store it in local storage but we store it in HTTP only cookies. This prevents us from excess attacks on the client side.

**1:37:38** · And after this user will stay logged in without re-entering credentials. If their access token expires they will get an unauthorized response And this is where we will use that refresh token which we stored to generate a new access token on the off server side. We can make a request with that new token, and this will successfully return us the data since we renewed the access token.

**1:38:03** · Next, let's get into OAuth 2 and OpenID Connect, which are some of the misunderstood concepts, and let's clarify whether these are authentication methods or authorization frameworks and how they work. OAuth 2 is one of the concepts that is often misunderstood.

**1:38:22** · It's an authorization framework and not an authentication. So, it answers what can this app access on behalf of the user.

**1:38:31** · For instance, if you want to grant an application access to your Google Drive to be able to read your files from there, you would typically connect your Google Drive for this external application.

**1:38:44** · And you're giving the app permission to access your data. The way it works is it first will redirect you to consent screen from the Google OAuth authentication, and it will show you the permission request. And if you allow access for this application to be able to read the drive files on your behalf, then it will return the authorization code to this external application, or it can also be your application.

**1:39:13** · And the way it works after that is that you exchange the code for token, and you return the access token from Google OAuth to be able to read the data.

**1:39:24** · That is the confusing part because you're getting back an access token for the Google Drive API, and you might think that this is an authentication method, but the access token just proves that the app can access your resources.

**1:39:39** · But it doesn't tell the app who you are.

**1:39:41** · It just proves that the app is allowed to access certain resources from your Google Drive. So, after this point, the application will be able to request files with that token and return the user files from Google Drive API.

**1:39:56** · Next, we have OpenID Connect, which adds authentication on top of OAuth 2.

**1:40:02** · So, when you click on sign in to Google, let's say, via your app, it will redirect you to the authorization endpoint. And this will show you the login screen where you grant access to sign in to Google through your application. If you enter your credentials and consent, then the provider will return the authorization code. And after this step, your application will exchange the code for tokens and return the access token in combination with the ID token.

**1:40:33** · From here, the access token is for OAuth 2 authorization, but the ID token is a JSON web token that contains your identity, which includes your email or username user ID.

**1:40:46** · Which means that after this point, your application is able to verify the signature and extract the user's identity to send the ID token for verification to your backend.

**1:40:59** · And by having this ID token, your application can now create its own session and grant the access token for that user.

**1:41:08** · This is a modern solution. It's secure and also scales well. And that's also why most applications nowadays use that type of authentication like sign in with Google, GitHub, Microsoft, and so on.

**1:41:20** · And lastly, let's cover single sign-on and identity protocols.

**1:41:25** · Single sign-on is a user experience, not an authentication method. Which means that you're able to log in once, but access multiple services. For example, when you want to log into Google or Okta, let's say you want to get access to your Gmail, to your Google Drive, to YouTube, to Google Calendar, you can do this by logging in once to the identity provider. Let's say it can be Google in this case if you want to access these services.

**1:41:55** · And single sign-on uses identity protocols underneath to validate these sessions. So, once you sign in with the identity provider, let's say it's Google in this case, your global session is stored in a session storage. And then you get back a single sign-on cookie to your client to be able to access other resources. So, let's say you want to access Gmail for the first time, then once you log in, you verify also the session and now you're able to access Gmail.

**1:42:26** · And for the next request, if you need to access Google Drive for the next one, you don't need to log in again because you have these cookie and the session stored in the session storage.

**1:42:37** · So, we just verify your session and if it's valid, then you get access to Google Drive as well. And similarly to YouTube, to Google Calendar and other services.

**1:42:47** · As I mentioned, single sign-on uses identity protocols underneath. And these protocols are SAML, which is Security Assertion Markup Language, or OpenID Connect. Both of these are identity protocols which are used in combination with single sign-on.

**1:43:06** · In case of SAML, to be able to access the app, you're redirected to login and this is where we use SAML for authentication.

**1:43:14** · This is a common solution in enterprise and legacy systems like Salesforce, corporate dashboards, and so on. It is an XML-based protocol, so once you want to sign in, you are redirected to login and then you get back the SAML assertion in XML format. And after that, your identity is confirmed for the user, and now you're able to access the third-party application.

**1:43:42** · SAML is still widely used, but it's an older version compared to OpenID Connect. So, the next option is the OpenID Connect as an identity protocol.

**1:43:52** · Let's say you want to access an app, and in this case it's Gmail.

**1:43:56** · You will be redirected to login to provide your credentials. And once you provide your credentials, the user is authenticated, and now you get back the ID token in JSON Web Token format. And this is what you will use for confirming your identity with Gmail.

**1:44:15** · This is, for instance, what Google uses under the hood, and it's a more modern approach compared to SAML, but both of them are still very secure and relevant.

**1:44:26** · These are the most common types of authentication, and that is just the first step for accessing our system.

**1:44:32** · After you know who the user is with authentication, you need to also know what they can do and what permissions they have. The authentication is just the first step before users can access your service. So, this tells you who the user is, and if they are allowed to access your service. That is when they send a login request, and you confirm or deny their identity. But after that, you also have the authorization step, which tells you what resources exactly this user can access to.

### Authorization

**1:45:00** · Basically, it tells you what they can do, what the user can do in your system. And that is what we will cover next in the next video.

**1:45:10** · Authorization is the step that happens after authentication, once someone is logging in into our system. So, once their login request is approved, which means that the system now knows who the user is, the next step is deciding what they can do, which is the step of authorization. It needs to check what resources or actions that user has permissions to access and also what are the denied actions for this user.

**1:45:32** · This is how we control security and privacy in the systems and in this video you'll learn how the applications and systems manage permissions using the three main authorization models. The first one is role-based access control. Next, we have attribute-based access control. Also, access control list, which is another way of managing authorization. Plus, you learn how technologies like OAuth 2 and JWTs help us to enforce those rules in practice.

**1:46:01** · So, authentication happens first, which tells us who the user is and if they are allowed to access our system. But, on the next step we have authorization, which determines what you can actually do as a user in this system. If we take a look at GitHub as an example and accessing repositories on GitHub, there you have different permissions for different users. For example, user A can have write access only, which means they can only push code to this repo.

**1:46:28** · But, on the other hand, we can have user B and here you can grant only read access, which means they can only read this repository, but they cannot push code to it or they cannot create pull requests and so on.

**1:46:41** · And on the other side, we can have also admin users, which have full control, so they can manage all the settings for the repository. They can even decide to delete this repository and so on. So, you can see that different users can have different access controls on systems. To manage these access controls, we have common authorization models. So, the one that we just looked at is the role-based authentication model, which assigns roles to users, something like admin, editor, or read-only access, write-only access.

**1:47:10** · And this is the most common approach among these authorization models. But, we also have attribute-based access control, which is based on the user or resource attributes. So, this is more flexible and more complex compared to the role-based authentication. And the other common approach is to have access control lists, ACL, and each resource here has its own permissions list. So, you can assign permission lists to a resource, and this is what will determine what resources you can access.

**1:47:43** · For example, this is a common way of managing Google Docs, and we will look at this in more detail now. And each of these models has its tradeoffs, pros and cons. So, this depends on the specific system requirements, but real systems often combine also multiple models together to have more complex and more secure setup. So, first up we have role-based access control, or RBAC as an acronym. Here, users are assigned to roles, and each role has a defined set of permissions.

**1:48:14** · For example, as you saw with the GitHub, you can have admins, and admins usually have full access to all resources. So, they can create, they can read, or update resources. They can even delete resources, and also manage other users in the roles. And next, you have editor, which is usually a bit less than admin. So, they can edit content like creating or reading content or updating resources, but they cannot delete resources, and they cannot also manage other users.

**1:48:45** · And next, you can have viewer users, which can only read data. So, they can read the resources and content, but they cannot update anything, or they cannot create anything in your system.

**1:48:56** · This is the most common way in authorization models, and this is used in apps that you use daily, like you saw with GitHub or Stripe dashboards or CMS tools, team management tools, and so on.

**1:49:09** · The next model is attribute-based access control, or ABAC in short. This access control goes beyond the roles, so it uses the user attributes or resource attributes and environment conditions to define the access. Some example policy you can see here. Let's say you want to only allow access if some conditions are met.

**1:49:31** · In this case, whenever the user department is set to HR and you can combine this with multiple conditions like whenever the resource attribute equals to internal and so on and only in this case you allow them access. And you either allow them read access or write access, so this can also be combined with the role-based authorization.

**1:49:52** · But in this case you are checking the user model or resource model in your database and based on the attributes you either allow or deny the access. So here as you can see we are checking user attributes like the department, the age or whatever you want to check here. Next you can also combine it with resource attributes like confidentiality or the owner of the resource or classification.

**1:50:18** · And this can also be combined with environment like time of the day, location, device type and so on.

**1:50:24** · Since you're combining these attributes to either grant or restrict access, this is more flexible than the role-based authorization, but it requires good policy management and generally it's more complex and you can encounter conflicts here with the attribute-based access control. The third common type is the access control list. Instead of providing role-based access or attribute-based access, you can have access control list for the specific resource. Let's say you have a resource like a document or a JSON file.

**1:50:54** · And here you can have a permission list on which users can access this document. Like user Alyssa has only read access or user Bob has both read and write access and another user has no access to this document. So as you can see, we're managing two things here. First of all, which users are allowed to access this document, and second, what are their permissions? So, each of the users has different permissions on this document.

**1:51:24** · ACLs are highly specific and also user-centric, which means it's hard to scale them well in systems with millions of users or objects unless you manage them carefully. But, for example, Google Drive is one example of this where you have documents like a Google Doc, and then you share this Google Doc with your colleagues, right? So, you share someone with read access only, and then you share this Doc with someone else, but now they can also edit and add comments to this document.

**1:51:54** · So, this is a example of ACL, access control list, which is used in Google Drive and Google Documents. This gives you more control over resources and documents, but it's also harder to scale with millions of users, but it's possible, as you can see, because Google Drive is using this for their documents, Excel sheets, and so on.

**1:52:17** · So, these were the access control models, but how do systems enforce those authorizations? This are where OAuth 2 and JWT or access tokens come into play.

**1:52:28** · So, first we have OAuth 2, which is delegated authorization, which is a protocol used when service wants to access another service's resources on a behalf of a user. For example, if you want to let a third-party app read your GitHub repositories, let's say you're deploying your app to Vercel, so you need to give Vercel control over your repository on GitHub.

**1:52:50** · Instead of giving your username and password to the third-party application, which won't be secure at all because you don't know what they can do with your username and password, this way you are giving them full control. Instead, GitHub gives them the token that represents the permissions which you approved to use.

**1:53:11** · So, you as a user sign the request with the third-party app to request access to your repositories, and then GitHub gives you the access token which you should create. So, you should also provide what resources, what repositories this third-party app can access, and also what they can do. Can they create, read, update, or can they delete, or whatever the permissions you set? And then GitHub sends them the token which contains the permissions which this third-party app is allowed to use.

**1:53:40** · And OAuth2 defines the flow for securely issuing and validating those tokens. So, you give them the access token and not your password which represents the permissions that you approved personally. So, it can be reading specific repos or also creating, pushing to those repositories, but not deleting those repositories. And next, we have also token-based authorization using JWT or bearer tokens and permission logic.

**1:54:09** · Once a user is authenticated, most systems use a token, typically a JWT token, or this can be also bearer token that carries this information like user ID, the roles like admin or editor, and also scopes which is what scopes they are allowed to access, and whenever this token is expiring and who is the issuer of this token. So, whenever a user makes a request, it always carries this token information and reaches to the backend server.

**1:54:38** · This is where the server will check your token and validity, and it will apply the appropriate permission logic. So, to not confuse this with authorization models, there is a key distinction. The token usually carries the identity and claims of your user as you see it here, but authorization models like role-based or attribute-based, this is what defines what is allowed to access as a user. So, tokens are just mechanisms while these are authorization models.

**1:55:06** · So, in summary, authorization isn't just letting users in like authentication, but it also controls what they can access once they are in.

**1:55:17** · We learned what authorization is, what are the three most common authorization models, which are role-based, attribute-based, and access control lists, and also you saw couple of real-world examples like how GitHub manages your authorization tokens, and it should give you an idea on when to use each model based on the system that you're building. And you also saw some implementation patterns with OAuth 2 or JWT tokens.

**1:55:41** · Each of these models has their own trade-offs, their own pros and cons, and real systems often combine multiple models to stay flexible and secure. APIs are like doors into your system. If you leave them unprotected, then attackers and anyone can walk right in and do whatever they want with your user data and overall the system. That's why in today's video we'll look at seven proven techniques which will help you to protect your APIs from unwanted attacks.

### Security

**1:56:11** · The first one we have in the list is rate limiting, which controls how many requests a client can make in a given time. For example, you can set a limit for user A to make, let's say, 100 requests per some period of time to your API. And if they cross that limit and, let's say, make 100 and one request, then you block the next request and allow some time to pass before they can send their next request. If you don't set this to your API, then attackers can overwhelm your system.

**1:56:40** · They can send like thousands of requests per minute and then overwhelm your API, which will take your system down, or it can also brute force your data. And these rate limits can be set per endpoint. For instance, let's say you have some {slash} comments endpoint, and here they can send a request to either create a comment or fetch comments. You can set that limit for endpoint level. So, these comments endpoint will be set to some strict number of requests per minute.

**1:57:11** · You can also set it per user or IP address. Let's say in A we have the IP address of first user, and then B for the second, C for this one, and your attacker has some IP address which corresponds to D.

**1:57:24** · If you get the 101st request from the D IP address, then you will know that this user overused the API, so you will block it at the user IP level.

**1:57:36** · And there is also overall rate limiting to protect from DDoS attacks. Since you can set the rate limit to work per user or per IP address, that means that this attacker alone cannot send that many requests. You will block it with your rate limiting in the API. But what they can do is they can spin up some bots, and each bot will have their own limit, right? Let's say you've set it to 100 per IP address. So, each of these bots has 100, and overall they have more than you would allow or your system could handle.

**1:58:08** · That's why you have also overall rate limitings, which can be some bigger number. So, whenever all the traffic coming into your server reaches or passes this number, then you will temporarily block all requests until you find out the root cause. And of course, these numbers are just examples, so in reality it's much more than 1,000, but that's just an example. The second one on the list is CORS, which stands for cross-origin resource sharing.

**1:58:34** · This controls which domain can call your API from a browser, and without proper CORS, malicious websites could trick users' browsers into making requests on their behalf. For instance, if your API is only meant to serve your front end up, which is that up.yourdomain.com, then only requests from this source should be allowed.

**1:58:58** · If anyone else sends you a request like up.anotherdomain.com, then you should block this request and not allow them to use your API for authenticating or using any of its data.

**1:59:12** · The third one is also a common one, which is SQL and no SQL injections.

**1:59:17** · Injection attacks can happen when the user input is directly included in the database query. For instance, attacker can modify it and send some queries to read or delete your data.

**1:59:29** · Here, for example, this part bypasses the checks entirely and then attacker can use this query to start reading data from your database or modify anything, or they can also delete all the data, all the user data, and any other tables that you have in this database.

**1:59:46** · So, to fix this, we always use parameterized queries or ORM safeguards.

**1:59:52** · The next technique to use is firewalls.

**1:59:55** · A firewall acts as a gatekeeper, filtering the malicious traffic from the other normal traffic. So, typically, you have it between your API and the incoming traffic. For example, if you use the AWS's web application firewall, this can block requests with unknown attack patterns such as suspicious SQL keywords or strange HTTP methods, which means it will block any suspicious requests from attackers, but it will allow others to bypass the request and reach to your API.

**2:00:27** · Some APIs are also private and should only be accessed from specific networks.

**2:00:32** · That's why we have also VPNs, which stands for virtual private networks. The APIs that are within the VPN network can only be accessed by someone who is also within that same network, which Which that some APIs are public facing, meaning these APIs will allow any requests from the internet from your users. But this for example can be within the VPN network, which means if a user from web tries to reach your API, then this request will be blocked because the user is not within the same network.

**2:01:04** · But on the other hand, if you have another user here, which is within the VPN network, they can make a request to these APIs and in this case they will bypass the checks and their will reach to your APIs.

**2:01:18** · This is useful where you have internal tools. Let's say you have internal admin dashboard and the API for this admin panel will only be reachable by employees connected to the company VPN.

**2:01:30** · Next we have CSRF, which stands for cross-site request forgery. This tricks a logged-in user's browser into making unwanted requests to the API. Let's say you as a user are logged in into your bank system and your bank system uses cookies for authentication. If the bank system is not secure and they only use session cookies, another malicious site might use your cookie and submit a hidden transferring money request through your cookie.

**2:01:58** · So to prevent such attacks, companies also use CSRF tokens in combination with session cookie. So the banking system will check if the session cookie is present, but it will also check if the CSRF token matches with the one that they have. And if it doesn't, then it will block this request from the other unknown source, while it will allow request from your behalf.

**2:02:23** · And the last one we have is XSS or it's also called cross-site scripting. This lets attackers to inject scripts into web pages served to other users. For example, if you have a comment section and this comment gets submitted to your API, next your API will also store it in a database. You can get normal requests like nice picture or something like that, and this will get to your API.

**2:02:48** · Your API will store it in the database.

**2:02:50** · So, everything is fine there. But, what if an attacker places a script in this comment section? And within this script, they can try to do many different things. For example, they can try to fetch the cookie for another user, or they can try to inject something into your database. And if you allow this, then it will reach to your server, and the information will be written into the database.

**2:03:14** · Later, when the other users load these comments section on their screen, they will get also the injected comment directly into their web page, and the browser will execute this malicious JavaScript code into the other users' browser. What you just went through were the first two sections of my system design mastery course, and this is just one piece in my mentorship program.

### What's next

**2:03:38** · If you want to go through the rest of these and actually master system design, not only at theory level, but to a point where you can design, build, and host full-stack systems end-to-end under my guidance, and get to senior and staff level by learning everything it takes to level up in your career, then there is a link in the description for you, which you can check out, apply, and see if you qualify for the program.

**2:04:03** · Hope you liked the course, and see you in the next one.