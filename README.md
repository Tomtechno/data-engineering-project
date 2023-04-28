# US Accidents (2016 - 2021)
A Countrywide Traffic Accident Dataset (2016 - 2021)

![Car accident](https://user-images.githubusercontent.com/69020112/235061206-d1b063b6-147d-4be3-8dc4-db6ea9c50eb5.jpg)

An estimated 42,915 people died in car crashes in the United States in 2021, a 10.5% increase from 2020. Knowing about car accidents in the USA is important for several reasons:

* Public safety: Understanding the causes and trends of car accidents can help policymakers and law enforcement officials take steps to reduce the frequency and severity of accidents. This can help to make the roads safer for all drivers, passengers, and pedestrians.

* Economic impact: Car accidents can have a significant economic impact, both in terms of medical expenses and lost productivity. By understanding the costs associated with accidents, policymakers can make informed decisions about how to allocate resources to prevent and respond to accidents.

* Insurance rates: Insurance companies use data on car accidents to set rates for drivers. Knowing the frequency and severity of accidents can help insurers to accurately price their policies, which can benefit drivers in the long run.

* Traffic planning: Data on car accidents can also inform traffic planning decisions, such as where to place traffic signals, speed limits, and other traffic control measures. This can help to reduce congestion and improve traffic flow, which can benefit drivers and communities.

Overall, understanding the trends and patterns of car accidents in the USA is essential for promoting public safety, supporting economic growth, and improving the quality of life for all Americans.


In the following link you can dive into the United States driving statistics.
- [Driving statistics](https://driving-tests.org/driving-statistics/)

## Dataset acknowledgements 
* Moosavi, Sobhan, Mohammad Hossein Samavatian, Srinivasan Parthasarathy, and Rajiv Ramnath. “A Countrywide Traffic Accident Dataset.”, 2019.

* Moosavi, Sobhan, Mohammad Hossein Samavatian, Srinivasan Parthasarathy, Radu Teodorescu, and Rajiv Ramnath. "Accident Risk Prediction based on Heterogeneous Sparse Data: New Dataset and Insights." In proceedings of the 27th ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems, ACM, 2019.

[To acces the dataset click here](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents)


## Structure of the production table
In order to have a good performance I got rid of the unnecesary features. 
| # |Feature              |Description                                         |
|---|---------------------|-----------------------------------------------------|
| 1 | ID                  | Identifier of the accident record                   |
| 2 | Severity            | Shows the severity of the accident                  |
| 3 | Start time          | Shows start time of the accident in local time zone |
| 4 | End time            | Shows end time of the accident in local time zone   |
| 5 | Description         | Shows a human provided description of the accident  |
| 6 | State               | Shows the state in address field                    |
| 7 | Weather conditions  | Shows the weather condition                         |


## Tools & Technology
- Infrastructure: `Terraform`
- Cloud Service: `Google Cloud Platform (GCP)`
- Data lake: `Google Cloud Storage (GCS)`
- Data Warehouse: `Google Big Query (GBQ)`
- Data transformation: `Data Build Tool (DBT)`
- Data visualization: `Google Data Studio (GDS)`
- Orchestration: `Prefect`


## Instructors acknowledgements
I appreciate the opportunity to attend this workshop. I am forever thankful for this opportunity.
- [Ankush Khanna](https://linkedin.com/in/ankushkhanna2)
- [Sejal Vaidya](https://linkedin.com/in/vaidyasejal)
- [Victoria Perez Mola](https://www.linkedin.com/in/victoriaperezmola/)
- [Kalise Richmond](https://www.linkedin.com/in/kaliserichmond/)
- [Jeff Hale](https://www.linkedin.com/in/-jeffhale/)
- [Alexey Grigorev](https://linkedin.com/in/agrigorev)
Please reach out to [alexey@datatalks.club](alexey@datatalks.club)

If you want to know more about the workshop:
- Register in [DataTalks.Club's Slack](https://datatalks.club/slack.html)
- Join the [`#course-data-engineering`](https://app.slack.com/client/T01ATQK62F8/C01FABYF2RG) channel
