import requests  # 导入requests库，用于发送HTTP请求
from urllib.parse import urlencode  # 导入urlencode函数，用于构建URL参数
import time  # 导入time模块，用于添加时间延迟
import re  #正则表达式
import random  # 导入random模块，用于生成随机数



class Get_url():
    # 定义初始化属性
    def __init__(self):
        # 这条是需要我们访问的 url ，实现翻页功能在主程序入口， 到时候传参给num就能实现翻页功能
        self.url = 'https://weibo.com/ajax/side/hotSearch'
        # 这是伪造头，待会会随机选取其中之一
        self.USER_AGENTS = [
            "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1"
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
            "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
            "Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50",
            "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
            "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
            "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12 "
        ]
        self.proxies = {
            'http': 'None',
            'https': 'None',
        }
        self.cookies={'cookies':'填入自己的cookies'}
        # 构建headers请求头 把ua伪造头通过random随机选取一个传进去
        self.headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "client-version": "v2.47.72",
    "cookie": "SCF=AiGlm1S8MPmlRb6iQ-F4SQQpGK1kSp76lVu0XOxSaugTvw7C8MmSmel8Ph1k2wIEahb7-ojPOBSIywOD-JvtBnw.; SUB=_2A25FThikDeRhGeBI71oQ-SzNwjqIHXVmIhRsrDV8PUNbmtAbLWzVkW9NRpKKIFEEZVzIQ0aDAztrXla-jQ9vkYAe; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWM3jzcfJED8zEySAr-Nayr5NHD95QcSoBReK.EeK.cWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNSoqX1h24eo24Sntt; ALF=02_1752298997; _s_tentry=passport.weibo.com; Apache=5509938242562.504.1749707000130; SINAGLOBAL=5509938242562.504.1749707000130; ULV=1749707000190:1:1:1:5509938242562.504.1749707000130:; WBPSESS=ci3NQz4P7pw07tMfOhf2Y0iNlsyUB_NrF2Z0ZejtVxhhGwkW2n1KKOuO7n3l4pOjbL5bKqfjVq3GycWYf-Tn2UPsIfGz0bPT-88OZ3jpWThIQPg214z_EQ-9wJgFp8T-CwdKwpFAiUVVx-WiwAEU1Q==",
    "priority": "u=1, i",
    "referer": "https://weibo.com/hot/search",
    "sec-ch-ua": '"Chromium";v="136", "Microsoft Edge";v="136", "Not.A/Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "server-version": "v2025.06.06.1",
    "user-agent": f"{random.choice(self.USER_AGENTS)}",
    "x-requested-with": "XMLHttpRequest"
}

    # 获取网页的json数据方法
    def get_url(self):
        try:
            # 用post请求发送， 传入url，请求头， ip代理 然后用json数据保存
            response = requests.get(self.url, headers=self.headers).json()
            # 退出函数返回 response
            return response

        # 生成错误日志发现具体的问题
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP 错误: {http_err}")
            print(f"状态码: {response.status_code}")
            print(f"响应内容: {response.text}")

        except requests.exceptions.ConnectionError as conn_err:
            print(f"连接错误: {conn_err}")
            print("请检查网络连接和代理服务器配置")
        except requests.exceptions.Timeout as timeout_err:
            print(f"请求超时: {timeout_err}")
            print("请检查网络连接或增加超时时间")
        except requests.exceptions.RequestException as req_err:
            print(f"请求发生错误: {req_err}")
            print("请检查请求参数和目标 URL")
        except Exception as e:
            print(f"发生未知错误: {e}")
            print("请检查代码逻辑和目标网页结构")



    # 提取json 关键数据方法
    def url_date(self):
        # 用res变量接收 get_url返回的数据
        res = self.get_url()
        data=res["data"]
        i=0
        for d in data['realtime']:
            i+=1
            print(f'当前热搜：{d["note"]}，排名：{i}')
        num=input("希望查看的热搜(输入排名)")
        hot=data['realtime'][int(num)-1]['note']
        josn_data=self.get_hot_search(hot)
        # print(josn_data)
        self.parse_hot_data(josn_data)
        print('分界线111111')


    # 按页数抓取数据
    def get_hot_search(self,keyword):
        # 构建请求参数
        host='m.weibo.cn'
        params = {
            'containerid': f'100103type=1&q=#{keyword}#',
            'page_type': 'searchall',
            'page': 1
        }
        base_url = 'https://%s/api/container/getIndex?' % host  # 基础URL，用于构建API请求URL
        url = base_url + urlencode(params)  # 将输入的中文关键词编码，构建出完整的API请求URL
        print(url)  # 打印请求的URL
        error_times = 3  # 设置错误尝试次数
        while True:
            response = requests.get(url, headers=self.headers)  # 发送HTTP GET请求
            if response.status_code == 200:  # 如果响应状态码为200（成功）
                if len(response.json().get('data').get('cards')) > 0:  # 检查是否有数据
                    return response.json()  # 返回JSON响应数据
            time.sleep(3)  # 等待3秒
            error_times += 1  # 错误尝试次数增加
            if error_times > 3:  # 如果连续出错次数超过3次
                return None  # 返回空值



        #修改后的页面爬取解析函数
    def parse_hot_data(self,data):
        # 提取信息
        for card in data["data"]["cards"]:
            if "mblog" in card:
                mblog = card["mblog"]
                user = mblog["user"]
                print("作者信息：")
                print(f"用户ID: {user['id']}")
                print(f"用户名: {user['screen_name']}")
                print(f"个人简介: {user['description']}")
                print(f"粉丝数: {user['followers_count']}")
                print(f"微博数: {user['statuses_count']}")
                print(f"性别: {'男' if user['gender'] == 'm' else '女'}")
                print(f"是否认证: {'已认证' if user['verified'] else '未认证'}")
                print(f"认证类型: {user['verified_type']}")
                print(f"用户等级: {user['urank']}")
                print(f"会员等级: {user['mbrank']}")
                print("\n发布内容：")
                print(f"发布时间: {mblog['created_at']}")
                # 使用正则表达式去除HTML标签
                clean_text = re.sub(r'<[^>]+>', '', mblog['text'])
                print(f"微博正文: {clean_text}")
                print(f"点赞数: {mblog['attitudes_count']}")
                print(f"评论数: {mblog['comments_count']}")
                print(f"转发数: {mblog['reposts_count']}")
                print("-" * 50)




    # 创建一个方法来运行上面的代码
    def run(self):
            self.url_date()

# 创建主程序入口
if __name__ == '__main__':
    run_1 = Get_url()
    run_1.run()
    print('爬取完毕！')