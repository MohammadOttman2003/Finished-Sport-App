# Were creating a basic Python Script that store some information about sports Injuries

injuries = {
    "acl tear": {
        "Description" : "A tear of the anterior cruciate ligament in the knee.",
        "Common Sports": ["Basketball, Soccer, Volleyball, Football"],
        "Treatment": "Surgery followed by Physical Therapy.",
        "Recovery Exercises": ["Nordic Curls","HamString Curls", "Back-Sled","Walking backwards on incline Treadmill"]
    },
    "concussion": {
        "Description" : "A brain injury caused by a blow to the head.",
        "Common Sports": ["Football", "Boxing", "Rugby"],
        "Treatment": "Rest and gradual return to activities. Nuero-Muscular Therapy along with rest can accelerate healing process.",
        "Recovery Exercises": ["Stationary Bike", "Walking"]
    },
    "sprained ankle": {
        "Description" : "An injury to the ligaments in the ankle.",
        "Common Sports" : ["Basketball", "Running", "Soccer"],
        "Treatment" : "Rest, ice, compression, and elevation (RICE).",
        "Recovery Exercises" : ["Calf Raises,", "Negative Calf Raises", "Balance on one foot", "Spell Alphabet with foot"]
    },
    "tibia fracture": {
        "Description" : "When a fall blow places more pressure on tibia causing a complete/partial break.",
        "Common Sports" : ["Football","Basketball","Rugby"],
        "Treatment" : "Surgery, usually one including nails or plates, followed by Physical Therapy",
        "Recovery Exercises" : ["One legged wall squats","leg curls","Step-ups","Calf raises"]
    },
    "meniscus tear": {
        "Description": "Damage to the cartilage that stabilizes and cushions the knee joint, often occurring alongside other knee injuries.",
        "Common Sports": ["Football", "Basketball", "Soccer", "Tennis"],
        "Treatment": "Treatment varies from rest and physical therapy to surgery, depending on the severity of the tear.",
        "Recovery Exercises": ["Quad sets", "Straight leg raises", "Hamstring curls", "Heel and calf stretches"]
    },
"rotator cuff tear": {
        "Description": "A tear in the muscles and tendons that stabilize the shoulder joint.",
        "Common Sports": ["Baseball", "Tennis", "Swimming"],
        "Treatment": "Physical therapy for mild tears, potentially surgery for severe cases.",
        "Recovery Exercises": ["Pendulum swings", "Wall climbs", "Resistance band exercises"]
    },
    "shin splints": {
        "Description": "Pain along the shin bone (tibia), commonly occurring from overuse.",
        "Common Sports": ["Running", "Soccer", "Dance"],
        "Treatment": "Rest, ice, and over-the-counter pain relievers; change in exercise routine to include low-impact activities.",
        "Recovery Exercises": ["Toe curls", "Calf stretches", "Shin stretches"]
    },
    "achilles tendonitis": {
        "Description": "Inflammation of the Achilles tendon, often due to overuse.",
        "Common Sports": ["Running", "Basketball", "Tennis"],
        "Treatment": "Rest, ice packs, anti-inflammatory medication, and physical therapy.",
        "Recovery Exercises": ["Calf stretches", "Ankle dorsiflexion", "Towel pull with toes"]
    },
    "groin pull": {
        "Description": "Strain of the muscles of the inner thigh.",
        "Common Sports": ["Hockey", "Soccer", "Baseball"],
        "Treatment": "Rest, ice, compression, and elevation. Severe cases may require physical therapy.",
        "Recovery Exercises": ["Lying adduction", "Gentle stretches", "Gradually increasing activity"]
    },
    "hamstring strain": {
        "Description": "Overstretching or tearing of the muscles along the back of the thigh.",
        "Common Sports": ["Running", "Soccer", "Basketball"],
        "Treatment": "Rest, ice, compression, and elevation; physical therapy for more severe strains.",
        "Recovery Exercises": ["Gentle stretching", "Strengthening exercises starting with light activity"]
    },
    "stress fractures": {
        "Description": "Small cracks in a bone caused by repetitive force, often from overuse.",
        "Common Sports": ["Track and Field", "Basketball", "Tennis", "Dance"],
        "Treatment": "Rest is crucial. Avoiding the activity that caused the injury until healed. May require protective footwear or braces.",
        "Recovery Exercises": ["Swimming", "Cycling"]
    },
    "tennis elbow": {
        "Description": "A painful condition caused by overuse of the elbow, not limited to tennis players.",
        "Common Sports": ["Tennis", "Golf", "Racquet Sports"],
        "Treatment": "Rest, ice, anti-inflammatory medications. Physical therapy focusing on stretching and strengthening the forearm muscles.",
        "Recovery Exercises": ["Wrist turns with weights", "Elbow bends", "Forearm stretches"]
    },
    "jumper's knee": {
        "Description": "Inflammation or injury of the patellar tendon, the cord-like tissue that joins the patella to the tibia (shinbone).",
        "Common Sports": ["Volleyball", "Basketball", "Track and Field activities involving jumping"],
        "Treatment": "Rest, ice, compression, and elevation. In some cases, corticosteroid injections or surgery may be necessary.",
        "Recovery Exercises": ["Quad stretches", "Leg presses", "Gradual return to jumping activities"]
    },
    "Lumbar Radiculopathy": {
        "Description": "Compression of the lumbar nerves causing pain or discomfort radiating down the leg.",
        "Common Sports": ["Weightlifting", "Golf", "Cycling"],
        "Treatment": "Physical therapy, anti-inflammatory medication, and in some cases, surgery.",
        "Recovery Exercises": ["Lower back stretches", "Core strengthening exercises", "Aerobic conditioning"]
    },
    "Plantar Fasciitis": {
        "Description": "Inflammation of the plantar fascia, the thick band of tissue on the bottom of the foot.",
        "Common Sports": ["Running", "Ballet", "Aerobic sports"],
        "Treatment": "Rest, ice, physical therapy, and night splints or orthotics.",
        "Recovery Exercises": ["Arch stretches", "Toe stretches", "Calf stretches"]
    },
    "MCL Sprain": {
        "Description": "A sprain or tear of the medial collateral ligament on the inside of the knee.",
        "Common Sports": ["Football", "Skiing", "Soccer"],
        "Treatment": "Bracing, rest, ice, and compression. Severe sprains may require surgery.",
        "Recovery Exercises": ["Hamstring curls", "Leg presses", "Knee flexion/extension"]
    },
    "Costochondritis": {
        "Description": "Inflammation of the cartilage that connects a rib to the breastbone, causing chest pain.",
        "Common Sports": ["Rowing", "Golf", "Tennis"],
        "Treatment": "Rest, heat or ice application, and pain relievers.",
        "Recovery Exercises": ["Stretching exercises for the chest", "Gentle strengthening for the upper body"]
    },
    "Pectoralis Major Tear": {
        "Description": "A tear of the pectoralis major muscle, common in activities involving heavy lifting.",
        "Common Sports": ["Weightlifting", "Wrestling", "Football"],
        "Treatment": "Ice, rest, and anti-inflammatory medication. Severe tears may require surgical repair.",
        "Recovery Exercises": ["Gentle stretching of the shoulder", "Gradual strength building"]
    },
    "Ulnar Collateral Ligament Injury": {
        "Description": "An injury to the ligament on the inner side of the elbow, often seen in throwing sports.",
        "Common Sports": ["Baseball", "Javelin throw"],
        "Treatment": "Rest, ice, and compression. Surgery known as Tommy John surgery may be needed for competitive athletes.",
        "Recovery Exercises": ["Elbow stretches", "Wrist stretches", "Gradual throwing program"]
    },
    "Navicular Fracture": {
        "Description": "A break in the navicular bone in the midfoot, often due to impact or overuse.",
        "Common Sports": ["Running", "Basketball", "Ballet"],
        "Treatment": "Immobilization in a cast or boot, with potential for surgery depending on the severity.",
        "Recovery Exercises": ["Toe curls", "Foot doming", "Gradual weight-bearing exercises"]
    },
    "Slap Lesion": {
        "Description": "A tear of the cartilage in the shoulder joint known as the labrum, specifically at the top where the bicep tendon attaches.",
        "Common Sports": ["Baseball", "Tennis", "Swimming"],
        "Treatment": "Physical therapy, and potentially arthroscopic surgery.",
        "Recovery Exercises": ["Shoulder stabilization exercises", "Rotator cuff strengthening",
                               "Scapular mobility exercises"]
    },
    "Compartment Syndrome": {
        "Description": "Increased pressure within one of the body's compartments which contains muscles and nerves, leading to muscle and nerve damage.",
        "Common Sports": ["Running", "Football", "Cycling"],
        "Treatment": "Surgical intervention known as fasciotomy is often required for acute cases.",
        "Recovery Exercises": ["Muscle stretching and strengthening", "Aerobic conditioning",
                               "Gentle muscle reconditioning"]
    },
    "Cubital Tunnel Syndrome": {
        "Description": "A condition caused by increased pressure on the ulnar nerve at the elbow.",
        "Common Sports": ["Baseball", "Tennis", "Golf"],
        "Treatment": "Bracing or splinting, physical therapy, and in severe cases, surgery.",
        "Recovery Exercises": ["Elbow and wrist stretches", "Nerve gliding exercises",
                               "Strengthening exercises for the arm"]
    },
    "Lumbar Radiculopathy": {
        "Description": "Compression of the lumbar nerves causing pain or discomfort radiating down the leg.",
        "Common Sports": ["Weightlifting", "Golf", "Cycling"],
        "Treatment": "Physical therapy, anti-inflammatory medication, and in some cases, surgery.",
        "Recovery Exercises": ["Lower back stretches", "Core strengthening exercises", "Aerobic conditioning"]
    },
    "Plantar Fasciitis": {
        "Description": "Inflammation of the plantar fascia, the thick band of tissue on the bottom of the foot.",
        "Common Sports": ["Running", "Ballet", "Aerobic sports"],
        "Treatment": "Rest, ice, physical therapy, and night splints or orthotics.",
        "Recovery Exercises": ["Arch stretches", "Toe stretches", "Calf stretches"]
    },
    "MCL Sprain": {
        "Description": "A sprain or tear of the medial collateral ligament on the inside of the knee.",
        "Common Sports": ["Football", "Skiing", "Soccer"],
        "Treatment": "Bracing, rest, ice, and compression. Severe sprains may require surgery.",
        "Recovery Exercises": ["Hamstring curls", "Leg presses", "Knee flexion/extension"]
    },
    "Costochondritis": {
        "Description": "Inflammation of the cartilage that connects a rib to the breastbone, causing chest pain.",
        "Common Sports": ["Rowing", "Golf", "Tennis"],
        "Treatment": "Rest, heat or ice application, and pain relievers.",
        "Recovery Exercises": ["Stretching exercises for the chest", "Gentle strengthening for the upper body"]
    },
    "Pectoralis Major Tear": {
        "Description": "A tear of the pectoralis major muscle, common in activities involving heavy lifting.",
        "Common Sports": ["Weightlifting", "Wrestling", "Football"],
        "Treatment": "Ice, rest, and anti-inflammatory medication. Severe tears may require surgical repair.",
        "Recovery Exercises": ["Gentle stretching of the shoulder", "Gradual strength building"]
    },
    "Ulnar Collateral Ligament Injury": {
        "Description": "An injury to the ligament on the inner side of the elbow, often seen in throwing sports.",
        "Common Sports": ["Baseball", "Javelin throw"],
        "Treatment": "Rest, ice, and compression. Surgery known as Tommy John surgery may be needed for competitive athletes.",
        "Recovery Exercises": ["Elbow stretches", "Wrist stretches", "Gradual throwing program"]
    },
    "Navicular Fracture": {
        "Description": "A break in the navicular bone in the midfoot, often due to impact or overuse.",
        "Common Sports": ["Running", "Basketball", "Ballet"],
        "Treatment": "Immobilization in a cast or boot, with potential for surgery depending on the severity.",
        "Recovery Exercises": ["Toe curls", "Foot doming", "Gradual weight-bearing exercises"]
    },
    "Slap Lesion": {
        "Description": "A tear of the cartilage in the shoulder joint known as the labrum, specifically at the top where the bicep tendon attaches.",
        "Common Sports": ["Baseball", "Tennis", "Swimming"],
        "Treatment": "Physical therapy, and potentially arthroscopic surgery.",
        "Recovery Exercises": ["Shoulder stabilization exercises", "Rotator cuff strengthening",
                               "Scapular mobility exercises"]
    },
    "Compartment Syndrome": {
        "Description": "Increased pressure within one of the body's compartments which contains muscles and nerves, leading to muscle and nerve damage.",
        "Common Sports": ["Running", "Football", "Cycling"],
        "Treatment": "Surgical intervention known as fasciotomy is often required for acute cases.",
        "Recovery Exercises": ["Muscle stretching and strengthening", "Aerobic conditioning",
                               "Gentle muscle reconditioning"]
    },
    "Cubital Tunnel Syndrome": {
        "Description": "A condition caused by increased pressure on the ulnar nerve at the elbow.",
        "Common Sports": ["Baseball", "Tennis", "Golf"],
        "Treatment": "Bracing or splinting, physical therapy, and in severe cases, surgery.",
        "Recovery Exercises": ["Elbow and wrist stretches", "Nerve gliding exercises",
                               "Strengthening exercises for the arm"]
    }

}


def get_injury_info(injury_name):
    injury_name_lower = injury_name.lower()
    injury = injuries.get(injury_name_lower)
    if injury:
        return injury
    else:
        return "Injury not found."