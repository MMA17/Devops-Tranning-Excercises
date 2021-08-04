File playbook là mysql.yml
- File này định nghĩa host được chạy trong file hosts
- Chương trình được chạy với quyền root (become: yes)
- Các role được chạy nằm trong phần roles

Role gồm các task là:
- cài MySQL - installMySQL.yml 
- Cấu hình MySQL (2 cách) sử dụng module copy để copy trực tiếp file config đã sửa trong /roles/mysql/files 
  hoặc sử dụng module template để chỉnh sửa file config thông qua biến trong /roles/mysql/vars
- Khởi tạo, xóa Database - database.yml
- Khởi tạo, xóa User - user.yml

Các task được include vào file main.yml trong folder roles/mysql/tasks
Khi chỉ cần sử dụng 1 số task nhất định thì comment các task còn lại