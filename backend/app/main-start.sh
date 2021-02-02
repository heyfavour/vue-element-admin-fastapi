ps -ux|grep python|grep main.py|awk '{print $2}'|awk -F '/' '{print $1}'|xargs kill -9
nohup python app/main.py >> server.log &
