#Prerequisites:

    ###Docker
    git -- https://www.atlassian.com/git/tutorials/install-git
    dockercompose
    Amazon account with admin privileges.
    
    
 #### How to provision this app
 
 - I use AWS EKS to orchestrate,provision this application.
 - I use docker to build image and store in registry and Using EKS clustering i create pods
 - For HA i use replicas which can increase later withoutdown time .
 - For monitoring purpose i use Grafana and prometheus for dashboar of my services
 - By using EKS i can do rollback easily to my previous deployments as well
 - I chosen this EKS ( microservices) which can be manages easily and can  troubleshoot the services.
 - This kind of approach can be easily automated using scripts.
 - the advantage of kubernets is can use the YAML scripts to deploy and up the service and reusability.
 
 
 
![Alt text](https://cdn-images-1.medium.com/max/2000/1*fqlivmOGP9jJrja4lWT6pA.png)
