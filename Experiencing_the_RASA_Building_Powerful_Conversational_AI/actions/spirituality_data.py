# Database of spiritual concepts
CONCEPTS = {
    "dharma": {
        "description": "Dharma refers to the religious, moral, and ethical duties that sustain individuals, society, and the natural world. It encompasses one's obligations and responsibilities according to one's position in society, stage of life, and natural tendencies. Dharma is often described as 'that which upholds or supports' and is considered one of the four goals of human life (purusharthas).",
        "related_concepts": ["karma", "moksha", "artha", "kama"]
    },
    "karma": {
        "description": "Karma refers to the spiritual principle of cause and effect where intent and actions of an individual (cause) influence their future (effect). Good intent and good deeds contribute to good karma and happier rebirths, while bad intent and bad deeds contribute to bad karma and suffering. It's often understood as 'what you sow, you shall reap'.",
        "related_concepts": ["dharma", "samsara", "moksha", "reincarnation"]
    },
    "moksha": {
        "description": "Moksha refers to liberation from the cycle of death and rebirth (samsara). It is the ultimate spiritual goal in Indian traditions and is considered the fourth and final goal of human life (purusharthas). Moksha is achieved through self-realization, spiritual knowledge, detachment from worldly concerns, and dissolution of ego.",
        "related_concepts": ["dharma", "karma", "samsara", "atman", "brahman"]
    },
    "atman": {
        "description": "Atman refers to the true self or essence of an individual beyond identification with phenomena. It is sometimes described as 'self' or 'soul' and is considered eternal, unchanging, and indistinguishable from Brahman (universal consciousness). The realization of one's Atman as identical with Brahman is a central goal in Vedanta philosophy.",
        "related_concepts": ["brahman", "moksha", "samsara", "consciousness"]
    },
    "brahman": {
        "description": "Brahman is the ultimate reality in Vedantic traditions, representing the unchanging, infinite, immanent, and transcendent reality which is the divine ground of all being. Brahman is often described as the 'World Soul' or 'Universal Soul' and is considered without attributes, beyond human conceptualization, yet the essence of all existence.",
        "related_concepts": ["atman", "moksha", "advaita", "consciousness"]
    },
    "yoga": {
        "description": "Yoga is a group of physical, mental, and spiritual practices aimed at harmonizing the mind, body, and spirit. While often associated with physical postures (asanas) in the West, traditional yoga encompasses a broader discipline including ethical precepts, breath control, meditation, and practices for transcending ordinary consciousness. The word 'yoga' comes from Sanskrit and means to unite or join.",
        "related_concepts": ["meditation", "pranayama", "asana", "samadhi"]
    },
    "meditation": {
        "description": "Meditation refers to techniques for focusing attention and awareness to achieve mental clarity, emotional calm, and spiritual insight. It is a central practice in many Indian spiritual traditions and is considered essential for self-realization. Different forms include mindfulness, contemplation, mantra recitation, and visualization.",
        "related_concepts": ["yoga", "dhyana", "samadhi", "consciousness"]
    },
    "ahimsa": {
        "description": "Ahimsa is the principle of non-violence toward all living beings. It's a cornerstone of several Indian religions including Hinduism, Buddhism, and Jainism. Ahimsa implies not causing harm through thoughts, words, or actions and promotes compassion, kindness, and love. Mahatma Gandhi's principle of non-violent resistance was derived from this concept.",
        "related_concepts": ["dharma", "satya", "karma", "ethics"]
    },
    "samsara": {
        "description": "Samsara refers to the cycle of death and rebirth that all beings go through according to their karma. It represents the continuous flow of life, death, and rebirth that is perpetuated by desire and ignorance. The ultimate spiritual goal in many Indian traditions is to break free from this cycle and achieve moksha (liberation).",
        "related_concepts": ["karma", "moksha", "reincarnation", "nirvana"]
    },
    "chakra": {
        "description": "Chakras are energy centers believed to exist in the subtle body. There are traditionally seven main chakras aligned along the spine from the base to the crown of the head. Each chakra corresponds to specific organs, emotions, and aspects of consciousness. Practices like yoga, meditation, and pranayama aim to balance and activate these energy centers.",
        "related_concepts": ["kundalini", "prana", "nadis", "subtle body"]
    }
}

# Database of meditation guides
MEDITATION_GUIDES = {
    "beginner": {
        "short": {
            "name": "Simple Breath Awareness",
            "duration": 5,
            "instructions": "Find a comfortable seated position with your back straight but not stiff. Close your eyes or maintain a soft gaze.\n\n1. Take a few deep breaths to settle in.\n2. Begin to notice your natural breathing pattern without changing it.\n3. Focus your attention on the sensation of breath entering and leaving your nostrils.\n4. When your mind wanders (which is natural), gently bring your attention back to your breath.\n5. Continue for 5 minutes, gradually extending the duration as you become more comfortable with the practice."
        },
        "medium": {
            "name": "Body and Breath Awareness",
            "duration": 15,
            "instructions": "Find a comfortable seated position with your back straight but not stiff. Close your eyes or maintain a soft gaze.\n\n1. Begin with 5 deep breaths, inhaling through your nose and exhaling through your mouth.\n2. Scan your body from head to toe, noticing any areas of tension and allowing them to relax.\n3. Bring your attention to your natural breathing pattern.\n4. Count each breath cycle (inhale and exhale) up to 10, then start again from 1.\n5. If your mind wanders, simply note the distraction without judgment and return to counting breaths.\n6. For the last few minutes, let go of counting and simply rest in awareness of your breath and body.\n7. Gradually become aware of your surroundings and gently open your eyes."
        },
        "long": {
            "name": "Guided Mindfulness Meditation",
            "duration": 30,
            "instructions": "Find a comfortable seated position with your back straight but not stiff. Close your eyes.\n\n1. Begin by taking 5 deep, cleansing breaths.\n2. Bring awareness to the points of contact between your body and the surface supporting you.\n3. Conduct a slow body scan from your toes to the top of your head, noting sensations without judgment.\n4. Shift attention to your breath, observing its natural rhythm without controlling it.\n5. Notice the sensation of breath at your nostrils, chest, and abdomen.\n6. When thoughts arise, acknowledge them with the mental note 'thinking,' and gently return to your breath.\n7. Expand your awareness to include sounds around you, noting them without analysis.\n8. Further expand to include all sensations, thoughts, and emotions as they arise and pass.\n9. For the final minutes, rest in open awareness, simply being present with whatever arises.\n10. Gradually reawaken your body with slight movements and slowly open your eyes."
        }
    },
    "intermediate": {
        "short": {
            "name": "So Hum Mantra Meditation",
            "duration": 10,
            "instructions": "Sit in a comfortable meditation posture with your spine erect and shoulders relaxed.\n\n1. Close your eyes and take a few deep breaths to center yourself.\n2. Begin to observe your natural breathing pattern.\n3. As you inhale, mentally repeat the sound 'So'.\n4. As you exhale, mentally repeat the sound 'Hum'.\n5. Let the mantra sync naturally with your breath without forcing it.\n6. When your mind wanders, gently bring it back to the mantra and your breath.\n7. Continue for 10 minutes, allowing the mantra to become more subtle over time."
        },
        "medium": {
            "name": "Anapana Meditation",
            "duration": 20,
            "instructions": "Sit in a comfortable meditation posture with your spine straight and shoulders relaxed.\n\n1. Close your eyes and take a few moments to settle your body.\n2. Bring your full attention to the sensation of breath at the entrance of your nostrils.\n3. Notice the subtle sensations as air passes in and out - temperature, texture, duration.\n4. Observe the beginning, middle, and end of each inhale and exhale.\n5. When your mind wanders, note the distraction and gently but firmly return attention to breath sensations.\n6. Maintain continuous awareness of each breath without controlling it.\n7. As your concentration deepens, try to notice increasingly subtle sensations.\n8. Continue for 20 minutes, maintaining equanimity with whatever arises."
        },
        "long": {
            "name": "Heart-Centered Meditation",
            "duration": 45,
            "instructions": "Sit comfortably with your spine straight. Relax your shoulders and rest your hands in your lap or on your thighs.\n\n1. Close your eyes and take several deep breaths to center yourself.\n2. Bring your awareness to your heart center in the middle of your chest.\n3. Imagine a warm, golden light glowing in your heart center.\n4. With each inhale, visualize this light growing brighter and more radiant.\n5. With each exhale, imagine this light expanding outward from your heart.\n6. When ready, invite a quality you wish to cultivate (love, compassion, peace) into this light.\n7. Allow this quality to permeate your entire being with each breath.\n8. If your mind wanders, gently return to the sensation and visualization at your heart.\n9. Gradually expand this light beyond yourself, encompassing loved ones, acquaintances, all beings.\n10. Remain in this expanded state of awareness for as long as comfortable.\n11. To close, bring your awareness back to your heart, then to your breath, and finally to your body.\n12. Gently open your eyes when ready."
        }
    },
    "advanced": {
        "short": {
            "name": "Self-Inquiry Meditation",
            "duration": 15,
            "instructions": "Sit in a comfortable meditation posture with your spine straight and body relaxed.\n\n1. Close your eyes and take a few deep breaths to center yourself.\n2. Begin by asking internally: 'Who am I?'\n3. Rather than intellectually answering, trace the 'I' thought to its source.\n4. Notice the silence or space from which the question arises.\n5. When thoughts arise, don't resist them, but ask 'To whom do these thoughts arise?'\n6. The answer will be 'To me'.\n7. Then ask 'Who is this I?' and again trace it to its source.\n8. Rest in the silence between thoughts, gradually abiding more in pure awareness.\n9. Continue this inquiry for 15 minutes, maintaining alertness without tension."
        },
        "medium": {
            "name": "Witness Consciousness Practice",
            "duration": 30,
            "instructions": "Sit in a comfortable meditation posture with your spine straight and body relaxed.\n\n1. Close your eyes and begin by observing your breath until your mind becomes relatively calm.\n2. Shift your attention from the breath to the act of being aware itself.\n3. Notice thoughts, emotions, and sensations as they arise, without judgment or analysis.\n4. Ask yourself: 'Who is aware of these experiences?'\n5. Rather than answering conceptually, rest in the space of the question.\n6. As identification with thoughts occurs, gently remind yourself 'I am the witness, not the thought'.\n7. Notice the unchanging awareness that persists regardless of what arises in consciousness.\n8. Allow yourself to abide as the witness, neither accepting nor rejecting any experience.\n9. If you become lost in thought, simply notice and return to witnessing.\n10. Continue for 30 minutes, gradually deepening into pure witnessing."
        },
        "long": {
            "name": "Neti-Neti Meditation",
            "duration": 60,
            "instructions": "Sit in a comfortable meditation posture with your spine straight and body relaxed.\n\n1. Begin with 10 minutes of breath awareness to steady the mind.\n2. Systematically investigate your experience by mentally noting 'not this, not this' (neti-neti) to all phenomena that arise.\n3. When bodily sensations arise, observe them and note 'I am not this body'.\n4. When emotions arise, observe them and note 'I am not these emotions'.\n5. When thoughts arise, observe them and note 'I am not these thoughts'.\n6. When memories or desires arise, observe them and note 'I am not these memories or desires'.\n7. Even when subtle states of bliss or special insights arise, note 'I am not even this'.\n8. Continue negating all objects of awareness, including the sense of being a separate self.\n9. Rest in what remains – the pure awareness that cannot be negated.\n10. Abide in this stateless state, neither accepting nor rejecting whatever arises.\n11. If identification recurs, gently resume the neti-neti investigation.\n12. Continue for up to 60 minutes, gradually dissolving all identification with phenomenal experience."
        }
    }
}

# Database of sacred texts
SACRED_TEXTS = {
    "bhagavad gita": {
        "name": "Bhagavad Gita",
        "description": "The Bhagavad Gita is a 700-verse Hindu scripture that is part of the epic Mahabharata. It is structured as a dialogue between Prince Arjuna and his guide and charioteer, Krishna, an avatar of Lord Vishnu. The conversation occurs just before the start of the Kurukshetra War, when Arjuna is overcome with moral dilemma about fighting his own relatives.",
        "key_teachings": [
            "The immortality of the soul (Atman)",
            "The nature of Dharma (duty/righteousness)",
            "Different paths to spiritual realization: Karma Yoga (path of action), Bhakti Yoga (path of devotion), Jnana Yoga (path of knowledge), and Raja Yoga (path of meditation)",
            "The importance of detachment from the fruits of one's actions",
            "The vision of God as the source of all existence"
        ]
    },
    "upanishads": {
        "name": "Upanishads",
        "description": "The Upanishads are a collection of philosophical texts that form the theoretical basis for the Hindu religion. They are considered by Hindus to contain revealed truths (Shruti) about the nature of ultimate reality (Brahman) and the path to liberation (Moksha).",
        "key_teachings": [
            "The concept of Brahman (ultimate reality) and its identity with Atman (individual soul)",
            "The illusory nature of the material world (Maya)",
            "The cycle of birth, death, and rebirth (Samsara)",
            "The path to liberation from this cycle (Moksha)",
            "The practice of meditation and self-inquiry for spiritual realization"
        ]
    },
    "yoga sutras": {
        "name": "Yoga Sutras of Patanjali",
        "description": "The Yoga Sutras of Patanjali is a foundational text of Yoga philosophy. Composed of 196 aphorisms (sutras), the text outlines the eight limbs of yoga, known as Ashtanga Yoga, and provides guidance on how to master the mind and achieve liberation.",
        "key_teachings": [
            "The eight limbs of yoga: Yama (restraints), Niyama (observances), Asana (posture), Pranayama (breath control), Pratyahara (withdrawal of senses), Dharana (concentration), Dhyana (meditation), and Samadhi (absorption)",
            "The concept of Chitta Vritti Nirodha (cessation of the fluctuations of the mind)",
            "The different types of Samadhi and the path to Kaivalya (liberation)",
            "The concept of Ishvara (Supreme Being) and devotion to it",
            "The nature of suffering and how to overcome it"
        ]
    },
    "vedas": {
        "name": "Vedas",
        "description": "The Vedas are a large body of religious texts originating in ancient India, composed in Vedic Sanskrit, and among the oldest scriptures of Hinduism. There are four Vedas: the Rigveda, the Yajurveda, the Samaveda, and the Atharvaveda. Each Veda has been subclassified into four major text types: Samhitas (hymns), Brahmanas (commentaries), Aranyakas (wilderness texts), and Upanishads (philosophical discussions).",
        "key_teachings": [
            "Rituals, hymns, and mantras for worship and spiritual practices",
            "Philosophical concepts including the nature of existence, consciousness, and divinity",
            "Social and ethical guidelines for communal living",
            "Knowledge about various sciences including medicine, astronomy, and mathematics",
            "The foundational concepts that later developed into the six orthodox schools of Hindu philosophy"
        ]
    }
}

# Database of spiritual practices
SPIRITUAL_PRACTICES = {
    "mantra": {
        "name": "Mantra Meditation",
        "description": "Mantra meditation involves the repetition of a sound, word, or phrase, often in Sanskrit, used to focus the mind and induce altered states of consciousness. Mantras are considered sacred sound vibrations that can align the practitioner with specific energetic qualities or deities.",
        "steps": "1. Choose a mantra that resonates with you (e.g., Om, So Hum, Om Namah Shivaya)\n2. Find a comfortable seated position\n3. Close your eyes and take a few deep breaths to center yourself\n4. Begin repeating your chosen mantra either aloud, in a whisper, or mentally\n5. Focus your full attention on the sound and vibration of the mantra\n6. When your mind wanders, gently bring it back to the mantra\n7. Continue for 10-30 minutes\n8. To finish, gradually slow the repetition and sit in silence for a few moments",
        "benefits": [
            "Calms and focuses the mind",
            "Reduces stress and anxiety",
            "Develops concentration",
            "Connects to specific spiritual qualities",
            "Helps transcend ordinary consciousness"
        ]
    },
    "pranayama": {
        "name": "Pranayama (Breath Control)",
        "description": "Pranayama consists of various breathing techniques designed to control prana (life force energy) in the body. These practices aim to purify the energy channels, balance the mind, and prepare the practitioner for deeper meditation.",
        "steps": "For basic Anulom Vilom (Alternate Nostril Breathing):\n\n1. Sit comfortably with your spine straight\n2. Rest your left hand on your left knee\n3. Raise your right hand and fold your index and middle fingers toward your palm (using thumb and ring fingers)\n4. Close your right nostril with your thumb and inhale slowly through the left nostril\n5. Close both nostrils and hold the breath briefly\n6. Release your thumb and exhale slowly through the right nostril\n7. Inhale through the right nostril\n8. Hold the breath\n9. Exhale through the left nostril\n10. This completes one round. Continue for 5-10 rounds, gradually increasing over time",
        "benefits": [
            "Balances the nervous system",
            "Improves respiratory function",
            "Enhances mental clarity",
            "Balances subtle energies in the body",
            "Prepares the mind for meditation"
        ]
    },
    "yoga": {
        "name": "Hatha Yoga",
        "description": "Hatha Yoga is a branch of yoga that emphasizes physical postures (asanas), breathing techniques (pranayama), and meditation. It aims to balance the body's energy, improve physical health, and prepare the practitioner for deeper spiritual practices.",
        "steps": "For a basic practice:\n\n1. Begin with a few minutes of centering, sitting quietly and connecting with your breath\n2. Perform gentle warm-up movements to prepare the body\n3. Practice a sequence of basic asanas (poses) such as Mountain Pose, Downward-Facing Dog, Warrior poses, and Child's Pose\n4. Hold each pose for several breaths, maintaining awareness of your alignment and sensations\n5. Include some gentle twists and stretches for the spine\n6. End with a few minutes in Savasana (Corpse Pose) for integration\n7. Close with a moment of gratitude or a simple meditation",
        "benefits": [
            "Improves physical flexibility and strength",
            "Balances the nervous system",
            "Enhances body awareness",
            "Prepares the body and mind for meditation",
            "Balances the flow of prana (life energy)"
        ]
    },
    "japa": {
        "name": "Japa (Mantra Repetition with Mala)",
        "description": "Japa is the meditative repetition of a mantra or divine name, often using a mala (string of 108 beads) to keep count. This practice helps focus the mind, cultivate devotion, and connect with divine energies.",
        "steps": "1. Choose a mantra or divine name that resonates with you\n2. Find a comfortable seated position with your spine straight\n3. Hold your mala in your right hand, with the beads resting on your middle finger\n4. Begin with the bead next to the guru bead (the larger central bead)\n5. Recite your mantra once as you touch the first bead with your thumb\n6. Move to the next bead and repeat\n7. Continue until you reach the guru bead (typically 108 repetitions)\n8. Do not cross over the guru bead; instead, turn the mala around and continue in the opposite direction if desired\n9. Practice with full concentration and devotion",
        "benefits": [
            "Develops one-pointed concentration",
            "Cultivates devotion and spiritual connection",
            "Creates positive mental patterns",
            "Calms the nervous system",
            "Builds spiritual discipline"
        ]
    }
}

def get_concept_info(concept_name):
    """Retrieves information about a spiritual concept."""
    return CONCEPTS.get(concept_name.lower())

def get_meditation_guide(experience_level, time_available):
    """Retrieves an appropriate meditation guide based on experience and time."""
    level_guides = MEDITATION_GUIDES.get(experience_level.lower())
    if not level_guides:
        return None
    
    if time_available <= 10:
        return level_guides.get("short")
    elif time_available <= 30:
        return level_guides.get("medium")
    else:
        return level_guides.get("long")

def get_sacred_text_info(text_name):
    """Retrieves information about a sacred text."""
    return SACRED_TEXTS.get(text_name.lower())

def get_practice_guide(practice_type):
    """Retrieves a guide for a specific spiritual practice."""
    return SPIRITUAL_PRACTICES.get(practice_type.lower())