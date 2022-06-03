//Часы
function startTime() {
    var today = new Date();
    var hours = today.getHours();
    var minutes = today.getMinutes();
    var seconds = today.getSeconds();
    document.getElementById('time').innerHTML =
        hours + ":" + minutes + ":" + seconds;
    var t = setTimeout(startTime, 1000);
}
//Конвертер
function convert(form) {
    var string = form.inputbox.value;
    var money = parseFloat(string);
    $(document).ready(function() {
        $("#fromUSD").click(function () {
            $.getJSON("http://api.fixer.io/latest?base=USD", function (data){
                $("#toUSD").click(function () {
                    $("#div2").empty();
                    var course = parseFloat(data.rates.USD);
                    var result = money *course;
                    $("#div2").append(result);
                });

                $("#toEUR").click(function () {
                    $("#div2").empty();
                    var course = parseFloat(data.rates.EUR);
                    var result = money *course;
                    $("#div2").append(result);
                });

                $("#toGBP").click(function () {
                    $("#div2").empty();
                    var course = parseFloat(data.rates.GBP);
                    var result = money *course;
                    $("#div2").append(result);
                });

                $("#toRUB").click(function () {
                    $("#div2").empty();
                    var course = parseFloat(data.rates.RUB);
                    var result = money *course;
                    $("#div2").append(result);

                });
            });
        });
        $("#fromEUR").click(function () {
            $.getJSON("http://api.fixer.io/latest?base=EUR", function (data){
                $("#toUSD").click(function () {
                    $("#div2").empty();
                    var course = parseFloat(data.rates.USD);
                    var result = money *course;
                    $("#div2").append(result);
                });

                $("#toEUR").click(function () {
                    $("#div2").empty();
                    var course = parseFloat(data.rates.EUR);
                    var result = money *course;
                    $("#div2").append(result);
                });

                $("#toGBP").click(function () {
                    $("#div2").empty();
                    var course = parseFloat(data.rates.GBP);
                    var result = money *course;
                    $("#div2").append(result);
                });

                $("#toRUB").click(function () {
                    $("#div2").empty();
                    var course = parseFloat(data.rates.RUB);
                    var result = money *course;
                    $("#div2").append(result);

                });
            });
        });
        $("#fromGBP").click(function () {
            $.getJSON("http://api.fixer.io/latest?base=GBP", function (data){
                $("#toUSD").click(function () {
                    $("#div2").empty();
                    var course = parseFloat(data.rates.USD);
                    var result = money *course;
                    $("#div2").append(result);
                });

                $("#toEUR").click(function () {
                    $("#div2").empty();
                    var course = parseFloat(data.rates.EUR);
                    var result = money *course;
                    $("#div2").append(result);
                });

                $("#toGBP").click(function () {
                    $("#div2").empty();
                    var course = parseFloat(data.rates.GBP);
                    var result = money *course;
                    $("#div2").append(result);
                });

                $("#toRUB").click(function () {
                    $("#div2").empty();
                    var course = parseFloat(data.rates.RUB);
                    var result = money *course;
                    $("#div2").append(result);

                });
            });
        });
        $("#fromRUB").click(function () {
        $.getJSON("http://api.fixer.io/latest?base=RUB", function (data){
        $("#toUSD").click(function () {
            $("#div2").empty();
            var course = parseFloat(data.rates.USD);
            var result = money *course;
            $("#div2").append(result);
        });

        $("#toEUR").click(function () {
            $("#div2").empty();
            var course = parseFloat(data.rates.EUR);
            var result = money *course;
            $("#div2").append(result);
        });

        $("#toGBP").click(function () {
            $("#div2").empty();
            var course = parseFloat(data.rates.GBP);
            var result = money *course;
            $("#div2").append(result);
        });

        $("#toRUB").click(function () {
            $("#div2").empty();
            var course = parseFloat(data.rates.RUB);
            var result = money *course;
            $("#div2").append(result);

            });
        });
    });

    $("input").click(function(){
        $("#div2").empty();
        money = 0;
    });
});
}