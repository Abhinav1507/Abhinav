# Abhinav
VOTING APPLICATION DEPLOYMENT USING  DOCKERS

A simple distributed voting application running across multiple Docker 
containers. Used to register and tabulate votes to either aid or take care of 
casting and counting votes. The voting application only accepts one vote 
per client. It does not register votes if a vote has already been submitted 
from a client.
Docker provides the ability to package and run an application in a loosely 
isolated environment called a container. The isolation and security allow 
you to run many containers simultaneously on a given host. Containers 
are lightweight because they don’t need the extra load of a hypervisor but 
run directly within the host machine’s kernel. This means you can run 
more containers on a given hardware combination than if you were using 
virtual machines.
