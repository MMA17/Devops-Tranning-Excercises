CÀI ĐẶT WORDPRESS BẰNG ANSIBLE

Roles:
    - geerlingguy.apache
    - geerlingguy.php
    - geerlingguy.mysql
    - geerlingguy.php-mysql
    - oefenweb.wordpress

Variables: /vars/main.yml
    - mysql_databases[] Database infomations
    - mysql_users[] User infomations
    - wordpress_installs[] wordpress configs
    
Quick Start:
    ansible-playbook playbook.yml