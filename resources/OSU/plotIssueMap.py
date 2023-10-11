def plotIssueMap(L4basin,domain_reach_data,reachstr,domain_reachids):

    import folium
    import random

    ZoomStart=14

    reachmap = folium.Map(
        location=domain_reach_data[reachstr]['clpoints'][0],
        tiles='cartodb positron',
        zoom_start=ZoomStart)

    for reach in domain_reachids:    

        reachstr=str(reach)

        if reachstr[0:4] != L4basin:
            continue

        randcolor="#"+''.join([random.choice('0123456789ABCDEF') for i in range(6) ] )                 
        reachpopup='reachid: '+reachstr

        reachpopup = reachpopup + '<br>' + 'n_rch_up:' + str(domain_reach_data[reachstr]['n_rch_up'])
        reachpopup = reachpopup + '<br>' + 'rch_id_up:' + str(domain_reach_data[reachstr]['rch_id_up'].data[0:])
        reachpopup = reachpopup + '<br>' + 'n_rch_down:' + str(domain_reach_data[reachstr]['n_rch_down'])    
        reachpopup = reachpopup + '<br>' + 'rch_id_dn:' + str(domain_reach_data[reachstr]['rch_id_dn'].data[0:])    

        if not domain_reach_data[reachstr]['river_name']=='NODATA':
            reachpopup=domain_reach_data[reachstr]['river_name'] + '. ' + reachpopup 


        folium.PolyLine(domain_reach_data[reachstr]['clpoints'], color=randcolor, popup=reachpopup,weight=2.5, opacity=1).add_to(reachmap)

    return reachmap
