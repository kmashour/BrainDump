---
domains:
  - "kubernetes"
  - "scheduling"
---

# How does Kubernetes scheduler work StackOverflow

**Source:** https://stackoverflow.com/questions/28857993/how-does-kubernetes-scheduler-work

---

Title: Live Content Description: Fetched live Source: https://stackoverflow.com/questions/28857993/how-does-kubernetes-scheduler-work \--- 

Skip to main content

[ ](https://stackoverflow.com "Stack Overflow")

  1. [ About ](https://stackoverflow.co/)
  2. Products
  3. [ For Teams ](https://stackoverflow.co/internal/)



  1. [ Stack Internal Implement a knowledge platform layer to power your enterprise and AI tools. ](https://stackoverflow.co/internal/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=top-nav&utm_content=stack-overflow-for-teams)
  2. [ Stack Data Licensing Get access to top-class technical expertise with trusted & attributed content. ](https://stackoverflow.co/data-licensing/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=top-nav&utm_content=overflow-api)
  3. [ Stack Ads Connect your brand to the world's most trusted technologist communities. ](https://stackoverflow.co/advertising/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=top-nav&utm_content=stack-overflow-advertising)
  4. [ Releases Keep up-to-date on features we add to Stack Overflow and Stack Internal. ](https://stackoverflow.blog/releases/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=top-nav&utm_content=releases)
  5. [About the company](https://stackoverflow.co/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=top-nav&utm_content=about-the-company) [Visit the blog](https://stackoverflow.blog/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=top-nav&utm_content=blog)



Loading…

  1. [](https://stackoverflow.com/help "Help Center and other resources")

     * [ Tour  Start here for a quick overview of the site  ](https://stackoverflow.com/tour)
     * [ Help Center  Detailed answers to any questions you might have  ](https://stackoverflow.com/help)
     * [ Meta  Discuss the workings and policies of this site  ](https://meta.stackoverflow.com)
     * [ About Us  Learn more about Stack Overflow the company, and our products  ](https://stackoverflow.co/)

  2. [ ](https://stackexchange.com "A list of all 184 Stack Exchange sites")
  3. ###  [current community](https://stackoverflow.com)

     * [ Stack Overflow  ](https://stackoverflow.com)

[help](https://stackoverflow.com/help) [chat](https://chat.stackoverflow.com/?tab=explore)

     * [ Meta Stack Overflow  ](https://meta.stackoverflow.com)

###  your communities 

[Sign up](https://stackoverflow.com/users/signup?ssrc=site_switcher&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f28857993%2fhow-does-kubernetes-scheduler-work) or [log in](https://stackoverflow.com/users/login?ssrc=site_switcher&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f28857993%2fhow-does-kubernetes-scheduler-work) to customize your list. 

### [more stack exchange communities](https://stackexchange.com/sites)

[company blog](https://stackoverflow.blog)

  4.   5. [Log in](https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f28857993%2fhow-does-kubernetes-scheduler-work)
  6. [Sign up](https://stackoverflow.com/users/signup?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f28857993%2fhow-does-kubernetes-scheduler-work)



New: Stack Overflow For Agents. The next generation of knowledge exchange.  [Learn more](https://agents.stackoverflow.com/?utm_medium=product&utm_source=stackoverflow-community&utm_campaign=sofa-launch)

  1.      1. [ Home ](https://stackoverflow.com/)
     2. [ Questions ](https://stackoverflow.com/questions)
     3. [ AI Assist ](https://stackoverflow.com/ai-assist)
     4. [ Tags ](https://stackoverflow.com/tags)
     5.      6. [ Stack Overflow for Agents ](http://agents.stackoverflow.com)
     7.      8. [ Challenges ](https://stackoverflow.com/beta/challenges)
     9. [ Chat ](https://chat.stackoverflow.com/?tab=explore)
     10. [ Articles ](https://stackoverflow.blog/contributed?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=so-blog&utm_content=experiment-articles)
     11. [ Users ](https://stackoverflow.com/users)
     12.      13. [ Companies ](https://stackoverflow.com/jobs/companies?so_medium=stackoverflow&so_source=SiteNav)
     14. [ Collectives ](#)

     15. Communities for your favorite technologies. [Explore all Collectives](https://stackoverflow.com/collectives-all)

  2. Stack Internal

Stack Overflow for Teams is now called **Stack Internal**. Bring the best of human thought and AI automation together at your work. 

[Try for free](https://stackoverflowteams.com/teams/create/free/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=side-bar&utm_content=explore-teams) [Learn more](https://stackoverflow.co/internal/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=side-bar&utm_content=explore-teams)

  3. [ Stack Internal ](#)
  4. Bring the best of human thought and AI automation together at your work. [Learn more](https://stackoverflow.co/internal/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=side-bar&utm_content=explore-teams-compact)




##### Collectives™ on Stack Overflow

Find centralized, trusted content and collaborate around the technologies you use most.

[ Learn more about Collectives ](https://stackoverflow.com/collectives)

**Stack Internal**

Knowledge at work

Bring the best of human thought and AI automation together at your work.

[ Explore Stack Internal ](https://stackoverflow.co/internal/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=side-bar&utm_content=explore-teams-compact-popover)

# [How does Kubernetes' scheduler work?](https://stackoverflow.com/questions/28857993/how-does-kubernetes-scheduler-work)

[ Ask Question ](https://stackoverflow.com/questions/ask)

Asked 11 years, 3 months ago

Modified [1 year, 8 months ago](https://stackoverflow.com?lastactivity "2024-10-05 08:52:31Z")

Viewed 46k times 

59 

[](https://stackoverflow.com/posts/28857993/timeline "Show activity on this post.")

How does Kubernetes' scheduler work? What I mean is that Kubernetes' scheduler appears to be very simple?

My initial thought is that this scheduler is just a simple admission control system, not a real scheduler. Is it that correct?

I found a short description, but it is not terribly informative:

> The kubernetes scheduler is a policy-rich, topology-aware, workload-specific function that significantly impacts availability, performance, and capacity. The scheduler needs to take into account individual and collective resource requirements, quality of service requirements, hardware/software/policy constraints, affinity and anti-affinity specifications, data locality, inter-workload interference, deadlines, and so on. Workload-specific requirements will be exposed through the API as necessary.

  * [kubernetes](https://stackoverflow.com/questions/tagged/kubernetes "show questions tagged 'kubernetes'")



[Share](https://stackoverflow.com/q/28857993 "Short permalink to this question")

[Improve this question](https://stackoverflow.com/posts/28857993/edit)

Follow 

[edited Mar 5, 2015 at 22:32](https://stackoverflow.com/posts/28857993/revisions "show all edits to this post")

[![aronchick's user avatar](https://i.sstatic.net/pwSSc.jpg?s=64)](https://stackoverflow.com/users/4322/aronchick)

[aronchick](https://stackoverflow.com/users/4322/aronchick)

7,1581212 gold badges5858 silver badges9595 bronze badges

asked Mar 4, 2015 at 15:15

[![Halacs's user avatar](https://i.sstatic.net/I1Ltz.jpg?s=64)](https://stackoverflow.com/users/1501605/halacs)

[Halacs](https://stackoverflow.com/users/1501605/halacs)

95222 gold badges99 silver badges2020 bronze badges




Add a comment   | 

##  4 Answers 4

Sorted by:  [ Reset to default ](https://stackoverflow.com/questions/28857993/how-does-kubernetes-scheduler-work?answertab=scoredesc#tab-top)

Highest score (default)  Trending (recent votes count more)  Date modified (newest first)  Date created (oldest first) 

91 

[](https://stackoverflow.com/posts/28874577/timeline "Show activity on this post.")

The paragraph you quoted describes where we hope to be in the future (where the future is defined in units of months, not years). We're not there yet, but the scheduler does have a number of useful features already, enough for a simple deployment. In the rest of this reply, I'll explain how the scheduler works today.

The scheduler is not just an admission controller; for each pod that is created, it finds the "best" machine for that pod, and if no machine is suitable, the pod remains unscheduled until a machine becomes suitable.

The scheduler is configurable. It has two types of policies, **FitPredicate** (see `master/pkg/scheduler/predicates.go`) and **PriorityFunction** (see `master/pkg/scheduler/priorities.go`). I'll describe them.

**Fit predicates** are required rules, for example the labels on the node must be compatible with the label selector on the pod (this rule is implemented in `PodSelectorMatches()` in `predicates.go`), and the sum of the requested resources of the container(s) already running on the machine plus the requested resources of the new container(s) you are considering scheduling onto the machine must not be greater than the capacity of the machine (this rule is implemented in `PodFitsResources()` in `predicates.go`; note that "requested resources" is defined as _pod.Spec.Containers[n].Resources.Limits_ , and if you request zero resources then you always fit). If any of the required rules are not satisfied for a particular (new pod, machine) pair, then the new pod is not scheduled on that machine. If after checking all machines the scheduler decides that the new pod cannot be scheduled onto any machine, then the pod remains in Pending state until it can be satisfied by one of the machines.

After checking all of the machines with respect to the fit predicates, the scheduler may find that multiple machines "fit" the pod. But of course, the pod can only be scheduled onto one machine. That's where priority functions come in. Basically, the scheduler ranks the machines that meet all of the fit predicates, and then chooses the best one. For example, it prefers the machine whose already-running pods consume the least resources (this is implemented in `LeastRequestedPriority()` in `priorities.go`). This policy spreads pods (and thus containers) out instead of packing lots onto one machine while leaving others empty. 

When I said that the scheduler is configurable, I mean that you can decide at compile time which fit predicates and priority functions you want Kubernetes to apply. Currently, it applies all of the ones you see in `predicates.go` and `priorities.go`.

[Share](https://stackoverflow.com/a/28874577 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/28874577/edit)

Follow 

[edited Nov 28, 2018 at 20:36](https://stackoverflow.com/posts/28874577/revisions "show all edits to this post")

[![Ivan Aracki's user avatar](https://i.sstatic.net/T1Mo3.jpg?s=64)](https://stackoverflow.com/users/2884309/ivan-aracki)

[Ivan Aracki](https://stackoverflow.com/users/2884309/ivan-aracki)

5,5811212 gold badges6969 silver badges8888 bronze badges

answered Mar 5, 2015 at 9:42

[![DavidO's user avatar](https://www.gravatar.com/avatar/624c0ab937a08a9bafc18841dcd4dc27?s=64&d=identicon&r=PG&f=y&so-version=2)](https://stackoverflow.com/users/4148679/davido)

[DavidO](https://stackoverflow.com/users/4148679/davido)

1,8031313 silver badges77 bronze badges

Sign up to request clarification or add additional context in comments. 

## 7 Comments 

Add a comment

[![](https://www.gravatar.com/avatar/6078165a3f6a8693a0b1a1101e9260c7?s=48&d=identicon&r=PG)](https://stackoverflow.com/users/1813875/harryz)

harryz

[harryz](https://stackoverflow.com/users/1813875/harryz) Over a year ago

I think there's something wrong with the old doc. Kuber use `request` to do scheduling and `limit` for resource restriction.

2015-10-19T08:51:31.207Z+00:00

0

Reply

  * Copy link



[![](https://www.gravatar.com/avatar/51928ad446f5433348c5882f60684bb5?s=48&d=identicon&r=PG)](https://stackoverflow.com/users/1134714/alph486)

alph486

[alph486](https://stackoverflow.com/users/1134714/alph486) Over a year ago

@DavidO Is there public documentation that describes the default Fit Predicates and Priority functions that are in place, in plain english instead of code? It would be helpful in order to explain to non-kubernites and make design decisions.

2016-06-20T17:19:56.2Z+00:00

0

Reply

  * Copy link



[![](https://i.sstatic.net/3biBH.png?s=64)](https://stackoverflow.com/users/2115797/sasha-fonseca)

Sasha Fonseca

[Sasha Fonseca](https://stackoverflow.com/users/2115797/sasha-fonseca) Over a year ago

So two years later did you reach the intended goal you mention at the beginning of your answer?

2017-06-17T10:18:32.21Z+00:00

5

Reply

  * Copy link



[![](https://www.gravatar.com/avatar/7540f1aac4d78cc963f6551e8307b757?s=48&d=identicon&r=PG)](https://stackoverflow.com/users/284111/andrew-savinykh)

Andrew Savinykh

[Andrew Savinykh](https://stackoverflow.com/users/284111/andrew-savinykh) Over a year ago

The links are now [github.com/kubernetes/community/blob/master/contributors/devel/…](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-scheduling/scheduler.md) and [github.com/kubernetes/community/blob/master/contributors/devel/…](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-scheduling/scheduler_algorithm.md)

2020-02-21T06:39:38.213Z+00:00

2

Reply

  * Copy link



[![](https://www.gravatar.com/avatar/7540f1aac4d78cc963f6551e8307b757?s=48&d=identicon&r=PG)](https://stackoverflow.com/users/284111/andrew-savinykh)

Andrew Savinykh

[Andrew Savinykh](https://stackoverflow.com/users/284111/andrew-savinykh) Over a year ago

@AndrewRalon looks like [github.com/kubernetes/community/blob/master/contributors/devel/…](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-scheduling/scheduling_code_hierarchy_overview.md) is the new one

2022-03-25T23:34:30.93Z+00:00

2

Reply

  * Copy link



Add a comment

7 

[](https://stackoverflow.com/posts/31017366/timeline "Show activity on this post.")

We've done customizations that, for example, apply multilevel affinity and anti affinity based on custom selectors. The scheduler isn't perfect, but it's pretty good for most service level workloads, and in the future should get a lot better. <https://docs.openshift.org/latest/admin_guide/scheduler.html#use-cases> describes one particular Kube scheduler config that provides that.

[Share](https://stackoverflow.com/a/31017366 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/31017366/edit)

Follow 

answered Jun 24, 2015 at 3:58

[![Clayton's user avatar](https://www.gravatar.com/avatar/80a4e371c3fbd7fb0fd9bb9d870d6084?s=64&d=identicon&r=PG)](https://stackoverflow.com/users/1650118/clayton)

[Clayton](https://stackoverflow.com/users/1650118/clayton)

3,32611 gold badge2121 silver badges1414 bronze badges

## 4 Comments 

Add a comment

[![](https://www.gravatar.com/avatar/833761cd202c03e01ac63c55021a4eec?s=48&d=identicon&r=PG)](https://stackoverflow.com/users/645491/trinitronx)

TrinitronX

[TrinitronX](https://stackoverflow.com/users/645491/trinitronx) Over a year ago

Great detailed resource on the k8s scheduler! Thanks for the link to OpenShift docs!

2016-09-12T19:06:51.587Z+00:00

0

Reply

  * Copy link



[![](https://www.gravatar.com/avatar/da8c63db24d7e098f7b06185e8d1dbbb?s=48&d=identicon&r=PG)](https://stackoverflow.com/users/845762/xudifsd)

xudifsd

[xudifsd](https://stackoverflow.com/users/845762/xudifsd) Over a year ago

Hi, the link is broken. Could you fix that?

2018-07-09T06:11:01.8Z+00:00

0

Reply

  * Copy link



[![](https://i.sstatic.net/qu5b6.jpg?s=64)](https://stackoverflow.com/users/3848679/surajd)

surajd

[surajd](https://stackoverflow.com/users/3848679/surajd) Over a year ago

@xudifsd here is the link to the latest docs [docs.okd.io/latest/admin_guide/scheduling/scheduler.html](https://docs.okd.io/latest/admin_guide/scheduling/scheduler.html)

2018-10-09T06:01:43.447Z+00:00

0

Reply

  * Copy link



[![](https://www.gravatar.com/avatar/a60cfb62f0dc0c498669dde0eaf443bd?s=48&d=identicon&r=PG&f=y&so-version=2)](https://stackoverflow.com/users/3611427/shakaib)

Shakaib

[Shakaib](https://stackoverflow.com/users/3611427/shakaib) Over a year ago

Here is the latest docs as of today - [docs.okd.io/latest/nodes/scheduling/nodes-scheduler-about.html](https://docs.okd.io/latest/nodes/scheduling/nodes-scheduler-about.html)

2022-10-19T19:23:40.993Z+00:00

0

Reply

  * Copy link



Add a comment

3 

[](https://stackoverflow.com/posts/77945531/timeline "Show activity on this post.")

The scheduler has a process set in place for it to pick a pod and place it in the right node and start it.

  1. The user starts a new pod.

  2. **Scheduler Queue:** This is the _[QueueSort](https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/#queue-sort)_ phase. Pod is added to the scheduling queue. Based on the priority given to the pod it starts to schedule the pod [PriorityClasses](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/).

  3. **Filtering:** This is the _[Filter](https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/#filter)_ phase. In this phase nodes that cannot schedule the pod are filtered based on resource limits, taints & tolerations, etc.

  4. **Scoring:** This is the _[Score](https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/#scoring)_ phase. In this phase, the scheduler scores the nodes filtered based on the free space available before and after scheduling and then assigns a score. The node with the highest score is taken.

  5. **Binding:** This is the _[Bind](https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/#scoring)_ phase. In this phase, the pod is bound to the node with the highest score and now the pod is finally scheduled.




**Advanced:** We also have _scheduling plugins_ which we can add to each phase. Along with pre and post-actions (Eg: PreFilter, PostFilter, PreScore, etc) for each phase where you can bind plugins. Read more about it [scheduling framework](https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/)

This is a short walk-through of the Kubernetes scheduler process. Hope it was helpful.

[Share](https://stackoverflow.com/a/77945531 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/77945531/edit)

Follow 

[edited Feb 6, 2024 at 6:03](https://stackoverflow.com/posts/77945531/revisions "show all edits to this post")

answered Feb 6, 2024 at 5:56

[![Oliver Paul K's user avatar](https://lh4.googleusercontent.com/-E6YuiyAbmtI/AAAAAAAAAAI/AAAAAAAAAAA/ACHi3rddaHALzapYcZDm1FEtTj1rl-NT7Q/s64-rj/photo.jpg)](https://stackoverflow.com/users/12497383/oliver-paul-k)

[Oliver Paul K](https://stackoverflow.com/users/12497383/oliver-paul-k)

56155 silver badges66 bronze badges

## Comments

Add a comment

2 

[](https://stackoverflow.com/posts/78938464/timeline "Show activity on this post.")

I think one can get quiet lost while trying to understand how the k8s-scheduler works so I'll try to provide an answer in a gradual way.

* * *

### Background: From the priority queue to the scheduling context

For simplicity, let's assume that the scheduler is watching a simple queue where all pods are sorted according to the priority.

The scheduler takes the pod with the higest priority and start the "scheduling context" process where it goes into two phases:

  1. The **scheduling** phase selects a node for the pod and are run serially.

  2. The **binding** phase applies that decision to the cluster.




Scheduling cycles are run serially, while binding cycles may run concurrently.

* * *

### Focus of this answer - how does the scheduler select nodes?

Let's focus of the **scheduling** phase mentioned above.

Inside this phase we have 2 important sub phases:

  1. Unrelevant nodes are getting filtered.
  2. Relevant nodes are being ranked based on a score.



#### Filtering

The default scheduler has 13 checks (also called as "_predicates_ ") that are being performed for each node:

`PodFitsHostPorts`: Checks if a Node has free ports (the network protocol kind) for the Pod ports the Pod is requesting.

`PodFitsHost`: Checks if a Pod specifies a specific Node by its hostname.

`PodFitsResources`: Checks if the Node has free resources (eg, CPU and Memory) to meet the requirement of the Pod.

`PodMatchNodeSelector`: Checks if a Pod’s Node Selector matches the Node’s label(s).

`NoVolumeZoneConflict`: Evaluate if the Volumes that a Pod requests are available on the Node, given the failure zone restrictions for that storage.

`NoDiskConflict`: Evaluates if a Pod can fit on a Node due to the volumes it requests, and those that are already mounted.

`MaxCSIVolumeCount`: Decides how many CSI volumes should be attached, and whether that’s over a configured limit.

`CheckNodeMemoryPressure`: If a Node is reporting memory pressure, and there’s no configured exception, the Pod won’t be scheduled there.

`CheckNodePIDPressure`: If a Node is reporting that process IDs are scarce, and there’s no configured exception, the Pod won’t be scheduled there.

`CheckNodeDiskPressure`: If a Node is reporting storage pressure (a filesystem that is full or nearly full), and there’s no configured exception, the Pod won’t be scheduled there.

`CheckNodeCondition`: Nodes can report that they have a completely full filesystem, that networking isn’t available or that kubelet is otherwise not ready to run Pods. If such a condition is set for a Node, and there’s no configured exception, the Pod won’t be scheduled there.

`PodToleratesNodeTaints`: checks if a Pod’s tolerations can tolerate the Node’s taints.

`CheckVolumeBinding`: Evaluates if a Pod can fit due to the volumes it requests. This applies for both bound and unbound PVCs.

#### Ranking based on score

There are 13 functions to decide how to score and rank nodes:

`SelectorSpreadPriority`: Spreads Pods across hosts, considering Pods that belong to the same Service, StatefulSet or ReplicaSet.

`InterPodAffinityPriority`: Computes a sum by iterating through the elements of weightedPodAffinityTerm and adding “weight” to the sum if the corresponding PodAffinityTerm is satisfied for that node; the node(s) with the highest sum are the most preferred.

`LeastRequestedPriority`: Favors nodes with fewer requested resources. In other words, the more Pods that are placed on a Node, and the more resources those Pods use, the lower the ranking this policy will give.

`MostRequestedPriority`: Favors nodes with most requested resources. This policy will fit the scheduled Pods onto the smallest number of Nodes needed to run your overall set of workloads.

`RequestedToCapacityRatioPriority`: Creates a requestedToCapacity based ResourceAllocationPriority using default resource scoring function shape.

`BalancedResourceAllocation`: Favors nodes with balanced resource usage.

`NodePreferAvoidPodsPriority`: Prioritizes nodes according to the node annotation scheduler.alpha.kubernetes.io/preferAvoidPods. You can use this to hint that two different Pods shouldn’t run on the same Node.

`NodeAffinityPriority`: Prioritizes nodes according to node affinity scheduling preferences indicated in PreferredDuringSchedulingIgnoredDuringExecution. You can read more about this in Assigning Pods to Nodes.

`TaintTolerationPriority`: Prepares the priority list for all the nodes, based on the number of intolerable taints on the node. This policy adjusts a node’s rank taking that list into account.

`ImageLocalityPriority`: Favors nodes that already have the container images for that Pod cached locally.

`ServiceSpreadingPriority`: For a given Service, this policy aims to make sure that the Pods for the Service run on different nodes. It favours scheduling onto nodes that don’t have Pods for the service already assigned there. The overall outcome is that the Service becomes more resilient to a single Node failure.

`CalculateAntiAffinityPriorityMap`: This policy helps implement pod anti-affinity.

`EqualPriorityMap`: Gives an equal weight of one to all nodes.

### Update

[Here](https://kubernetes.io/docs/reference/scheduling/config/#scheduling-plugins) is an updated list of all plugins that enabled by default.

* * *

### Advanced - The Scheduling Framework

Taken from [here](https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/#interfaces).

The following picture shows the scheduling context of a Pod and the interfaces that the scheduling framework exposes.

[![enter image description here](https://i.sstatic.net/0kPA8xoC.png)](https://i.sstatic.net/0kPA8xoC.png)

As being described in the original [design proposel](https://github.com/kubernetes/enhancements/tree/master/keps/sig-scheduling/624-scheduling-framework#proposal) \- the main idea behind the "Scheduling Framework" is that it defines way to extend the default behaviour of the scheduler (the "Default Scheduler") by writing extension points in the Kubernetes Scheduler in the form of "plugins".

Plugins add scheduling behaviors to the scheduler, and are included at compile time.

The scheduler's `ComponentConfig` will allow plugins to be enabled, disabled, and reordered. Custom schedulers can write their plugins "[out-of-tree](https://github.com/kubernetes/enhancements/tree/master/keps/sig-scheduling/624-scheduling-framework#custom-scheduler-plugins-out-of-tree)" and compile a scheduler binary with their own plugins included.

(*) The queue sort extension point is a special case. It is not part of a scheduling context and may be called concurrently for many pod pairs.

* * *

### Bonus - the 3 scheduling queues in kube-scheduler

From [here](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-scheduling/scheduler_queues.md).

> Queueing mechanism is an integral part of the scheduler.
> 
> It allows the scheduler to pick the most suitable pod for the next scheduling cycle.
> 
> Given a pod can specify various conditions that have to be met at the time of scheduling, such as existence of a persistent volume, compliance with pod anti-affinity rules or toleration of node taints, the mechanism needs to be able to postpone the scheduling action until the cluster may meet all the conditions for the successful scheduling.

The mechanism relies on three queues:

(1) active (activeQ): providing pods for immediate scheduling.

(2) unschedulable (unschedulableQ): for parking pods which are waiting for certain condition(s) to happen.

(3) backoff (podBackoffQ): exponentially postponing pods which failed to be scheduled (e.g. volume still getting created) but are expected to get scheduled eventually.

[Share](https://stackoverflow.com/a/78938464 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/78938464/edit)

Follow 

[edited Oct 5, 2024 at 8:52](https://stackoverflow.com/posts/78938464/revisions "show all edits to this post")

answered Sep 1, 2024 at 22:18

[![Rotem jackoby's user avatar](https://www.gravatar.com/avatar/107522343c9ed3b01cdc0d3eece92241?s=64&d=identicon&r=PG)](https://stackoverflow.com/users/1103953/rotem-jackoby)

[Rotem jackoby](https://stackoverflow.com/users/1103953/rotem-jackoby)

23.1k1414 gold badges146146 silver badges140140 bronze badges

## Comments

Add a comment

##  Your Answer 

Thanks for contributing an answer to Stack Overflow!

  * Please be sure to _answer the question_. Provide details and share your research!



But _avoid_ …

  * Asking for help, clarification, or responding to other answers.
  * Making statements based on opinion; back them up with references or personal experience.



To learn more, see our [tips on writing great answers](https://stackoverflow.com/help/how-to-answer).

Draft saved

Draft discarded

### Sign up or [log in](https://stackoverflow.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f28857993%2fhow-does-kubernetes-scheduler-work%23new-answer)

Sign up using Google 

Sign up using Email and Password 

Submit

### Post as a guest

Name

Email

Required, but never shown

### Post as a guest

Name

Email

Required, but never shown

Post Your Answer  Discard 

By clicking “Post Your Answer”, you agree to our [terms of service](https://stackoverflow.com/legal/terms-of-service/public) and acknowledge you have read our [privacy policy](https://stackoverflow.com/legal/privacy-policy).

Start asking to get answers

Find the answer to your question by asking.

[Ask question](https://stackoverflow.com/questions/ask)

Explore related questions

  * [kubernetes](https://stackoverflow.com/questions/tagged/kubernetes "show questions tagged 'kubernetes'")



See similar questions with these tags.

  * The Overflow Blog 
  * [Announcing Stack Overflow for...](https://stackoverflow.blog/2026/06/10/announcing-stack-overflow-for-agents/ "Announcing Stack Overflow for Agents​​​​‌﻿‍﻿​‍​‍‌‍﻿﻿‌﻿​‍‌‍‍‌‌‍‌﻿‌‍‍‌‌‍﻿‍​‍​‍​﻿‍‍​‍​‍‌﻿​﻿‌‍​‌‌‍﻿‍‌‍‍‌‌﻿‌​‌﻿‍‌​‍﻿‍‌‍‍‌‌‍﻿﻿​‍​‍​‍﻿​​‍​‍‌‍‍​‌﻿​‍‌‍‌‌‌‍‌‍​‍​‍​﻿‍‍​‍​‍‌‍‍​‌﻿‌​‌﻿‌​‌﻿​​‌﻿​﻿​﻿‍‍​‍﻿﻿​‍﻿﻿‌‍​﻿‌‍﻿‌‌﻿​﻿​‍﻿‍‌﻿​﻿‌﻿‌​‌‍​‌‌‍​﻿‌‍‍﻿‌‍﻿﻿‌﻿‌‍‌‍‌‌‌﻿​‍‌‍‌‍‌‍﻿​‌‍﻿﻿‌﻿‌﻿​‍﻿‍‌‍​﻿‌‍﻿﻿​‍﻿﻿‌‍‍‌‌‍﻿‍‌﻿‌​‌‍‌‌‌‍﻿‍‌﻿‌​​‍﻿﻿‌‍‌‌‌‍‌​‌‍‍‌‌﻿‌​​‍﻿﻿‌‍﻿‌‌‍﻿﻿‌‍‌​‌‍‌‌​﻿﻿‌‌﻿​​‌﻿​‍‌‍‌‌‌﻿​﻿‌‍‌‌‌‍﻿‍‌﻿‌​‌‍​‌‌﻿‌​‌‍‍‌‌‍﻿﻿‌‍﻿‍​﻿‍﻿‌‍‍‌‌‍‌​​﻿﻿‌​﻿‌​​﻿‍​​﻿‌﻿​﻿​‍‌‍​﻿‌‍​﻿​﻿‌​‌‍‌‍​‍﻿‌‌‍‌​‌‍‌​​﻿‌‍​﻿​‍​‍﻿‌​﻿‌​‌‍‌‌​﻿‌﻿‌‍​‍​‍﻿‌‌‍​‌‌‍​‌​﻿‌‍‌‍​‍​‍﻿‌‌‍​‍​﻿‍​‌‍‌​​﻿‌‍​﻿‍‌​﻿‍​​﻿‍​​﻿‍‌​﻿‌​‌‍​‍​﻿‌‌​﻿‌‍​﻿‍﻿‌﻿‌​‌﻿‍‌‌﻿​​‌‍‌‌​﻿﻿‌‌‍​‍‌‍﻿​‌‍﻿﻿‌‍‌﻿‌‌​​‌‍﻿﻿‌﻿​﻿‌﻿‌​​﻿‍﻿‌﻿​​‌‍​‌‌﻿‌​‌‍‍​​﻿﻿‌‌﻿‌​‌‍‍‌‌﻿‌​‌‍﻿​‌‍‌‌​﻿﻿﻿‌‍​‍‌‍​‌‌﻿​﻿‌‍‌‌‌‌‌‌‌﻿​‍‌‍﻿​​﻿﻿‌‌‍‍​‌﻿‌​‌﻿‌​‌﻿​​‌﻿​﻿​‍‌‌​﻿​﻿‌​​‌​‍‌‌​﻿​‍‌​‌‍​‍‌‌​﻿​‍‌​‌‍‌‍​﻿‌‍﻿‌‌﻿​﻿​‍﻿‍‌﻿​﻿‌﻿‌​‌‍​‌‌‍​﻿‌‍‍﻿‌‍﻿﻿‌﻿‌‍‌‍‌‌‌﻿​‍‌‍‌‍‌‍﻿​‌‍﻿﻿‌﻿‌﻿​‍﻿‍‌‍​﻿‌‍﻿﻿​‍‌‍‌‍‍‌‌‍‌​​﻿﻿‌​﻿‌​​﻿‍​​﻿‌﻿​﻿​‍‌‍​﻿‌‍​﻿​﻿‌​‌‍‌‍​‍﻿‌‌‍‌​‌‍‌​​﻿‌‍​﻿​‍​‍﻿‌​﻿‌​‌‍‌‌​﻿‌﻿‌‍​‍​‍﻿‌‌‍​‌‌‍​‌​﻿‌‍‌‍​‍​‍﻿‌‌‍​‍​﻿‍​‌‍‌​​﻿‌‍​﻿‍‌​﻿‍​​﻿‍​​﻿‍‌​﻿‌​‌‍​‍​﻿‌‌​﻿‌‍​‍‌‍‌﻿‌​‌﻿‍‌‌﻿​​‌‍‌‌​﻿﻿‌‌‍​‍‌‍﻿​‌‍﻿﻿‌‍‌﻿‌‌​​‌‍﻿﻿‌﻿​﻿‌﻿‌​​‍‌‍‌﻿​​‌‍​‌‌﻿‌​‌‍‍​​﻿﻿‌‌﻿‌​‌‍‍‌‌﻿‌​‌‍﻿​‌‍‌‌​‍‌‍‌﻿​​‌‍‌‌‌﻿​‍‌﻿​﻿‌﻿​​‌‍‌‌‌‍​﻿‌﻿‌​‌‍‍‌‌﻿‌‍‌‍‌‌​﻿﻿‌‌﻿​​‌﻿‌‌‌‍​‍‌‍﻿​‌‍‍‌‌﻿​﻿‌‍‍​‌‍‌‌‌‍‌​​‍​‍‌﻿﻿‌")

  * [Developers are emotionally attached to their...](https://stackoverflow.blog/2026/06/12/developers-are-emotionally-attached-to-their-tools/ "Developers are emotionally attached to their tools​​​​‌﻿‍﻿​‍​‍‌‍﻿﻿‌﻿​‍‌‍‍‌‌‍‌﻿‌‍‍‌‌‍﻿‍​‍​‍​﻿‍‍​‍​‍‌﻿​﻿‌‍​‌‌‍﻿‍‌‍‍‌‌﻿‌​‌﻿‍‌​‍﻿‍‌‍‍‌‌‍﻿﻿​‍​‍​‍﻿​​‍​‍‌‍‍​‌﻿​‍‌‍‌‌‌‍‌‍​‍​‍​﻿‍‍​‍​‍‌‍‍​‌﻿‌​‌﻿‌​‌﻿​​‌﻿​﻿​﻿‍‍​‍﻿﻿​‍﻿﻿‌‍​﻿‌‍﻿‌‌﻿​﻿​‍﻿‍‌﻿​﻿‌﻿‌​‌‍​‌‌‍​﻿‌‍‍﻿‌‍﻿﻿‌﻿‌‍‌‍‌‌‌﻿​‍‌‍‌‍‌‍﻿​‌‍﻿﻿‌﻿‌﻿​‍﻿‍‌‍​﻿‌‍﻿﻿​‍﻿﻿‌‍‍‌‌‍﻿‍‌﻿‌​‌‍‌‌‌‍﻿‍‌﻿‌​​‍﻿﻿‌‍‌‌‌‍‌​‌‍‍‌‌﻿‌​​‍﻿﻿‌‍﻿‌‌‍﻿﻿‌‍‌​‌‍‌‌​﻿﻿‌‌﻿​​‌﻿​‍‌‍‌‌‌﻿​﻿‌‍‌‌‌‍﻿‍‌﻿‌​‌‍​‌‌﻿‌​‌‍‍‌‌‍﻿﻿‌‍﻿‍​﻿‍﻿‌‍‍‌‌‍‌​​﻿﻿‌‌‍‌‌‌‍‌‌‌‍‌​​﻿​‍‌‍​‍​﻿‌​​﻿‌‍‌‍‌‍​‍﻿‌​﻿​﻿​﻿‌​‌‍​‍​﻿‍​​‍﻿‌​﻿‌​‌‍‌‍‌‍​﻿‌‍​‍​‍﻿‌‌‍​‍​﻿‌‌​﻿‌‌​﻿​‍​‍﻿‌​﻿​‍‌‍​‍‌‍​﻿‌‍​﻿​﻿​‍​﻿‌‌‌‍​﻿​﻿​‌‌‍​﻿‌‍‌‌​﻿‌​​﻿‌​​﻿‍﻿‌﻿‌​‌﻿‍‌‌﻿​​‌‍‌‌​﻿﻿‌‌‍​‍‌‍﻿​‌‍﻿﻿‌‍‌﻿‌‌​​‌‍﻿﻿‌﻿​﻿‌﻿‌​​﻿‍﻿‌﻿​​‌‍​‌‌﻿‌​‌‍‍​​﻿﻿‌‌﻿‌​‌‍‍‌‌﻿‌​‌‍﻿​‌‍‌‌​﻿﻿﻿‌‍​‍‌‍​‌‌﻿​﻿‌‍‌‌‌‌‌‌‌﻿​‍‌‍﻿​​﻿﻿‌‌‍‍​‌﻿‌​‌﻿‌​‌﻿​​‌﻿​﻿​‍‌‌​﻿​﻿‌​​‌​‍‌‌​﻿​‍‌​‌‍​‍‌‌​﻿​‍‌​‌‍‌‍​﻿‌‍﻿‌‌﻿​﻿​‍﻿‍‌﻿​﻿‌﻿‌​‌‍​‌‌‍​﻿‌‍‍﻿‌‍﻿﻿‌﻿‌‍‌‍‌‌‌﻿​‍‌‍‌‍‌‍﻿​‌‍﻿﻿‌﻿‌﻿​‍﻿‍‌‍​﻿‌‍﻿﻿​‍‌‍‌‍‍‌‌‍‌​​﻿﻿‌‌‍‌‌‌‍‌‌‌‍‌​​﻿​‍‌‍​‍​﻿‌​​﻿‌‍‌‍‌‍​‍﻿‌​﻿​﻿​﻿‌​‌‍​‍​﻿‍​​‍﻿‌​﻿‌​‌‍‌‍‌‍​﻿‌‍​‍​‍﻿‌‌‍​‍​﻿‌‌​﻿‌‌​﻿​‍​‍﻿‌​﻿​‍‌‍​‍‌‍​﻿‌‍​﻿​﻿​‍​﻿‌‌‌‍​﻿​﻿​‌‌‍​﻿‌‍‌‌​﻿‌​​﻿‌​​‍‌‍‌﻿‌​‌﻿‍‌‌﻿​​‌‍‌‌​﻿﻿‌‌‍​‍‌‍﻿​‌‍﻿﻿‌‍‌﻿‌‌​​‌‍﻿﻿‌﻿​﻿‌﻿‌​​‍‌‍‌﻿​​‌‍​‌‌﻿‌​‌‍‍​​﻿﻿‌‌﻿‌​‌‍‍‌‌﻿‌​‌‍﻿​‌‍‌‌​‍‌‍‌﻿​​‌‍‌‌‌﻿​‍‌﻿​﻿‌﻿​​‌‍‌‌‌‍​﻿‌﻿‌​‌‍‍‌‌﻿‌‍‌‍‌‌​﻿﻿‌‌﻿​​‌﻿‌‌‌‍​‍‌‍﻿​‌‍‍‌‌﻿​﻿‌‍‍​‌‍‌‌‌‍‌​​‍​‍‌﻿﻿‌")

  * Featured on Meta 
  * [Native Ads Coming To Comments](https://meta.stackexchange.com/questions/418563/native-ads-coming-to-comments)

  * [Policy: Generative AI (e.g., ChatGPT) is banned](https://meta.stackoverflow.com/questions/421831/policy-generative-ai-e-g-chatgpt-is-banned)

  * [Help Shape the 2026 Developer Survey!](https://meta.stackoverflow.com/questions/438884/help-shape-the-2026-developer-survey)




### Linked

[ 0 ](https://stackoverflow.com/questions/44718760/where-the-node-capabilities-are-stored-in-kubernetes "Question score \(upvotes - downvotes\)") [Where the node capabilities are stored in kubernetes](https://stackoverflow.com/questions/44718760/where-the-node-capabilities-are-stored-in-kubernetes?noredirect=1)

### Related

[ 3 ](https://stackoverflow.com/questions/48529337/kubernetes-job-scheduling-api "Question score \(upvotes - downvotes\)") [Kubernetes - Job scheduling API](https://stackoverflow.com/questions/48529337/kubernetes-job-scheduling-api)

[ 0 ](https://stackoverflow.com/questions/53440923/how-kubernetes-does-scheduling-and-deploying-of-pods "Question score \(upvotes - downvotes\)") [How kubernetes does scheduling and deploying of pods?](https://stackoverflow.com/questions/53440923/how-kubernetes-does-scheduling-and-deploying-of-pods)

[ 4 ](https://stackoverflow.com/questions/54820777/k8s-how-scheduler-assigns-the-nodes "Question score \(upvotes - downvotes\)") [k8s - how scheduler assigns the nodes](https://stackoverflow.com/questions/54820777/k8s-how-scheduler-assigns-the-nodes)

[ 0 ](https://stackoverflow.com/questions/55336552/resource-allocation-in-kubernetes-how-are-pods-scheduled "Question score \(upvotes - downvotes\)") [Resource Allocation in Kubernetes: How are pods scheduled?](https://stackoverflow.com/questions/55336552/resource-allocation-in-kubernetes-how-are-pods-scheduled)

[ 0 ](https://stackoverflow.com/questions/56676572/how-scheduler-talks-to-api-server "Question score \(upvotes - downvotes\)") [How scheduler talks to API server?](https://stackoverflow.com/questions/56676572/how-scheduler-talks-to-api-server)

[ 1 ](https://stackoverflow.com/questions/62943925/kubernetes-scheduler-extenders-when-are-they-invoked "Question score \(upvotes - downvotes\)") [Kubernetes Scheduler Extenders - when are they invoked?](https://stackoverflow.com/questions/62943925/kubernetes-scheduler-extenders-when-are-they-invoked)

[ 3 ](https://stackoverflow.com/questions/64260771/how-does-the-kubernetes-api-server-start-a-newly-scheduled-pod-on-a-node "Question score \(upvotes - downvotes\)") [How does the Kubernetes API server start a newly scheduled pod on a node?](https://stackoverflow.com/questions/64260771/how-does-the-kubernetes-api-server-start-a-newly-scheduled-pod-on-a-node)

[ 1 ](https://stackoverflow.com/questions/67099378/clarification-on-kubernetes-qos-relation-to-scheduling "Question score \(upvotes - downvotes\)") [Clarification on Kubernetes QoS relation to scheduling](https://stackoverflow.com/questions/67099378/clarification-on-kubernetes-qos-relation-to-scheduling)

[ 2 ](https://stackoverflow.com/questions/69389043/kubernetes-scheduler "Question score \(upvotes - downvotes\)") [Kubernetes scheduler](https://stackoverflow.com/questions/69389043/kubernetes-scheduler)

[ 2 ](https://stackoverflow.com/questions/70105320/what-is-the-relationship-between-scheduling-policies-and-scheduling-configuratio "Question score \(upvotes - downvotes\)") [What is the relationship between scheduling policies and scheduling Configuration in k8s](https://stackoverflow.com/questions/70105320/what-is-the-relationship-between-scheduling-policies-and-scheduling-configuratio)

####  [ Hot Network Questions ](https://stackexchange.com/questions?tab=hot)

  * [ Magnet in Young Female Passenger's Belongings Disrupts Plane's Compass ](https://movies.stackexchange.com/questions/132009/magnet-in-young-female-passengers-belongings-disrupts-planes-compass)
  * [ What material and/or process should I use to attach glazed tile to kitchen drywall? ](https://diy.stackexchange.com/questions/330871/what-material-and-or-process-should-i-use-to-attach-glazed-tile-to-kitchen-drywa)
  * [ I'd like to use a recent version of bash as my login shell in macos ](https://apple.stackexchange.com/questions/486579/id-like-to-use-a-recent-version-of-bash-as-my-login-shell-in-macos)
  * [ Has my interdisciplinary background hurt my math writing? ](https://academia.stackexchange.com/questions/226940/has-my-interdisciplinary-background-hurt-my-math-writing)
  * [ Where should I put the cheese? ](https://puzzling.stackexchange.com/questions/138481/where-should-i-put-the-cheese)
  * [ Journal is asking us for proof of collaboration after submitting paper with multiple affiliations ](https://academia.stackexchange.com/questions/226926/journal-is-asking-us-for-proof-of-collaboration-after-submitting-paper-with-mult)
  * [ What denominations teach about other denomination's beliefs? ](https://christianity.stackexchange.com/questions/114062/what-denominations-teach-about-other-denominations-beliefs)
  * [ Exponent that makes minimal polynomial of Frobenius a Weil polynomial ](https://mathoverflow.net/questions/512222/exponent-that-makes-minimal-polynomial-of-frobenius-a-weil-polynomial)
  * [ Regression on oddly-structured truncated data ](https://stats.stackexchange.com/questions/676236/regression-on-oddly-structured-truncated-data)
  * [ Translating Russian color terms сизый / голубой: strategies for colors without direct English equivalents ](https://english.stackexchange.com/questions/639901/translating-russian-color-terms-%d1%81%d0%b8%d0%b7%d1%8b%d0%b9-%d0%b3%d0%be%d0%bb%d1%83%d0%b1%d0%be%d0%b9-strategies-for-colors-without-d)
  * [ Best way to view a 3.3V 80MHz clock on a scope? ](https://electronics.stackexchange.com/questions/769786/best-way-to-view-a-3-3v-80mhz-clock-on-a-scope)
  * [ I can't get correct distance in Proj using proj_geod() ](https://gis.stackexchange.com/questions/500953/i-cant-get-correct-distance-in-proj-using-proj-geod)
  * [ My postdoc project starts to feel like an impossible task. What do I do? ](https://academia.stackexchange.com/questions/226942/my-postdoc-project-starts-to-feel-like-an-impossible-task-what-do-i-do)
  * [ Can I use Mann-Whitney U test with repeated measurements across time (non-independent samples in cohorts)? ](https://stats.stackexchange.com/questions/676216/can-i-use-mann-whitney-u-test-with-repeated-measurements-across-time-non-indepe)
  * [ Ghost Protocol: Hunt the Invisible Alien ](https://puzzling.stackexchange.com/questions/138490/ghost-protocol-hunt-the-invisible-alien)
  * [ Natural transformations between metric spaces ](https://math.stackexchange.com/questions/5140259/natural-transformations-between-metric-spaces)
  * [ Another Catan longest road question ](https://boardgames.stackexchange.com/questions/64518/another-catan-longest-road-question)
  * [ Does this introduce tight coupling? ](https://softwareengineering.stackexchange.com/questions/461249/does-this-introduce-tight-coupling)
  * [ Custom optional parameters for classes in LaTeX ](https://tex.stackexchange.com/questions/763607/custom-optional-parameters-for-classes-in-latex)
  * [ What was the first game with a Wanted system? ](https://gaming.stackexchange.com/questions/419002/what-was-the-first-game-with-a-wanted-system)
  * [ Is the difficulty of pinning down conscious experience evidence of eliminative materialism? ](https://philosophy.stackexchange.com/questions/138984/is-the-difficulty-of-pinning-down-conscious-experience-evidence-of-eliminative-m)
  * [ крылатый meaning in context ](https://russian.stackexchange.com/questions/30292/%d0%ba%d1%80%d1%8b%d0%bb%d0%b0%d1%82%d1%8b%d0%b9-meaning-in-context)
  * [ Details of IAS seminar on Monstrous Moonshine ](https://mathoverflow.net/questions/512188/details-of-ias-seminar-on-monstrous-moonshine)
  * [ Straightening out bent/bulging transparencies ](https://photo.stackexchange.com/questions/138544/straightening-out-bent-bulging-transparencies)

more hot questions 

[ Question feed ](https://stackoverflow.com/feeds/question/28857993 "Feed of this question and its answers")

#  Subscribe to RSS 

Question feed 

To subscribe to this RSS feed, copy and paste this URL into your RSS reader.

![](https://stackoverflow.com/posts/28857993/ivc/faa9?prg=aa501bcf-ca68-4db0-8c6f-ab8f4da52f72)

lang-yaml

[](https://stackoverflow.com)

##### [Stack Overflow](https://stackoverflow.com)

  * [Questions](https://stackoverflow.com/questions)
  * [Help](https://stackoverflow.com/help)
  * [Chat](https://chat.stackoverflow.com/?tab=explore)



##### [Business](https://stackoverflow.co/)

  * [Stack Internal](https://stackoverflow.co/internal/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=footer&utm_content=teams)
  * [Stack Data Licensing](https://stackoverflow.co/data-licensing/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=footer&utm_content=data-licensing)
  * [Stack Ads](https://stackoverflow.co/advertising/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=footer&utm_content=advertising)



##### [Company](https://stackoverflow.co/)

  * [About](https://stackoverflow.co/)
  * [Press](https://stackoverflow.co/company/press/)
  * [Work Here](https://stackoverflow.co/company/work-here/)
  * [Legal](https://stackoverflow.com/legal)
  * [Privacy Policy](https://stackoverflow.com/legal/privacy-policy)
  * [Terms of Service](https://stackoverflow.com/legal/terms-of-service/public)
  * [Contact Us](https://stackoverflow.com/contact)
  * Your Privacy Choices 
  * [Cookie Policy](https://policies.stackoverflow.co/stack-overflow/cookie-policy)



##### [Stack Exchange Network](https://stackexchange.com)

  * [ Technology ](https://stackexchange.com/sites#technology)
  * [ Culture & recreation ](https://stackexchange.com/sites#culturerecreation)
  * [ Life & arts ](https://stackexchange.com/sites#lifearts)
  * [ Science ](https://stackexchange.com/sites#science)
  * [ Professional ](https://stackexchange.com/sites#professional)
  * [ Business ](https://stackexchange.com/sites#business)
  * [ API ](https://api.stackexchange.com/)
  * [ Data ](https://data.stackexchange.com/)



  * [Blog](https://stackoverflow.blog?blb=1)
  * [Facebook](https://www.facebook.com/officialstackoverflow/)
  * [Twitter](https://twitter.com/stackoverflow)
  * [LinkedIn](https://linkedin.com/company/stack-overflow)
  * [Instagram](https://www.instagram.com/thestackoverflow)



Site design / logo © 2026 Stack Exchange Inc;  user contributions licensed under  [CC BY-SA](https://stackoverflow.com/help/licensing) .  rev 2026.6.12.43530
