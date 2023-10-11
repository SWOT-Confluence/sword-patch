def apply_sword_patches(patch_data,domain_reach_data_orig):
    
    import copy
    
    # based off the function in run_MOI
    
    domain_reach_data=copy.deepcopy(domain_reach_data_orig)

    reaches_to_patch=list(patch_data['reach_data'].keys())

    print('Read in patches for:',len(reaches_to_patch),' reaches.')
    print('... for reach ids: ',list(reaches_to_patch))
        
    for reachid in reaches_to_patch:
        
        reachidstr=str(reachid)
        
        if reachidstr not in domain_reach_data.keys():
            
            print(reachidstr)
            
            print( reachidstr in domain_reach_data.keys() )
            
            print(reachid,' is not included in this domain. Not patching.')
        else:
            print('Patching',reachid)
            for data_element in patch_data['reach_data'][reachid]:

                if data_element != 'metadata':
                    
                    if data_element == 'n_rch_up' or data_element == 'n_rch_down':
                        data_type='scalar'
                    elif data_element == 'rch_id_up' or data_element == 'rch_id_dn':
                         data_type='vector'
                    else:
                         print('unknown data type found in patch! crash imminent...')                    

                    print('  Patching data element:',data_element)                        
                    print('    In the patch:',patch_data['reach_data'][reachid][data_element])                
                    print('    In SWORD:',domain_reach_data[reachidstr][data_element])

                    # apply patch
                    if data_type=='vector':
                        domain_reach_data[reachidstr][data_element].data[:]=patch_data['reach_data'][reachid][data_element]
                    else:
                        domain_reach_data[reachidstr][data_element]=patch_data['reach_data'][reachid][data_element]

                    print('    In SWORD after fix:',domain_reach_data[reachidstr][data_element])

    return domain_reach_data
