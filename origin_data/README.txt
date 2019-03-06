首先拿到guid
构造一个js函数
function getGuidChild(){
    return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1);
}

然后是
function getGuid(){
    return getGuidChild()+getGuidChild()+'-'+getGuidChild()+'-'+getGuidChild()+getGuidChild()+'-'+getGuidChild()+getGuidChild()+getGuidChild();
}
这样就拿到了guid

接下来number参数是wens

接下来通过cookie拿到vjkl5的值，传入接口(GET方式)
这个在python访问列表页的时候就拿到(时间是1个小时，40分钟重新拿一次，也就是整个流程重新来一次)

然后接口页通过js输出

