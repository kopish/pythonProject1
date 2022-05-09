def function():
    var = "new variable"

    def function_inner():
        nonlocal var
        print(var)
        var = "local inner"

    print(var)
    function_inner()
    print(var)


var = "Global variable"
print(var)
function()
print(var)


var = "Global variable 3"
function()
print(var)