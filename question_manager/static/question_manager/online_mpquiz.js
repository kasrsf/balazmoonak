(function(){
    var app = angular.module('MultiplayerQuiz',[]);
    app.config(function($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken'
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken'
        $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
    });

    app.controller('QuestionController', function($scope, $http, $timeout, $interval){
        var intervalPromise;
        $scope.inProgress = true;
        $scope.pause = false;
        $scope.id = -1;
        $scope.score = 0;
        $scope.progressValue = 100;
        $scope.category = -1;
        $http.get("./questions.json").success(function(response){
            $scope.questions = response;
            $scope.nextQuestion();
        });

        $scope.showRightAnswer = function() {
            var correct_elt = document.getElementById("1")
            correct_elt.style.color = "white";
            correct_elt.style.backgroundColor = "green";
        }
        $scope.showWrongAnswer = function(answer) {
            var wrong_elt = document.getElementById(answer)
            wrong_elt.style.color = "white";
            wrong_elt.style.backgroundColor = "red";
        }
        $scope.checkAnswer = function(answer){
            if ($scope.pause == false) {
                $scope.pause = true;
                $scope.showRightAnswer();
                if(answer === 1){
                    $scope.score++;
                } else {
                    $scope.showWrongAnswer(answer);
                }
            }
        };
        $scope.nextQuestion = function(){
            $scope.pause = false;
            $scope.progressValue = 100;
            $scope.id++;
            $scope.question = ($scope.questions[$scope.id] && $scope.questions[$scope.id].fields) || false//Questions.get_by_id($scope.id);
            $scope.question.choices = [ {"id":1, "text": $scope.question.right_answer} , {"id":2, "text" : $scope.question.choice2}, {"id":3, "text": $scope.question.choice3},
                {"id":4, "text": $scope.question.choice4}];

            if ($scope.category == -1)
                $scope.category = $scope.question.category


            if($scope.question === false){
                var data = $.param({
                               type: "omp",
                               id: $scope.user_id,
                               score: $scope.score,
                               category_id: $scope.category,
                               match_id: $scope.match_id
                           });

                var targetURL = "/leaderboard/" + $scope.category + "/";
                $http.post(targetURL, data)

                $timeout(function() {
                    $http.get("./other_score.json").success(function(response) {
                        $scope.other_score = response['score']
                    })
                    $scope.inProgress = false;
                    $scope.finish = true;

                }, 1000);
            }
            $scope.question.choices.shuffle();

            $timeout(function() {
                intervalPromise = $interval(function(){
                $scope.progressValue -= 1;
                if ($scope.progressValue == 0) {
                    $scope.showRightAnswer();
                    $timeout(function() {
                        $scope.nextQuestion();
                    }, 1000);
                }
            }, 100, 100)
            }, 500);

        };

    });
})();

Array.prototype.shuffle = function() {
    var input = this;

    for (var i = input.length-1; i >=0; i--) {

        var randomIndex = Math.floor(Math.random()*(i+1));
        var itemAtIndex = input[randomIndex];

        input[randomIndex] = input[i];
        input[i] = itemAtIndex;
    }
    return input;
};
