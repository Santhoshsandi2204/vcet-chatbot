# VCET Database & Fallback Search Logic

VCET_DATA = {
    "collegeName": "Velammal College of Engineering & Technology",
    "principal": "Dr. P. Alli",
    "director": "Dr. N. Rajkumar",
    "accreditations": [
        "Autonomous Institution",
        "Accredited by NAAC with 'A' Grade",
        "All UG Departments Accredited by NBA"
    ],
    "contact": {
        "admissionPhone": "+91 99949 94991",
        "officePhone": "0452-2465289",
        "email": "principal@vcet.ac.in",
        "address": "Velammal Nagar, Madurai to Rameshwaram High Road, Viraganoor, Madurai - 625 009",
        "hours": "08:25 AM to 04:10 PM"
    },
    "courses": [
        {
            "code": "B.E. CSE",
            "name": "B.E. Computer Science and Engineering",
            "dept": "Computer Science",
            "duration": "4 Years",
            "eligibility": "10+2 with 50% in PCM (Physics, Chemistry, Maths)",
            "fee": "₹85,000 / year (Govt Quota) | ₹1,50,000 / year (Management)",
            "description": "NBA Accredited. Focuses on algorithms, data structures, software engineering, databases, cloud, and machine learning."
        },
        {
            "code": "B.Tech. IT",
            "name": "B.Tech. Information Technology",
            "dept": "Information Technology",
            "duration": "4 Years",
            "eligibility": "10+2 with 50% in PCM",
            "fee": "₹85,000 / year (Govt Quota) | ₹1,50,000 / year (Management)",
            "description": "NBA Accredited. Specializes in internet architectures, system security, software design, wireless networks, and web engineering."
        },
        {
            "code": "B.Tech. AI&DS",
            "name": "B.Tech. Artificial Intelligence and Data Science",
            "dept": "Artificial Intelligence",
            "duration": "4 Years",
            "eligibility": "10+2 with 50% in PCM",
            "fee": "₹85,000 / year (Govt Quota) | ₹1,60,000 / year (Management)",
            "description": "Designed for advanced statistical analysis, machine learning algorithms, deep learning models, and big data architectures."
        },
        {
            "code": "B.E. Cyber Security",
            "name": "B.E. Computer Science & Engineering (Cyber Security)",
            "dept": "Cyber Security",
            "duration": "4 Years",
            "eligibility": "10+2 with 50% in PCM",
            "fee": "₹85,000 / year (Govt Quota) | ₹1,60,000 / year (Management)",
            "description": "Focused on digital forensics, cryptography, malware analysis, network defenses, threat prevention, and software security."
        },
        {
            "code": "B.E. ECE",
            "name": "B.E. Electronics and Communication Engineering",
            "dept": "Electronics & Communication",
            "duration": "4 Years",
            "eligibility": "10+2 with 50% in PCM",
            "fee": "₹85,000 / year (Govt Quota) | ₹1,40,000 / year (Management)",
            "description": "NBA Accredited. Covers VLSI designs, embedded controllers, IoT networks, telemetry systems, and mobile signal processing."
        },
        {
            "code": "B.E. EEE",
            "name": "B.E. Electrical and Electronics Engineering",
            "dept": "Electrical & Electronics",
            "duration": "4 Years",
            "eligibility": "10+2 with 50% in PCM",
            "fee": "₹85,000 / year (Govt Quota) | ₹1,20,000 / year (Management)",
            "description": "NBA Accredited. Deals with high-voltage systems, electric vehicle drives, smart grids, renewable energy, and power grids management."
        },
        {
            "code": "B.E. VLSI",
            "name": "B.E. Electronics Engineering (VLSI)",
            "dept": "Electronics & Communication",
            "duration": "4 Years",
            "eligibility": "10+2 with 50% in PCM",
            "fee": "₹85,000 / year (Govt Quota) | ₹1,30,000 / year (Management)",
            "description": "Specialized electronics design stream covering silicon microchips, IC designs, FPGA testing, and hardware descriptive languages."
        },
        {
            "code": "B.E. MECH",
            "name": "B.E. Mechanical Engineering",
            "dept": "Mechanical Engineering",
            "duration": "4 Years",
            "eligibility": "10+2 with 45% in PCM",
            "fee": "₹75,000 / year (Govt Quota) | ₹1,10,000 / year (Management)",
            "description": "NBA Accredited. Covers manufacturing automation, CAD design modeling, thermal systems, fluid dynamics, and robotics science."
        },
        {
            "code": "B.E. CIVIL",
            "name": "B.E. Civil Engineering",
            "dept": "Civil Engineering",
            "duration": "4 Years",
            "eligibility": "10+2 with 45% in PCM",
            "fee": "₹75,000 / year (Govt Quota) | ₹1,00,000 / year (Management)",
            "description": "NBA Accredited. Focuses on structural mechanics, concrete mix design, soil dynamics, geodetic surveying, and environmental planning."
        },
        {
            "code": "MBA",
            "name": "Master of Business Administration",
            "dept": "Management Studies",
            "duration": "2 Years",
            "eligibility": "Bachelor's degree with 50% + valid TANCET MBA score",
            "fee": "₹1,20,000 / year",
            "description": "Post-graduate training in financial planning, corporate communications, brand marketing, HR, and operations management."
        },
        {
            "code": "M.E. CS",
            "name": "M.E. Communication Systems",
            "dept": "Electronics & Communication",
            "duration": "2 Years",
            "eligibility": "B.E. in ECE / Electronics with valid TANCET / GATE score",
            "fee": "₹80,000 / year",
            "description": "Post-graduate study in advanced optical communications, wireless systems, signal detection, and telecom networks."
        },
        {
            "code": "M.E. PSE",
            "name": "M.E. Power Systems Engineering",
            "dept": "Electrical & Electronics",
            "duration": "2 Years",
            "eligibility": "B.E. in EEE / Electrical with valid TANCET / GATE score",
            "fee": "₹80,000 / year",
            "description": "Advanced research studies in smart grid stability, digital protective relays, load forecasting, and power converters."
        }
    ],
    "departments": [
        {
            "name": "Computer Science",
            "hod": "Dr. G. Vinoth Chakkaravarthy",
            "email": "hod.cse@vcet.ac.in",
            "staff": [
                { "name": "Dr. G. Vinoth Chakkaravarthy", "role": "HOD & Professor", "email": "vinoth.cse@vcet.ac.in", "ext": "501" },
                { "name": "Dr. N. Rajkumar", "role": "Director & Professor", "email": "rajkumar.cse@vcet.ac.in", "ext": "502" },
                { "name": "Dr. P. Alli", "role": "Principal & Professor", "email": "principal@vcet.ac.in", "ext": "100" },
                { "name": "Dr. A. M. Rajeswari", "role": "Associate Professor", "email": "rajeswari.cse@vcet.ac.in", "ext": "503" },
                { "name": "Dr. V. Akilandeswari", "role": "Associate Professor", "email": "akila.cse@vcet.ac.in", "ext": "504" },
                { "name": "Mr. K. Azarudeen", "role": "Assistant Professor I", "email": "azarudeen.cse@vcet.ac.in", "ext": "505" }
            ]
        },
        {
            "name": "Cyber Security",
            "hod": "Dr. J. V. Anchitaalagammai",
            "email": "hod.cyber@vcet.ac.in",
            "staff": [
                { "name": "Dr. J. V. Anchitaalagammai", "role": "HOD & Professor", "email": "anchita.cyber@vcet.ac.in", "ext": "521" },
                { "name": "Dr. S. Kavitha", "role": "Associate Professor", "email": "kavitha.cyber@vcet.ac.in", "ext": "522" },
                { "name": "Mr. S. Murali", "role": "Assistant Professor II", "email": "murali.cyber@vcet.ac.in", "ext": "523" }
            ]
        },
        {
            "name": "Information Technology",
            "hod": "Dr. R. Kavitha",
            "email": "hod.it@vcet.ac.in",
            "staff": [
                { "name": "Dr. R. Kavitha", "role": "HOD & Professor", "email": "kavitha.it@vcet.ac.in", "ext": "601" }
            ]
        },
        {
            "name": "Artificial Intelligence",
            "hod": "Dr. S. Sasikala",
            "email": "hod.aids@vcet.ac.in",
            "staff": [
                { "name": "Dr. S. Sasikala", "role": "HOD & Professor", "email": "sasikala.aids@vcet.ac.in", "ext": "602" }
            ]
        },
        {
            "name": "Electronics & Communication",
            "hod": "Dr. S. Vasuki",
            "email": "hod.ece@vcet.ac.in",
            "staff": [
                { "name": "Dr. S. Vasuki", "role": "HOD & Professor", "email": "vasuki.ece@vcet.ac.in", "ext": "701" },
                { "name": "Dr. K. Kavitha", "role": "Professor (VLSI stream)", "email": "kavitha.ece@vcet.ac.in", "ext": "702" }
            ]
        },
        {
            "name": "Electrical & Electronics",
            "hod": "Dr. A. Shunmugalatha",
            "email": "hod.eee@vcet.ac.in",
            "staff": [
                { "name": "Dr. A. Shunmugalatha", "role": "HOD & Professor", "email": "shunmugalatha.eee@vcet.ac.in", "ext": "801" }
            ]
        },
        {
            "name": "Mechanical Engineering",
            "hod": "Dr. G. Manikandan",
            "email": "hod.mech@vcet.ac.in",
            "staff": [
                { "name": "Dr. G. Manikandan", "role": "HOD & Professor", "email": "manikandan.mech@vcet.ac.in", "ext": "901" },
                { "name": "Mr. M. Rajachandra Sekar", "role": "Assistant Professor III", "email": "rajachandra.mech@vcet.ac.in", "ext": "902" }
            ]
        },
        {
            "name": "Civil Engineering",
            "hod": "Dr. R. Ganesan",
            "email": "hod.civil@vcet.ac.in",
            "staff": [
                { "name": "Dr. R. Ganesan", "role": "HOD & Professor", "email": "ganesan.civil@vcet.ac.in", "ext": "401" }
            ]
        },
        {
            "name": "Management Studies",
            "hod": "Dr. N. Arun Sankar",
            "email": "hod.mba@vcet.ac.in",
            "staff": [
                { "name": "Dr. N. Arun Sankar", "role": "HOD & Professor", "email": "arunsankar.mba@vcet.ac.in", "ext": "301" }
            ]
        },
        {
            "name": "Science & Humanities",
            "hod": "Dr. A. Pushpalatha (Maths)",
            "email": "hod.sh@vcet.ac.in",
            "staff": [
                { "name": "Dr. A. Pushpalatha", "role": "HOD & Professor (Mathematics)", "email": "pushpa.maths@vcet.ac.in", "ext": "201" },
                { "name": "Dr. R. Rajesh", "role": "HOD & Professor (Physics)", "email": "rajesh.physics@vcet.ac.in", "ext": "202" },
                { "name": "Dr. C. Sankar", "role": "HOD & Professor (Chemistry)", "email": "sankar.chemistry@vcet.ac.in", "ext": "203" },
                { "name": "Dr. S. Gomathy", "role": "HOD & Professor (English)", "email": "gomathy.english@vcet.ac.in", "ext": "204" }
            ]
        }
    ],
    "transport": {
        "notes": "VCET operates transit fleets within a 30 km radius of Madurai. Boarding pass bookings are handled at the administrative desk.",
        "contacts": [
            { "role": "Transport In-charge", "name": "Mr. M. Rajachandra Sekar", "phone": "+91 99440 63309" },
            { "role": "Transport Manager", "name": "Mr. Siva Sakthi", "phone": "+91 96556 72040" },
            { "role": "Transport Manager (Alt)", "name": "Mr. Boopathy", "phone": "+91 90477 64647" }
        ],
        "routes": [
            { "zone": "Route 1 (Thirunagar Line)", "points": "Thirunagar, Thirumangalam, Pykara, Madurai Central, Viraganoor Campus", "fee": "₹24,000" },
            { "zone": "Route 2 (Koodal Nagar Line)", "points": "Koodal Nagar, Goripalayam, Kalavasal, Fathima College, Campus gate", "fee": "₹26,000" },
            { "zone": "Route 3 (Mattuthavani Line)", "points": "Mattuthavani Bus Stand, Anna Nagar, KK Nagar, Othakadai, Campus", "fee": "₹22,000" },
            { "zone": "Route 4 (Nagamalai Western)", "points": "Nagamalai Pudukottai, Madurai Kamaraj University, Samayanallur", "fee": "₹30,000" },
            { "zone": "Route 5 (Corridor Local)", "points": "Sellur, Simmakkal, Periyar Central, South Gate, Viraganoor", "fee": "₹20,000" },
            { "zone": "Route 6 (Suburban Distant)", "points": "Melur, Vadipatti, Sholavandan, Usilampatti suburban zones", "fee": "₹34,000" }
        ]
    }
}

# Fallback text matching engine if no Gemini API Key is supplied
def match_fallback_response(query):
    query = query.lower().strip()
    
    # GREETINGS
    if any(greet in query for greet in ["hi", "hello", "hey", "greetings", "good morning", "good afternoon"]):
        return ("Hello! I am the **VCET AI Assistant** running in local mode. "
                "How can I help you today? You can ask about our NBA-accredited courses, Principal, "
                "HODs, or transport helpline numbers.")

    # PRINCIPAL / LEADERSHIP
    if any(kw in query for kw in ["principal", "director", "alli", "rajkumar", "leadership"]):
        return (f"**Velammal College of Engineering & Technology Leadership Team:**\n\n"
                f"* **Principal:** {VCET_DATA['principal']}\n"
                f"* **Director:** {VCET_DATA['director']}\n"
                f"* **Official Contact Email:** {VCET_DATA['contact']['email']}\n"
                f"* **Office landline:** {VCET_DATA['contact']['officePhone']}\n\n"
                f"You can query details about admissions directly by calling **{VCET_DATA['contact']['admissionPhone']}**.")

    # COURSES / BRANCHES / ELIGIBILITY
    if any(kw in query for kw in ["course", "courses", "major", "majors", "program", "programs", "admission", "fees", "fee"]):
        # Check specific course
        if "cyber" in query or "security" in query:
            c = next(x for x in VCET_DATA["courses"] if "Cyber" in x["code"])
            return f"### {c['name']} ({c['code']})\n\n{c['description']}\n\n* **Duration:** {c['duration']}\n* **Eligibility:** {c['eligibility']}\n* **Annual Fee:** {c['fee']}"
        if "cse" in query or "computer science" in query:
            c = next(x for x in VCET_DATA["courses"] if x["code"] == "B.E. CSE")
            return f"### {c['name']} ({c['code']})\n\n{c['description']}\n\n* **Duration:** {c['duration']}\n* **Eligibility:** {c['eligibility']}\n* **Annual Fee:** {c['fee']}"
        if "it" in query or "information technology" in query:
            c = next(x for x in VCET_DATA["courses"] if x["code"] == "B.Tech. IT")
            return f"### {c['name']} ({c['code']})\n\n{c['description']}\n\n* **Duration:** {c['duration']}\n* **Eligibility:** {c['eligibility']}\n* **Annual Fee:** {c['fee']}"
        if "ai" in query or "data science" in query or "aids" in query:
            c = next(x for x in VCET_DATA["courses"] if "AI&DS" in x["code"])
            return f"### {c['name']} ({c['code']})\n\n{c['description']}\n\n* **Duration:** {c['duration']}\n* **Eligibility:** {c['eligibility']}\n* **Annual Fee:** {c['fee']}"
        if "ece" in query or "electronics" in query:
            if "vlsi" in query:
                c = next(x for x in VCET_DATA["courses"] if "VLSI" in x["code"])
                return f"### {c['name']} ({c['code']})\n\n{c['description']}\n\n* **Duration:** {c['duration']}\n* **Eligibility:** {c['eligibility']}\n* **Annual Fee:** {c['fee']}"
            c = next(x for x in VCET_DATA["courses"] if x["code"] == "B.E. ECE")
            return f"### {c['name']} ({c['code']})\n\n{c['description']}\n\n* **Duration:** {c['duration']}\n* **Eligibility:** {c['eligibility']}\n* **Annual Fee:** {c['fee']}"
        if "eee" in query or "electrical" in query:
            c = next(x for x in VCET_DATA["courses"] if x["code"] == "B.E. EEE")
            return f"### {c['name']} ({c['code']})\n\n{c['description']}\n\n* **Duration:** {c['duration']}\n* **Eligibility:** {c['eligibility']}\n* **Annual Fee:** {c['fee']}"
        if "mech" in query or "mechanical" in query:
            c = next(x for x in VCET_DATA["courses"] if "MECH" in x["code"])
            return f"### {c['name']} ({c['code']})\n\n{c['description']}\n\n* **Duration:** {c['duration']}\n* **Eligibility:** {c['eligibility']}\n* **Annual Fee:** {c['fee']}"
        if "civil" in query:
            c = next(x for x in VCET_DATA["courses"] if "CIVIL" in x["code"])
            return f"### {c['name']} ({c['code']})\n\n{c['description']}\n\n* **Duration:** {c['duration']}\n* **Eligibility:** {c['eligibility']}\n* **Annual Fee:** {c['fee']}"
        if "mba" in query or "management" in query:
            c = next(x for x in VCET_DATA["courses"] if x["code"] == "MBA")
            return f"### {c['name']} ({c['code']})\n\n{c['description']}\n\n* **Duration:** {c['duration']}\n* **Eligibility:** {c['eligibility']}\n* **Annual Fee:** {c['fee']}"

        # Return list of all courses
        clist = "\n".join([f"* **{c['code']}**: {c['name']} ({c['duration']})" for c in VCET_DATA["courses"]])
        return ("Velammal College of Engineering & Technology offers the following UG & PG programs:\n\n"
                f"{clist}\n\n"
                "To see details of a specific course, ask me e.g., 'Tell me about B.Tech AI&DS'.")

    # HODs / DEPARTMENTS
    if any(kw in query for kw in ["hod", "hods", "head", "heads", "department", "departments"]):
        hlist = "\n".join([f"* **{d['name']}:** {d['hod']} ({d['email']})" for d in VCET_DATA["departments"]])
        return ("### VCET HOD Directory:\n\n"
                f"{hlist}\n\n"
                "You can view contacts or write to HODs directly at these email IDs.")

    # STAFF / FACULTY
    if any(kw in query for kw in ["staff", "faculty", "professors", "professor", "teachers", "teacher"]):
        if "cse" in query or "computer" in query:
            dept = next(x for x in VCET_DATA["departments"] if x["name"] == "Computer Science")
            slist = "\n".join([f"* **{s['name']}** ({s['role']}) - Ext: {s['ext']}, Email: {s['email']}" for s in dept["staff"]])
            return f"### Computer Science Department Faculty:\n\n{slist}"
        if "cyber" in query or "security" in query:
            dept = next(x for x in VCET_DATA["departments"] if x["name"] == "Cyber Security")
            slist = "\n".join([f"* **{s['name']}** ({s['role']}) - Ext: {s['ext']}, Email: {s['email']}" for s in dept["staff"]])
            return f"### Cyber Security Department Faculty:\n\n{slist}"

        return "VCET has over 120+ senior faculty members. Try asking about a specific department's faculty, e.g. 'Show me CSE staff list'."

    # TRANSPORT
    if any(kw in query for kw in ["transport", "bus", "buses", "route", "routes", "travel", "manager"]):
        rlist = "\n".join([f"* **{r['zone']}:** covers {r['points']} — Annual Fee: **{r['fee']}**" for r in VCET_DATA["transport"]["routes"]])
        clist = "\n".join([f"* **{c['name']}** ({c['role']}) - Phone: **{c['phone']}**" for c in VCET_DATA["transport"]["contacts"]])
        return ("### VCET Bus Transit System:\n\n"
                f"**Available Routes:**\n{rlist}\n\n"
                f"**Transport Helpline Contacts:**\n{clist}")

    # LOCATION / ADDRESS
    if any(kw in query for kw in ["location", "address", "where", "map", "directions", "reach"]):
        return (f"**Velammal College of Engineering & Technology (VCET) Location:**\n\n"
                f"**Address:** {VCET_DATA['contact']['address']}\n\n"
                f"**Directions:** We are located on the Madurai-Rameshwaram Highway (NH 49), "
                f"near Viraganoor Ring Road junction, Madurai.")

    # GENERAL CONTACTS
    if any(kw in query for kw in ["contact", "phone", "number", "numbers", "enquiry", "email", "office"]):
        return (f"### VCET Office Contacts:\n\n"
                f"* **Admissions Hotline:** {VCET_DATA['contact']['admissionPhone']} (Call for seats/fees)\n"
                f"* **General Office Landline:** {VCET_DATA['contact']['officePhone']} (08:25 AM to 04:10 PM)\n"
                f"* **Primary Email:** {VCET_DATA['contact']['email']}\n"
                f"* **Physical Address:** {VCET_DATA['contact']['address']}")

    # DEFAULT FALLBACK
    return ("I'm currently running in Local Mode. I can answer questions about VCET's courses, "
            "HODs, leadership, transport, location, and office contacts. Try asking:\n\n"
            "* 'Who is the Principal of VCET?'\n"
            "* 'Show me HOD names'\n"
            "* 'What courses are available in VCET?'\n"
            "* 'Give me the transport routes and fees'")
