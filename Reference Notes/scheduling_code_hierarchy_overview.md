---
domains:
  - "kubernetes"
  - "scheduling"
---

# Scheduler Code Hierarchy Overview

**Source:** https://github.com/kubernetes/community/blob/master/contributors/devel/sig-scheduling/scheduling_code_hierarchy_overview.md

## Introduction

The scheduler watches for newly created Pods that have no Node assigned.
For every Pod that the scheduler discovers, the scheduler becomes responsible
for finding the best Node for that Pod to run on.
Scheduling in general is quite an extensive field in computer science which takes
into account various range of constraints and limitations.
Each workload may require a different approach to achieve optimal scheduling results.
To help in building a scheduler (the default or a custom one) and to share
elements of the scheduling logic,
[the scheduling framework](https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/)
was implemented.
The framework does not provide all pieces to build a new scheduler from scratch.
Queues, caches, scheduling algorithms and other building elements are still needed to assemble
a fully functional unit. This document aims at describing how all the individual
pieces are put together and what’s their role in the overall architecture
so a developer can quickly orient in the code.

## Scheduling a pod

The default scheduler instance has a loop running indefinitely
which (every time there’s a pod) is responsible for invoking the scheduling logic
and making sure a pod gets either a node assigned or requeued for future processing.
Each loop consists of a blocking scheduling and a non-blocking binding cycle.
The scheduling cycle is responsible for running the scheduling algorithm selecting
the most suitable node for placing the pod.
The binding cycle makes sure the kube-apiserver is made aware of the selected
node at the right time. A pod may be bound immediately, or in the case of gang scheduling,
wait until all its sibling pods have their node assigned.

### Scheduling cycle

Each cycle honors the following steps:
1. Get the next pod for scheduling
2. Schedule a pod with provided algorithm
3. If a pod fails to be scheduled due to `FitError`, run preemption plugin in
   `PostFilterPlugin` (if the plugin is registered) to nominate a node where
   the pods can run. If preemption was successful,
   let the current pod be aware of the nominated node.
   Handle the error, get the next pod and start over.
4. If the scheduling algorithm finds a suitable node, store the pod into
   the scheduler cache (`AssumePod` operation) and run plugins from the `Reserve`
   and `Permit` extension point in that order. In case any of the plugins fails,
   end the current scheduling cycle, increase relevant metrics and handle
   the scheduling error through the `Error` handler.
5. Upon successfully running all extension points, proceed to the binding cycle.
   At the same time start processing another pod (if there’s any).

### Binding cycle

Consists of the following four steps ran in the same order:
- Invoking `WaitOnPermit` (internal API) of plugins from `Permit` extension point. Some plugins from the extension point
  may send a request for an operation requiring to wait for a condition
  (e.g. wait for additional resources to be available or wait for all pods
  in a gang to be assumed).
  Under the hood, `WaitOnPermit` waits for such a condition to be met within a timeout threshold.
- Invoking plugins from `PreBind` extension point.
- Invoking plugins from `Bind` extension point.
- Invoking plugins from `PostBind` extension point.

In case of processing of any of the extension points fails, `Unreserve` operation
of all `Reserve` plugins is invoked (e.g. free resources allocated for a gang of pods).

## Configuring and assembling the scheduler

The scheduler codebase spans across various locations:
- `cmd/kube-scheduler/app`: location of the controller code alongside definition of CLI arguments (honors the standard setup for all Kubernetes controllers)
- `pkg/scheduler`: the default scheduler codebase root directory
- `pkg/scheduler/core`: location of the default scheduling algorithm
- `pkg/scheduler/framework`: scheduling framework alongside plugins
- `pkg/scheduler/internal`: implementation of the cache, queues and other internal elements
- `staging/src/k8s.io/kube-scheduler`: location of ComponentConfig API types
- `test/e2e/scheduling`: scheduling e2e
- `test/integration/scheduler`: scheduling integration tests
- `test/integration/scheduler_perf`: scheduling performance benchmarks
