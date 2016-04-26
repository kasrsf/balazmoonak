Array.prototype.shuffle = function() {
    var input = this;

    for (var i = input.length-1; i >=0; i--) {

        var randomIndex = Math.floor(Math.random()*(i+1));
        var itemAtIndex = input[randomIndex];

        input[randomIndex] = input[i];
        input[i] = itemAtIndex;
    }
    return input;
}

function QuestionController(Questions, $scope){
    $scope.reset = function() {
        $scope.inProgress = false;
        $scope.score = 0;
    };
    $scope.reset();
    $scope.start = function(){
        $scope.inProgress = true;
        $scope.id = 0;
        $scope.score = 0;
        $scope.question = Questions.get_by_id($scope.id);

    };
    $scope.checkAnwer = function(answer){
        if(answer === Questions.get_by_id($scope.id).answer){
            $scope.score++;
        }
        $scope.nextQuestion();
        console.log($scope.id);
    };
    $scope.nextQuestion = function(){
        $scope.id++;
        $scope.question = Questions.get_by_id($scope.id);

        if($scope.question === false){
            $scope.inProgress = false;
            $scope.finish = true;
        }
    };
}

