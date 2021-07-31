import threadGetContent
import time


def main():
    wr = open('output.csv', 'w')
    wr.write("name/title; content; created date; url\n")
    wr.close()
    urls = [
        'https://bizflycloud.vn/tin-tuc/caas-20210622161033206.htm',
        'https://bizflycloud.vn/tin-tuc/update-windows-de-tranh-cac-lo-hong-moi-phat-hien-20210316175940812.htm',
        'https://bizflycloud.vn/tin-tuc/bizfly-tron-bo-giai-phap-chuyen-doi-so-tu-goc-den-ngon-cho-doanh-nghiep-20210304174755621.htm',
        'https://bizflycloud.vn/tin-tuc/bizfly-cloud-khai-sale-tang-66-tong-gia-tri-thanh-toan-lan-dau-tien-tat-ca-cac-dich-vu-cloud-2021030317153524.htm',
        'https://bizflycloud.vn/tin-tuc/cac-dac-diem-cua-dien-toan-dam-may-doanh-nghiep-can-tan-dung-toi-da-de-phat-trien-nhanh-20210306113145181.htm'
    ]
    start_time = time.time()

    # Cach 1:Khong su dung khong Multi-thread
    # for url in urls:
    #     threadGetContent.get_content(url)

    # Cach 2: Su dung Multi-thread
    threadGetContent.get_all_content(urls)
    wr.close()
    run_time = time.time() - start_time
    print(str(run_time) + " seconds")


if __name__ == '__main__':
    main()
