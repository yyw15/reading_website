/**
 * Created by Ma_Zi_jun on 2016/7/28.
 */
$(function () {
  var fullMark = 5;
  $star = $('.score-star');
  $star.bind('mouseover', function() {
      var order = $star.index($(this));
      for (var j = 0; j < fullMark; j++){
          if (j <= order){
              $star.eq(j).removeClass('glyphicon-star-empty');
              $star.eq(j).addClass('glyphicon-star');
          } else {
              $star.eq(j).removeClass('glyphicon-star');
              $star.eq(j).addClass('glyphicon-star-empty');
          }
      }
  });
})