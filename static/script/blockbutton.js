$(document).ready(function () {
    $(".yourFormId").submit(function () {
        $(".btnSubmit").attr("disabled", true);
        return true;
    });
});
