# What is SRE
- Keep large scale system reliable.
0 Measure / Analyze / Decide/ Act / Rellect
- Measure - 
- Basic stat and probablity

# Golden signals
- Latency - the time it takes to serve a request
- Traffic - 
- Errors - define the rate of requests that are failing
- Saturation - the over capacity of the system (Utilization)
 
# SRE
- SLI - service level indicator. From user prespective.
- SLO - service level objective. Target on how often you want them to be operating.
- Error budget - how did you performed against your target. Foundation for preparing for incidents.
- Realibility - system behaving as expected.
- Availbility - the amount of time a service is usable.
- 99 percent latency below one second.
- How to improve resiliance:
  - Load reduction
        - Throttling, load shedding/prioritization, queuing, load balancing
    Latency reduction
        - Caching, regional replication
    Load adaptation
        - Autoscaling, overprovisioning
    Resilience (specifically)
        - Timeouts, circuit breakers, bulkheads, retries, failovers, fallbacks
    Meta-techniques
        - Improving tooling, perhaps to scale up or fail over faster; especially impactful in cases when slow humans are in a system’s critical path
- Relationship between request rate and latency - saturated system.
- We can load balance to balance request rate, or load shading.
- Merge the code, fire pipeline,
-  Observability operates on the order of systems, not on the order of functions.
-  Observability is for figuring out where in your systems to find the code you need to debug
- Wikipedia
  - CDN - regional DNS
  - Each datacenter has two caching layer. If not cached forward to app server.
  - Application Layer
  - Open source software
  - Lot of caching layer
- Need a control plane to control the system during outage. Seperate from data plane.
- Seperate requests into management layer and data layer.
- Distributed storage system
- Security
  - MDM / Device encryption
     
# Infrastructure as code
    - Infrastructure as code in test file.
    - AWS, networking, caches, managed database.
    - Trace problem
    - Used branches for infra project     
# Immutable infrastructure
    - Stop changing infra in production
    - Build artifacts - images.
    - Assure that the thing in config is what in your test env.
    - Functionaly test your whole infrastructure as a unit.
    - Leading to pipeline thinking. 
    - Because you are bringing static artifacts. Leads to pipeline thinking. 
# Scheduler
    - Kubernetes.
# Devops
    - Bridging the gap between dev ( code / build / release)
    - Ops (Deploy / Monitor / Operate) .
# SRE
    Resilance big system.
    Software is robustly build.
    SRE - used software engineer practice
    Build tools to simplify processes.
# Nana Tech
    - SRE , Devops person that keeps system realibiale. 
    - Treat operation as software.
    - SRE build software to build realibility of the system. 
## System
    - server
    - database
    - disk
## Realibility
    - E.g. email system that is down. 
    - User do not notice relaibility of the system. 
    - More the team should worry about realibity. 
    - Traffic overload.
## How to make system realiable
    - When you make changes to your system (change in the service) - 
    - Want to make changes (stay competitive) . By software dev.
    - But app need to be accessibile.
    - Dev make a change -> Ops manual testing. Slow down the release process.
    - SRE automate the process of evaluating the affect of change. Automating process. 
# SLA
    - How relabile a systen will be to end user
    - Express as 100% Avaibility 
    - Achieve 100% is difficult. 
    - 99.9
    - 9999.9 Availbility
    - Agreement . 99 percent, system can be done max 3.65 days in a year. The rest of the time it should work.
    - 1M Req / week. 
    - Who define SLA? Business pepole.  Engineer define them in technical level.
    - How much down time is allowed. 
## Error budget 
    - Downtime
    - allow to have that much downtime, 
    - SLA is a parameters. 
    - More resource, Until the system is recovered. Turn Up SLA/ Release will slow down

## SRE Task
    - Code -> Test - > Build -> Evaluate an SLA -> Proper monitoring of the system
    - Configure proper monitoring and logging.
    - At some point we will have an outage. 
    - Monitoring , Logging and Alerting. Detect issues  + Alerts
    - When the issue is alerts, the alert message should contain all the needed information. 
    - On call support. 

# Who is doing SRE
    - Both teams work at the same goal.
    - SRE team take care of automation.

# 
The secret to success is availbiility 
- SLA - agreement with users. 99% of time, 1 seconds. Promise
- SLO - With SLO every promise define the objective within your team . Goal within your team. SLO > SLA. 
- SLI - Actual performance of the service.

# SRE Course
Design your system for desired level of relibility.
## SRE Process
- Service level indicator , objective , agreements.
- Monitoring and observability
- On call 
- Incident response
- Post incident review
- Automation
- Devops - imporve software deliveiry. SRE - achive realibility. 
- SRE , care about SLO.
- SLO - The 95% of request in the last 7 day under 200 ml
- SLO < SLA , external 

# Release engineering
- Feature flag
- Blue / Green
- CI/CD
- Small changes
- Canary release 

# Monitoring and observability
- Multi dimension 
- time / app / host / user /endpoint / status. (all 502 errors that occur in the last hour)
- an event is a record of everything that occurred while one particular request interacted with your service.
- Metric - scalar values collected to represent system state, with tags optionally appended
- , the fundamental limitation of a metric is that it is a pre-aggregated measure
- In an event-based approach, a web server request could be instrumented to record each parameter (or dimension) submitted with the request (for example, userid), the intended subdomain (www, docs, support, shop, cdn, etc.), total duration time, any dependent child requests, 
  the various services involved (web, database, auth, billing) to fulfill those child requests, the duration of each child request, and more
- Tracing is a fundamental software debugging technique wherein various bits of information are logged throughout 
  a program’s execution for the purpose of diagnosing problems
- Distributed tracing is a method of tracking the progression of a 
  single request—called a trace—as it is handled by various services that make up an application.
- 