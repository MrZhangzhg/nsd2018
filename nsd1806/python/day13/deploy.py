def check_version():


def download():


def check_md5():


def deploy():


if __name__ == '__main__':
    new_ver = check_version()
    if not new_ver:
        print('没有新版本软件')
        exit(1)
    download()
    file_ok = check_md5()
    if not file_ok:
        print('文件已损坏')
        exit(2)
    deploy()
    download()    # 更新本地live_version
    print('部署完成!!!')
