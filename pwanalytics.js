function PageviewTracker (name, pagename) {
  this.name = name;
  this.data = {
    page : pagename,
    count : 0,
  };
}

function PyWebAnalytics() {

  this.data = {};

  // Serialize dictionary data into querystring
  // From: http://stackoverflow.com/questions/1714786/querystring-encoding-of-a-javascript-object
  this.serialize = function(obj) {
    var str = [];
    for(var p in obj)
      if (obj.hasOwnProperty(p)) {
        str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
      }
    return str.join("&");
  }

  this.send = function() {
    var i = new Image();
    var request_url = "//localhost:5000/collect?" + this.serialize(this.data);
    i.src = request_url;
  }

  this.set_param = function(param, value) {
    this.data[param] = value; 
  }
}

var pwa = new PyWebAnalytics();

// Set pagename to be URL for now
pwa.set_param("pagename", window.location.href);

// Phone home (to collector)
pwa.send();

console.log("PyWebAnalytics has loaded!");
