<!doctype html>
<html lang="pl">
<?php

loadPartial('head.php');

$line_id = $_GET['id'];

?>

<body class="products">

<?php loadPartial('header.php'); ?>

<h1>Szczegóły linii: <?= $line_id ?> </h1>

<div class="line-details" data-line="<?= $line_id ?>">



</div>
<script src="/dist/application.js"></script>
<script>
    (function() {
        $(document).ready(function () {
            lineDetails.init();
        });
    })(jQuery);
</script>
</body>