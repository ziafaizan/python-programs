def group_synonyms(synonym):
    main_dict={}
    for item in synonym:
        for key,value in item.items():
            if main_dict.get(value):
                main_dict[value].append(key)
                continue
            if main_dict.get(key):
                main_dict[key].append(value)
                continue
            main_dict[key]=[value]
    res=[[key]+val for key,val in main_dict.items()]
    print(res)


synonyms=[{"Dg set": "Diesel generator"},
        {"Organization": "Organisation"},
        {"Group": "Organization"},
        {"Orange": "Kinnu"},
        {"Orange": "narangi"}]
group_synonyms(synonyms)
