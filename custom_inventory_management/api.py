import frappe 

#http://0.0.0.0:8000/api/method/customer_inventory_management.api.method_name

#read operations

@frappe.whitelist()
def get_items(code):
    items=frappe.db.sql(f"""SELECT item_name item_group FROM `tabItem` WHERE
    item_code='{code}'""",as_dict=True)
    return items
#http://0.0.0.0:8000/api/method/custom_inventory_management.api.get_items
    



#--------------------------------------------------------------
@frappe.whitelist()
def add_items(code,name,group):
    try:
        items_added=frappe.get_doc({"doctype":"Item",
        "item_code":code,
        "item_name":name,
        "item_group":group
        })
        items_added.insert()
        return items_added
    except:
        items_added={"Empty":{}}
        return items_added

#------------------------------------------------ 
    
#http://0.0.0.0:8000/api/method/custom_inventory_management.api.get_items
    

#By-product



#update


#


@frappe.whitelist()
def update_items(code,name):
    try:
        frappe.db.sql(f"""UPDATE `tabItem`
        SET item_name='{name}' WHERE item_code='{code}'
         """)
        frappe.db.commit()
        return 200
    except:
        return 400

#delete items
@frappe.whitelist()
def delete_items(code):
    try:
        frappe.db.sql(f"""DELETE FROM `tabItem` WHERE item_code='{code}'
        """)
        frappe.db.commit()
        return "Succes"
    except:
        return "Failure"
