$(function() {
    var blockedUrl = (/url=(.+?)(&|$)/.exec(location.search)||[,null])[1]
    document.getElementById('url').textContent = blockedUrl
    $.ajax({
        'url': '/blocked/',
        'contentType': 'application/data',
        'data': JSON.stringify({'url': blockedUrl}),
        'type': 'POST',
    })
})
