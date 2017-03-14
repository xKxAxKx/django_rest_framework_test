var djangoBlog = angular.module('djangoBlog', []);


function mainController($scope, $http){
    $scope.readEntries =function() {
        $http.get('/api/entries/')
            .success(function(data) {
                $scope.formData = {};
                $scope.entries = data;
                console.log(data);
        })
        .error(function(data) {
            console.log('Error: ' + data);
        });
    };

    $scope.createEntry = function() {
        $http.post('/api/entries/', $scope.formData)
            .success(function(data) {
                console.log(data);
                $scope.readEntries();
            })
            .error(function(data) {
                console.log('Error: ' + data);
            });
    };

    $scope.deleteEntry = function(id) {
        $http.delete('/api/entries/' + id + '/')
            .success(function(data) {
                console.log(data);
                $scope.readEntries();
            })
            .error(function(data) {
                console.log('Error: ' + data);
            });
    };

    $scope.readEntries();

}
