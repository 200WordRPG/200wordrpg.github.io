(function(w, d) {
  function stdOnEnd(script, cb) {
    script.onload = function () {
      this.onerror = this.onload = null;
      cb(null, script);
    };

    script.onerror = function () {
      this.onerror = this.onload = null;
      cb(new Error('Failed to load ' + this.src), script);
    };
  }

  function ieOnEnd(script, cb) {
    script.onreadystatechange = function () {
      if (this.readyState != 'complete' && this.readyState != 'loaded') return;
      this.onreadystatechange = null;
      cb(null, script);
    };
  }

  w.isReady = false;
  w.loadJSDeferred = function(src, cb) {
    function loadJS() {
      w.isReady = true;

      var script = d.createElement('script');
      script.src = src;

      if (cb) {
        ('onload' in script ? stdOnEnd : ieOnEnd)(script, cb);

        if (!script.onload) {
          stdOnEnd(script, cb);
        }
      }

      var ref = d.getElementsByTagName('script')[0];
      ref.parentNode.insertBefore(script, ref);
    }

    if (w.isReady) loadJS();
    else if (w.addEventListener) w.addEventListener("load", loadJS, false);
    else if (w.attachEvent) w.attachEvent("onload", loadJS);
    else w.onload = loadJS;
  }
}(window, document));
