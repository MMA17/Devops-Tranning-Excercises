4 tính năng thể hiện trong OOP:

    - Tính đóng gói: Các đối tượng khác không thể tác động trực tiếp lên thuộc tính của các đối tượng khác mà phải thông qua các phương thức công khai do đối tượng đó cung cấp.
    - Tính kế thừa: Các lớp con sẽ có tất cả các thuộc tính, phương thức của lớp cha.
    - Tính đa hình: Các đối tượng có thể cùng kế thừa từ 1 lớp cha nhưng có giá trị thuộc tính khác nhau.
    - Tính trừu tượng: Loại bỏ những thứ phức tạp, không cần thiết của đối tượng, chỉ tập trung vào những gì cốt lõi, quan trọng.

Đa kế thừa:
    - Các lớp con kế thừa nhiều từ nhiều lớp cha được gọi là đa kế thừa.
    - Các lớp cha có các thuộc tính, phương thức giống nhau thì lớp con ưu tiên kế thừa lớp cha được khai báo trước.

Constructor trong python:
    - __new__() định nghĩa tạo ra instance cho class, trả về instance cho class hiện tại
    - __init__() gán các giá trị cho class sau khi nó đã được khởi tạo. __init__() được chạy mỗi khi instance được khởi tạo.

Sử dụng Abstract Class, interface trong Python:
    - Cần inport 2 module ABC và abstractmethod trong package abc.
    - Sử dụng @abstractmethod để áp dụng cho các phương thức abstract.