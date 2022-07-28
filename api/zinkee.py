import numpy as np

def gatData(response_json, records, TypeFields, Campos):
    for reg in response_json:
        records.append(reg["id"])
        for n in range (0, len(reg["data"])):
            if((TypeFields[n] == "T") or (TypeFields[n] == "F") or (TypeFields[n] == "H")or (TypeFields[n] == "B") or (TypeFields[n] == "V")):
                Campos.append(reg["data"][n]["valor"])
            elif((TypeFields[n] == "N")):
                Campos.append(reg["data"][n]["valor"]["number"])
            elif((TypeFields[n] == "D")):
                try:
                    if((reg["data"][n]["valorRel"])==  None):
                            try:
                                Campos.append(reg["data"][n]["valor"]["number"])
                            except:
                                Campos.append(reg["data"][n]["valor"])
                    else:
                        Campos.append(reg["data"][n]["valorRel"])
                        
                except:
                        Campos.append(reg["data"][n]["valor"]["numberFixed"])
            elif((TypeFields[n] == "U") or (TypeFields[n] == "LV") or (TypeFields[n] == "UG") or (TypeFields[n] == "RM")):
                Campos.append(reg["data"][n]["valorRel"])
            else:
                Campos.append("-")
                
    VCampos = np.array(Campos)
    MCampos = np.reshape(VCampos, (len(records), len(TypeFields)))
    content = MCampos.tolist()
    return content
