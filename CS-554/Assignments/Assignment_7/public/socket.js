(function ($) {

    let socket = io.connect('http://localhost:3000');

    $("form").submit(function (event) {
        event.preventDefault();

        let obj = {
            username: $("#username").val(),
            query: $("#query").val(),
            message: $("#message").val()
        }

        console.log("Sending to server");
        socket.emit("receive", obj);

        $("#username").prop("readonly", true);
        $("#query").val('')
        $("#message").val('')
    })

    socket.on('search', (obj) => {
        console.log("Received object");
        let output = $("#results");
        let list = $('<ul>').attr("id", "image-list").addClass('list-group'); 

        output.append(list); 

        list.append($('<li>').text("Username: " + obj.username).addClass('list-group-item'), $('<li>').text("Message: " + obj.message).addClass('list-group-item')); 

        if (obj.results.length == 0) {
            list.append($('<li>').text("Results: None").addClass('list-group-item'))
        } else {
            obj.results.forEach(element => {
                list.append($('<li>').addClass('list-group-item').append('<img src=' + element.largeImageURL + ' style="width:400px;" class="center"/>'))
            });
        }
    })
})(jQuery)
