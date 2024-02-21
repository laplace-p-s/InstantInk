function save_announce(is_auto){
    var date = new Date();
    var Y = date.getFullYear();
    var M = ("00" + (date.getMonth()+1)).slice(-2);
    var D = ("00" + date.getDate()).slice(-2);
    var h = ("00" + date.getHours()).slice(-2);
    var m = ("00" + date.getMinutes()).slice(-2);
    var s = ("00" + date.getSeconds()).slice(-2);
    var date_text = Y + '/' + M + '/' + D + ' ' + h + ':' + m + ':' + s;
    if(is_auto){
        $('#saveinfo').text('Auto Saved (' + date_text +')');
    }else{
        $('#saveinfo').text('Saved (' + date_text +')');
    }
};

function auto_save(){
    if($('#auto_save_switch').prop("checked")){
        $.post(window.location.href, {text: $('#editor').val()}, function() {
            save_announce(true);
        });
    }
};

$(document).ready(function() {
    $.get('file.txt', function(data) {
        $('#editor').val(data);
    });
    $.get('fileinfo', function(data) {
        $('#fileinfo').text(data);
    });
    $('#save').click(function() {
        $.post(window.location.href, {text: $('#editor').val()}, function() {
            save_announce(false);
        });
    });
    $(window).bind('keydown', function(e) {
        if (e.ctrlKey || e.metaKey) {
            switch (String.fromCharCode(e.which).toLowerCase()) {
                case 's':
                    e.preventDefault();
                    $.post(window.location.href, {text: $('#editor').val()}, function() {
                        save_announce(false);
                    });
                    break;
            }
        }
    });
    // Auto save every 10 seconds
    setInterval(auto_save, 10000);
});
