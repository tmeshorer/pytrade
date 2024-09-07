- Company:
  - Core database as time series data.
  - Original in golang.
  - Learned from deploying 1.x in production, go garbage collection. 
  - Figure way around the garbage . scale behind 1.x can handle. 
  - Design completly different.
  - Askiing small , 10x amount of data , series cardianlity. 
  - 100x scale. Resign it and lang of avail. 
  - Go , Rust not mature, influx product . 
  - Go ofcourse, time series database,right time to choose more powerfull system lang.
  - C++, Rwote it rust, completly in rust, redesign. 
  - Default is in rust. When in doubt do Riust.
  - Core of database , Rust 
  - Two team:
    - query time
    - write team - ingestion.
  - Assemble them into a product. 
  - 4 tiers:
    - Two cloud : multi tenant - entry level.
    - Dedicated : single tenant cloud.
    - Cluserted : clustered team. on prem version of it. own AWS, own GKE.
    -   Take core component, turn it on prem product.
    -   Need licensing, build the licensing bit, server in rust, that manage licensing. 
    -   K8S operator, talk to licensing server, to retrieve licenses.
    -   Modified the query engine to enforce the licesne. 
    -   Lines get blured. Those kind of team that engineering product team do.
    - Single server version - monolotityh. influx db open source, influx db pro. 
    - Pro version have scaling feature - multiple instance of pro. as read replicas.
    - Intent much simpler product, no k8s involve. cluster no run on single server.
    - On the clustered team. Most of team 4-8 pepole. Clustered team has five pepole.
    - Engineer is transferring. 5 pepole. 
    - Clustered team:
      - 1) Interface with customer, lots of developement, prefemonace gaps. 
        2) Work trough install issues, pain points,
        3) Configuration auth, with identity provider, not 
        4) Does this thing handle query load, write load,
        5) Make product easier to install, disabling auth. 
        6) Work with k8s, troubleshoot installation, preformance issue with queries.
        7) 70% k8s work
        8) 30% writing code. 
        9) Long term goal, doing more code, less kubernetes. 