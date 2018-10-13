var lineDetails = (function () {

    var that = {};

    that.init = function() {
        var detailsContainer = $('.line-details'),
            lineId = detailsContainer.data('line'),
            lines = [];

        $.ajax('/data/lines.json', {
            dataType: 'json',
            method: 'get',
            success: function(data) {
                console.log(data);
                lines = data['lines'];
            }
        });

        console.log('Szczegóły linii: ' + lineId);
    };

    return that;

})(jQuery);

var linesList = (function () {

    var that = {};

    that.init = function() {
        $.ajax('/data/lines.json', {
            dataType: 'json',
            method: 'get',
            success: function(data) {
                displayLineBlocks(data['lines']);
            }
        });
    };

    function displayLineBlocks(lines) {
        console.log(lines);
        for(var i = 0; i < lines.length; i++) {
            var id = lines[i].hasOwnProperty('ID') ? lines[i]['ID'] : null;
            var name = lines[i].hasOwnProperty('Name') ? lines[i]['Name'] : null;

            if(id && name) {
                createLineBlock(id,name);
            }

        }
    }

    function createLineBlock(id,name) {
        var template = $('.line-block-template'),
            list = $('.lines-list'),
            html = template.html();

        html = html.split('__ID__').join(id);
        html = html.split('__NAME__').join(name);

        list.append(html);

    }

    return that;

})(jQuery);