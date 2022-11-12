def get_graph_from_model(arr):
    category_to_count = {}
    for i in arr:
        category_to_count[i] = category_to_count.get(i, 0) + 1
    
    
    category_type, crime_count= [], []
    for cat, count in category_to_count.items():
        category_type.append(cat)
        crime_count.append(count)
    crime_percent = []
    total_crime = sum(crime_count)
    for i in crime_count:
        crime_percent.append((i/total_crime)*100)
    
    #the benchmarking lists are category_type, crime_count
    import matplotlib.pyplot as plt
    a = plt.figure()
    plt.pie(crime_count, labels=category_type)
    plt.savefig('media/plotted_graph/pie.png')

    b = plt.figure()
    plt.bar(category_type, crime_count)
    plt.savefig('media/plotted_graph/hist.png')
    percent_of_most_crime = max(crime_percent)
    idx_of = crime_percent.index(percent_of_most_crime)
    top_category = category_type[idx_of]
    res = top_category
    return res

def get_criminal_analysis(arr):
    criminal_dict = {}
    for i in arr:
        criminal_dict[i] = criminal_dict.get(i, 0) + 1
    
    criminal_name, crimina_crime_count = [], []
    for criminal, count in criminal_dict.items():
        criminal_name.append(criminal.name)
        crimina_crime_count.append(count)
    
    import matplotlib.pyplot as plt
    a = plt.figure()
    plt.bar(criminal_name, crimina_crime_count)
    plt.savefig('media/plotted_graph/criminal_hist.png')

    b = plt.figure()
    plt.pie(crimina_crime_count, labels=criminal_name)
    plt.savefig('media/plotted_graph/crim_pie.png')
    max_crime_done_by = max(crimina_crime_count)
    idx_of = crimina_crime_count.index(max_crime_done_by)
    top_category = criminal_name[idx_of]
    res = top_category
    return res

