---
domains:
  - "aws"
class: reference-note
tier: reference-note
tags:
  - aws/cloudfront
---

# Module 3-13: AWS CloudFront CDN

## 2. Content Delivery Networks & CloudFront Integration


---

## CDN - Content Delivery Network (Amazon CloudFront)
- Amazon CloudFront Provides highly available cache to compensate using multiple resources for less latency "**ex:** Accessing data from S3 buckets through different countries"
- using CloudFront is more economically efficient than using different Buckets.
- These Cache Locations are called Edge Locations.
![Pasted image 20221103030233](https://user-images.githubusercontent.com/109697567/200859517-5740e0c2-2478-4a47-9fc4-df78dd78be47.png)


Red squares refers to edge locations, if edge locations doesn't have the requested data cached it uses its high speed links to the main s3 bucket source and fetch the data so the fetch process was faster than the user connecting directly to the s3 and if the data was requested again its already cached in the edge location 

Using Cloud-Front is guaranteed to be cheaper than fetching content directly from an s3 bucket, can be a question on how to reduce s3 bucket cost usage
