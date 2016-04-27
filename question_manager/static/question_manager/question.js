//var questionModule = angular.module('QuestionApp', []);
//questionModule.factory('Questions', function($http) {
//    var q = this;
//    $http.get("./questions.json").success(function (response){
//        q.questions = response.data;
//    });
//
//    return {
//        get_by_id: function(id){
//            if(id < q.questions.length){
//                q.questions[id].Choices.shuffle();
//                return q.questions[id];
//
//            }
//            else{
//                return false;
//            }
//        }
//    };
//});
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

(function(){
    var app = angular.module('singlePlayerQuiz',[]);
    app.controller('QuestionController', function($scope, $http){
        $scope.questions = []
        $http.get("./questions.json").success(function(response){
            $scope.questions = response;
        });
        $scope.reset = function() {
            $scope.inProgress = false;
            $scope.score = 0;
            $scope.finish = false;
        };
        $scope.reset();
        $scope.start = function(){
            $scope.inProgress = true;
            $scope.id = 0;
            $scope.score = 0;
            $scope.questions.shuffle();
            $scope.questions = $scope.questions.slice(1,5);
            $scope.question = $scope.questions[$scope.id].fields || false//Questions.get_by_id(this.id);
            $scope.question.choices = [ {"id":1, "text": $scope.question.right_answer} , {"id":2, "text" : $scope.question.choice1}, {"id":3, "text": $scope.question.choice2},
                {"id":4, "text": $scope.question.choice3}];
            console.log($scope.question.choices);
            $scope.question.choices.shuffle();

        };
        $scope.checkAnswer = function(answer){
            if(answer === 1 ){//$scope.questions[$scope.id].fields.right_answer){//Questions.get_by_id($scope.id).answer){
                $scope.score++;
            }
            $scope.nextQuestion();
        };
        $scope.nextQuestion = function(){
            $scope.id++;
            $scope.question = ($scope.questions[$scope.id] && $scope.questions[$scope.id].fields) || false//Questions.get_by_id($scope.id);
            $scope.question.choices = [ {"id":1, "text": $scope.question.right_answer} , {"id":2, "text" : $scope.question.choice1}, {"id":3, "text": $scope.question.choice2},
                {"id":4, "text": $scope.question.choice3}];
            console.log($scope.question);
            if($scope.question === false){
                $scope.inProgress = false;
                $scope.finish = true;
            }
        };
    });
})();


//
//function QuestionController($http, $scope){
//    var q = this;
//    q.questions = [];
//    $http.get("./questions.json").success(function (response){
//        q.questions = response;
//        console.log(q.questions);
//    });
//    $scope.reset = function() {
//        $scope.inProgress = false;
//        $scope.score = 0;
//    };
//    $scope.reset();
//    $scope.start = function(){
//        $scope.inProgress = true;
//        $scope.id = 0;
//        $scope.score = 0;
//        $scope.question = this.questions[$scope.id]//Questions.get_by_id($scope.id);
//        console.log($scope.question)
//
//    };
//    $scope.checkAnwer = function(answer){
//        if(answer === questions[$scope.id].answer){//Questions.get_by_id($scope.id).answer){
//            $scope.score++;
//        }
//        $scope.nextQuestion();
//        console.log($scope.id);
//    };
//    $scope.nextQuestion = function(){
//        $scope.id++;
//        $scope.question = questions[$scope.id]//Questions.get_by_id($scope.id);
//
//
//        if($scope.question === false){
//            $scope.inProgress = false;
//            $scope.finish = true;
//        }
//    };
//}
