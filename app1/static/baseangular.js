var app = angular.module('myApp',  []);

app.config(function($interpolateProvider,$httpProvider){
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $interpolateProvider.startSymbol('[[')
    $interpolateProvider.endSymbol(']]')
});


 app.controller('BookController', function($scope,$http,$timeout) {



        // $scope.locationn = false;
        //     $scope.departmentt = false;
        //     $scope.categoryy = false;

        //     $scope.subcategoryy = false;
        //     $scope.sku = false;


            $http.get("/api/v1/book/").then(function(response){
            			//debugger

                        $scope.mybook = response.data
                  });


            $scope.load_data = function(){
            	            $http.get("/api/v1/book/").then(function(response){
				                        $scope.mybook = response.data
                				  });

            				}


            $scope.add_book = function(){





                                           $scope.book_data= [{ 
                                                        "book_name" : $scope.add_book_name,
                                                        "nob" : $scope.add_noofbooks,
                                                        "rack": $scope.add_racknumber
                                                  }]
                                            $http({
                                                    url: "/api/v1/book/",
                                                    method: "POST",
                                                    data: $scope.book_data,
                                                    }).then(function successCallback(response) {
                                                                  $scope.add_book_name = ""
                                                                  $scope.add_noofbooks = ""
                                                                  $scope.add_racknumber = ""

                                                                $('#addBookModal').modal('hide');
                                                                $scope.load_data()
                                                            }, function errorCallback(response) {
                                                                  console.log("Error code");
                                                        }
                                                    );
                    
                                        }

            $scope.edit_book = function(book_id){
                                                    $scope.book_id = book_id
                                                    $http({
                                                              url: "/api/v1/book/", 
                                                              method: "GET",
                                                              params: {book_id: book_id}
                                                           }).then(function successCallback(response) {
                                                                   $scope.edit_bookdetails = response.data[0]
                                                                  $('#editBookModals').modal('show');
                                                                  // $scope.location_data()
                                                        }, function errorCallback(response) {

                                                              console.log("Error code");
                                                    });
                                                }

            $scope.update_book = function(){
                                             $scope.update_data= [{ 
                                                          "book_id" : $scope.edit_bookdetails.book_id,
                                                          "book_name" : $scope.edit_bookdetails.book_name,
                                                          "nob" : $scope.edit_bookdetails.num_of_books,
                                                          "rack" : $scope.edit_bookdetails.rack_number
                                                    }]
                                              $http({
                                                      url: "/api/v1/book/",
                                                      method: "PUT",
                                                      data: $scope.update_data,
                                                      }).then(function successCallback(response) {
                                                                  $('#editBookModals').modal('hide');
                                                                  $scope.load_data()
                                                              }, function errorCallback(response) {

                                                                    console.log("Error code");
                                                          }
                                                      );
                                          }
            $scope.delete_book = function(book_id){
                                                    // debugger
                                                    $scope.book_id = book_id
                                                    $http({
                                                              url: "/api/v1/book/", 
                                                              method: "DELETE",
                                                              params: {book_id: book_id}
                                                           }).then(function successCallback(response) {
                                                                  if (response.data=="Failed"){
                                                                    alert("Cannot delete some instances of model 'Location' because they are referenced through a protected foreign key")
                                                                  }
                                                                  else{
                                                                      $scope.load_data()
                                                                      console.log("Success code");
                                                                  }
                                                        }, function errorCallback(response) {
                                                              alert("Cannot delete some instances of model 'Location' because they are referenced through a protected foreign key")
                                                              console.log("Error code");
                                                    });
                                                 }



    });