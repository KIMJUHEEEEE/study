import controller
import view
import domain

controller= controller.AIController()
controller.file_read()
while True:
    view.menu_display()
    menu=view.input_select_menu()
    if menu=='1':
        email=view.input_email()
        name,age,major=view.input_ai_entity()
        controller.register_controller(domain.AIEntity(name,age,email,major))
    elif menu=='2':
        controller.get_all_entity_controller()
    elif menu=='3':
        email=view.input_email()
        name,age,major=view.input_ai_entity()
        controller.update_controller(domain.AIEntity(name,age,email,major))
    elif menu=='4':
        email=view.input_email()
        controller.delete_controller(email)
    elif menu=='5':
        email=view.input_email()
        controller.get_entity_controller(email)
    elif menu=='0':
        controller.file_write()
        break
    else:
        view.message_display("0부터 5까지 중에서 선택하세요")
    continue