function showpage() {
    var sess = getParameterByName('session');
    if (sess) {
        var div = document.getElementById("container");
        div.style.display='block';
        document.write('<script src="sessions/' + sess + '"></script>')
    } else {
        var div = document.getElementById("welcome");
        div.style.display = "block";
    }
} 

function dxreplay(sess,w,t) {
    console.log("GOT " + sess);
    if (sess) {
        var div = document.getElementById("container");
        div.style.display='block';
        div.style.width = w;
        document.write('<script src="/static/sessions/' + sess + '"></script>')
    } else {
        document.write('<p>hello world</p>')
    }
    
}

function getParameterByName(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}
