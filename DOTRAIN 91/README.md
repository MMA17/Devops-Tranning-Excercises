CÀI ĐẶT WORDPRESS BẰNG ANSIBLE

Minimum Ansible Version: 2.4

Requirements:
    
    - php (5.3.2+)
    - mysql (5.0+)
    - apache2 (with mod_rewrite enabled)

Roles:

    - geerlingguy.apache    (https://galaxy.ansible.com/geerlingguy/apache)
    - geerlingguy.php       (https://galaxy.ansible.com/geerlingguy/php)
    - geerlingguy.mysql     (https://galaxy.ansible.com/geerlingguy/mysql)
    - geerlingguy.php-mysql (https://galaxy.ansible.com/geerlingguy/php-mysql)
    - oefenweb.wordpress    (https://galaxy.ansible.com/oefenweb/wordpress)

Variables: /vars/main.yml.example

Update your own configs and rename it (main.yml)

    - mysql_databases[] Database infomations
    - mysql_users[] User infomations
    - wordpress_installs[] wordpress configs
    
Quick Start:

    ansible-playbook playbook.yml