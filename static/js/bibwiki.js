
// JavaScript functions for BibTeX/Bibitem generator for URL
//
// (C) Arshad Mehmood, 2020. https://arshadmehmood.com
//
// Made available under the terms of the GNU GPL v2 or any later version at your
// option.
//

function pageNotFound() {
    alert("That page could not be found via the Wikipedia API. Sorry.");
}

function url_content(url, callback){
  $.ajax({
    url: '/submit',
      type: "POST",
    contentType: 'application/json;charset=UTF-8',
    data: JSON.stringify({url: url}),
    success: callback
  });
}

function updateBibtex() {
    var input = $('#input').val();
    url_content(input,function(data){
      $('#output').text(data[0]);
      $('#output1').text(data[1]);
      $('#sample').html(data[2]);
    });
}

// The following is from http://stackoverflow.com/a/3855394

(function($) {
    $.QueryString = (function(a) {
        if (a == "") return {};
        var b = {};
        for (var i = 0; i < a.length; ++i)
        {
            var p=a[i].split('=');
            if (p.length != 2) continue;
            b[p[0]] = decodeURIComponent(p[1].replace(/\+/g, " "));
        }
        return b;
    })(window.location.search.substr(1).split('&'))
})(jQuery);

