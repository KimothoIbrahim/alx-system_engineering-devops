Hey fellows, We Had an Outage! 😂

The following postmortem describes an outage we experienced with our api infrastructure and how we resolved it.


Issues summary:

At 11:37 am to 1:15 pm EAT we experienced an issue with our API with many of our users reporting 500 error response messages.  The outage stemmed from an enormous uptake of our API with hits increasing by 427%. This was way beyond what our current infrastructure can handle.


Timeline [all in East African Time]:

At 11:37 am: users reported difficulty accessing API
At 11:42 am: pager alerted teams
At 12:54 pm: server clones were deployed
At 1:15 pm: services were restored to the new capacity.


Route Cause:

At 11:37 am EAT our two servers began receiving more than normal traffic. Regular users reported having to wait longer than is typical and making repeated calls to the api so as to complete previously simple calls. 

Resolution and recovery:

At 11:42 am EAT monitoring systems picked up on customer reports and alerted our engineers who quickly investigated and escalated the issue. By 12:54 pm the team identified the issue as one of excess traffic and deployed server clones to deal with the extra traffic. By 1:15pm everything was running smoothly.

Corrective and preventive measures:

We have conducted literal review and analysis of the issue. The following are actions we are taking to avert a recurrence of the issue

Institute a monitoring tool to regularly check server hits vis-a-vis the current server capacity.
Automate server deployment whe server hits surpass the current infrastructural capacity.

