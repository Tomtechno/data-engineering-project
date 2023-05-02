# US Accidents (2016 - 2021)
A Countrywide Traffic Accident Dataset (2016 - 2021)

![Car accident](https://user-images.githubusercontent.com/69020112/235061206-d1b063b6-147d-4be3-8dc4-db6ea9c50eb5.jpg)

An estimated 42,915 people died in car crashes in the United States in 2021, a 10.5% increase from 2020. Knowing about car accidents in the USA is important for several reasons:

* Public safety: Understanding the causes and trends of car accidents can help policymakers and law enforcement officials take steps to reduce the frequency and severity of accidents. This can help to make the roads safer for all drivers, passengers, and pedestrians.

* Economic impact: Car accidents can have a significant economic impact, both in terms of medical expenses and lost productivity. By understanding the costs associated with accidents, policymakers can make informed decisions about how to allocate resources to prevent and respond to accidents.

* Insurance rates: Insurance companies use data on car accidents to set rates for drivers. Knowing the frequency and severity of accidents can help insurers to accurately price their policies, which can benefit drivers in the long run.

* Traffic planning: Data on car accidents can also inform traffic planning decisions, such as where to place traffic signals, speed limits, and other traffic control measures. This can help to reduce congestion and improve traffic flow, which can benefit drivers and communities.

Overall, understanding the trends and patterns of car accidents in the USA is essential for promoting public safety, supporting economic growth, and improving the quality of life for all Americans.

With this project I would like to know which are the most dangerous states in the United States, which was the most dangerous year and what is the weather that leaded most of the accidents.


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

## Reproduce it yourself
PREREQUISITES
* Git clone the repo
```bash
git clone https://github.com/Tomtechno/data-engineering-zoomcamp.git
```
* Make a virtual environment with python and install prefect. I chose python 3.9 as it is the recommended version
```bash
conda create -n projectEnv python=3.9 prefect
```
* Activate your new env
```bash
conda activate projectEnv
```
1. Setup your Google Cloud environment
- Create a [Google Cloud Platform project](https://console.cloud.google.com/cloud-resource-manager)
- Configure Identity and Access Management (IAM) for the service account. Go to "IAM & Admin > Service Account" and create an account giving it the following privileges: BigQuery Admin, Storage Admin and Storage Object Admin
- Go to Actions and click on "Manage keys > Add Key > Create New Key". Save the key as a JSON file to your project directory e.g. to `~/.gc/<credentials>`
- Install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/install-sdk)
- Let the [environment variable point to your GCP key](https://cloud.google.com/docs/authentication/application-default-credentials#GAC), authenticate it and refresh the session token
```bash
export GOOGLE_APPLICATION_CREDENTIALS=<path_to_your_credentials>.json
gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS
gcloud auth application-default login
```
2. Install all required dependencies into your environment
```bash
pip install -r requirements.txt
```
3. Setup your infrastructure
- Assuming you are using Linux AMD64 run the following commands to install Terraform - if you are using a different OS please choose the correct version [here](https://developer.hashicorp.com/terraform/downloads) and exchange the download link and zip file name

```bash
sudo apt-get install unzip
cd ~/bin
wget https://releases.hashicorp.com/terraform/1.4.1/terraform_1.4.1_linux_amd64.zip
unzip terraform_1.4.1_linux_amd64.zip
rm terraform_1.4.1_linux_amd64.zip
```
- To initiate, plan and apply the infrastructure, adjust and run the following Terraform commands
```bash
cd Terraform/
terraform init
terraform plan -var="project=<your-gcp-project-id>"
terraform apply -var="project=<your-gcp-project-id>"
```
4. Setup your orchestration
- If you do not have a prefect workspace, sign-up for the prefect cloud
- Create a workspace [here](https://app.prefect.cloud/auth/login) and an [API key](https://app.prefect.cloud/my/api-keys).
- Add the previously created API key and the name of your workspace as repository secrets
- Create the [prefect blocks](https://docs.prefect.io/concepts/blocks/) via the cloud UI
     - run `prefect block register -m prefect_gcp` in the VSCode terminal in your virtual env (projectEnv)
     - go to your workspace in prefect cloud
        1. add gcs bucket block
        2. name the block 'project-gcs' so you won't need to make any changes in the prefect flows; fill in the other fields with bucket name 
        3. create a credentials block  with the name 'project-gcp-creds' if you don't want to change anything   
- To execute the flow, run the following commands in two different terminals
```bash
prefect agent start -q 'default'
```
```bash
python prefect/etl_web_to_gcs.py
python prefect/etl_gcs_to_bq.py
```

5. Execute DBT to create the result tables 
- Following this [steps](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/week_4_analytics_engineering/dbt_cloud_setup.md) written by [MekongDelta-mind](https://github.com/MekongDelta-mind)
IN THE STEP 6 MAKE SURE TO:
- Name the dataset "dbt_tomtechno":

IN THE STEP 6 MAKE SURE TO:
- Git clone the next repo:
```bash
git@github.com:Tomtechno/data-engineering-project.git
```
- In the DBT develop tab you can connect to the project created and stored in this [repo](https://github.com/Tomtechno/data-engineering-project/Dbt).

Now try running the following commands:

```bash
dbt run
dbt test
```
When the job executed successfully you'll see the following tables/views created under the "dbt_tomtechno" dataset
![this1](https://user-images.githubusercontent.com/69020112/235795633-43059a78-fe53-4387-9fb1-4592b0611c7f.png)


## Dashboard
* You can now query the data and connect it to looker to visualize the data with [Looker Studio](https://lookerstudio.google.com/navigation/reporting)
![Basic_report jpg_page-0001](https://user-images.githubusercontent.com/69020112/235322122-e7b542cd-f888-4871-9dfb-e9e2597ee641.jpg)


[Click here](https://lookerstudio.google.com/reporting/49229423-1c2a-44ba-931b-83a214490beb/page/hycOD) to see my Looker dashboard.

* In graph 1 can be seen that most accidents take place in two states:

    *28% of them occur in the state of California (CA)

    *14% of them occur in the state of Florida (FL)

* In graph 2 can be seen that almost all accidents, 2.5M, have a medium severity of 2.

* In graph 3 can be seen that the most accidents, 1.1M, occur in a fair weather. Almost 700000 of them take place in the year of 2021.

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
