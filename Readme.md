#Prerequisites:

    ###Docker
    git -- https://www.atlassian.com/git/tutorials/install-git
    dockercompose
    Amazon account with admin privileges.
    
    
 #### How to provision this app
 

    - Kubectl command tells the cluster Master to create a Deployment.
    - The Master checks for available nodes and schedules app instances (Pods) onto Nodes.
    - Pods are scheduled onto their nodes. Note that once Pods are scheduled to a Node, they are tied to that Node and will terminate with the Node.
    - The Master monitors the Nodes to ensure that the correct number of app instances is running.
 
 
![Alt text](https://cdn-images-1.medium.com/max/2000/1*fqlivmOGP9jJrja4lWT6pA.png)
