Pyenv là gì ?
    Pyenv là công cụ quản lý các phiên bản python giúp việc cài đặt và sử dụng các phiên bản riêng cho từng project dễ dàng hơn.

Virtualenv là gì, tại sao lại cần tới virtualenv trong python ?
    Virtualenv dùng để tạo môi trường ảo được sử dụng cùng Pyenv, môi trường ảo này giúp project chạy phiên bản python khác độc lập với phiên bản tại máy host

Cách để chạy một project python với virtualenv hay pipenv?
    1, Tải phiên bản cần thiết - pyenv install "version"
    2, Tạo môi trường với phiên bản tương ứng - pyenv virtualenv "version" "env_name"
    3, Gán môi trường đã tạo cho project - pyenv local "env_name"

dependency package là gì, tại tạo lại cần tới chúng ?
    dependency package là các gói thư viên ngoài, không đi cùng bộ cài python chuẩn được gán vào trong project đảm bảo thực hiện các công việc khác nhau.

pip là gì ?
    Pip hay pip3 là trình quản lý, cài đặt các gói modules/packages cho Python. 

nghiên cứu cách sử dụng requirements.txt và Pipfile ?
    requirements.txt, pipfile lưu ra các gói và phiên bản của gói đó được sử dụng trong project. Được sử dụng để đóng gói, theo dõi các packages được sử dụng 

