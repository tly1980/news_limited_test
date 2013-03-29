$(function() {
    // Handler for .ready() called.
    $.getJSON('commits.json', function(data) {
        //console.log(data);
        var tpl = '<tr>{{#committer}}<td>{{name}}</td><td>{{date}})</td>{{/committer}}<td><a href="{{html_url}}" target="_blank">{{sha}}</a></td></tr>';
        var tr_html = '';
        var $tbody =$('tbody.commits');
        $('.repo').text(data.repo)
        for (var i =0; i < data.commits.length; i++){
            li_html = Mustache.render(tpl, data.commits[i]);
            $tbody.append(li_html);
        }

    });
});