"""
Spanish phrase database and AI system prompts.
Pure data module - no side effects on import.
"""

VOCABULARY = [
    # --- Greetings & Small Talk ---
    {
        "spanish": "¿Qué onda?",
        "english": "What's up? / What's going on?",
        "category": "greetings",
        "notes": "Very common in Mexico, informal",
    },
    {
        "spanish": "¿Qué tal?",
        "english": "How's it going?",
        "category": "greetings",
        "notes": "Common across all Spanish-speaking countries",
    },
    {
        "spanish": "¿Todo bien?",
        "english": "Everything good? / All good?",
        "category": "greetings",
        "notes": "Often answered with 'Todo bien' or 'Más o menos'",
    },
    {
        "spanish": "Más o menos",
        "english": "More or less / So-so",
        "category": "greetings",
        "notes": "Universal response when things are okay but not great",
    },
    {
        "spanish": "¡Qué buena onda!",
        "english": "What good vibes! / That's so cool!",
        "category": "greetings",
        "notes": "Mexico; also used as 'You're so cool/chill'",
    },
    {
        "spanish": "¿De dónde eres?",
        "english": "Where are you from?",
        "category": "greetings",
        "notes": "Essential conversation opener",
    },
    {
        "spanish": "¿A qué te dedicas?",
        "english": "What do you do for work? / What do you do?",
        "category": "greetings",
        "notes": "More natural than '¿Cuál es tu trabajo?'",
    },
    {
        "spanish": "Estoy aprendiendo español",
        "english": "I'm learning Spanish",
        "category": "greetings",
        "notes": "Say this and people will be patient and helpful",
    },
    {
        "spanish": "Habla más despacio, por favor",
        "english": "Speak more slowly, please",
        "category": "greetings",
        "notes": "Critical phrase for beginners",
    },
    {
        "spanish": "¿Cómo se dice...?",
        "english": "How do you say...?",
        "category": "greetings",
        "notes": "Fill in the blank with what you want to say",
    },
    {
        "spanish": "No entiendo",
        "english": "I don't understand",
        "category": "greetings",
        "notes": "",
    },
    {
        "spanish": "¿Puedes repetir?",
        "english": "Can you repeat that?",
        "category": "greetings",
        "notes": "",
    },
    {
        "spanish": "¡Hasta luego!",
        "english": "See you later! / Goodbye!",
        "category": "greetings",
        "notes": "",
    },
    {
        "spanish": "¡Nos vemos!",
        "english": "See you! / See you around!",
        "category": "greetings",
        "notes": "Very casual, common among friends",
    },
    {
        "spanish": "¡Cuídate!",
        "english": "Take care!",
        "category": "greetings",
        "notes": "Warm send-off",
    },
    {
        "spanish": "¿Cuánto tiempo llevas aquí?",
        "english": "How long have you been here?",
        "category": "greetings",
        "notes": "Good for starting conversations with travelers",
    },
    {
        "spanish": "Mucho gusto",
        "english": "Nice to meet you",
        "category": "greetings",
        "notes": "",
    },
    {
        "spanish": "¿Hablas inglés?",
        "english": "Do you speak English?",
        "category": "greetings",
        "notes": "Last resort phrase",
    },

    # --- Food & Restaurant ---
    {
        "spanish": "¿Me puede traer la carta?",
        "english": "Can you bring me the menu?",
        "category": "food",
        "notes": "Polite restaurant request",
    },
    {
        "spanish": "¿Qué me recomienda?",
        "english": "What do you recommend?",
        "category": "food",
        "notes": "Great for finding local favorites",
    },
    {
        "spanish": "Quiero pedir...",
        "english": "I want to order...",
        "category": "food",
        "notes": "Follow with the dish name",
    },
    {
        "spanish": "¿Está picante?",
        "english": "Is it spicy?",
        "category": "food",
        "notes": "Critical in Mexico!",
    },
    {
        "spanish": "Sin cebolla, por favor",
        "english": "Without onion, please",
        "category": "food",
        "notes": "Template: 'Sin [ingredient], por favor'",
    },
    {
        "spanish": "La cuenta, por favor",
        "english": "The bill, please",
        "category": "food",
        "notes": "Standard way to ask for the check",
    },
    {
        "spanish": "¿Está incluida la propina?",
        "english": "Is the tip included?",
        "category": "food",
        "notes": "Tip customs vary by country",
    },
    {
        "spanish": "Está delicioso",
        "english": "It's delicious",
        "category": "food",
        "notes": "",
    },
    {
        "spanish": "¡Qué rico!",
        "english": "How delicious! / Yummy!",
        "category": "food",
        "notes": "Enthusiastic reaction to good food",
    },
    {
        "spanish": "Soy alérgico a los mariscos",
        "english": "I'm allergic to seafood",
        "category": "food",
        "notes": "Template: 'Soy alérgico/a a...'",
    },
    {
        "spanish": "¿Tiene opciones vegetarianas?",
        "english": "Do you have vegetarian options?",
        "category": "food",
        "notes": "",
    },
    {
        "spanish": "Para llevar",
        "english": "To go / Takeout",
        "category": "food",
        "notes": "",
    },
    {
        "spanish": "Para comer aquí",
        "english": "To eat here / Dine in",
        "category": "food",
        "notes": "",
    },
    {
        "spanish": "Otra cerveza, por favor",
        "english": "Another beer, please",
        "category": "food",
        "notes": "Template: 'Otro/a [item], por favor'",
    },
    {
        "spanish": "¿Me puede traer agua?",
        "english": "Can you bring me water?",
        "category": "food",
        "notes": "Ask for 'agua purificada' (purified water) in Mexico",
    },
    {
        "spanish": "¿Qué lleva este platillo?",
        "english": "What's in this dish? / What does it come with?",
        "category": "food",
        "notes": "'Platillo' = dish/plate",
    },

    # --- Directions & Transportation ---
    {
        "spanish": "¿Cómo llego a...?",
        "english": "How do I get to...?",
        "category": "directions",
        "notes": "Fill in with destination",
    },
    {
        "spanish": "¿Está lejos?",
        "english": "Is it far?",
        "category": "directions",
        "notes": "",
    },
    {
        "spanish": "A la derecha",
        "english": "To the right",
        "category": "directions",
        "notes": "",
    },
    {
        "spanish": "A la izquierda",
        "english": "To the left",
        "category": "directions",
        "notes": "",
    },
    {
        "spanish": "Todo recto",
        "english": "Straight ahead",
        "category": "directions",
        "notes": "Also 'derecho' or 'recto'",
    },
    {
        "spanish": "En la esquina",
        "english": "On the corner",
        "category": "directions",
        "notes": "",
    },
    {
        "spanish": "¿Dónde está el metro?",
        "english": "Where is the subway / metro?",
        "category": "directions",
        "notes": "",
    },
    {
        "spanish": "¿Cuánto cuesta el taxi?",
        "english": "How much does the taxi cost?",
        "category": "directions",
        "notes": "Always ask before getting in!",
    },
    {
        "spanish": "Lléveme a...",
        "english": "Take me to... (for taxis)",
        "category": "directions",
        "notes": "Formal command used with taxi drivers",
    },
    {
        "spanish": "Bájame aquí",
        "english": "Drop me off here / Let me off here",
        "category": "directions",
        "notes": "Mexico; also 'Aquí está bien'",
    },
    {
        "spanish": "¿A qué hora sale el autobús?",
        "english": "What time does the bus leave?",
        "category": "directions",
        "notes": "",
    },
    {
        "spanish": "¿Cuánto tarda en llegar?",
        "english": "How long does it take to get there?",
        "category": "directions",
        "notes": "",
    },

    # --- Shopping & Bargaining ---
    {
        "spanish": "¿Cuánto cuesta?",
        "english": "How much does it cost?",
        "category": "shopping",
        "notes": "Basic shopping question",
    },
    {
        "spanish": "¿Cuánto vale?",
        "english": "How much is it worth / How much does it cost?",
        "category": "shopping",
        "notes": "Slightly more casual variant",
    },
    {
        "spanish": "Está muy caro",
        "english": "It's very expensive",
        "category": "shopping",
        "notes": "Starting point for bargaining",
    },
    {
        "spanish": "¿Me puede dar un descuento?",
        "english": "Can you give me a discount?",
        "category": "shopping",
        "notes": "Worth asking at markets",
    },
    {
        "spanish": "¿Tiene algo más barato?",
        "english": "Do you have something cheaper?",
        "category": "shopping",
        "notes": "",
    },
    {
        "spanish": "Solo estoy mirando",
        "english": "I'm just looking / Just browsing",
        "category": "shopping",
        "notes": "Polite way to decline pushy vendors",
    },
    {
        "spanish": "Me lo llevo",
        "english": "I'll take it",
        "category": "shopping",
        "notes": "",
    },
    {
        "spanish": "¿Acepta tarjeta?",
        "english": "Do you accept card?",
        "category": "shopping",
        "notes": "Many smaller shops are cash only",
    },
    {
        "spanish": "¿Tiene cambio?",
        "english": "Do you have change?",
        "category": "shopping",
        "notes": "Change is often scarce; have small bills",
    },
    {
        "spanish": "¿En qué talla?",
        "english": "In what size?",
        "category": "shopping",
        "notes": "They'll ask you this in clothing stores",
    },
    {
        "spanish": "¿Lo tienen en otro color?",
        "english": "Do you have it in another color?",
        "category": "shopping",
        "notes": "",
    },

    # --- Socializing & Making Friends ---
    {
        "spanish": "¿Quieres tomar algo?",
        "english": "Do you want to get a drink?",
        "category": "socializing",
        "notes": "'Tomar algo' = have a drink (coffee, beer, etc.)",
    },
    {
        "spanish": "¿Vamos a bailar?",
        "english": "Do you want to dance? / Shall we dance?",
        "category": "socializing",
        "notes": "",
    },
    {
        "spanish": "¿Dónde está la fiesta?",
        "english": "Where is the party?",
        "category": "socializing",
        "notes": "",
    },
    {
        "spanish": "Me cae bien",
        "english": "I like him/her (personality) / He/she seems cool",
        "category": "socializing",
        "notes": "About personality, NOT romantic. 'Me cae' = my impression of them",
    },
    {
        "spanish": "Me cae mal",
        "english": "I don't like him/her / He/she rubs me the wrong way",
        "category": "socializing",
        "notes": "About personality. Opposite of 'me cae bien'",
    },
    {
        "spanish": "¿Tienes WhatsApp?",
        "english": "Do you have WhatsApp?",
        "category": "socializing",
        "notes": "WhatsApp is THE messaging app in Latin America",
    },
    {
        "spanish": "¿Nos tomamos una foto?",
        "english": "Should we take a photo? / Can we take a photo?",
        "category": "socializing",
        "notes": "",
    },
    {
        "spanish": "Estoy con mis amigos",
        "english": "I'm with my friends",
        "category": "socializing",
        "notes": "",
    },
    {
        "spanish": "¿Qué planes tienes?",
        "english": "What are your plans? / What are you up to?",
        "category": "socializing",
        "notes": "",
    },
    {
        "spanish": "¿A dónde vamos?",
        "english": "Where are we going?",
        "category": "socializing",
        "notes": "",
    },
    {
        "spanish": "¡Salud!",
        "english": "Cheers! / To your health!",
        "category": "socializing",
        "notes": "Toast when drinking",
    },
    {
        "spanish": "Invita la casa",
        "english": "It's on the house",
        "category": "socializing",
        "notes": "What a bartender says when giving you a free drink",
    },

    # --- Emotions & Reactions ---
    {
        "spanish": "¡No manches!",
        "english": "No way! / Are you kidding me! / Wow!",
        "category": "reactions",
        "notes": "Mild expletive, very common in Mexico. Clean version of a stronger phrase.",
    },
    {
        "spanish": "¡Híjole!",
        "english": "Wow! / Oh my! / Gosh!",
        "category": "reactions",
        "notes": "Mexico; expresses surprise, concern, or dismay",
    },
    {
        "spanish": "¡Órale!",
        "english": "Alright! / Let's go! / Right on! / Wow!",
        "category": "reactions",
        "notes": "Very versatile Mexican expression; tone determines meaning",
    },
    {
        "spanish": "¡Qué pena!",
        "english": "How embarrassing! / What a shame!",
        "category": "reactions",
        "notes": "'Qué pena' often means embarrassing, not pitiful",
    },
    {
        "spanish": "Me da igual",
        "english": "I don't care / It's all the same to me / Whatever",
        "category": "reactions",
        "notes": "Neutral indifference; not necessarily rude",
    },
    {
        "spanish": "¡Qué lástima!",
        "english": "What a pity! / That's too bad!",
        "category": "reactions",
        "notes": "",
    },
    {
        "spanish": "Estoy harto",
        "english": "I'm fed up / I'm sick of it",
        "category": "reactions",
        "notes": "'Harto/a' = fed up, sick and tired",
    },
    {
        "spanish": "¡Ándale!",
        "english": "Come on! / Hurry up! / That's it! / Go!",
        "category": "reactions",
        "notes": "Mexico; very versatile based on context and tone",
    },
    {
        "spanish": "Tengo flojera",
        "english": "I'm feeling lazy / I can't be bothered",
        "category": "reactions",
        "notes": "Mexico; 'flojera' = laziness/sluggishness",
    },
    {
        "spanish": "¡Qué suerte!",
        "english": "How lucky! / What luck!",
        "category": "reactions",
        "notes": "",
    },
    {
        "spanish": "¡Qué horror!",
        "english": "How awful! / That's terrible!",
        "category": "reactions",
        "notes": "",
    },

    # --- Essential Slang & Expressions ---
    {
        "spanish": "¡Chale!",
        "english": "No way! / That sucks! / Come on!",
        "category": "slang",
        "notes": "Mexico; expresses disappointment or disbelief",
    },
    {
        "spanish": "Buena onda",
        "english": "Good vibes / Cool person / Chill",
        "category": "slang",
        "notes": "Can describe a person ('es buena onda' = he/she is cool) or situation",
    },
    {
        "spanish": "Mala onda",
        "english": "Bad vibes / Uncool / That's not cool",
        "category": "slang",
        "notes": "Opposite of 'buena onda'",
    },
    {
        "spanish": "No hay bronca",
        "english": "No problem / No worries / It's fine",
        "category": "slang",
        "notes": "Mexico; 'bronca' = problem/fight",
    },
    {
        "spanish": "Hay bronca",
        "english": "There's a problem / There's an issue",
        "category": "slang",
        "notes": "",
    },
    {
        "spanish": "Echar un ojo",
        "english": "To keep an eye on something / To take a look",
        "category": "slang",
        "notes": "Literally 'throw an eye'",
    },
    {
        "spanish": "La neta",
        "english": "The truth / For real / Honestly",
        "category": "slang",
        "notes": "Mexico; 'La neta es que...' = The truth is that...",
    },
    {
        "spanish": "¿En serio?",
        "english": "Seriously? / Really? / Are you serious?",
        "category": "slang",
        "notes": "",
    },
    {
        "spanish": "¡Claro que sí!",
        "english": "Of course! / Absolutely!",
        "category": "slang",
        "notes": "",
    },
    {
        "spanish": "¡Para nada!",
        "english": "Not at all! / No way!",
        "category": "slang",
        "notes": "",
    },
    {
        "spanish": "Sin duda",
        "english": "Without a doubt / Definitely",
        "category": "slang",
        "notes": "",
    },
    {
        "spanish": "Ahí nos vemos",
        "english": "See you there / See you around",
        "category": "slang",
        "notes": "Casual parting phrase",
    },
    {
        "spanish": "Que te vaya bien",
        "english": "I hope things go well for you / Take care",
        "category": "slang",
        "notes": "Warm farewell",
    },
    {
        "spanish": "¿Qué rollo?",
        "english": "What's the deal? / What's going on? / What's up?",
        "category": "slang",
        "notes": "Mexico; 'rollo' = situation/thing",
    },
    {
        "spanish": "Echar la flojera",
        "english": "To be lazy / To hang out doing nothing / To chill",
        "category": "slang",
        "notes": "",
    },
    {
        "spanish": "A ver",
        "english": "Let's see / Hmm / OK then",
        "category": "slang",
        "notes": "Filler phrase; buys time while thinking",
    },
    {
        "spanish": "Pues",
        "english": "Well... / So... / I mean...",
        "category": "slang",
        "notes": "Most common filler word in Spanish",
    },
    {
        "spanish": "O sea",
        "english": "I mean / Like / In other words",
        "category": "slang",
        "notes": "Like 'like' or 'I mean' in English",
    },
    {
        "spanish": "Estar en las nubes",
        "english": "To be in the clouds / To be daydreaming / To be spacey",
        "category": "slang",
        "notes": "Idiom; 'Estás en las nubes' = You're daydreaming",
    },
    {
        "spanish": "¡Qué chido!",
        "english": "How cool! / That's awesome!",
        "category": "slang",
        "notes": "Mexico; very common among young people",
    },
    {
        "spanish": "¡Qué padre!",
        "english": "How cool! / That's great!",
        "category": "slang",
        "notes": "Mexico; 'padre' literally means father but colloquially means cool",
    },
    {
        "spanish": "Ya",
        "english": "Already / OK / Yeah / Got it / Enough",
        "category": "slang",
        "notes": "Most versatile word in Spanish; tone determines everything",
    },
    {
        "spanish": "¿Ya?",
        "english": "Already? / Done? / Ready?",
        "category": "slang",
        "notes": "",
    },
    {
        "spanish": "¡Órale, pues!",
        "english": "Alright then! / OK, sure! / Let's do it!",
        "category": "slang",
        "notes": "Mexico; agreement/enthusiasm",
    },
    {
        "spanish": "Me llama la atención",
        "english": "It catches my attention / I find it interesting",
        "category": "slang",
        "notes": "Idiom for something that interests you",
    },

    # --- Emergencies & Important Situations ---
    {
        "spanish": "¡Ayuda!",
        "english": "Help!",
        "category": "emergencies",
        "notes": "",
    },
    {
        "spanish": "Llame a la policía",
        "english": "Call the police",
        "category": "emergencies",
        "notes": "",
    },
    {
        "spanish": "Necesito un médico",
        "english": "I need a doctor",
        "category": "emergencies",
        "notes": "",
    },
    {
        "spanish": "Me robaron",
        "english": "I was robbed / They robbed me",
        "category": "emergencies",
        "notes": "",
    },
    {
        "spanish": "Estoy perdido",
        "english": "I'm lost",
        "category": "emergencies",
        "notes": "'Perdido/a' for male/female speaker",
    },
    {
        "spanish": "¿Dónde está el hospital?",
        "english": "Where is the hospital?",
        "category": "emergencies",
        "notes": "",
    },

    # --- Practical Daily Phrases ---
    {
        "spanish": "¿Tiene wifi?",
        "english": "Do you have wifi?",
        "category": "practical",
        "notes": "Pronounced 'wee-fee' in Spanish",
    },
    {
        "spanish": "¿Cuál es la contraseña?",
        "english": "What's the password?",
        "category": "practical",
        "notes": "'Contraseña' = password",
    },
    {
        "spanish": "¿Dónde está el baño?",
        "english": "Where is the bathroom?",
        "category": "practical",
        "notes": "Essential travel phrase",
    },
    {
        "spanish": "¿A qué hora abren?",
        "english": "What time do you open?",
        "category": "practical",
        "notes": "",
    },
    {
        "spanish": "¿A qué hora cierran?",
        "english": "What time do you close?",
        "category": "practical",
        "notes": "",
    },
    {
        "spanish": "¿Puedo ver el menú?",
        "english": "Can I see the menu?",
        "category": "practical",
        "notes": "",
    },
    {
        "spanish": "Permiso",
        "english": "Excuse me (to pass) / May I?",
        "category": "practical",
        "notes": "Used when squeezing past people or asking permission",
    },
    {
        "spanish": "Con permiso",
        "english": "Excuse me / Pardon me (when passing through)",
        "category": "practical",
        "notes": "",
    },
    {
        "spanish": "Disculpe",
        "english": "Excuse me (to get attention) / Sorry",
        "category": "practical",
        "notes": "Used to get a waiter's attention or apologize",
    },
    {
        "spanish": "¿Me puede ayudar?",
        "english": "Can you help me?",
        "category": "practical",
        "notes": "",
    },
    {
        "spanish": "No sé",
        "english": "I don't know",
        "category": "practical",
        "notes": "",
    },
    {
        "spanish": "Un momento, por favor",
        "english": "One moment, please",
        "category": "practical",
        "notes": "",
    },
    {
        "spanish": "¿Cuánto tiempo lleva esperando?",
        "english": "How long have you been waiting?",
        "category": "practical",
        "notes": "Good for striking up conversation in lines",
    },
]

CATEGORIES = sorted(set(item["category"] for item in VOCABULARY))

SYSTEM_PROMPT_CONVERSATION = """You are a friendly Spanish conversation partner helping someone learn conversational Spanish. Your name is Sofía.

Rules:
- ALWAYS respond in Spanish, no matter what the user says
- Use natural, colloquial Spanish - not textbook Spanish
- Keep responses SHORT (1-3 sentences) so they are easy to understand and repeat
- If the user makes a grammar mistake, gently correct it by using the correct form naturally in your response (don't lecture them explicitly)
- If the user writes in English, respond in Spanish and kindly note "En español, por favor :)"
- Use common filler words and expressions naturally: bueno, pues, mira, oye, a ver, la verdad es que...
- Be warm, encouraging, and fun. Use expressions like ¡Qué bueno!, ¡Órale!, ¡Qué chido!, ¡Qué padre!
- Occasionally ask short follow-up questions to keep the conversation flowing
- Match the user's energy level and topic
- Use ¡ and ¿ correctly as they appear in real Spanish text
- If the user seems stuck, gently offer a hint or rephrase in simpler Spanish

Remember: You are helping them learn fast through real conversation, not grammar drills. Keep it fun and natural."""
