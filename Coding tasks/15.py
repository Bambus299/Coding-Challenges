import req 
import post 

Start_Data = req.get_data("15")
items = Start_Data["items"]
positions = Start_Data["positions"]

sorted_items = [item for _, item in sorted(zip(positions, items))]


print(sorted_items)

answer = post.post_data("15", sorted_items)
print(answer)


    