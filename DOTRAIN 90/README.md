CÀI ĐẶT WORDPRES BẰNG ANSIBLE

Inventory: Chứa thông tin remote server

Roles:
- apache
- mysql
- php
- wordpress

    Thông số cấu hình cho từng role được lưu trong /vars/main.yml của từng role

    Role apache:
    - Cài đặt apache, Cấu hình thông số webservẻ
    - Cấu hình đường dẫn đến web root, port

    Role mysql:
    - Cài đặt mysql, cấu hình thông số mysql
    - Tạo Database, user, gán quyền cho user

    Role: php:
    - Cài php và các gói liên quan để kết nối tới mysql + apache

    Role wordpress:
    - Copy folder chứa chương trình wordpress sang remote server
    - Cấu hình thông số database, user cho wordpress.

    Lưu ý: 
    - Thông tin database và user trong folder vars của role mysql và wordpress phải giống nhau  
    - Chương trình phải được chạy với python3 để không gây ra lỗi khi cài pymysql