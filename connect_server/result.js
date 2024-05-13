var http=require('https');
var fs=require('fs');
//網域名稱172.20.10.9
var hostname='自己的網域名稱';
var port=8080;
//讀取json檔案
fs.readFile('檔案路徑/value.js',function(err,Info){
  if(err){
    return console.error(err);
  }
  var value=Info.toString();
})
//放server顯示的資料
var server=http.createServer(function(req,res){
  res.statusCode=200;
  res.setHeader('Content-Type','text/plain');
  res.end(value);
})
server.listen(port,hostname);
