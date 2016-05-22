// docCookies cookie library copied from:
// https://developer.mozilla.org/en-US/docs/Web/API/Document/cookie/Simple_document.cookie_framework
var docCookies = {
  getItem: function (sKey) {
    if (!sKey) { return null; }
    return decodeURIComponent(document.cookie.replace(new RegExp("(?:(?:^|.*;)\\s*" + encodeURIComponent(sKey).replace(/[\-\.\+\*]/g, "\\$&") + "\\s*\\=\\s*([^;]*).*$)|^.*$"), "$1")) || null;
  },
  setItem: function (sKey, sValue, vEnd, sPath, sDomain, bSecure) {
    if (!sKey || /^(?:expires|max\-age|path|domain|secure)$/i.test(sKey)) { return false; }
    var sExpires = "";
    if (vEnd) {
      switch (vEnd.constructor) {
        case Number:
          sExpires = vEnd === Infinity ? "; expires=Fri, 31 Dec 9999 23:59:59 GMT" : "; max-age=" + vEnd;
          break;
        case String:
          sExpires = "; expires=" + vEnd;
          break;
        case Date:
          sExpires = "; expires=" + vEnd.toUTCString();
          break;
      }
    }
    document.cookie = encodeURIComponent(sKey) + "=" + encodeURIComponent(sValue) + sExpires + (sDomain ? "; domain=" + sDomain : "") + (sPath ? "; path=" + sPath : "") + (bSecure ? "; secure" : "");
    return true;
  },
  removeItem: function (sKey, sPath, sDomain) {
    if (!this.hasItem(sKey)) { return false; }
    document.cookie = encodeURIComponent(sKey) + "=; expires=Thu, 01 Jan 1970 00:00:00 GMT" + (sDomain ? "; domain=" + sDomain : "") + (sPath ? "; path=" + sPath : "");
    return true;
  },
  hasItem: function (sKey) {
    if (!sKey) { return false; }
    return (new RegExp("(?:^|;\\s*)" + encodeURIComponent(sKey).replace(/[\-\.\+\*]/g, "\\$&") + "\\s*\\=")).test(document.cookie);
  },
  keys: function () {
    var aKeys = document.cookie.replace(/((?:^|\s*;)[^\=]+)(?=;|$)|^\s*|\s*(?:\=[^;]*)?(?:\1|$)/g, "").split(/\s*(?:\=[^;]*)?;\s*/);
    for (var nLen = aKeys.length, nIdx = 0; nIdx < nLen; nIdx++) { aKeys[nIdx] = decodeURIComponent(aKeys[nIdx]); }
    return aKeys;
  }
};
//  End docCookies

function PageviewTracker (name, pagename) {
  this.name = name;
  this.data = {
    page : pagename,
    count : 0,
  };
}

function PyWebAnalytics() {

  this.data = {};
  this.cookie_name = '_pwa';
  this.cookie_expire = 63072000;

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

  this.generate_user_id= function() {
    // rfc4122 v4 compliant uuid 
    // From: http://stackoverflow.com/questions/105034/create-guid-uuid-in-javascript
    var rfc4122_v4 = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
      var r = Math.random()*16|0, v = c == 'x' ? r : (r&0x3|0x8);
      return v.toString(16);
    });
    
    // Append current timestamp
    return rfc4122_v4 + '.' + new Date().getTime().toString();
  }

  this.send = function() {
    var i = new Image();
    var request_url = "//collector.pywebanalytics.org/?" + this.serialize(this.data);
    i.src = request_url;
  }

  this.set_param = function(param, value) {
    this.data[param] = value; 
  }

  this.init_cookie = function() {
    var user_id = docCookies.getItem(this.cookie_name) || this.generate_user_id();
    docCookies.setItem(this.cookie_name, user_id, this.cookie_expire);
    this.set_param('user_id', user_id);
  }

  this.init = function() {
    this.init_cookie();
  }

  this.init();
}

var pwa = new PyWebAnalytics();

// Set pagename to be URL for now
pwa.set_param("pagename", window.location.href);

// Phone home (to collector)
pwa.send();

console.log("PyWebAnalytics has loaded!");
