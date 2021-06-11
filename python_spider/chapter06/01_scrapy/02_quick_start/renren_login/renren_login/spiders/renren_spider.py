import scrapy


class RenrenSpiderSpider(scrapy.Spider):
    name = 'renren_spider'
    allowed_domains = ['passport.csdn.net']
    start_urls = ['http://renren.com/']

    def parse(self, response):
        # url = "http://rrwapi.renren.com/account/v1/loginByPassword"
        # headers = {
        #     "Content-Type": "application/json;charset=UTF-8",
        #     "Host": "rrwapi.renren.com",
        #     "Origin": "http://renren.com",
        #     "Referer": "http://renren.com /",
        #     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
        # }
        # data = {
        #     "appKey": "bcceb522717c2c49f895b561fa913d10",
        #     "callId": "1623378862793",
        #     "password": "47cbbc00bc011fe1f84da83ee7d78c1f",
        #     "sessionKey": "",
        #     "sig": "d560d802a50396fcd4be8e44ba548282",
        #     "user": "18814121269",
        # }
        url = "https://passport.csdn.net/v1/register/pc/login/doLogin"
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Origin": "https://passport.csdn.net",
            "Referer": "https://passport.csdn.net/login",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
        }
        uaToken = "140#GFbdHQyMzzWLaQo2WZs+jtSOy0v8SSWtcXOPXfbabq6hknU85NrtD6K+3lL6483V2MZS7EvxGpLyb3cMz7Vv+6OySG+bcXDOmeLbvYEUrW9cM48V0g7XzWGXlp1zz/MTLt0B0bzxhoHxatVRzzrb22U3lp1xzOpnKmWqHOTx2PPmIp6ezzrb2BbMQ+cjzPcjV2eqCQni2Prsmt11zFcT2X5VlpkczPc/V2M8mFrH2jDDbj0alQFIB2TSQuCsxPPtV2iEuzWYHDZT/tspzFPs21S1lpaYx8PzVO98uzPY2IFuntsxzQFo2OSkl3IbzPWtIf4qUJQrubX4orvZrI7ZbI8yUULFXxy0zTTOnCi+9uEYjaAovwGjJGMeVlFkakPvLzo6L+n55tG62zfKxRx52Q1eYAi/oFKc1tS5piaW6Al8fLEyEJc7FuTEzU122p9G9I28XIrLZiOPOIe9Speg0ZxYPKp55EyssfO3/BXI/IHK5432W76W6ReyA5POtfpny8cmGQFKPDa1myjsebjKKQxyHIqtJxC/df+IM+rpzaX2vWnkSXxzKOIlU/5xTymUpzMqQ0IasVdKm9qSgqH/N3DfYfifPYFZnWkq2i8ne3BKa5rNDvLSOrSVZqbYEFrz4dcNR1TI79PJmIEm1VkyoHtxZiSONtQIAE6g9hEcgQ9hK/K4J1bPBpFOPMw0yJM1YJgrfGm4EEn2hWiRJaTlkO/iNtAqTJoi4eJyUa073EiADgGTFbt8MuoCDq1rPm/pFVL6NTLGytjIBFvbmXiAhoMyhWGfbCNSLpUGqMvBLrppxH+ilAp3WCPt3cxPAMvVhdGa7NqV0iXCP40BK267ezlBbWEOi+0Gb1tJfx93Ti6WO69TJXchi2JGVNV+nlFiYlR0GEHO5qPFImf4zrFuvs7EqWZfs1Nlwsf10ckO+OeveO/q5cTuLo4NK6XjOPHYDTWfgDyqaYzZCdaYy/+U2ABKRD1VbU55godRlIxFRK0TnsoQAIZNCUVqDIso1+rp/oXqENergJPJNlgQ9oYLrQ9OoWymGOp/1QOykltCgQWXukOMFc7EBdVu4fgBteUzxuCbjyNYlSPXdLWciQJbTs3FMbz5ShOieJKVWiWdSbLnU8KT1p4oNPjwGcs+krBhd0vEWEEP5xez0qiHvt3o00Iisn41unBc58mC+WppUf65aNbayr6v6XDfNBxGk0LENzOT+eTfIHvZfWNxscVBUhfxIt46RtPKSez03sdfgBI9aGIyRNSgfnGQl2DHoiJE4dlZWtileqlDk76NRGvDQhRZeh0eDcezK6z9/H7u1hWtctl1vwX9X+Tm83Uz6taXBYho0X6BANbkRVm1tTXezEl+e7yV74zy097tTITTYOo9D3JLLxiJ+jB82692LTEPw1AcYVZJ/u98fZZNmLDiCQLmgB6cCz/lrHmfrMILKMfESZ8bsUFzvli27OhBT7mZPeVGKFJdlg3QFjFuYTfUaCDK1W66Dz/3yLO/1hs97Dcjo2oJy1mD7RIIzB3quERIWOJV3ebP6qGz7FrVJHWRCIkE8rh3ulylpmNzRSpCEAQODxV05PiMmTJ7a8H+6golTvn9OHE7N3ajcCbRdn1SqStBEAtCNYUSd/szsK0H+yHbfvBgzgSM+FAqNWHtv6qjWcwWtMPkvKrg2k2t728gUrY1LRUZ6aBSpVxNKuGmnCYKU/8fNu7hK2Xjt82rCbwfFRRge2CJuEFgUWis3UO1rsPi6M0TXqybZzshugcohl75jQgoYPgl8VrIJsvjRjW/exOe0cIwy3IT2z=="
        data = {
            "loginType": "1",
            "pwdOrVerifyCode": "csdncsdna5673",
            "uaToken": uaToken,
            "userIdentification": "18814121269",
            "webUmidToken": "T2gADSKcjwNvLz1X7_3a66Uo3Is-ArIO8454K8Ilq44nvUWsrdtL0iUMizOeRrIaIxs=",
        }
        request = scrapy.FormRequest(url=url, headers=headers, callback=self.paser_page, formdata=data)
        yield request

    def paser_page(self, response):
        print(" # " * 10)
        print(response.text)
        with open("test.html", "wb") as fp:
            fp.write(response.body)
        print(" # " * 10)

"""
由于人人网登录方式问题，现在暂时登录失败。
"""