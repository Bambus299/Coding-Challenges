import req
import post
import json 

Data = req.get_data("12")
print(Data)

Solution = ["True", "True", "True", "False", "True", "False", "False", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "False", "True", "True", "True", "True", "True", "False", "True", "True", "False", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "True", "False", "True", "True", "True",]

answer = post.post_data("12",Solution)
print(answer)