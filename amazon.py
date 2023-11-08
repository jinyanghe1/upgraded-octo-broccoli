import requests
r = requests.get("https://www.amazon.cn/gp/product/B01M8L5Z3Y")
print(r.status_code)
#是503，说明访问错误
print(r.encoding)
#ISO-8859-1
r.encoding = r.apparent_encoding
print(r.text)
'''/usr/local/bin/python3.11 /Users/hejinyang/PycharmProjects/learning_spider/amazon.py 
503
ISO-8859-1
<!DOCTYPE html>
<!--[if lt IE 7]> <html lang="zh-CN" class="a-no-js a-lt-ie9 a-lt-ie8 a-lt-ie7"> <![endif]-->
<!--[if IE 7]>    <html lang="zh-CN" class="a-no-js a-lt-ie9 a-lt-ie8"> <![endif]-->
<!--[if IE 8]>    <html lang="zh-CN" class="a-no-js a-lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!-->
<html class="a-no-js" lang="zh-CN"><!--<![endif]--><head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<title dir="ltr">Amazon.cn</title>
<meta name="viewport" content="width=device-width">
<link rel="stylesheet" href="https://images-na.ssl-images-amazon.com/images/G/01/AUIClients/AmazonUI-3c913031596ca78a3768f4e934b1cc02ce238101.secure.min._V1_.css">
<script>

if (true === true) {
    var ue_t0 = (+ new Date()),
        ue_csm = window,
        ue = { t0: ue_t0, d: function() { return (+new Date() - ue_t0); } },
        ue_furl = "fls-cn.amazon.cn",
        ue_mid = "AAHKV2X7AFYLW",
        ue_sid = (document.cookie.match(/session-id=([0-9-]+)/) || [])[1],
        ue_sn = "opfcaptcha.amazon.cn",
        ue_id = 'JC9SWMC52Y0FRGWX293R';
}
</script>
</head>
<body>

<!--
        To discuss automated access to Amazon data please contact api-services-support@amazon.com.
        For information about migrating to our APIs refer to our Marketplace APIs at https://developer.amazonservices.com.cn/index.html/ref=rm_c_sv, or our Product Advertising API at https://associates.amazon.cn/gp/advertising/api/detail/main.html/ref=rm_c_ac for advertising use cases.
-->

<!--
Correios.DoNotSend
-->

<div class="a-container a-padding-double-large" style="min-width:350px;padding:44px 0 !important">

    <div class="a-row a-spacing-double-large" style="width: 350px; margin: 0 auto">

        <div class="a-row a-spacing-medium a-text-center"><i class="a-icon a-logo"></i></div>

        <div class="a-box a-alert a-alert-info a-spacing-base">
            <div class="a-box-inner">
                <i class="a-icon a-icon-alert"></i>
                <h4>请输入您在下方看到的字符</h4>
                <p class="a-last">抱歉，我们只是想确认一下当前访问者并非自动程序。为了达到最佳效果，请确保您浏览器上的 Cookie 已启用。</p>
                </div>
            </div>

            <div class="a-section">

                <div class="a-box a-color-offset-background">
                    <div class="a-box-inner a-padding-extra-large">

                        <form method="get" action="/errors/validateCaptcha" name="">
                            <input type=hidden name="amzn" value="rPyqP4KpALyekLhI5JIVEQ==" /><input type=hidden name="amzn-r" value="&#047;gp&#047;product&#047;B01M8L5Z3Y" />
                            <div class="a-row a-spacing-large">
                                <div class="a-box">
                                    <div class="a-box-inner">
                                        <h4>请输入您在这个图片中看到的字符：</h4>
                                        <div class="a-row a-text-center">
                                            <img src="https://images-na.ssl-images-amazon.com/captcha/usvmgloq/Captcha_alvmohuigv.jpg">
                                        </div>
                                        <div class="a-row a-spacing-base">
                                            <div class="a-row">
                                                <div class="a-column a-span6">
                                                    <label for="captchacharacters">输入字符</label>
                                                </div>
                                                <div class="a-column a-span6 a-span-last a-text-right">
                                                    <a onclick="window.location.reload()">换一张图</a>
                                                </div>
                                            </div>
                                            <input autocomplete="off" spellcheck="false" id="captchacharacters" name="field-keywords" class="a-span12" autocapitalize="off" autocorrect="off" type="text">
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <div class="a-section a-spacing-extra-large">

                                <div class="a-row">
                                    <span class="a-button a-button-primary a-span12">
                                        <span class="a-button-inner">
                                            <button type="submit" class="a-button-text">继续购物</button>
                                        </span>
                                    </span>
                                </div>

                            </div>
                        </form>

                    </div>
                </div>

            </div>

        </div>

        <div class="a-divider a-divider-section"><div class="a-divider-inner"></div></div>

        <div class="a-text-center a-spacing-small a-size-mini">
            <a href="https://www.amazon.cn/gp/help/customer/display.html/ref=footer_claim?ie=UTF8&nodeId=200347160">使用条件</a>
            <span class="a-letter-space"></span>
            <span class="a-letter-space"></span>
            <span class="a-letter-space"></span>
            <span class="a-letter-space"></span>
            <a href="https://www.amazon.cn/gp/help/customer/display.html/ref=footer_privacy?ie=UTF8&nodeId=200347130">隐私声明</a>
        </div>

        <div class="a-text-center a-size-mini a-color-secondary">
          &copy; 1996-2015, Amazon.com, Inc. or its affiliates
          <script>
           if (true === true) {
             document.write('<img src="https://fls-cn.amaz'+'on.cn/'+'1/oc-csi/1/OP/requestId=JC9SWMC52Y0FRGWX293R&js=1" />');
           };
          </script>
          <noscript>
            <img src="https://fls-cn.amazon.cn/1/oc-csi/1/OP/requestId=JC9SWMC52Y0FRGWX293R&js=0" />
          </noscript>
        </div>
    </div>
    <script>
    if (true === true) {
        var head = document.getElementsByTagName('head')[0],
            prefix = "https://images-cn.ssl-images-amazon.com/images/G/01/csminstrumentation/",
            elem = document.createElement("script");
        elem.src = prefix + "csm-captcha-instrumentation.min.js";
        head.appendChild(elem);

        elem = document.createElement("script");
        elem.src = prefix + "rd-script-6d68177fa6061598e9509dc4b5bdd08d.js";
        head.appendChild(elem);
    }
    </script>
</body></html>


进程已结束，退出代码为 0
'''
print(r.request.headers)
#说明了user-agent是一个requests
#下面模拟浏览器向amazon发送信息
kv = {'user-agent': 'Mozilla/5.0'}
url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
r = requests.get(url, headers=kv)
print(r.status_code)
#200
r.encoding = r.apparent_encoding
print(r.text[:1000])
