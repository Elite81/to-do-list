$(document).ready(function (){
    $("#form").on("submit", function (e){
        e.preventDefault();

        const form = $(this);

        

        $.ajax({
            url:window.location.href,
            method: "POST",
            data: form.serialize(),
            success: function(response){
                $("#task-list").append(`
                    <li data-id="${response.id}">
                        ${response.task} (${response.tatus})
                    </li>
                `);

                form[0].reset();
                $(".invalid-feedback").remove();
                $(".is-invalid").removeClass("is-invalid");
            },
            error: function(xhr){
                const errors = xhr.responseJSON.errors;
                $(".invalid-feedback").remove();
                $(".is-invalid").removeClass("is-invalid");
                $.each(errors, function (field, messages) {
                    const input = $("#id_" + field)
                    input.addClass("is-invalid");
                    input.after(`
                        <div class="invalid-feedback">
                            ${messages[0]}
                        </div>
                    `);
                });
            }

                
        });
    });
});