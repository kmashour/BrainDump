
apiVersion: v1

kind: PersistentVolumeClaim

metadata:

  annotations:

    kubectl.kubernetes.io/last-applied-configuration: |

      {"apiVersion":"v1","kind":"PersistentVolumeClaim","metadata":{"annotations":{},"name":"claim-log-1","namespace":"default"},"spec":{"accessModes":["ReadWriteOnce"],"resources":{"requests":{"storage":"50Mi"}}}}

  creationTimestamp: "2026-07-11T12:33:39Z"

  finalizers:

  - kubernetes.io/pvc-protection

  name: claim-log-1

  namespace: default

  resourceVersion: "4645"

  uid: b7123459-9693-496e-bb61-45972ad1a65f

spec:

  accessModes:

  - ReadWriteOnce

  resources:

    requests:

      storage: 50Mi

  volumeMode: Filesystem

status:

  phase: Pending



apiVersion: v1

items:

- apiVersion: v1

  kind: PersistentVolume

  metadata:

    annotations:

      kubectl.kubernetes.io/last-applied-configuration: |

        {"apiVersion":"v1","kind":"PersistentVolume","metadata":{"annotations":{},"name":"pv-log"},"spec":{"accessModes":["ReadWriteMany"],"capacity":{"storage":"100Mi"},"hostPath":{"path":"/pv/log"},"persistentVolumeReclaimPolicy":"Retain"}}

    creationTimestamp: "2026-07-11T12:23:37Z"

    finalizers:

    - kubernetes.io/pv-protection

    name: pv-log

    resourceVersion: "3862"

    uid: 4ff66e23-723b-4ea2-9753-f45285513268

  spec:

    accessModes:

    - ReadWriteMany

    capacity:

      storage: 100Mi

    hostPath:

      path: /pv/log

      type: ""

    persistentVolumeReclaimPolicy: Retain

    volumeMode: Filesystem

  status:

    lastPhaseTransitionTime: "2026-07-11T12:23:37Z"

    phase: Available

kind: List

metadata:

  resourceVersion: ""





In this example the Reclaim policy is set in the PV and not the PVC and the only flagged issue is the access mode when I fixed it worked what Iam asking is shouldn't the pv and pvc have the same parameters ? 

It is a very logical assumption to think that the PV and PVC should be exact identical mirrors of each other, but in Kubernetes, they actually serve two different roles.

The easiest way to understand it is to think of the PV as the physical hardware (managed by the Administrator) and the PVC as a voucher or request (created by the Developer).

Here is exactly why they do not need identical parameters, and why fixing the access mode was the only thing required to make your binding work.

1. The Reclaim Policy Belongs ONLY to the PV
You noted that the persistentVolumeReclaimPolicy is set on the PV and not the PVC. This is by design.

The PVC doesn't care what happens to the hard drive after it is done using it.

The Reclaim Policy is strictly an instruction for the cluster administrator: "When the user deletes their PVC, what should the cluster do with this hard drive? Should we Retain the data, or Delete the disk entirely?" Because it is a hardware lifecycle rule, it only exists on the PV.

2. Capacity: The PVC is a "Minimum Requirement"
You might have noticed that your PVC requested 50Mi, but the PV had 100Mi.

They do not need to be exactly the same size.

A PVC is essentially asking the cluster: "Find me a drive that is at least 50Mi." * Since the 100Mi PV satisfies that minimum requirement, Kubernetes happily binds them together. (Note: The PVC will lock up the entire 100Mi PV. You cannot bind two 50Mi PVCs to a single 100Mi PV).

3. Access Modes: The Strict Match
This is why your binding failed initially.

Your PVC explicitly demanded a volume that supports ReadWriteOnce (can be mounted by a single node).

Your PV was advertised as ReadWriteMany (can be mounted by many nodes).

Even though ReadWriteMany sounds "better," Kubernetes is very strict about matching these modes. The PV's advertised access modes must exactly contain what the PVC is requesting. Once you aligned these, the cluster saw a PV that was big enough and had the right access rights, so it bound them.

Summary of the Binding Rules
For a PVC to successfully bind to a PV, here is what actually matters:

Parameter	Does it have to match exactly?	The Rule
Capacity	NO	PV capacity must be ≥ PVC request.
Access Mode	YES	PV must support the exact mode the PVC requests.
Storage Class	YES	If the PVC asks for storageClassName: slow, the PV must be slow. (If left blank, both must be blank).
Reclaim Policy	NO	Exists only on the PV.