"use strict";

function copyToClipboard(text) {
    const textArea = document.createElement('textarea');
    textArea.textContent = text;
    document.body.append(textArea);
    textArea.select();
    document.execCommand("copy");
    document.body.removeChild(textArea);
}

function copyCodeOnClick(element) {
    const text = element.textContent;
    copyToClipboard(text);
}

function bla() {
    var example_body = document.getElementsByClassName("example-body")[5];
    copyIpythonTerminalOnClick(example_body);
}

function copyIpythonTerminalOnClick(example_body) {
    var in_tags = example_body.getElementsByTagName("code")[0].getElementsByTagName("in");

    var content = "";
    for(var i=0; i < in_tags.length; i++) {
        content += "\n" + in_tags[i].textContent;
    }
    console.log(content);
    copyToClipboard(content);
}


// Find an element with the #qrcode id and replace it with the a QR code
function prepare_qr_code() {
    var element = document.getElementById("qrcode");
    if (element !== null) {
        var url = element.textContent;
        element.textContent = "";
        var qrcode = new QRCode("qrcode", {
            text: url,
            width: 550,
            height: 550,
            colorDark : "black",
            colorLight : "white",
            correctLevel : QRCode.CorrectLevel.H
        });
    }
}
