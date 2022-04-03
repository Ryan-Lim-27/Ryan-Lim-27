import logging
from telegram import *
from telegram.ext import *
from inv_room import Room
from Multi_rooms import Multi_rooms


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

SCOPE = 'https://www.googleapis.com/auth/spreadsheets'
SERVICE_ACCOUNT_FILE = 'credentials1.json'
SPREADSHEET_ID = '1rogWkMq5k0c2LorB42ow3Bx5aRDGGnu7bYbqKMw-ynU'

room_name = None
light_status = None
room = ("study!B2","living!B2","living!C2")


def r(x,stat):      #Room name, light status
    print(str(stat))
    r = Room( SCOPE,SERVICE_ACCOUNT_FILE,SPREADSHEET_ID,room[x])
    r.Data(stat)
    r.api()

def m(x,stat):
    m = Multi_rooms (SCOPE,SERVICE_ACCOUNT_FILE,SPREADSHEET_ID)
    m.Data(x,stat)
    m.api()

def selection(room_name):
    if (room_name == 'study'):
        if (light_status=='on'):
            r(0,1)
            print('study light turn on')
        else:
            r(0,0)
            print('study light turn off')
    elif (room_name == 'living'):
        if (light_status == 'lamp_on'):
            print('lamp light turn on')
            r(1,1)
        elif (light_status == 'lamp_off'):
            r(1,0)
            print('lamp light turn off')
        elif (light_status == 'sofa_off'):
            print('Sofa light turn off')
        elif (light_status == 'sofa_on'):
            print('Sofa light turn on')
        elif (light_status == 'L_A_on'):
            print('Living Room lights all turn on')
            m((room[1],room[2]),(1,1))
        elif (light_status == 'L_A_off'):
            print('Living Room lights all turn on')
            m((room[1],room[2]),(0,0))


def start(update: Update, context: CallbackContext) -> str:
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    
    keyboard = [
        [
            InlineKeyboardButton("Living", callback_data='living'),
            InlineKeyboardButton("Dining", callback_data='dining'),
            InlineKeyboardButton("Study", callback_data='study'),
        ],
        [
            InlineKeyboardButton("Option 3", callback_data='3'),
            InlineKeyboardButton("Cancel", callback_data='end'),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)
    #query.edit_message_text(text=f"Selected option: {query.data}")
    return 'rooms'

    
def living(update: Update, context: CallbackContext) -> str:
    global room_name
    query = update.callback_query
    query.answer()

    keyboard = [
        [
            InlineKeyboardButton("Lamp On", callback_data= 'lamp_on'),
            InlineKeyboardButton("Lamp Off", callback_data= 'lamp_off'),

        ],
        [
            InlineKeyboardButton("Sofa light On", callback_data= 'sofa_on'),
            InlineKeyboardButton("Sofa light Off", callback_data= 'sofa_off'),
        ],
        [   InlineKeyboardButton("Living Room lights On", callback_data= 'L_A_on'),],

        [   InlineKeyboardButton("Living Room lights Off", callback_data= 'L_A_off'),],

        [   InlineKeyboardButton("Cancel", callback_data= 'end'),],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    query.message.reply_text('Please choose:', reply_markup=reply_markup)
    query.edit_message_text(text=f"Selected option: {query.data}")
    room_name = 'living'
    return 'confirm'


def study(update: Update, context: CallbackContext) -> str:
    global room_name
    query = update.callback_query
    query.answer()

    keyboard = [
        [
            InlineKeyboardButton("On", callback_data= 'on'),
            InlineKeyboardButton("Off", callback_data= 'off'),

        ],
        [
            InlineKeyboardButton("Cancel", callback_data= 'end'),
        ],
        
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    query.message.reply_text('Please choose:', reply_markup=reply_markup)
    query.edit_message_text(text=f"Selected option: {query.data}")
    room_name = "study"
    
    return 'confirm'


def end(update: Update, context: CallbackContext) -> str:
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over.
    """
    global light_status
    global room_name
    query = update.callback_query
    if (room_name == None):
        query.edit_message_text(text= "okay")
    else:
        query.edit_message_text(text=f"{room_name} Rooms's lights are turn {query.data}")
    light_status = query.data
    print(room_name)
    selection(room_name)
    
    query.answer()
    #update.message.reply_text("All done Master")
    light_status = room_name = None

    return ConversationHandler.END 



def main():

    
    updater = Updater("1702411434:AAHTGnqiFrqTURQYJ0AwVrHl1jjRhg7C2xA")
    dispatcher = updater.dispatcher

    
    
    

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start',start)],
        states={
            
            'rooms': [
                CallbackQueryHandler(living, pattern='^' + 'living' +'$'),
                CallbackQueryHandler(study, pattern='^' + 'study' +'$'),
                
            ],
            'confirm':[ 
                CallbackQueryHandler(end, pattern='^'+'lamp_on'+'$'),
                CallbackQueryHandler(end,pattern='^'+ 'lamp_off' +'$'),
                CallbackQueryHandler(end, pattern='^'+'sofa_on'+'$'),
                CallbackQueryHandler(end,pattern='^'+ 'sofa_off' +'$'),
                CallbackQueryHandler(end, pattern='^'+'L_A_on'+'$'),
                CallbackQueryHandler(end,pattern='^'+ 'L_A_off' +'$'),
                CallbackQueryHandler(end, pattern='^'+'on'+'$'),
                CallbackQueryHandler(end,pattern='^'+ 'off' +'$'),
            ],
    
        },
        fallbacks=[CallbackQueryHandler(end,pattern='^'+ 'end' +'$')], 
    )

    
    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()
    

if __name__ == '__main__':
    
    main()


'''
conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start',start)],
        states={
            'rooms':[ 
                CallbackQueryHandler(study, pattern='^'+'study'+'$'),
                CallbackQueryHandler(living, pattern='^'+'living'+'$'),
                CallbackQueryHandler(end,pattern='^'+ 'end' +'$'),  
            ],
            'confirm':[ 
                CallbackQueryHandler(confirm, pattern='^'+'on'+'$'),
                CallbackQueryHandler(confirm,pattern='^'+ 'off' +'$'), 
                CallbackQueryHandler(confirm, pattern='^'+'lon'+'$'),
                CallbackQueryHandler(confirm,pattern='^'+ 'loff' +'$'),
                CallbackQueryHandler(confirm, pattern='^'+'son'+'$'),
                CallbackQueryHandler(confirm,pattern='^'+ 'soff' +'$'),
            ],
            'end':[ 
                CallbackQueryHandler(room_name, pattern='^'+'back'+'$'),
                CallbackQueryHandler(end,pattern='^'+ 'done' +'$'),  
            ],
        },
        fallbacks=[CommandHandler('start', start)], 
    )

def confirm(update: Update, context: CallbackContext) -> str:
    global light_status
    global room_func
    query = update.callback_query
    query.answer()

    keyboard = [
        [
            InlineKeyboardButton("Done", callback_data= 'done'),

        ],
        [
            InlineKeyboardButton(f"Return to {room_name} room menu", callback_data= 'back'),
        ],
        
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    query.message.reply_text('Please choose:', reply_markup=reply_markup)
    query.edit_message_text(text=f"{room_name} Rooms's lights are turn {query.data}")
    light_status = query.data
    print(room_name)
    selection(room_name)
    
    print("in confirm func " + str(x))
    #print("room function: "+room_func(x))
    return 'end'

living_handler = ConversationHandler(
        entry_points=[
            CallbackQueryHandler(living, pattern='^' + 'living' +'$'),
        ],
        states={
            'confirm':[ 
                CallbackQueryHandler(end, pattern='^'+'lon'+'$'),
                CallbackQueryHandler(end,pattern='^'+ 'loff' +'$'),
                CallbackQueryHandler(end, pattern='^'+'son'+'$'),
                CallbackQueryHandler(end,pattern='^'+ 'soff' +'$'),
            ],
            

        },
        fallbacks=[
            
            CallbackQueryHandler(end,pattern='^'+ 'end' +'$'),
        ], 
        
        map_to_parent={
            'confirm':'end',
        }
        
    )

study_handler = ConversationHandler(
        entry_points=[
            CallbackQueryHandler(study, pattern='^' + 'study' +'$'),
        ],
        states={
            'confirm':[ 
                CallbackQueryHandler(end, pattern='^'+'on'+'$'),
                CallbackQueryHandler(end,pattern='^'+ 'off' +'$'), 
            ],

        },
        fallbacks=[
            
            CallbackQueryHandler(end,pattern='^'+ 'done' +'$'),
        ], 

        map_to_parent={
            'end':'end',
        }
    )

'''