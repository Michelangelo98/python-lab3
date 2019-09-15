from telegram.ext import Updater,CommandHandler,MessageHandler,Filters

import telegram
from sys import argv



def start(bot, update):

    update.message.reply_text("Hello!")


def show_all_task(bot,update) :

    file_in = open(argv[1])
    todo_list = file_in.read().splitlines()
    file_in.close()

    if todo_list == [""] or todo_list == [] :
        update.message.reply_text("Nothing to do, here!")
    else:
        update.message.reply_text(str(todo_list))




def new_task(bot,update,args) :

    file_in = open(argv[1])
    todo_list = file_in.read().splitlines()
    file_in.close()

    to_add = " ".join(args)

    if to_add in todo_list :
        update.message.reply_text("The task was already present")
        return



    file_out = open(argv[1],'a')


    file_out.write(to_add + "\n")

    file_out.close()


    update.message.reply_text("The new task was succesfully added")




def remove_task(bot,update,args) :



    file_in = open(argv[1])
    todo_list = file_in.read().splitlines()
    file_in.close()

    file_out = open(argv[1],"w")

    to_remove = " ".join(args)

    print(to_remove)
    if to_remove in todo_list :
        todo_list.remove(to_remove)
        update.message.reply_text("The task was succesfully removed")

    else :
        update.message.reply_text("The task was not found")

    for task in todo_list:
        file_out.write(task + "\n")

    file_out.close()






def remove_all_task(bot,update,args) :


    file_task = open(argv[1])
    todo_list = file_task.read().splitlines()
    file_task.close()


    to_remove = " ".join(args)
    remove_list = []

    # utilizzo il for-list per evitare un "out of range"
    for action in todo_list:

        if action.count(to_remove) != 0:
            remove_list.append(action)
            

    if remove_list == []:
        update.message.reply_text("The task was not found")

    else:

        for task in remove_list:
            todo_list.remove(task)

        update.message.reply_text("Task removed: ")
        update.message.reply_text(remove_list)

        file_task = open(argv[1], "w")
        for task in todo_list:
            file_task.write(task + "\n")

        file_task.close()


def error(bot,update) :
    update.message.reply_text("This bot answer only commands")



def main():
    '''
    it manage a task list implented in a bot
    :return:
    '''



    updater = Updater("718524122:AAF9wHSx1_L2nDelEAqH72-hOUqeJXWaq5M")
    dispatcher = updater.dispatcher

    start_task_handler = CommandHandler("start", start)
    dispatcher.add_handler(start_task_handler)

    show_task_handler = CommandHandler("showTasks",show_all_task)
    dispatcher.add_handler(show_task_handler)

    new_task_handler = CommandHandler("newTask",new_task,pass_args=True)
    dispatcher.add_handler(new_task_handler)

    remove_task_handler = CommandHandler("removeTask", remove_task, pass_args=True)
    dispatcher.add_handler(remove_task_handler)

    remove_all_task_handler = CommandHandler("removeAllTask", remove_all_task, pass_args=True)
    dispatcher.add_handler(remove_all_task_handler)

    error_task_handler = MessageHandler(Filters.text,error)
    dispatcher.add_handler(error_task_handler)






    updater.start_polling()
    updater.idle()




if __name__ == '__main__':
    main()
