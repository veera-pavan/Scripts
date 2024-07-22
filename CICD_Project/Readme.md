#Project Details

Description: This is end to end CICD project for Java based application using build gradle 

Life cycle of this CICD pipeline:

CI part

- build java application using gradle
- push artifact to azure artifacts

CD part

- pull the artifcat
- pull the artifacts related to database
- deploy and configure data base(psql)
- execute schema on the data base
- deploy and start the application 


