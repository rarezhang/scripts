conn = new Mongo("127.0.0.1:27017")
db = conn.getDB('pima')
print(db)

var months = ["Apr", "May", "Jun", "Jul", "Aug", "Sep"]
var mon_len = months.length;

for (var  k = 0; k < mon_len; k++) {
    m = months[k];
    for (var i=1;i<32;i++) {
        if (i < 10) {
            var time= m + ' 0' + i;
            var j=db.tweets.find({created_at:{$regex: time}}).count();
            print(time + ':' + j);
         }
        else {
            var time = m + ' ' + i;
            var j=db.tweets.find({created_at:{$regex: time}}).count();
            print(time + ':' + j);
        }
     
     }
}



