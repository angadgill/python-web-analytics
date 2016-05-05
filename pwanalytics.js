function PageviewTracker (name, pagename) {
  this.name = name;
  this.data = {
    page : pagename,
    count : 0,
  };
}

function PyWebAnalytics() {

  this.send_to_server_ = function(data) {
    //TODO: Send data to server. Where? Which server?
  }
  this.send = function(tracker_type) {
    if (tracker_type == "pageview") {
      //TODO: Instantiate tracker object? 
    }
  }
}

// Serialize dictionary data into querystring
// From: http://stackoverflow.com/questions/1714786/querystring-encoding-of-a-javascript-object
serialize = function(obj) {
  var str = [];
  for(var p in obj)
    if (obj.hasOwnProperty(p)) {
      str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
    }
  return str.join("&");
}

console.log("PyWebAnalytics has loaded!");
