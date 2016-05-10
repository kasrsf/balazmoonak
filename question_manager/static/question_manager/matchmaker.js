(function(){
    var app = angular.module('MatchMaker',[]);
    app.config(function($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken'
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken'
        $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
    });


    app.controller('MatchController', function($scope, $http, $interval, $location){

        $http.get("./available_match.json").success(function(response){
            if (response) {
                match_id = response[0].pk
                var data = $.param({
                               type: "mch",
                               id: $scope.user_id,
                               match_id: match_id
                           });

                var targetURL = $location.path();
                $http.post(targetURL, data).success(function(response){
                    window.location = "/omatches/" + match_id;
                });
            } else {
                var data = $.param({
                               type: "nm",
                               id: $scope.user_id,
                               category_id: $scope.category_id
                           });

                var targetURL = $location.path();
                $http.post(targetURL, data).success(function(response) {
                    $scope.match_id = response['id'];
                    $scope.target_url = "./" + $scope.match_id + "/check_match.json"
                });
            }
        });

        $interval(function() {
            $scope.counter++;
            if ($scope.counter == 4)
                $scope.counter = 1;

            $http.get($scope.target_url).success(function(response){
                match_found = response['status'];
                if (match_found == 'y')
                    window.location = "/omatches/" + $scope.match_id;
            });

        }, 500);
    });

})();
