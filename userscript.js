// ==UserScript==
// @name         Neopets - Shapeshifter Script Maker
// @match        http://www.neopets.com/medieval/shapeshifter.phtml*
// ==/UserScript==

function getDeltas() {
    var pieces = {};
    $("table[border=1][bordercolor='gray']").find("img[name='i_']:not(:first)").each(function(k,v) {
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

var board = getBoard();
var shapes = getShapes();

if(shapes !== null) {
    $(".content").prepend("<center><textarea rows='4' cols='100'>" + board + "\n" + shapes + "</textarea></center>");
}