#Prerequisites:

    ###Docker
    git -- https://www.atlassian.com/git/tutorials/install-git
    dockercompose
    GCP account with admin privileges.
    
  ##### to test the app
  execute fortunescrapper.py script using python installed already.
  $ python fortunescrapper.py.
  
  It will create html file click on it, you can see random message generated.
    
 #### How the  service can be provision,orchestrate and maintain.
 
    - To enable this we create image using docker using Dockerfile.
    - we push this image to google registery
    - Using kubectl command we can deploy,scale and update the images and run the services.
    - This kubectle using minikube as VM where master k8's is running which makes API calls to pods to check the service ports
    - This whole this runs with set of command lines which i have wrote in seperate kubectlcommands file for reference
    - Below instructions and image defines how this works
    -- Kubectl command tells the cluster Master to create a Deployment.
    -- The Master checks for available nodes and schedules app instances (Pods) onto Nodes.
    -- Pods are scheduled onto their nodes. Note that once Pods are scheduled to a Node, they are tied to that Node and will terminate with the Node.
    -- The Master monitors the Nodes to ensure that the correct number of app instances is running.
    -- This whole Kuberenetes engine can be monitored using Grafana and Prometheus in a dashboard.
    
 
 
![Alt text](https://cdn-images-1.medium.com/max/2000/1*30p6uwfaCfrQFvvfJuMozg.png)
