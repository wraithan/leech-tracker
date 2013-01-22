$(function() {
    $.ajax({
        'url': '/list/'
    }).done(function(data){
        var list = $('#blockedList')
        JSON.parse(data).forEach(function(element){
            var item = $('<li>', {
                text: parseWhen(element.when)
            })
            item.prepend($('<a>', {
                href: element.url,
                text: element.url,
            }))
            list.append(item)
        })
    })
})

function pad(n) { return n<10 ? '0'+n : n}

function parseWhen(when) {
    var date = new Date(when)
    return (' on ' + date.toDateString() + ' at ' +
            pad(date.getHours()) + ':' + pad(date.getMinutes()))
}
