# Book a ride 


The application is split into microservices

- User management
    * Keeps track of all user data, auth and ratings. Ratings would be calculated on the basis of feedback given by a rider & captain.
- Dispatcher
    * Has all the logic about matching a rider to a captain. Rider would be matched on the basis of nearby captains and the type of cab request from user.
    * All the data needed to make the decision would be pushed to the dispatcher.
- Geo tracker
    * Location tracking of user(riders and captains). The captain's device can send the location every few seconds(4-5s) to the system, as failover each location hit can also be augmented with a acceleration vector which could be used in cases where the driver location hasnt been updated for some time(10-20secs). The service most under load should be dispatcher and the geo tracking system.
    * Different geo queries 
        + Distance between points (spherical distance)
        + Route distance between points (Actual distance by road, measure of time)