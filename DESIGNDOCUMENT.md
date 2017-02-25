# Design Doc

The app is split into microservices

- User management
    * Keeps track of all user data, auth and ratings.
- Dispatcher
    * Has all the logic about matching a rider to a captain.
    * All the data needed to make the decision would be pushed to the dispatcher.
- Geo tracker
    * Location tracking of user(riders and captains)
    * Different geo queries 
        + Distance between points (spherical distance)
        + Route distance between points (Actual distance by road, measure of time)


### User Mangement
This would be pretty much a HTTP-REST service doing crud operations, the scale wont be very high so a normal mysql schema based store would be able to handle it.


### Dispatcher and Geo tracker
Both of the services would have to handle large number of concurrent requests and serve responses at a very high scale. 
A event loop driven strategy should be better here. Node is a good choice to handle workloads like these.
As a data store we would like to go with a combination of postgres(awesome at handling geo queries) and a key value store like redis/riak to store the dispatcher state.
The postgres database can be partitioned easily on the basis of location to make the indexing and searching faster.
A cache can be used to store the drivers in a geo-hash by key as the geo-hash. All results can be coalated by querying a geo hash(decide on the radius threshold) redis seems to be the right choice given the already geoquery rich eco system.

#### Dispatching Logic
Dispatcher would obviously need to take in geo locations of the captain and the rider, apart from this mutltiple attributes like
 - Rating of driver and rider
 - Preferences of driver like cash rides etc can be also taken in account

#### Geo tracker
The system in ideal condition needs to know about the actual location of captain to match riders.
The captain's device can send the location every few seconds(4-5s) to the system, as failover each location hit can also be augmented with a acceleration vector which could be used in cases where the driver location hasnt been updated for some time(10-20secs).
The service most under load should be dispatcher and the geo tracking system.
Handling large scale(2mil captains). The device would only send a request if the vehicle is moving. Considering a node process can handle about 10-20k req/s and running the application on a quad core machine the system should scale to 2 mil request by having around 50 machines(obviously this wont be static as load can vary by time.)

### Infrastructure
All of these services(ideally wrapped in a container) can be deployed on instances load balanced by a l-4 LB. Dealing with microservices service discovery can be done through traditional methods easily.

Since ride booking is not constant all the time a autoscaling architecture seems to be the right way going ahead. 
The ASG(using AWS terminology) should be able to scale on characterstics like connections and cpu utilizations.



