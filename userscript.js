// ==UserScript==
// @name         Neopets - Shapeshifter Script Maker
// @match        http://www.neopets.com/medieval/shapeshifter.phtml*
// ==/UserScript==

function getDeltas() {
    var pieces = {};
    var items = $("table[border=1][bordercolor='gray']").find("img[name='i_']:not(:last)").get();
    items.splice(0, 0, items.pop());
    $(items).each(function(k,v) {
        pieces[$(v).attr("src").substr(0,52)] = k; // use substr up to 52 just in case mouseover is triggered
    });
    return pieces;
}

var deltas = getDeltas();

function tableScripter(table) {
    var lines = [];
    table.find("tr").each(function(k,v) {
        var line = '';
        $(v).find("td").each(function(k1,v1) {
            line += $(v1).find("img").length;
        });
        lines.push(line);
    });
    return "'" + lines.join() + "'";
}

function getShapes() {
    var shapes = [];
    $($("big")[1]).parent().parent().find("table[cellpadding='0']").each(function(k1,v1) {
        shapes.push(tableScripter($(v1)));
    });
    if(!shapes.length) {
        return null;
    }
    return "pieces = [" + shapes.join(", ") + "]";
}

function getBoard() {
    var lines = [];
    $("table[align=center][cellpadding=0][cellspacing=0][border=0]").find("tr").each(function(k,v) {
        var line = '';
        $(v).find("img").each(function(k1,v1) {
            line += deltas[$(v1).attr("src").substr(0,52)];
        });
        lines.push(line);
    });
    return "board = Board('" + lines.join() + "', " + (Object.keys(deltas).length - 1) + ")";
}

$("#copy").live( "click", function() {
    var $temp = $("<textarea>");
    $("body").append($temp);
    $temp.val(getBoard() +"\n" + getShapes()).select();
    document.execCommand("copy");
    $temp.remove();
    $("#copy").fadeOut();
});

$("table[border=1][bordercolor='gray']").after("<p><center><button id='copy'>Copy Board Code</button></center>");
