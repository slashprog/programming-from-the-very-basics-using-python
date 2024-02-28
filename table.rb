print "Enter a number: "
num = gets.to_i

1.upto(10) do |i|
  puts "#{num} x #{i} = #{num * i}"
end

