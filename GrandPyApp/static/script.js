$("document").ready(function(){

    $("#validate").on('click',function(){
        
        let question = $("#question").val();
        console.log(question);

        $.ajax({
            url: "http://localhost:5000/process",
            type: "POST",
            data: {"question": question},
        }).done(function(data) {
            $('#question').val(data['answer']);
            console.log(data);
        });
    });
});
