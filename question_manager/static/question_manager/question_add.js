
angular.module('questionApp',[])
.config(function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken'
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken'
    $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
}).controller('qCtrl', function($socpe){
  $scope.save = function(){
    var data = $.param({
                  question_text : $scope.question.text,
                  right_answer : $scope.question.right_answer,
                  choice4 : $scope.question.choice4,
                  choice2 : $scope.question.choice2,
                  choice3 : $scope.question.choice3,
                  category : $scope.question.category
               });

    var targetURL = "/question/";
    $http.post(targetURL, data);
  };
});
