import csv
import json
import sys
import pprint

FIELDS = [
    "Username",
    "Need.Comments",
    "Employment",
    "Forum.Threads",
    "Desired.Skills",
    "Forum.Thread.Subscriptions",
    "Acquired.Skills",
    "Highest.Education",
    "Num.Logins",
    "Year.of.Birth",
    "Last.Access.Time",
    "Forum.Subscriptions",
    "Course.Project.Comments",
    "Need.Joins",
    "Forum.PostsReplies",
    "Forum.Post.Likes.Made",
    "Location",
    "Need.Join.Requests",
    "Solution.Uploads",
    "Gender",
    "NeedForum.File.Uploads",
    "Badges.Received"
]

def format_value(value):
    if isinstance(value, basestring) or isinstance(value, list):
        return value if value else None
    else:
        return value


def get_value(value):
    if not isinstance(value, basestring):
        if value and not isinstance(value, dict):
            try:
                a = iter(value)
                return len(value)
            except:
                return value
    else:
        return value


def convert_to_csv(json_data, filename):
    final_doc = []
    with open(filename, 'w') as f:
        for i, (username, userdata) in enumerate(json_data.iteritems()):
            final_dict = {}
            final_dict["Username"] = username
            for key, value in userdata.iteritems():
                final_key = key.replace(" ", ".").replace("/", "")
                final_value = get_value(value)
                final_dict[final_key] = final_value
            final_doc.append(final_dict)
            # if i > 500:
            #     break
        json.dump(final_doc, f)



def main():
    with open(sys.argv[1]) as f:
        json_data = json.load(f)
    convert_to_csv(json_data, sys.argv[2])


if __name__ == '__main__':
    main()
