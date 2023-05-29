// maybe we skipped something  here .-video 139 -Abhishek


$(document).ready(function(){
    // add to cart
    $('.add_to_cart').on('click', function(e){
        e.preventDefault();
        package_id = $(this).attr('data-id');
        alert(package_id);
    })
});