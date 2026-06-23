
Working with ETCDCTL and ETCDUTL

#### WORKING WITH ETCDCTL & ETCDUTL

`**etcdctl**` is a command line client for [**etcd**](https://github.com/coreos/etcd).  
In all our Kubernetes hands-on labs, the ETCD key-value database is deployed as a static pod on the master. The version used is v3.

To make use of `**etcdctl**` for tasks such as backup, verify it is running on API version 3.x:

1. etcdctl version

Example:

1. controlplane ~ ➜  etcdctl version
2. etcdctl version: 3.5.16
3. API version: 3.5

#### Backing Up ETCD

#### Using `**etcdctl**` (Snapshot-based Backup)

To take a snapshot from a running etcd server, use:

1. ETCDCTL_API=3 etcdctl \
2.   --endpoints=https://127.0.0.1:2379 \
3.   --cacert=/etc/kubernetes/pki/etcd/ca.crt \
4.   --cert=/etc/kubernetes/pki/etcd/server.crt \
5.   --key=/etc/kubernetes/pki/etcd/server.key \
6.   snapshot save /backup/etcd-snapshot.db

#### Required Options

- `**--endpoints**` points to the etcd server (default: localhost:2379)
    
- `**--cacert**` path to the CA cert
    
- `**--cert**` path to the client cert
    
- `**--key**` path to the client key
    

#### Using `**etcdutl**` (File-based Backup)

For offline file-level backup of the data directory:

1. etcdutl backup \
2.   --data-dir /var/lib/etcd \
3.   --backup-dir /backup/etcd-backup

This copies the etcd backend database and WAL files to the target location.

#### Checking Snapshot Status

You can inspect the metadata of a snapshot file using:

1. etcdctl snapshot status /backup/etcd-snapshot.db \
2.   --write-out=table

This shows details like size, revision, hash, total keys, etc. It is helpful to verify snapshot integrity before restore.

#### Restoring ETCD

#### Using `**etcdutl**`

To restore a snapshot to a new data directory:

1. etcdutl snapshot restore /backup/etcd-snapshot.db \
2.   --data-dir /var/lib/etcd-restored

To use a backup made with `**etcdutl backup**`, simply copy the backup contents back into `**/var/lib/etcd**` and restart etcd.

#### Notes

- `**etcdctl snapshot save**` is used for creating `**.db**` snapshots from live etcd clusters.
    
- `**etcdctl snapshot status**` provides metadata information about the snapshot file.
    
- `**etcdutl snapshot restore**` is used to restore a `**.db**` snapshot file.
    
- `**etcdutl backup**` performs a raw file-level copy of etcd’s data and WAL files without needing etcd to be running.