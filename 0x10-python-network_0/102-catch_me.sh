!/bin/bash
#makes a request to 0.0.0.0:5000/catch_me cause the server to respond "you got me"
curl -s -o /dev/null -w "You got me!" --data "" "0.0.0.0:5000/catch_me"