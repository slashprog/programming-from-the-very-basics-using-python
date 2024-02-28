function main()
    print("Enter a number: ")  
    flush(stdout)
    num = parse(Int, readline())
    
    for i in 1:10
        println("$num x $i = $(num * i)")
    end
    flush(stdout)
end

main()
