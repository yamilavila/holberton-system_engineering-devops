# Task 0 Debugging Nginx & ApacheBench 

exec {'ulimit-file':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx && sudo service nginx restart'
}
