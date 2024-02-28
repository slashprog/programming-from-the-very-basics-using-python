print "Enter a number: "
num = read_line.chomp.to_i

1.upto(10) do |i|
  puts "#{num} x #{i} = #{num * i}"
end

