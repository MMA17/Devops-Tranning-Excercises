Ansible là gì ?

    Là công cụ dùng để tự động hóa việc cài đặt, cấu hình các máy chủ thông qua các file yaml đã được định nghĩa trước.

Mô hình của ansible khác gì với mô hình của saltstack?

    Salt Stack  
        - hoạt động dựa trên mô hình master - minion giao tiếp với nhau qua port riêng 4505-4506
        - Xác thực thông qua việc xác thực trên master server

    Ansible server 
        - hoạt động độc lập, giao tiếp với các server để cấu hình thông qua ssh port 22
        - Xác thực thông qua ssh key 

        Mô hình của Salt Stack là Master - Agent còn Ansible là Agentless.

Các thành phần trong ansible ?

    1, File định nghĩa các host theo group
    2, File playbook định nghĩa cách cấu hình máy chủ 

Cấu trúc project của ansible ?

    Gồm 7 các folder:
        - tasks – chứa danh sách các task chính được thực thi trong role này.
        - handlers – chứa các handler, có thể được dùng trong role này hoặc các role khác.
        - defaults – chứa các biến được dùng default cho role này
        - vars – chứa thông tin các biến dùng trong role, biến trong vars sẽ override biến trong default
        - files – chứa các file cần dùng để deploy trong role này, cụ thể như file binary, file cài đặt…
        - templates – chứa các file template theo jinja format đuôi *.j2 (có thể là file config, file systemd…).
        - meta – định nghĩa 1 số metadata của role này, như là dependencies

Các cách để debug ansible ?

    - Sử dụng module debug để in ra các biến trong playbook 
    - Enable log_path trong ansible config để lưu log ra file
    - sử  dụng flag -vvv trong quá trình chạy để in ra nhiều thông tin hơn
    - sử dụng flag -e để ghi đè các biến được truyền vào trong chương trình


