import json

from tool.function import curlData, debug
from ws_function import analysis

if __name__ == "__main__":
    s = "[{\"RunEval\":\"w61ZS27CgzAQPQtRFsK2wqh6AcKUVcKOw5DDpcOIQhVJGhYNwpVDV1HDrl7CoMKIQDAYCjZWeRLCmgh7Pm/DnngGWcOZwp7Do8ODw7Eaw4nDuCvDncK9wqUywr58wrzCnmTDssK5P8K/w4t9cjgyw5/Ds0lAOC1eQALDhDpOw4h/SGQlw63CisKpwoTDmkLCgHcwC8KBw6rCgTEUF3TCgB0kDBLCkD9SR8OWw6AJw4nCgRjDlBoVwoDDgEFYTMOwIAh3wpsowrlcU8O5HcKlwonDnAQhwoUiexjDs2/Dt1zCrXpud07Cv8KWwpQJIXzDphUbwpzCmj7Dsw3DvU7DscK6fcO8w79MLF/DjjTDiMOLd0hQw7bDsxTCsMKpw67ClQbDncOBwp5wK3V7McOVwr3CqcOXwqtQBcOqNkUtCMOKHHp8VyDChzFae8OVw4IewqgxRm3CtMOuw58MJlhNNcKdw4V+PifCs3tiA8KaYXHCmMONw5YrBxQVA8ODaDQTwo7DuzLDqBvCpDTCqsONwq3DocOqwrbCoWoUalfDnWsMY8Oew5vCpcOsw77ClsKow5ddPsOmwqrDrCzCt8Orw7wZGT3CsjNjwrZAwqs+wo4tEMO2woPCmcKIwrgqd8KOwoctY8K3wobDmMKQK8KDQ8OcKMOuBcKawrnCrF7CrTvCpAk3wpvDhSlbIQrDgRkPfgA=\",\"Count\":\"52602\"},{\"裁判要旨段原文\":\"本院认为，债权人行使撤销权，应当以真实、合法的债权为前提，并需符合《中华人民共和国合同法》规定的撤销权行使条件。债权人依法行使撤销权，对债务人和受让财产的第三人而言，均构成不利后果，特别是受让财产的第三人并非债权债务关系的当事人，通过撤销权的方式使其承受不利后\",\"案件类型\":\"2\",\"裁判日期\":\"2014-12-04\",\"案件名称\":\"丹东通宇建筑工程公司与丹东客来多购物广场有限公司、丹东市金源房地产开发有限公司债权人撤销权纠纷审判监督民事判决书\",\"文书ID\":\"FcKOwrcBA0EMw4NWOmV9wqnCuMO/SMKWG1YAw4lBdMOFRVXCj8Kew45gwrAiRUgsHcOKQkLDnzDDs8KBYMObw7rDsxPCgsKRQ1ROwrwlw5sdw47CmcObw4PDoiRpS8Kgw7E1HMKwwqHCksKpEnrCqcOVw7xdwo9zZ0k5w5gDwpbCvMOOwqzDlihLwrRBw5NBVj/Ct8KTwoTCgB/Cr3JGcnU0a8Otw4vDhcKyw7kIw6TCnMKbGcK+Z8O1w4kqEMK9ZMKIw4HCuU8/\",\"审判程序\":\"再审\",\"案号\":\"（2013）民抗字第48号\",\"法院名称\":\"最高人民法院\"},{\"裁判要旨段原文\":\"本院认为，山东省农业科学院中心实验室计量认证合格证书因未参加年检而过期，以及案涉樱桃园存在受气候因素影响而减产的事实，一、二审法院均已作出确认，山东省工业产品生产许可证办公室出具的《证明》以及中国农业新闻网的相关报道均无新的证明对象和证明内容，不构成“足以推翻\",\"案件类型\":\"2\",\"裁判日期\":\"2015-06-26\",\"案件名称\":\"山东富海实业股份有限公司、曲忠全与山东富海实业股份有限公司、曲忠全等环境污染责任纠纷再审复查与审判监督民事裁定书\",\"文书ID\":\"DcOOwrcNw4BADMOAw4DClcKkVy4Vw7cfw4nDrgkcUzgiFsKKw5vCp2cqwofDslzCjkAAw6nDscOAMg9TSz7DlBrCksOgIcK3w6rDtnfCvMKTFXx2wpPDunIiRUnDlmdbCzLDgGEwEGrCqQgtH8KLCMOqL8K6w5k7H2c4V8KDa8ObV8KZw7hGJnjDlxrDv8KrM8KKwpcKLmLDnjDCoQPDgMOZw6XDvsK3w5PCqsOxHHsobgwLwq/CmwVuw5cbX8KNw6YH\",\"审判程序\":\"再审审查与审判监督\",\"案号\":\"（2014）民申字第1782号\",\"法院名称\":\"最高人民法院\"},{\"裁判要旨段原文\":\"综上所述，郇年春的再审申请不符合《中华人民共和国民事诉讼法》第二百条第六项规定的情形。本院依照《中华人民共和国民事诉讼法》第二百零四条第一款之规定，裁定如下\",\"案件类型\":\"2\",\"裁判日期\":\"2015-06-01\",\"案件名称\":\"郇年春、网络科技时代海口实验学校与郇年春、网络科技时代海口实验学校项目转让合同纠纷申请再审民事裁定书\",\"文书ID\":\"FcKOwrkRADEIA1vDojcOeUzDvyUdR8OESEgLw7LCjmHCh8KZwrlddggPPsKEw506eEQGwqLDiMOhdgE0w5LCkDdOGTnDgcKjwrVow5V8woTCslHCg8KCZsOqw5fDm1hNw5rDk8O3aMKEFcKPw5Y5wpczEnNOwoZ6wofCv8OEw6d7UxrCuB84wobDgm4cMsOBwqU5cmUDIXnCgMKCw6TDgC3CtBTCusOLw6ofKWjDk2LDoA7CmnRTeCTCnznCk08Gw7EH\",\"审判程序\":\"再审审查与审判监督\",\"案号\":\"（2015）民申字第761号\",\"法院名称\":\"最高人民法院\"},{\"案件类型\":\"2\",\"裁判日期\":\"2014-06-23\",\"案件名称\":\"章瀚与厦门金原融资担保有限公司一般借款合同纠纷申请再审民事裁定书\",\"文书ID\":\"DcKMwrcRw4AwDMOEVnrCkWJQw4nCuMO/SHbCgwJ3QD9uIcKyw4NCPEDDlMOWwoDDnx4fw6HCsMKXIsK/wpRQwqpaVcOuw41+wrJ2YMOOw6MTwrJaZxjCjRJUS1EpTwDDjsO+w7InasKCwpIWNsOhZgrCucKNwphHBcOJUF7DhcKCdcOVwoRrPULCm8Kvw4cfHMK5C8OXw5TDo0rDosKvwpvDnsO/X8Kvwro4HBPCli3Cu8OHMsKIw4pDb8K6O8OnUDXDhsOAw7gA\",\"审判程序\":\"再审审查与审判监督\",\"案号\":\"（2014）民申字第966号\",\"法院名称\":\"最高人民法院\"},{\"裁判要旨段原文\":\"本院认为：关于沈志平起诉请求给付的5833300元款项的性质。从案件基本事实看，该5833300元由《欠条》产生的483万元及《承诺书》载明的100万元构成。《欠条》产生的483万元系沈志平及其岳父毛家伟等人承包经营绵阳福潮公司后，双方当事人解除承包协议时进行\",\"案件类型\":\"2\",\"裁判日期\":\"2013-12-23\",\"案件名称\":\"朱玉成与沈志平、一审被告绵阳市福潮高新建材制品有限公司企业承包经营合同纠纷申请再审民事裁定书\",\"文书ID\":\"DcKOw4sVADEIAlvDksKoaMKOfsOWw75Lw5oceTBAw4bCrTvCh8Oiw4zDqsKYwonDg8KFwq0+QcK2e3hkw5/Cm3dkLcOdV0nDmsK8KkXDvcOTHFcue8OKcsKVP0YRwo7Cv8OMw6vDgcKtwq/Cv8KGLW5Pw4bCkMKUYsKewrvCjjLCpHk3wqZVNcKCLMOyw7BrwpnDlBZiBcKidnTDgMOWwqN8wqzDiMOOwpnDi8KmBDDCqcK/VzFtQcObwo9cRUVLw6HDrjxcwpfDvA3Dogc=\",\"审判程序\":\"再审\",\"案号\":\"（2013）民申字第1507号\",\"法院名称\":\"最高人民法院\"},{\"裁判要旨段原文\":\"本院经审查认为，宋皓通过个人借款、协调有业务关系及无业务关联的房地产开发公司借款及帮助申请贷款等多种途径为贵州新世纪集团房地产开发有限公司开发＆ｌｄｑｕｏ;世纪佳苑＆ｒｄｑｕｏ;、＆ｌｄｑｕｏ;世纪雅苑＆ｒｄｑｕｏ;两房地产项目提供启动资金、项目运营资金，并承\",\"案件类型\":\"1\",\"裁判日期\":\"2014-12-29\",\"案件名称\":\"宋皓犯受贿罪刑事决定书\",\"文书ID\":\"DcKOwrcRw4AwDMOEVmLDpsKrFMKDw7Yfw4nDrgEcwrpsVHDCiWFqAcKOwqnCkcOBYcOywoE/cD5dworDqMKJfcKZwowaw5c9wooVWT/DqcOZMMOOWsOTw4fDjsKqw6BTMMKCw6zDggtxaCjCnMObR8KowrrDpFfDpHTDl33Ds8Okw77DkMKjdcK7woxYwr44RDsuw5HDoWZ+LHvDvhR8QiV/w73CqHV7w7I1wp7CqFbCn8OuwpUbFTfDncKIZcOKMk5Cw77ChVfDuAA=\",\"审判程序\":\"再审\",\"案号\":\"（2012）刑监字第182-1号\",\"法院名称\":\"最高人民法院\"},{\"裁判要旨段原文\":\"本院认为：本案申请再审的焦点是库柏公司超额交付的金额为1471162元增值税发票是否构成税务损失。根据国家税务总局2006年10月17日修订的《增值税专用发票使用规定》第十四条第一款“一般纳税人取得专用发票后，发生销货退回、开票有误等情形但不符合作废条件的，或\",\"案件类型\":\"2\",\"裁判日期\":\"2014-12-17\",\"案件名称\":\"厦门聚亿电气设备有限公司与库柏电气（上海）有限公司一般买卖合同纠纷申请再审民事裁定书\",\"文书ID\":\"DcKNw4cJAEEMw4RacljCp8KnY8O/JcOdfQbCgRAzwpDCrGlZw6NZwqjDqQzDkj9fwqPCuC0vwp9dRFI1wpjDqMOqw6tpwobDlcKZLMKQw6DDgxUgw4LDq8Klw7fDq2jChFLDrGV1ATPDgsOHc1LDv8OywpbDnjrCphLCnyJKwpxEw5zCicK6wpXDn8K9wrnDv3hTw4Zsw7tSXgc0wrPCg8OaH8K2URI8V3DCs8Okw6t6wqRzw7nCp8K6csKJMsOPRsKKwrTCjjrDkhTCn34=\",\"审判程序\":\"再审审查与审判监督\",\"案号\":\"（2014）民申字第454号\",\"法院名称\":\"最高人民法院\"},{\"裁判要旨段原文\":\"本院认为：华东铝业公司主张巨化集团公司应为巨化物流公司与华东铝业公司于2009年和2010年签订《贸易资金合作协议》所形成的债务承担连带保证责任的依据不足，理由如下：第一，2009年和2010年《贸易资金合作协议》的签订主体为华东铝业公司和巨化物流公司，巨化集\",\"案件类型\":\"2\",\"裁判日期\":\"2013-10-18\",\"案件名称\":\"再审申请人浙ＸＸ东铝业股份有限公司与被申请人巨化集团公司、一审被告浙ＸＸ东巨化物流有限公司借款合同纠纷申请再审民事裁定书\",\"文书ID\":\"FcKNwrUBw4NADABXEkPDucKiw71HworDkx/DoMOcw6Z5wpzChcKLwqrCkwXCsMKsIsKxworDgsKgw6jChsKIwoBSdsOUS8OYw4vCmR7Cr2Ezw7IowpMjw7jDs8K5YgDCn8OuBwrDqsOobcKFcMO9AsO7wrvDnMOww5zDs0HCs8KewrjCqcO0wpF6UA7CrnLCisOqwpvDlcOFw5HCiMObcSDDqy3Co3kJw5IWw7HClcKIQzDDnhbCqsOmBMK5w7bDl8KMwqXDsmVGFcOUwo5Yw496w4IEPw==\",\"审判程序\":\"再审\",\"案号\":\"（2013）民申字第868号\",\"法院名称\":\"最高人民法院\"},{\"裁判要旨段原文\":\"本院认为：一、关于胡素娟、许春红是否为适格原告的问题。虽然《房地产买卖协议书》并非胡素娟、许春红亲笔所签，从协议签订到履行均由胡素娟之父胡国安代为办理，但是胡素娟、许春红对协议内容并无异议，在一、二审以及再审审查阶段均明确认可胡国安的代理行为，胡国安亦认可该事\",\"案件类型\":\"2\",\"裁判日期\":\"2014-08-28\",\"案件名称\":\"襄阳市房屋租赁修缮公司与胡素娟、许春红一般买卖合同纠纷申请再审民事裁定书\",\"文书ID\":\"HcONwrkRA0EIAMKwwpZ4Fwh5w7svw6k8TsKUworDgC/CjMOCQBvChjJSwrAHKF0rw5oHXsKzw5cKAQhJw5R4U8ORGW7CmcODwpLDggTCtz17Mm4kworDjgvCiDDCq8KGIX5UwrLCmWPCqsKKGQJywrJewrAQw6QswpJ1QBAtwp3DlnUhG8KAwo/CmALDhMOiw6YPehzCpWbDtsOlw4TDshs1w7IAw47Dp8KMwo7DjMOKHcKWw7vDuMKQDcOEK8Oew4Nfw7wB\",\"审判程序\":\"再审审查与审判监督\",\"案号\":\"（2014）民申字第227号\",\"法院名称\":\"最高人民法院\"},{\"案件类型\":\"4\",\"裁判日期\":\"2014-11-28\",\"案件名称\":\"李俊清申请内蒙古自治区呼和浩特市回民区人民法院执行行为违法确认申诉审查通知书\",\"文书ID\":\"DcKNwrcBADAIw4NewqIlw4AYw5rDvyfChcOFwpMsXVMoasOUOk/CjMKIwpjDjkMTGMKvwp3CgMKew5JDAxcywqFMDsKrDMKnE8OVwpvDk8O6w7A2woxqdg5YRyEvAcOVa0vDjsKUw5R4WMKifCN8fHMlKcKRw4ozw6LCrcOGw65xwociwo1gey89w6/Do8OuOFluwrzCvHFdR8OHI8OXwrAsw4LCpi4Zw7fDvgXCkCZGw5QrwrJrG14ZZ8O5wqfCr8OkAw==\",\"案号\":\"（2014）确监字第35号\",\"法院名称\":\"最高人民法院\"}]"
    s2 = "[{\"RunEval\":\"w61aw4tuwoMwEMO8FsKiHMKMwqjDugMowqd8QsKPK8KEIsKSNhwaKkJPUcO+wr1AGhcwNlAMGBgJTQR+w6zDrsOswqzCjVHCtsOnw7B4wroGccO4wpXDrMOewpI4wrx8wrzCvsOHw5HDp8O+fMKIw7fDkcOxw4Qcw4shD2A0wrzCgATDgDoUwrLChEBWUsKuWMKVwpBbAHgHwrMAZA/CjCHCucOgE8OEIGAAMgDCgC7CkBAAw5IFw7JBAgDCqUHDlMOgCcOBISQAwoTCsMOAaADCkBMAwpoCAMKgwrPChcOHBTAVbMOXw7V3wpsgwrpcwpPDuDtIwqJ4w6PDusOke8Opw4XCmHPCu2fDncO4dcK7w5vDtBhJKXjCnsODwqzCvMOBwqbDssKcWUNzS37Cu8O9w7vCsznCscOsccOawoPCrMKswoU8Sn8qBsOLw53CrcOfAXJjFcK/a8O7Kn0qw45Ww7/CnMKbw4rCvRYpElzCqMKNQTE3d8KyHcKjwoXDm0bCt1vDtsOow5LCrXPDn8O/DcOoMcKqw69QLcOjw7VNUsKWwodYwqnDucOFKkXCr8OPwrJONgrCtcKiw5J3N3lPwpTCkWHDp3xSw4NXaMOlw5LCpcONwpwgLsOnwrHDhsKNw6nChsKgwopRwoh+VhLDpXvDksOwJnnClMOVIEcwO8K+HcOOwrJ8w6fCl8KtDUXDmcOJwrPDlMOqRcKgc8OIwqPDkjPCkUUtZidywrvDmcO2wpTCjml2w4DDrMKdcAbDu8K0GV7CiC84wq1OJ0ZGX3MYEcKCwqPDksKSXcO/wrQ4IcO1OE4ZRB7DvMKRw6teLiLChcK8FsO1McOBLFnDiEpXwqjDrcO2w5/Ci8O6w4bCucKgw63DhMOIbMKbw6ZZw4PDmUBZwobDrcKCwprDqcKbw7V6w5TDiMOzSsODfcO+WSPCpcKTw7s4B37Cmh1dw5BJckrCs8OGwq3ChzbCs8OdHw==\",\"Count\":\"207\"},{\"裁判要旨段原文\":\"据此，依照《最高人民法院关于适用的解释》第五百一十九条、《最高人民法院关于执行案件立案、结案若干问题的意见》第十六条第一款第（四）项之规定，裁定如下\",\"不公开理由\":\"\",\"案件类型\":\"5\",\"裁判日期\":\"2018-03-10\",\"案件名称\":\"株洲鑫鼎投资担保有限公司与陈慧群、王良旦、王静追偿权纠纷一案终本裁定书\",\"文书ID\":\"FcOOwrcBBDEMw4TDgMKWaFdUSMKnw75Lw7rDuxjDgcKgwozCjnXDusOEwpVMwq8SbsKcwpvCl2dwL8OjLsO4KSRBw6jDiMOowrDDrn0jw63DmsKYPULDvMO4w6zCql4Tax4GwonCicO4Ri7DoGrCvULCnhzDtxzCssOydQHCvQfDmmwXeUTDvcOlwpsyFcOlWsO+w4ptAhXDisKlwrHDtsOiw69QIsO4wpTDsxw1wqjDlsK3aVhjB8O5woPCn27CohnCglnDnmVkw5skfg==\",\"审判程序\":\"\",\"案号\":\"（2017）湘0211执恢54号\",\"法院名称\":\"株洲市天元区人民法院\"},{\"裁判要旨段原文\":\"依照《最高人民法院关于适用〈中华人民共和国民事诉讼法〉的解释》第五百一十九条的规定，裁定如下\",\"不公开理由\":\"\",\"案件类型\":\"5\",\"裁判日期\":\"2018-03-10\",\"案件名称\":\"宁乡县信达小额贷款有限责任公司、宁乡县九龙寨农业科技发展有限公司企业借贷纠纷执行实施类执行裁定书\",\"文书ID\":\"FcKPwrkRRDEMQlvDkmXCpB/DqnLDvyXCrcKXwoAZw6YRwoB1wovChMKGwpfCm8KSwrDCssOOLcKLLibDkBdawpzCu8OVBXfDgC41HV3DnRINVn/CkA93wpdaKF7CksKFwpzCpTPCs8OaPWbDoR7DosK5w7BHw7ZvVMOgO8KZw4jDm3xfacOgTSrCnHbDkMOEw5kXw5jCkMKdw7FwNmnDgcOdD8KpY8KYU8KnZD5ua3h+w6zDtcOGPy05KsO8XMOHwr4rw5XDvnrDiz8=\",\"审判程序\":\"\",\"案号\":\"（2017）湘0124执1699-2号\",\"法院名称\":\"宁乡县人民法院\"},{\"裁判要旨段原文\":\"本院认为：原告与被告结婚时间较长，婚后共同生育了小孩，建立了一定的夫妻感情。夫妻间为琐事发生争吵是婚姻中较为普遍的现象，双方应冷静地处理问题，互相包容，互相理解。原告提交的证据不能证明夫妻感情确已完全破裂，原告要求与被告离婚的诉讼请求，本院依法不予支持。据此，\",\"不公开理由\":\"\",\"案件类型\":\"2\",\"裁判日期\":\"2018-03-10\",\"案件名称\":\"彭某某与周某某离婚纠纷 民事判决书\",\"文书ID\":\"DcKMw4kJAEEIw4Baw7I+wp46asO/JcOtfgLCgRBITsKUw6Rww5Z4PA7Dm0FiLQFzwql1eMOnGcOtw6zCkQYIwoNREF4cUAJBOMKFwr3DisK4PHrDkyxIw45PwrnDmiDDqycOIcKEUcOpIRjCl8KKW8OXUwTCncOhwq0HERo9w7/CocK9wrHCjDZFUUYjZcKVLsOMw6LDn8O6w47Di18AwodVDjbDvsKEwrwXw641ASxuGMOzwoDDkxoSwp0bfw==\",\"审判程序\":\"一审\",\"案号\":\"（2017）湘0381民初2984号\",\"法院名称\":\"湘乡市人民法院\"},{\"裁判要旨段原文\":\"本院经审查认为：民事主体从事民事活动，不得违反法律，不得违背公序良俗。本案中，被告贺某2无视我国的婚姻家庭制度在自己有配偶的情况下与原告贺某1保持不正当男女关系，原告贺某1明知被告有配偶仍与其保持不正当男女关系，双方的行为违背了社会公德，损害了社会的公序良俗。\",\"不公开理由\":\"\",\"案件类型\":\"2\",\"裁判日期\":\"2018-03-10\",\"案件名称\":\"贺某1与贺某2不当得利纠纷一审民事裁定书\",\"文书ID\":\"DcOPSRHDgEAIADBLw5wsT07Dv8KSw5rCicKCRMOYwogMTh0ZZSjCqUTCnljDo8OeMnfCtXDDtsK1Swpbw77DpsOGw4lJW0vDmsKow4BaAggPWRRQwqHDrMKRw6LDjDLCrMKtw5DCocOhRBzCrXfDjUtuw4DCkC3Cv8Ocw5rCgktxNMOoBDUdeMOTV8OWw4vCuMKieEbDnCTDhRFvOcO0wq3CvA3DsQbCv17CmMKmfATCkWxjEsOYwpsVI3/Cp8Ovw4jDrwM=\",\"审判程序\":\"一审\",\"案号\":\"（2017）湘1224民初2184号\",\"法院名称\":\"溆浦县人民法院\"},{\"裁判要旨段原文\":\"依照《中华人民共和国民事诉讼法》第二百四十二条、第二百四十三条、第二百四十四条、第二百五十三条的规定，裁定如下\",\"不公开理由\":\"\",\"案件类型\":\"5\",\"裁判日期\":\"2018-03-10\",\"案件名称\":\"陈顺华、谢军买卖合同纠纷执行实施类执行裁定书\",\"文书ID\":\"DcKOwrcNw4BADMOEVsKSXsK5VMOcfyTCu8OjAcOEwoEzHnvCqMOCYgtZQltFw4gHd8Oew4MADlhWPTQHwovCssO4wrAGw4bDhFfDpsKpSsKPKGPDpMOzw5HDucOJwqTDr3lewrnDvRbDhC17RMO+UMK4GsOtFMKnU21iUMK9wqrDl8Oiw4Ruwo9DwpggNzEhw69dw6DDgsKoTBLDqMOQP8KpHMKcWsOoKsOZw6vDlcO/IyBxw7dnP1Y5w5fCvMKdBMOEPX1gHw==\",\"审判程序\":\"\",\"案号\":\"（2018）湘0104执恢180号\",\"法院名称\":\"长沙市岳麓区人民法院\"},{\"裁判要旨段原文\":\"文字上有误，应予补正，现裁定如下\",\"不公开理由\":\"\",\"案件类型\":\"2\",\"裁判日期\":\"2018-03-10\",\"案件名称\":\"陈晖元诉刘爱芳补正裁定书\",\"文书ID\":\"DcKLw4cJw4BADMOAVnI5wrfCp8Orw74jJR/CgUBSTMOZwoFNITNMCkpPLT0yXMO0wpnDs8OmwpFTw4kAesK/w6woTzLDjsKEwpwjw4XCmGXCtHoQw49hXcKSBsKeRCfCn8K4w5/Cs2vCrMKkw5vCri5aKX8yw75CO8Oww5UPN2hnSW0lw63Cg8K7dS0jQsOQwr/DrsOjw4zCs8K+f8OvRsOVLcKxwqhhX2EWXsOEwqwCw6Fnw6lYYGbDrihiwoTDvgE=\",\"审判程序\":\"一审\",\"案号\":\"（2018）湘0103民初3号\",\"法院名称\":\"长沙市天心区人民法院\"},{\"裁判要旨段原文\":\"本院认为，原告长沙万强通信科技有限公司的撤诉申请，是对其诉权的自行处分，其申请符合法律规定，依照《中华人民共和国民事诉讼法》第一百五十四条第一款之规定，裁定如下\",\"不公开理由\":\"\",\"案件类型\":\"2\",\"裁判日期\":\"2018-03-10\",\"案件名称\":\"长沙市万强通信科技有限公司与湖南有线汝城网络有限公司买卖合同纠纷一审民事裁定书\",\"文书ID\":\"DcOOw4kNADEIBMOBwpRgOAxPwowhw7/CkHbDvy1VwpPClC1GwqrCkVXDqyXCosOCwptIwrRYai/CicKObsKICcOJGz85T8KLw5TCmHDDnx0FT8Kyw6YLTzzDjcOCwrVzbko4LcOBwpTCmxN8w44yw5jCgQXDjBrDkxvDnhNLFRJ9w5/Ds8KJwrIbwodQwqbCs1puVizDjsKSQcKpw6/Cr17Clm/CksKnwr8ZN3DClcOeVsOfMz/DjMO/SMKHw5zCmwAawpHDvMKqPg==\",\"审判程序\":\"一审\",\"案号\":\"（2018）湘0181民初420号\",\"法院名称\":\"浏阳市人民法院\"},{\"裁判要旨段原文\":\"依照《中华人民共和国民事诉讼法》第二百五十七条第（一）项，裁定如下\",\"不公开理由\":\"\",\"案件类型\":\"5\",\"裁判日期\":\"2018-03-10\",\"案件名称\":\"长沙市蓝盾模板科技有限公司与湖南省第三工程有限公司、吴霖建设工程施工合同纠纷执行裁定书\",\"文书ID\":\"DcKNwrcBACAMw4NeSi8jwqTDvH8STMO2IknCsFgCMRPDo8K0SMKfwrg6wq53w7bCssKPwqbDqyzDv3vDpFYmCMOQwqEaXTzCtDRJNzzCnHsPc8ORwpprw4/CtcOTw5gQw5oxCkrCpW5xD2AnJ8Kjb8KqwoMtUcKvJHXDvsKWw5DCp8OxLsOBF8O3T8O3ei4yeFVRw5rCl8KHw70BwplZMMKwwpgwC8KUw4TCrz0lw5bCicKVwp9zGcORQcKLAknDsAc=\",\"审判程序\":\"\",\"案号\":\"（2018）湘0112执154号之一\",\"法院名称\":\"长沙市望城区人民法院\"},{\"裁判要旨段原文\":\"依照《中华人民共和国民事诉讼法》第二百五十七条第（一）项之规定，裁定如下\",\"不公开理由\":\"\",\"案件类型\":\"5\",\"裁判日期\":\"2018-03-10\",\"案件名称\":\"（2017）湘0922执74号李德华申请桃江县德盛环保建材有限责任公司买卖合同纠纷终结执行裁定书\",\"文书ID\":\"DcKOwrcRw4BADMODVlLDtsKrVMOcfyTCq2MBw6LCsBLDiV9CKE8sP8OKccKwVyBMw7BCwoLDh8Kkw6fDpXHDtMOYCsOzcwFQR8OTKSHDmMKjFyLDiFUpw7tcVcKJwrwuw6NpKxo9w50uwolfwrA1wrrDuMKwwoIUI8KObcKIYsKPw7NKfF0Xw5BWwqEKwrzCuEsTWMKeCcKpw7fDrmMuw4XCqsObw4LDhcOAw6w2RHt1PsOcVsO1woVpCk7CsDHCmHo/\",\"审判程序\":\"\",\"案号\":\"（2018）湘0922执74号\",\"法院名称\":\"桃江县人民法院\"},{\"裁判要旨段原文\":\"依据《最高人民法院关于适用＜中华人民共和国民事诉讼法＞的解释》第五百一十九条的规定，裁定如下\",\"不公开理由\":\"\",\"案件类型\":\"5\",\"裁判日期\":\"2018-03-10\",\"案件名称\":\"（2017）湘0922执557号丁勇泉与陈余良交通事故责任纠纷终本裁定书\",\"文书ID\":\"DcKOw5kBADEERFtCHMOxwonCjMO+S8OaLcOgHcKoWxDCnsKVMGnCnhx5w4XDk8K9F8OrEA13woXDl8KbZ8OFwoUHw6TCvsOpWBZ9XSIewrcXUsOww5XCh8O0CjdNw7M5wp5rw6hcHDnCnVDDshddwqfChcOgwpTDvHJHwpXDtsOHwr3CjsKZTcKywpvDi8KJw5ZRFEPCpMKowpTDlcKwWizDtxwKBjx6wqnClsOHw7I3w5ZzwrpqbcOUw41/w7AfO2HDqkrDoFsf\",\"审判程序\":\"\",\"案号\":\"（2017）湘0922执557号\",\"法院名称\":\"桃江县人民法院\"},{\"裁判要旨段原文\":\"\",\"不公开理由\":\"\",\"案件类型\":\"5\",\"裁判日期\":\"2018-03-10\",\"案件名称\":\"谢正宜与洞口县竹市建筑工程有限责任公司林睦健刘成文民间借贷纠纷执行结案通知书\",\"文书ID\":\"DcOIwrcBw4AwCADCsMKXw6jCmMKRw7rDv0nCiUbDqcO2w7DDnFbCkSPCqwzDl8Kyw78lw5Fiw5HDuQJ8w7kJOsKkZMK5w7XDnsKISknDkl4uUHjDrj7CscOJMFPDj0BTYMOgwopLY8OjKcKYO8OjI2sNX3lKA8OPwpDCpWJXwpnCqEDDusOhw4REI1PDs8K2YXrDqm5kw4rDhjnCmBLCkF03wpAgw4zCm8OQw7RmwpvCoQnDiEPChsKnKkrCsSpMegVRwqMf\",\"审判程序\":\"\",\"案号\":\"（2017）湘0525执632号\",\"法院名称\":\"洞口县人民法院\"},{\"裁判要旨段原文\":\"\",\"不公开理由\":\"\",\"案件类型\":\"5\",\"裁判日期\":\"2018-03-10\",\"案件名称\":\"申请执行人李梅先与被执行人廖建光劳务合同纠纷结案通知书\",\"文书ID\":\"FcOMQRJEMQQFw4ArIXgswoPCuMO/wpHDvsOMwrrCqzrDjMOLJhpSwpLDjsKXDMKHZHfCjcKzMl0XwoHCvcKgLsOVw6dJwqrDt8ONa8OhdsKCw6TDlsKswrfDoDVjagPCpcO2U8KaYVXCtcKrwrXDlwvCo8OgOQjCs2VdWQlRwrcKCMKrw6XDpFTCmsK8wrVTwoTChcKndBIjMxQhI0XDh8KNRsOjwpwhw5DCvyrCisO7wrDDvcOsCR/DjMOSIQLCryRgHsKMw7bCqsOJDw==\",\"审判程序\":\"\",\"案号\":\"（2018）湘0124执恢36号\",\"法院名称\":\"宁乡县人民法院\"},{\"裁判要旨段原文\":\"本院认为：人民法院已生效的法律文书，应当得到执行，申请执行人的合法权益应当得到保护。我院依法受理申请执行人的执行申请后，依职权开展执行工作，穷尽了执行措施，被执行人无其他可供执行财产，案件目前不具备继续执行的条件，符合终结本次执行程序的相关规定。据此，本院依据\",\"不公开理由\":\"\",\"案件类型\":\"5\",\"裁判日期\":\"2018-03-10\",\"案件名称\":\"王云林申请王建新、浏阳市新蓝烟花制造有限公司执行裁定书\",\"文书ID\":\"DcKOwrcRw4BADMKAVlLClsK+VMOcfyTCu8Khw6PDgMKVcTjDtjRTXy3DtUDDjsO5XsKTCcK4RD88OsK5XT0NKcKvFMOdw5BDwo3CscOxEEvCj8Ojw54lw7IJEHnCmEwodcOHTwprwp7DqSbCjcKJwrZ3w4lIwqDCt8KYA8K7woNwM8Kmw7pBw5pcwoJtw4/CrxoZZMO4wqUQTcOow6wfw7/Dpy7DjyoQKMK6wrLCgXHCq8KlcWxjfsKkFV4fNMOAwrNpw78A\",\"审判程序\":\"\",\"案号\":\"（2017）湘0181执3330号\",\"法院名称\":\"浏阳市人民法院\"},{\"裁判要旨段原文\":\"依照《中华人民共和国民事诉讼法》第二百四十条、第二百四十二条、第二百四十三条、第二百四十四条、第二百五十三条之规定，裁定如下\",\"不公开理由\":\"\",\"案件类型\":\"5\",\"裁判日期\":\"2018-03-10\",\"案件名称\":\"陈玉英、张树申请执行被执行人刘英民间借贷纠纷执行裁定书\",\"文书ID\":\"FcKOwrcRBEEMw4NawpLClzbClMOtwr/CpMK/T8KYABzDksOnw7TCpDQywpZSw54TAMKgwpJ9wrQTYsObLCPDi0tEw6DCpcOUUg0uw7HCtsK3w7V9EXkuHsKVfMKrworDqMKhDh09eMKveMKMOcO8w7FXPsORw7INwq0CJG4owrd+MTZAw5PDnMKGZRHDtcOfwo87w4HDnMOBTMOFw6g4wp0Pf8K6ZCfDk8OGOcOCwpPCjyXCgnwHGUzDnMOSZsK9w5LDoxNNwqnCkMOhBw==\",\"审判程序\":\"\",\"案号\":\"（2017）湘0105执3169号\",\"法院名称\":\"长沙市开福区人民法院\"},{\"裁判要旨段原文\":\"依照最高人民法院《关于适用〈中华人民共和国民事诉讼法〉的解释》第五百一十九条和《关于执行案件决立案、结案若干问题的意见》第十四条（二）项的规定裁定如下\",\"不公开理由\":\"\",\"案件类型\":\"5\",\"裁判日期\":\"2018-03-10\",\"案件名称\":\"（2017）湘0922执445号中国农业银行股份有限公司桃江县支行申请王新星等合同、无因管理、不当得利纠纷普通执行终结本次执行程序裁定书\",\"文书ID\":\"DcKPw4sRADEIQltSwqMRwo9+YsO/JcOtXjgww4MDUsKywohFfcOaamlBwq8tS8K5wqfDjsOIeTo4O0RKw6caXRDDnMOkwqTCkcKzAcOvbRlFI3ccZcKFCiTDl8OmFMKLw5XDqT/Dn8KMwrwhwpPDjy3DtcKmLVrCmcKzf0N8fcK3e3rCicOVw4F3dMKjIF0vQsOlX3ICw5HDl8KNwpZEIsO1w5fDkcKhwrs2w6o0Q8OKwr5/f0fCvxbDhHnDvAPDt8O+NwYf\",\"审判程序\":\"\",\"案号\":\"（2017）湘0922执445号之三\",\"法院名称\":\"桃江县人民法院\"},{\"裁判要旨段原文\":\"本院经查认为，申请人的财产保全申请符合法律规定，依照《中华人民共和国民事诉讼法》第一百零一条、第一百零三条、第一百五十四条第一款第四项，《最高人民法院关于适用〈中华人民共和国民事诉讼法〉的解释》第一百七十一条之规定，裁定如下\",\"不公开理由\":\"\",\"案件类型\":\"2\",\"裁判日期\":\"2018-03-10\",\"案件名称\":\"首某某与文某财产保全民事裁定书\",\"文书ID\":\"FcKOw4kNA0EMw4Naw7Jtw4/Dk2fDvyVlw7PCowQCw5LCiMOcw6nDnMK5MMOlw5LCrMKtV8KOw5J7ImJPNHPDmmoIw4kXwrxDwonCpEzCgDVFDW3Chk7CoxpjwoDCm1jDt8OJwrvDj3s4wrJBwrhcw4DDsxbCtwYQSMO8wr4Fwo7DpMO6wpMbwr18c19Nd1FjHCdrw73CgcKdaTnCmCsmeicudHEibcKOwrfDtsOLw70iwrlaWHXCiXpcw6vDt8KAPUDCtcOgBw==\",\"审判程序\":\"其他\",\"案号\":\"（2018）湘0703财保23号\",\"法院名称\":\"常德市鼎城区人民法院\"},{\"裁判要旨段原文\":\"据此，依照《最高人民法院关于适用的解释》第五百一十九条规定，裁定如下\",\"不公开理由\":\"\",\"案件类型\":\"5\",\"裁判日期\":\"2018-03-10\",\"案件名称\":\"中国银行股份有限公司湖南湘江新区分行、郭威金融借款合同纠纷执行实施类执行裁定书\",\"文书ID\":\"FcKNw4cRA0EIw4BaIsKHJ8Kww5B/ST5/wqUZwokPw5zDkcKaX8OhworCqADCgikfYMOmdsKRUy/CscOJVTgwwrbDhcKyGcOww5DCtSgUGcK0QsKSwp1ww7ooCALDlVfCisOSwrbCgj3DhHnDuMKCwpdQdkN0wpnDsVVFwo7DmCNNCcOobirCsTzCm0vDnVFkeS9gwqPCvsOLw59zTMKZw4/CrMKBWU/CusOJc1TDuFjDsh0PGsO6wrHDvF9iIxt5wqTDnT8=\",\"审判程序\":\"\",\"案号\":\"（2017）湘0104执1438号之二\",\"法院名称\":\"长沙市岳麓区人民法院\"},{\"裁判要旨段原文\":\"依照《最高人民法院关于适用的解释》第五百一十九条规定，裁定如下\",\"不公开理由\":\"\",\"案件类型\":\"5\",\"裁判日期\":\"2018-03-10\",\"案件名称\":\"长沙锐信现代药机制造有限公司、湖南通源机电科技有限公司民间借贷纠纷执行实施类执行裁定书\",\"文书ID\":\"FcKNwrkRADEIA1vDogfChwZMw78lHcKXw61owrTDksKEeAccwqJoEcKkBDwYScKgw6jCpMOswr1ow5PDhcOdVMKEZMOqwpl3wqvCoAwGw7MEX0vCvATCu8Omw6DCj8KMRMKzK8KJRncowqUywqw7wrDDrsKPwqhQb8Oyw5YWeTU6w7sOI8KNO1nDmWHCpiDCkAXDjsOEwq06dcOewoHDi8OQwpdFVjnDuMK8wpUPwrjCoW3CmsO3w7jCncKYaFdaa8OEw7XDrcKLw6bDtcO3AQ==\",\"审判程序\":\"\",\"案号\":\"（2017）湘0104执2024号之一\",\"法院名称\":\"长沙市岳麓区人民法院\"},{\"裁判要旨段原文\":\"本院认为：根据《中华人民共和国合同法》的规定，依法成立的合同，对当事人具有法律约束力，当事人应当按照约定全面履行自己的合同义务。本案中，原告与被告毛远林通过签订分期付款合同、被告毛远林申请信用卡、原告发放信用卡等一系列的行为，已经形成了信用卡合同，该合同合法有\",\"不公开理由\":\"\",\"案件类型\":\"2\",\"裁判日期\":\"2018-03-10\",\"案件名称\":\"中国工商银行股份有限公司湘潭分行与毛远林、辜姣奇信用卡纠纷一审民事判决书\",\"文书ID\":\"DcKOwrcRw4BACMOAViLChxIew5h/JMK7U8KjwpMiw4jCisOZwohMMMKzw6XCtMKSXsOtwrhPwrRNw7MNV1wXwqfCgXU8w5kQFGMxwohwwqtFw74hXw7Dg3jCmS0QcBw1w5rCiD4zVMOuGVfDjcKrw5s7w53CicK/ajTCjH0CTcOewqDDkGnDkcK3w44CCMOFw6DCo8K6w5vClsK/fSNGGMO0w44Pw6wpcCPCgSQtQsOIMsOma8KBf33CssKLCMOxw58vfcO3AQ==\",\"审判程序\":\"一审\",\"案号\":\"（2017）湘0302民初4013号\",\"法院名称\":\"湘潭市雨湖区人民法院\"},{\"裁判要旨段原文\":\"依照《最高人民法院关于适用的解释》第五百一十九条的规定，裁定如下\",\"不公开理由\":\"\",\"案件类型\":\"5\",\"裁判日期\":\"2018-03-10\",\"案件名称\":\"当代置业（湖南）有限公司申请执行被执行人雷星抚养费纠纷执行裁定书\",\"文书ID\":\"DcOOw4cBw4BACAPDgcKWMMKZJ8Kxw7/CknwFwqw0wo7DnsOOwosbw43CgE10w63DkVdLw5rCpBZ3cgfDnsKLw5rDn8Oaw4p3wpnCmjRNIMOdw6Auw4LDq2DCqEETwpRTwqV0w5o7w67DoXdXYsOrXkbCjgDChzfDnMKmC0xDw7hBfS4lBMO2XsO9U8KhDcO0wrnDmA1OewHCiRoZw6fDhEgrCcOVUz0WwqfDssOHw7fCtsKfwrwHSyR3NMO5w6XDq8OLw51RAsO6Aw==\",\"审判程序\":\"\",\"案号\":\"（2017）湘0105执2867号之一\",\"法院名称\":\"长沙市开福区人民法院\"}]"
    s3 = "[{\"RunEval\":\"w61aw51uwoIwGH0WwowXbVjDtgLDhCsfYcKXXxpiw5BNLiZLZVfDhncfIDIowpXDosKgwqzDqEnDiGdowr/Cn8Ozwp3CnhZIXMOuw6PDrcOuGMOJw7grXcK9wqUyPnzCvMK+w4vDpHPCvcOfw4h1wrLDnTHDn8OzScOAOG1eQALDjHMow6QRGnnCksOtwopTCWsLA8Oew4EsDFYPwoxhccOBCVpHw78gAXTCgBh0DSbDkDDDmAFPaA4tYQVgIAQHDQ/CgnDCtcKIwpLDgzHClcOfUcKaw4hFEFIowrLCizHDv3TDjsOdwqrDq3TDpnTCicKkw4wIw6Ezwq/CmMOgw5TDjMKZT8KYZ8KKw5vDpcOvwr8TwojDpcODwpkHecO5DAnDin7ClMKCTXfCrwzCuF1Mw4HCrcO1w63DhFTDj8KmH8KvShXCqMObFMK1IGh7w6jDiF3CgcOsw4dow63DlgjCu8Knw4c9bnfDu8O+LWBAw5TDkMOQUcOiw5sCHTfDtcOIwplUDcKODsKUKRo2w69HwofCiDHCr2g5ej3Dk8KsAsKxwqjCqsKuwrPDlhLCoxNkwrfCs1fCrCPCnkxawrdFwq1/w6TDjVwJw6bDhsOnJkbCp8O0w7rCqMKdwo1SbHp6w4xlw78Jw5MEwrVnJQ0UcxdAwolCfT3DrsO1XcOpJF/CmsOPw4hWc8OUeMOvw5DCj8OWE8OSwoAPYcKHw4gDwp5aWcOOeMOwAw==\",\"Count\":\"54\"},{\"裁判要旨段原文\":\"本院认为：上诉人鲁彤以非法占有为目的，使用诈骗的方法吸收公众存款，数额特别巨大，其行为已构成集资诈骗罪，依法应予惩处。鉴于鲁彤尚能如实供述自己的罪行，可对其从轻处罚。一审法院根据鲁彤犯罪的事实、犯罪的性质、情节和对于社会的危害程度所作判决，事实清楚，证据确实、\",\"案件类型\":\"1\",\"裁判日期\":\"2015-06-09\",\"案件名称\":\"鲁彤集资诈骗罪二审刑事裁定书\",\"文书ID\":\"FcKOwrkRBEEIA1PDon9MYCDDv8KQbsOPwpHCoVLCtcK6woYiGQdbLMOlw6XCgl/DghfDncOiQsK+AlstFMKgwrNGW8KEw5BqwqMKUsOfGClwwqk4UcKYLCfDvMK9wpTDtT3CqAdrw6nDngnCr8OYGsOPbcKXw6XCtCoTw67Cq8OmwqNrBMOXw6LDsEF6DsOWw7/Cu3XDpsKow6rCjsOnJB7CgsOCw7LCiEc/w7o0bMOgOcOhwqduambDjcKpw5bDsmgxI8OKUUUfJsKkw7wA\",\"审判程序\":\"二审\",\"案号\":\"（2015）高刑终字第248号\",\"法院名称\":\"北京市高级人民法院\"},{\"裁判要旨段原文\":\"本院认为，公民、法人或者其他组织提起行政诉讼，应当属于人民法院行政诉讼受案范围。本案中，＆ｌｄｑｕｏ;城乡效能监察总结报告＆ｒｄｑｕｏ;属于行政机关上下级之间进行内部管理的行为，对外部不具有约束力，亦对相对人的权利义务不产生实际影响。《最高人民法院关于执行﹤中\",\"案件类型\":\"3\",\"裁判日期\":\"2015-06-08\",\"案件名称\":\"徐永庆与中华人民共和国监察部其他二审行政裁定书\",\"文书ID\":\"FcOOw4kRBDEIBEHClwDCoQY9OcO9N2lnw78VGVUkQcKQZAJkWMKvU8OnRD9ODB07c1zDhT1lwo/DtcKywpLDiwPCpzlYw73CilhSwpFvw6sXdCvDusOJw7XCpsKFPzhXAMO8wojDkyFvIz7CkXLDt8OVWMO9woFUJMK2M8KNZHpWLSrDrjLDh0Z+clB8OR08PxnDhyrCl8K+wrtkHDHDksK1LsOjBmYdwojCjFsmw4TDt8KsTHp3wr0f\",\"审判程序\":\"二审\",\"案号\":\"高行终字第1337号\",\"法院名称\":\"北京市高级人民法院\"},{\"裁判要旨段原文\":\"本院认为：本案中，赵清林诉至法院，要求判令北京市市政工程管理处有限公司向其支付2012年和2013年供暖费2700元。经查，赵清林已于1989年在北京市市政工程管理处办理退休，其上述诉讼请求实质为企业是否为退休人员报销供暖费、支付供暖费补贴的事项，因该事项不属\",\"案件类型\":\"2\",\"裁判日期\":\"2015-06-10\",\"案件名称\":\"赵清林福利待遇纠纷申诉、申请民事裁定书\",\"文书ID\":\"DcOMRwHDgEAIADBLw6zDsWQcw74lwrUREAtzZ2QUw6hnw6lWSkHDqMKFL0l4wocew5DDpHXCtU5Lw4XDhALDh8K5w5Bpwo7CmcK5QEjDuMKhw6FWwp4QYMK+W8O1wrHDrVfDvxBzw63Dg8OUw4XDm8OGwpNdRlQwwoHCkcK6Wy81QxZnw7UpV8OfSMK7wo14PcKoWVo8SHLDrTHCgmAvwrLDhz7DicKqUXIXw5PCuQEQw7TCn8K9SXzDt8KOwoxsPg==\",\"审判程序\":\"再审审查与审判监督\",\"案号\":\"（2015）高民申字第01645号\",\"法院名称\":\"北京市高级人民法院\"},{\"裁判要旨段原文\":\"本院认为：当事人对自己提出的诉讼请求所依据的事实有责任提供证据加以证明。没有证据或者证据不能足以证明当事人的事实主张的，由负有举证责任的当事人承担不利后果。本案中，赵汉松主张其存在延时加班、双休日加班及法定节假日加班，但未提供充分证据予以证实，故一、二审法院对\",\"案件类型\":\"2\",\"裁判日期\":\"2015-06-10\",\"案件名称\":\"赵汉松劳动争议申诉、申请民事裁定书\",\"文书ID\":\"DcKNwrkRADAMw4JWw7JvwqfCjMK/w71HSgoaTsKIBsOMTQnDmMOuw6rDncKLBsKqwpHDmVzChcOCBcKbwp7CqEfCp3NSVsOGZcOnJMOawqnCiMKFwpYCwoDDkFjCr8Ksw4HCnnYcwqBDLl/DosO1w6t7wqXDinbCicKMw4oYIMOpw77DiMOsw7TDkMK1P8Khw7NhwrPCosKxwpTCkxwiwpfColHCisKkK8KFw7kQw4LCuH8hA33DrDIBwoYvVsKHacKpwoJSw55ew7vDnwxiw6l+dh4=\",\"审判程序\":\"再审审查与审判监督\",\"案号\":\"（2015）高民申字第01628号\",\"法院名称\":\"北京市高级人民法院\"},{\"裁判要旨段原文\":\"本院认为，公民、法人或者其他组织提起行政诉讼，应当属于人民法院行政诉讼受案范围。本案中，＆ｌｄｑｕｏ;城乡效能监察总结报告＆ｒｄｑｕｏ;属于行政机关上下级之间进行内部管理的行为，对外部不具有约束力，亦对相对人的权利义务不产生实际影响。《最高人民法院关于执行﹤中\",\"案件类型\":\"3\",\"裁判日期\":\"2015-06-08\",\"案件名称\":\"徐学俊与中华人民共和国监察部其他二审行政裁定书\",\"文书ID\":\"FcOMwrkBAzEIBMOAwpZAfMKrEATDtF/DksOZw6kEA8KjUsKveMOTwrlhw5NzPMOhfcOmwozDm8ObG0dewpUtIsOtwp7DkCvCmcK6V8OiwqB6woorEsKlwozDiS57HsOEOFp8HXQ1w4XCqsKRDMORwozDvMOnw6XDocKUXBZ8YzEUw49mc8OwQl3DhsKrw7QYTXTCg09YJiXCmRsbwq7CoMOWEQ0rwqwdwqhvw7w8w5AhRmw7fcK9w7PCsijDpcK+FMK8w7EP\",\"审判程序\":\"二审\",\"案号\":\"（2015）高行终字第1339号\",\"法院名称\":\"北京市高级人民法院\"},{\"裁判要旨段原文\":\"本院认为，公民、法人或者其他组织提起行政诉讼，应当属于人民法院行政诉讼受案范围。本案中，＆ｌｄｑｕｏ;城乡效能监察总结报告＆ｒｄｑｕｏ;属于行政机关上下级之间进行内部管理的行为，对外部不具有约束力，亦对相对人的权利义务不产生实际影响。《最高人民法院关于执行﹤中\",\"案件类型\":\"3\",\"裁判日期\":\"2015-06-08\",\"案件名称\":\"赵桂芬与中华人民共和国监察部其他二审行政裁定书\",\"文书ID\":\"DcKOw4kNADEIA1vCgnBkeWLCjsO+S8Oaw7wsazzDsmnCiMKQQ8K6w70GZMKFw5NXwpc+Y8K0Cl3CjyJKVFsiOsKtw514XwwmwprCt1YgalpwNA1WwpTCscOQw4Zww5DDkcK9PmgOwpvCj8OrfAdNw4hXw5cxeXwWUFcsE1tlwpXDpcKjEMOkwrDDlsK6woptwqkbw4LDhcOjwqpLwp7Dvm48w7XCu8KteU7DksOYHcO1FsO5PMK5XQY+w6TDm8Oow4M0Pw==\",\"审判程序\":\"二审\",\"案号\":\"（2015）高行终字第1343号\",\"法院名称\":\"北京市高级人民法院\"},{\"裁判要旨段原文\":\"本院认为：\\n根据《中华人民共和国立法法》第八十四条并参照国家知识产权局制定的《施行修改后的专利法的过渡办法》的规定，本案应适用《专利法》进行审理。\\n《专利法》第二十二条第二款规定：“新颖性，是指在申请日以前没有同样的发明或者实用新型在国内外出版物上公开发表\",\"案件类型\":\"3\",\"裁判日期\":\"2015-06-08\",\"案件名称\":\"三井化学株式会社与中华人民共和国国家知识产权局专利复审委员会其他二审行政判决书\",\"文书ID\":\"HcKPw4sNRDEIA1vDom84BnjDqcK/wqTCjcO2w6bCkcKswrFMw5nChTrCm8KlPSzDsX07w4EnPA0TBcOAWsOuDivDtcKxw43CgcOXwo1rWwVqHMKDECrDnWIlw4lfwoTDvnslw4txegvCuSLDg8KtOMKuwrDCpz1ww40qw6YtwrvDqnrCvUTDmjPDgXLDksO9w4TDhMOVw6rClVDCnnXDmnvDvcKrwqDCp8OKwp03SMOVw4cnPsO0ZzXDr0DDkMOIw6xaw4hDbgIbRy3DqAc=\",\"审判程序\":\"二审\",\"案号\":\"（2015）高行（知）终字第1050号\",\"法院名称\":\"北京市高级人民法院\"},{\"裁判要旨段原文\":\"本院认为，根据《政府信息公开条例》第二十一条第（一）项的规定，申请公开的政府信息属于公开范围的，行政机关应当告知申请人获取该政府信息的方式和途径。本案中，鞠桂凤向石景山区政府申请公开＆ｌｄｑｕｏ;石景山区政府2003年3月5日作出的《关于常秀金同志反映拆迁补偿\",\"案件类型\":\"3\",\"裁判日期\":\"2015-06-05\",\"案件名称\":\"鞠桂凤与北京市石景山区人民政府信息公开二审行政判决书\",\"文书ID\":\"FcKPw4kNRDEMQltywrzDp2jDh8K4w7/CksOmw48NwpAewojCuHbDgsO2aQHDp8KsW8KAwocxIMKmw4DDusKhWsKCX8OXwqnCpi3DlcKMLzR5wpfCgks5Wz0Ow5ghw7FJwrtMfsKVZMKMXWzCsGNBwqbClkrClA7Dr8Oxw7fCvi1PXFonwrESwq3CtHLDjRcnwrPChcOHesKIQ1nCngw+U8KHw55RwqvDrsKVwpUawpptw6QAI2ZzEx1lGl/Dr8KLwovDug7ChcO+ccOhHw==\",\"审判程序\":\"二审\",\"案号\":\"（2015）高行终字第1304号\",\"法院名称\":\"北京市高级人民法院\"},{\"裁判要旨段原文\":\"本院认为，公民、法人或者其他组织提起行政诉讼，应当属于人民法院行政诉讼受案范围。本案中，＆ｌｄｑｕｏ;城乡效能监察总结报告＆ｒｄｑｕｏ;属于行政机关上下级之间进行内部管理的行为，对外部不具有约束力，亦对相对人的权利义务不产生实际影响。《最高人民法院关于执行﹤中\",\"案件类型\":\"3\",\"裁判日期\":\"2015-06-08\",\"案件名称\":\"吴玉柱与中华人民共和国监察部其他二审行政裁定书\",\"文书ID\":\"FcONw4cBA0EIw4DDgMKWw4jDoQksw7RfwpJ9BWjCpD7DlSA6wrvDjcOgOW3DoVXChTdHQhvDuHQ1bzfDpMK5C8K/wppAw4HDvHdUw5zDgsO5w4bDosKVw57DozXDhlvDg8KJQcOAwojDjBxKwpw3w6LDmErDuMKCRg/DqQJMwrJtwoEBwo81w50qw47DksOGNsKVSD45w4HCj0LCjcKlU8KmBcKgSsK/w5MGw6XChQV5wprDi8O2wrotw5LDs2tGw5rChj4+w6fCmWXDgh8=\",\"审判程序\":\"二审\",\"案号\":\"（2015）高行终字第1341号\",\"法院名称\":\"北京市高级人民法院\"},{\"案件类型\":\"2\",\"裁判日期\":\"2015-06-09\",\"案件名称\":\"吴少英劳动争议申诉、申请民事裁定书\",\"文书ID\":\"DcOOwrkBA0EIBMKwwpbChsOjWQh5w7svw4lOFcOpDkFEwqjDtsOkw5VEwrs/P8OtwpDComfDhmTDjhXDuUkATTtIGUnCvcOOP0hXHxUrPsOjw77CkMKLExrDk8KVwpY3w581w7DChMOJw4PDjDbClXnDrQNbPsKKwrQUTApHw69SUCh2GMO1MWnCjlbDtGXCssOXwolOw5vDhsO8U37CsHPCocOmw7g6MsKqOCbCmsKqwpzDsx3DoMOmwq0+eGnDgsOcKz8=\",\"审判程序\":\"再审\",\"案号\":\"（2015）高民申字第00314号\",\"法院名称\":\"北京市高级人民法院\"}]"
    debug(json.loads(s2.replace("\n", "\/n")))
    debug(analysis(s3))