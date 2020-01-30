(function ($) {
  function checkPrime(n) {
    if (n <= 1) {
      return (false)
    }
    else if (n === 2) {
      return (true)
    } else {
      for (var i = 2; i < n; i++) {
        if (n % i === 0) {
          return (false)
        }
      }
      return (true)
    }
  }

  var myForm = $("#prime-input")
  myForm.submit(function (event) {

    var checkNumber = $("#num-input").val()
    if (checkNumber === '') {
      alert("No input entered, please enter a number to check")
    } else if (checkPrime(parseInt(checkNumber))) {
      var isPrimeString = "<li class='is-prime'>" + String(checkNumber) + " is a prime number</li>"
      $("#attempts").append(isPrimeString)
    } else {
      var isnotPrimeString = "<li class='not-prime'>" + String(checkNumber) + " is NOT a prime number</li>"
      $("#attempts").append(isnotPrimeString)
    }

    event.preventDefault()

  })

})(jQuery)