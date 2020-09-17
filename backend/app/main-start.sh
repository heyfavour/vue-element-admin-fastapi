netstat -anp |grep 8080|awk '{print $7}'|awk -F '/' '{print $1}'|xargs kill -9
netstat -anp |grep 8080|awk '{print $7}'|awk -F '/' '{print $1}'|xargs kill -9
nohup python app/main.py >> server.log & 
