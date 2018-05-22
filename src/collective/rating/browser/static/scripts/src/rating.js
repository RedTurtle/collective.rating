require.config({
    "paths": {
      "rating": PORTAL_URL + "/++plone++collective.rating/scripts/src/jquery.star-rating-svg",
    }
});
requirejs(["jquery", "rating"], function($, rating){

  function get_portal_url(){
    return $('base').attr('href') || $('body').attr('data-base-url') || window.PORTAL_URL || '';
  }

  function reload_average(){
    $.post(baseUrl + '/get_avg_rating', {}, function (data) {
      data = JSON.parse(data);
      $(".average-rating").starRating('setRating', data['avg_rating'], false);
      $(".num_rating").text(data['num_rating'])
    });
  }

  function get_star_size_my_rating(data){
    $.post(baseUrl + '/get_star_size', {}, function (max_rating){
      var totalStars = JSON.parse(max_rating)['max_rating'];
      render_my_rating(data, totalStars);
    });
  }

  function get_star_size_avg_rating(data){
    $.post(baseUrl + '/get_star_size', {}, function (max_rating){
      var totalStars = JSON.parse(max_rating)['max_rating'];
      render_avg_rating(data, totalStars);
    });
  }

  function render_my_rating(data, totalStars){
    data = JSON.parse(data);
    $(".my-rating").starRating({
        totalStars: totalStars,
        starSize: 25,
        disableAfterRate: false,
        useFullStars: true,
        initialRating: data['current_value'],
        callback: function(currentRating, $el){
          baseUrl = get_portal_url();
          $.post(baseUrl + '/update_rating', {
            current_rating: currentRating,
          }, function (data) {
            reload_average();
          });
        }
    });
    $(".my-rating").children().each(
      function( index ){
        $(this).attr('tabindex', 0);
        $(this).attr('title', parseInt(index) + 1);
        $(this).keyup(function(event) {
            if (event.keyCode === 13) {
                $( this ).click();
            }
        });
        $( this ).focus(function(){
          $( this ).trigger("mouseover");
        });
      }
    );
  }

  function render_avg_rating(data, totalStars){
    data = JSON.parse(data);
    $(".average-rating").starRating({
        totalStars: totalStars,
        starSize: 25,
        readOnly: true,
        useFullStars: true,
        initialRating: data['avg_rating'],
    });
    $(".num_rating").text(data['num_rating'])
  }

  $(document).ready(function(){
    baseUrl = get_portal_url();

    $('.delete-rating').on('click', function(){
      $.post(baseUrl + '/delete_rating', {}, function(data){
        $('.my-rating').starRating('setRating', 0, false);
        reload_average();
      })
    })

    if($('.average-rating').length > 0){
      $.post(baseUrl + '/get_avg_rating', {}, function(data){
        get_star_size_avg_rating( data );
      });
    }

    if($('.my-rating').length > 0){
      $.post(baseUrl + '/get_rating', {}, function(data){
        get_star_size_my_rating( data );
      });
    }

    if($('.rating-collection').length > 0){
      $('.rating-collection').each(function(){
        result = $(this).data('rating');
        $(this).starRating({
          starSize: 25,
          readOnly: true,
          useFullStars: true,
          totalStars: result['max_rating'],
        });
        $(this).starRating('setRating', result['rating'], false);
        $(this).find('.num-voti').text(result['number_of_ratings']);
      });
    }
  });
});
