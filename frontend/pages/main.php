<!doctype html>
<html lang="pl">
<?php loadPartial('head.php'); ?>

<?php
//
//$lines = [
//    123 => 'Pętla A',
//    124 => '',
//    125 => '',
//    126 => '',
//    225 => '',
//    228 => '',
//    304 => '',
//    312 => '',
//    354 => '',
//    420 => '',
//    468 => '',
//    502 => ''
//]
//
//?>

<body class="">

<?php loadPartial('header.php'); ?>

<div class="main-container">
    <h1>Wybierz linię</h1>
    <ul class="row lines-list">
    </ul>
</div>
<div class="line-block-template">
    <li class="col-xs-12 col-sm-6 col-md-4 col-lg-3">
        <a class="line-block" href="/line?id=__ID__">
            ID Linii: __ID__<br/>
            Nazwa: __NAME__
        </a>
    </li>
</div>
<script src="/dist/application.js"></script>
<script>
    (function() {
        $(document).ready(function () {
            linesList.init();
        });
    })(jQuery);
</script>
</body>

