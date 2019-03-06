from tool.function import getCookie, debug
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}
# url = "http://wenshu.court.gov.cn/list/list/?sorttype=1&number=XJ657HP5&guid=6192d305-0519-670993ab-62b066cd3825&conditions=searchWord+%E9%87%8D%E5%BA%86%E5%B8%82%E7%AC%AC%E4%BA%8C%E4%B8%AD%E7%BA%A7%E4%BA%BA%E6%B0%91%E6%B3%95%E9%99%A2+SLFY++%E6%B3%95%E9%99%A2%E5%90%8D%E7%A7%B0%3A%E9%87%8D%E5%BA%86%E5%B8%82%E7%AC%AC%E4%BA%8C%E4%B8%AD%E7%BA%A7%E4%BA%BA%E6%B0%91%E6%B3%95%E9%99%A2"
url = "https://nl.tan90.club/test/testHeader.html"
debug(getCookie(url, header=header, proxy_ip="60.169.248.56:49933", timeout=5))

# $(function(){$("#con_llcs").html("浏览：508次")});$(function()
#                                                 {var caseinfo=JSON.stringify(
# {"文书ID":"c4e81e21-4737-41fd-b0e1-a8c001115df1", "案件名称":"周飞、江苏天迈投资有限公司执行审查类执行裁定书", "案号":"（2017）最高法执复60号", "审判程序":"", "上传日期":"\/Date(1523462400000)\/", "案件类型":"5", "补正文书":"2", "法院名称":"最高人民法院", "法院ID":"0", "法院省份":"最高人民法院", "法院地市":"", "法院区县":"", "法院区域":"", "文书类型":null, "文书全文类型":"1", "裁判日期":null, "结案方式":null, "效力层级":null, "不公开理由":"", "DocContent":"", "文本首部段落原文":"", "诉讼参与人信息部分原文":"", "诉讼记录段原文":"周飞不服江苏省高级人民法院（以下简称江苏高院）（2017）苏执异23号执行裁定，向本院申请复议。本院依法组成合议庭进行审查，现已审查终结", "案件基本情况段原文":"", "裁判要旨段原文":"", "判决结果段原文":"", "附加原文":"", "文本尾部原文":""});$(
#     document).attr("title", "周飞、江苏天迈投资有限公司执行审查类执行裁定书");$("#tdSource").html("周飞、江苏天迈投资有限公司执行审查类执行裁定书 （2017）最高法执复60号");$(
#     "#hidDocID").val("c4e81e21-4737-41fd-b0e1-a8c001115df1");$("#hidCaseName").val("周飞、江苏天迈投资有限公司执行审查类执行裁定书");$(
#     "#hidCaseNumber").val("（2017）最高法执复60号");$("#hidCaseInfo").val(caseinfo);$("#hidCourt").val("最高人民法院");$(
#     "#hidCaseType").val("5");$("#HidCourtID").val("0");$("#hidRequireLogin").val("0");});$(function()
#                                                                                            {var dirData = {Elements:["RelateInfo", "LegalBase"], RelateInfo:[{name: "审理法院", key: "court", value: "最高人民法院"}, {name: "案件类型", key: "caseType", value: "执行案件"}, {name: "案由", key: "reason", value: ""}, {name: "裁判日期", key: "trialDate", value: "2018-01-01"}, {name: "当事人", key: "appellor", value: "周飞,江苏天迈投资有限公司,陶明"}], LegalBase:[{法规名称:'《中华人民共和国民事诉讼法》', Items:[{法条名称:'第二百二十五条', 法条内容:'第二百二十五条   系统尚未收录或引用有误&amp;#xA;'}]}]}; if ($("#divTool_Summary").length > 0) {$(
#     "#divTool_Summary").ContentSummary({data: dirData});}});$(function() {
# var jsonHtmlData = "{\"Title\":\"周飞、江苏天迈投资有限公司执行审查类执行裁定书\",\"PubDate\":\"2018-04-12\",\"Html\":\"<div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'><p></div><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'><title></title></div><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'></p></div><a type='dir' name='WBSB'></a><div style='TEXT-ALIGN: center; LINE-HEIGHT: 25pt; MARGIN: 0.5pt 0cm; FONT-FAMILY: 宋体; FONT-SIZE: 22pt;'>中华人民共和国最高人民法院</div><div style='TEXT-ALIGN: center; LINE-HEIGHT: 30pt; MARGIN: 0.5pt 0cm; FONT-FAMILY: 仿宋; FONT-SIZE: 26pt;'>执 行 裁 定 书</div><div style='TEXT-ALIGN: right; LINE-HEIGHT: 30pt; MARGIN: 0.5pt 0cm;  FONT-FAMILY: 仿宋;FONT-SIZE: 16pt; '>（2017）最高法执复60号</div><a type='dir' name='DSRXX'></a><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>复议申请人（申请执行人）：周飞，男，汉族，1954年9月9日出生，住。</div><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>委托诉讼代理人：熊智，北京市北斗鼎铭律师事务所律师。</div><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>被申请人：江苏天迈投资有限公司，住所地江苏省南京市建邺区。</div><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>法定代表人：朱岩，该公司董事长。</div><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>被执行人：陶明，男，汉族，1963年生，住。</div><a type='dir' name='SSJL'></a><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>周飞不服江苏省高级人民法院（以下简称江苏高院）（2017）苏执异23号执行裁定，向本院申请复议。本院依法组成合议庭进行审查，现已审查终结。</div><a type='dir' name='AJJBQK'></a><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>原告周飞与被告陶明、中住佳展地产（徐州）有限公司、中佳（徐州）房地产开发有限公司、江苏天迈投资有限公司（以下简称天迈投资公司）、江苏青石置业有限公司（前身为南京天迈置业有限公司，2014年11月24日更为现名）、第三人重庆首创环境治理有限公司（前身为重庆海众房地产开发有限公司，2014年4月21日更为现名）股权及权益转让纠纷一案，江苏高院于2014年9月10日作出（2012）苏商初字第0005号民事判决：一、陶明应自本判决生效后10日内向周飞支付2.555亿元人民币并支付至2012年5月25日起诉之日，按中国人民银行同期流动资金贷款基准利率计算的利息。二、驳回周飞其他诉讼请求。周飞、陶明不服上述判决，均向本院提出上诉。本院于2016年12月24日作出（2014）民二终字第259号民事判决：驳回上诉，维持原判。因陶明未按上述生效判决履行义务，周飞向江苏高院申请执行，该院于2017年1月5日立案执行，案号为（2017）苏执1号。执行过程中，周飞向江苏高院提交书面申请，申请追加天迈投资公司为被执行人。</div><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>周飞申请称，根据最高人民法院（2014）民二终字第259号民事判决第20页查明的内容，可以认定天迈投资公司实为陶明个人开办的独资企业，其享有该公司100%的股权。依据《最高人民法院关于民事执行中变更、追加当事人若干问题的规定》（以下简称变更追加规定）第一条及《最高人民法院关于人民法院执行工作若干问题的规定（试行）》（以下简称执行规定）第53条、第54条的规定，请求追加天迈投资公司为被执行人。</div><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>天迈投资公司辩称，执行中追加被执行人应限于法律和司法解释明确规定的情形。天迈投资公司的股东为上海鑫圯环保科技有限公司（以下简称鑫圯公司），其与本案申请执行人和被执行人均无关联。最高人民法院未判令天迈投资公司承担责任，最高人民法院（2014）民二终字第259号民事判决第20页中的有关内容不能作为申请追加天迈投资公司为被执行人的依据。请求驳回周飞的追加被执行人申请。</div><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>陶明辩称，周飞申请追加天迈投资公司为被执行人无事实法律依据，应予以驳回。</div><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>江苏高院异议程序中查明，本院在（2014）民二终字第259号民事判决书第20页“本院认为”部分中认定：本案的实际情况表明，本案当事人通过间接、迂回的方式持有投资性权益的做法在一定程度上具有一贯性和连续性，并不限于2011年6月8日《协议》签订之前。以天迈投资公司的股权为例，在股权让与担保的负担解除后，陶明本可登记为享有天迈投资公司100%股权的股东。但目前天迈投资公司的股权并未实际登记在陶明名下，而是在陶明的安排下辗转变更至王笠、陶一华名下。陶明虽然未登记为天迈投资公司的股东，其通过王笠、陶一华代持股权的方式并不改变其对天迈投资公司的实际控制关系。</div><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>江苏高院另查明，天迈投资公司的类型为有限责任公司（非自然人投资或控股的法人独资），现股东为鑫圯公司，该公司的营业执照载明，公司成立日期为2010年3月10日，类型为有限责任公司（台港澳法人独资），注册资本为人民币100万，住所地在上海市闵行区。2017年5月3日，江苏高院向江苏省工商行政管理局发出协助执行通知书（附民事裁定），请求协助冻结陶明（鑫圯公司代持有）所持有的天迈投资公司100%股权及配股、收益、红利。</div><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>江苏高院认为，变更追加规定第一条规定：“执行过程中，申请执行人或其继承人、权利承受人可以向人民法院申请变更、追加当事人。申请符合法定条件的，人民法院应予支持。”根据上述规定，申请追加天迈投资公司为被执行人应符合法定条件，否则不应支持。《最高人民法院关于人民法院执行工作若干问题的规定（试行）》（以下简称执行规定）第53条规定：“对被执行人在有限责任公司、其他法人企业中的投资权益或股权，人民法院可以采取冻结措施。冻结投资权益或股权的，应当通知有关企业不得办理被冻结投资权益或股权的转移手续，不得向被执行人支付股息或红利。被冻结的投资权益或股权，被执行人不得自行转让。”第54条规定：“被执行人在其独资开办的法人企业中拥有的投资权益被冻结后，人民法院可以直接裁定予以转让，以转让所得清偿其对申请执行人的债务。对被执行人在有限责任公司中被冻结的投资权益或股权，人民法院可以依据《中华人民共和国公司法》第三十五条、第三十六条的规定，征得全体股东过半数同意后，予以拍卖、变卖或以其他方式转让。不同意转让的股东，应当购买该转让的投资权益或股权，不购买的，视为同意转让，不影响执行。人民法院也可允许并监督被执行人自行转让其投资权益或股权，将转让所得收益用于清偿对申请执行人的债务。”根据上述规定，人民法院可以对被执行人在有限责任公司、其他法人企业、独资开办的法人企业中的投资收益或股权依法执行，但上述规定并未规定可以追加被执行人所投资或入股的公司为被执行人。天迈投资公司为有限责任公司，现股东为鑫圯公司，最高人民法院（2014）民二终字第259号民事判决中未认定陶明是鑫圯公司所持天迈公司股权的实际持有人，周飞适用上述规定申请追加天迈投资公司为被执行人无事实法律依据，不予支持。江苏高院已对天迈投资公司的股权采取冻结措施，能否执行该股权应在另案鑫圯公司提起的案外人异议程序中处理。据此，依照《中华人民共和国民事诉讼法》第一百五十四条第一款第十一项，变更追加规定第一条、第三十条之规定，江苏高院于2017年8月21日作出（2017）苏执异23号执行裁定：驳回周飞申请追加天迈投资公司为被执行人的申请。</div><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>周飞不服江苏高院上述裁定，向本院申请复议，主要理由为：一、陶明为天迈投资公司的实际控制人并享有相应权益是的事实已由最高人民法院生效判决确认。最高人民法院（2014）民二终字第259号民事判决书“本院认为”部分认定，陶明虽然未登记为天迈投资公司的股东，其通过王苙、陶一华代持股权的方式并不改变其对天迈投资公司的实际控制关系。二、天迈投资公司实为陶明个人开办的独资企业，其本人享有100%公司股权。三、陶明未按生效判决履行义务，反而进行了财产转移，江苏高院裁定不予追加天迈投资公司为被执行人、并中止对其股权的冻结，是对申请执行人依法享有的权益的进一步伤害。1、天迈投资公司的100%股权从王苙、陶一华手中转让至现在的股东鑫圯公司的行为发生在2015年12月23日，即2014年江苏高院作出陶明应当履行其支付义务的判决之后。2、根据执行规定第53条、第54条等规定，追加天迈投资公司为被执行人于法有据。综上，周飞请求本院撤销江苏高院（2017）苏执异23号执行裁定，依法追加天迈投资公司为被执行人。</div><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>天迈投资公司提交答辩意见称，江苏高院（2017）苏执异23号执行裁定事实清楚、适用法律正确。1、生效判决明确天迈投资公司不承担付款义务。2、陶明非该公司股东，其与他人之间的权益纠纷和该公司及公司股东无关。</div><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>陶明未提交意见。</div><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>本院查明，江苏高院冻结鑫圯公司所持有的天迈投资公司100%股权及配股、收益、红利后，鑫圯公司已对此提起案外人异议，目前相关程序尚在进行过程中。</div><a type='dir' name='CPYZ'></a><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>本院认为，本案的争议焦点为：复议申请人周飞申请追加天迈投资公司为被执行人是否符合法定条件。</div><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>变更追加规定第一条规定，执行过程中，申请执行人或其继承人、权利承受人可以向人民法院申请变更、追加当事人。申请符合法定条件的，人民法院应予支持。根据上述规定，人民法院在执行程序中变更、追加被执行人应当符合必要的法定条件，即应当符合《中华人民共和国民事诉讼法》第二百三十二条、变更追加规定等规定中的条件，否则不应支持。</div><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>本案中，本院在（2014）民二终字第259号民事判决书中认定，陶明通过王苙、陶一华代持股权的方式并不改变其对天迈投资公司的实际控制关系。复议申请人周飞据此提出，陶明是天迈投资公司的实际控制人，天迈投资公司为陶明个人开办的独资企业，其享有100%股权，故根据执行规定第53条、第54条等规定，应追加天迈投资公司为被执行人。执行规定第53条规定，对被执行人在有限责任公司、其他法人企业中的投资权益或股权，人民法院可以采取冻结措施。冻结投资权益或股权的，应当通知有关企业不得办理被冻结投资权益或股权的转移手续，不得向被执行人支付股息或红利。被冻结的投资权益或股权，被执行人不得自行转让。第54条规定，被执行人在其独资开办的法人企业中拥的投资权益被冻结后，人民法院可以直接裁定予以转让，以转让所得清偿其对申请执行人的债务。对被执行人在有限责任公司中被冻结的投资权益或股权，人民法院可以依据《中华人民共和国公司法》第三十五条、第三十六条（现《中华人民共和国公司法》第七十一条、七十二条、七十三条）的规定，征得全体股东过半数同意后，予以拍卖、变卖或以其他方式转让。不同意转让的股东，应当购买该转让的投资权益或股权，不购买的，视为同意转让，不影响执行。分析上述规定，系关于人民法院如何执行被执行人在其独资开办的法人企业或者在有限责任公司、其他法人企业中的股权或投资权益的规定，与人民法院能否追加被执行人并无关联。换言之，即使符合上述规定中的条件，人民法院亦应是直接执行被执行人在相关有限责任公司、企业法人中所有的股权、投资权益，而不能迳行追加有关有限责任公司、企业法人为被执行人。本案中，无论被执行人陶明是否是天迈投资公司的实际控制人，抑或天迈投资公司是否是陶明独资开办的法人企业，人民法院均不能依据执行规定第53条、第54条的规定追加天迈投资公司为被执行人。至于是否可直接执行复议申请人周飞所称的陶明在天迈投资公司的股权、投资权益，应由江苏高院在鑫圯公司提起的案外人异议程序及相关法律程序中审查处理。</div><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>综上，江苏高院（2017）苏执异23号执行裁定驳回周飞申请追加江苏天迈投资有限公司为被执行人的申请并无不当，应予维持。本院依照《中华人民共和国民事诉讼法》第二百二十五条，《最高人民法院关于人民法院办理执行异议和复议案件若干问题的规定》第二十三条第一项规定，裁定如下：</div><a type='dir' name='PJJG'></a><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>驳回复议申请人周飞的复议申请，维持江苏省高级人民法院（2017）苏执异23号执行裁定。</div><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>本裁定为终审裁定。</div><a type='dir' name='WBWB'></a><div style='TEXT-ALIGN: right; LINE-HEIGHT: 25pt; MARGIN: 0.5pt 72pt 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>审 判 长　刘雅玲</div><div style='TEXT-ALIGN: right; LINE-HEIGHT: 25pt; MARGIN: 0.5pt 72pt 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>审 判 员　薛贵忠</div><div style='TEXT-ALIGN: right; LINE-HEIGHT: 25pt; MARGIN: 0.5pt 72pt 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>审 判 员　邱　鹏</div><br/><div style='TEXT-ALIGN: right; LINE-HEIGHT: 25pt; MARGIN: 0.5pt 72pt 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>二〇一八年一月××日</div><div style='TEXT-ALIGN: right; LINE-HEIGHT: 25pt; MARGIN: 0.5pt 72pt 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>法官助理　苏　萌</div><div style='TEXT-ALIGN: right; LINE-HEIGHT: 25pt; MARGIN: 0.5pt 72pt 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>书 记 员　陈晓宇</div>\"}";
# var jsonData
