let ns = {};

// Create the model instance
ns.model = (function() {
    'use strict';

    let $event_pump = $('body');

    // Return the API
    return {
        'read': function() {
            let ajax_options = {
                type: 'GET',
                url: 'api/cities',
                accepts: 'application/json',
                dataType: 'json'
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_read_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        create: function(cityname) {
            let ajax_options = {
                type: 'POST',
                url: 'api/cities',
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify({
                    'cityname': cityname
                })
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_create_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        update: function(data, cityname) {
            let ajax_options = {
                type: 'PUT',
                url: 'api/cities/' + cityname,
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify({
                    'data': data,
                    'cityname': cityname
                })
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_update_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        'delete': function(cityname) {
            let ajax_options = {
                type: 'DELETE',
                url: 'api/cities/' + cityname,
                accepts: 'application/json',
                contentType: 'plain/text'
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_delete_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        }
    };
}());

ns.view = (function() {
    'use strict';

    var $data = $('#data'),
        $cityname = $('#cityname');

    return {
        reset: function() {
            $cityname.val('');
            $data.val('').focus();
        },
        update_editor: function(data, cityname) {
            $data.val(data);
            $cityname.val(cityname).focus();
        },
        build_table: function(cities) {
            let rows = ''

            $('.cities table > tbody').empty();

            if (cities) {
                for (let i=0, l=cities.length; i < l; i++) {
                    rows += `<tr><td class="cityname">${cities[i].cityname}</td><td>${cities[i].data}</td></tr>`;
                }
                $('table > tbody').append(rows);
            }
        },
        error: function(error_msg) {
            $('.error')
                .text(error_msg)
                .css('visibility', 'visible');
            setTimeout(function() {
                $('.error').css('visibility', 'hidden');
            }, 3000)
        }
    };
}());

ns.controller = (function(m, v) {
    'use strict';

    let model = m,
        view = v,
        $event_pump = $('body'),
        $cities = $('#cities'),
        $data = $('#data');

    setTimeout(function() {
        model.read();
    }, 100)

    function validate(cityname) {
        return cityname !== "";
    }

    $('#create').click(function(e) {
        let cityname = $('#cityname').val(),
            data = $data.val();

        e.preventDefault();

        if (validate(cityname)) {
            model.create(cityname)
        } else {
            alert('Problem retrieving city data');
        }
    });

    $('#update').click(function(e) {
        let cityname = $cityname.val(),
            data = $data.val();

        e.preventDefault();

        if (validate(cityname)) {
            model.update(data, cityname)
        } else {
            alert('Problem retrieving city data');
        }
        e.preventDefault();
    });

    $('#delete').click(function(e) {
        let cityname = $cityname.val();

        e.preventDefault();

        if (validate('placeholder', cityname)) {
            model.delete(cityname)
        } else {
            alert('Problem deleting city');
        }
        e.preventDefault();
    });

    $('#reset').click(function() {
        view.reset();
    })

    $('table > tbody').on('dblclick', 'tr', function(e) {
        let $target = $(e.target),
            cityname,
            data;

        cityname = $target
            .parent()
            .find('td.cityname')
            .text();

        data = $target
            .parent()
            .find('td.data')
            .text();

        view.update_editor(data, cityname);
    });

    // Handle the model events
    $event_pump.on('model_read_success', function(e, data) {
        view.build_table(data);
        view.reset();
    });

    $event_pump.on('model_create_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_update_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_delete_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_error', function(e, xhr, textStatus, errorThrown) {
        let error_msg = textStatus + ': ' + errorThrown + ' - ' + xhr.responseJSON?.detail;
        view.error(error_msg);
        console.log(error_msg);
    })
}(ns.model, ns.view));