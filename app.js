/* ==========================================================================
   Full-Stack VCET AI Chatbot Client Script
   ========================================================================== */

const API_BASE = "http://127.0.0.1:5000/api";
let vcetDatabase = null;

// Chat session state
let currentSessionId = null;
let chatSessions = {}; // Format: { sessionId: { title: "...", messages: [...] } }

document.addEventListener("DOMContentLoaded", () => {
    // 1. Initialize API fetch & populate tabs
    fetchVcetData();

    // 2. Setup theme toggle
    setupThemeToggle();

    // 3. Setup drawer toggle controls
    setupDrawerControls();

    // 4. Setup Chat Engine & session history
    loadChatSessionsFromStorage();
    setupChatEngine();
});

/* ==========================================================================
   API Queries & Directory Rendering
   ========================================================================== */
async function fetchVcetData() {
    const engineBadge = document.getElementById("engine-badge");
    try {
        const response = await fetch(`${API_BASE}/info`);
        if (!response.ok) throw new Error("Backend server not responding");
        
        vcetDatabase = await response.json();
        
        // Populate directory GUI elements
        renderCourses();
        renderStaff();
        populateTransportCalculator();
        renderTransportRoutes();
        setupDirectorySearch();
        
        engineBadge.innerText = "Engine: Live";
        engineBadge.style.color = "#10b981"; // green
    } catch (error) {
        console.error("Failed to connect to Python backend:", error);
        engineBadge.innerText = "Engine: Offline (Connecting...)";
        engineBadge.style.color = "#ef4444"; // red
    }
}

// 1. Render Course Tab
function renderCourses(searchTerm = "") {
    const container = document.getElementById("courses-list-container");
    if (!vcetDatabase) return;

    container.innerHTML = "";
    const query = searchTerm.toLowerCase();
    const filtered = vcetDatabase.courses.filter(c => 
        c.name.toLowerCase().includes(query) ||
        c.code.toLowerCase().includes(query) ||
        c.dept.toLowerCase().includes(query)
    );

    if (filtered.length === 0) {
        container.innerHTML = `<div style="text-align:center; color:var(--text-muted); padding:1rem; font-size:0.8rem;">No courses found.</div>`;
        return;
    }

    filtered.forEach(course => {
        const card = document.createElement("div");
        card.className = "glass-card";
        card.innerHTML = `
            <div class="drawer-c-header">
                <h4>${course.name}</h4>
                <span class="badge-code">${course.code}</span>
            </div>
            <p class="drawer-c-desc">${course.description}</p>
            <div class="drawer-c-meta">
                <span><i class="fa-solid fa-clock"></i> ${course.duration}</span>
                <span><i class="fa-solid fa-receipt"></i> ${course.fee.split('|')[0]}</span>
            </div>
        `;
        container.appendChild(card);
    });
}

// 2. Render Staff Directory Tab
function renderStaff(searchTerm = "") {
    const container = document.getElementById("staff-list-container");
    if (!vcetDatabase) return;

    container.innerHTML = "";
    const query = searchTerm.toLowerCase();
    let matchesFound = false;

    vcetDatabase.departments.forEach(dept => {
        const filtered = dept.staff.filter(person => 
            person.name.toLowerCase().includes(query) ||
            person.role.toLowerCase().includes(query) ||
            dept.name.toLowerCase().includes(query)
        );

        if (filtered.length > 0) {
            matchesFound = true;
            const heading = document.createElement("div");
            heading.style.margin = "1rem 0 0.4rem 0";
            heading.style.fontSize = "0.75rem";
            heading.style.color = "var(--text-muted)";
            heading.style.textTransform = "uppercase";
            heading.style.letterSpacing = "0.5px";
            heading.style.fontWeight = "600";
            heading.innerText = `${dept.name} Dept`;
            container.appendChild(heading);

            filtered.forEach(person => {
                const isHod = person.role.includes("HOD");
                const card = document.createElement("div");
                card.className = `glass-card staff-card ${isHod ? 'hod-card' : ''}`;
                card.innerHTML = `
                    <div class="s-avatar ${!isHod ? 'staff-icon' : ''}">
                        <i class="fa-solid ${isHod ? 'fa-user-tie' : 'fa-user-graduate'}"></i>
                    </div>
                    <div class="s-details">
                        <h4>${person.name}</h4>
                        <p class="s-role">${person.role}</p>
                        <div class="s-meta">
                            <span><i class="fa-solid fa-envelope"></i> <a href="mailto:${person.email}">${person.email}</a></span>
                            <span><i class="fa-solid fa-phone"></i> Ext: ${person.ext}</span>
                        </div>
                    </div>
                `;
                container.appendChild(card);
            });
        }
    });

    if (!matchesFound) {
        container.innerHTML = `<div style="text-align:center; color:var(--text-muted); padding:1rem; font-size:0.8rem;">No staff found.</div>`;
    }
}

// 3. Populate Transit fee calculator
function populateTransportCalculator() {
    const selector = document.getElementById("route-selector");
    if (!vcetDatabase) return;

    selector.innerHTML = `<option value="">-- Select Transit Route --</option>`;
    vcetDatabase.transport.routes.forEach((route, index) => {
        const option = document.createElement("option");
        option.value = index;
        option.innerText = route.zone;
        selector.appendChild(option);
    });

    selector.addEventListener("change", (e) => {
        const priceDisplay = document.querySelector("#calc-result .calc-price");
        const idx = e.target.value;
        if (idx === "") {
            priceDisplay.innerText = "—";
        } else {
            priceDisplay.innerText = vcetDatabase.transport.routes[idx].fee;
        }
    });
}

// 4. Render Transit Routes list
function renderTransportRoutes() {
    const container = document.getElementById("routes-list-container");
    if (!vcetDatabase) return;

    container.innerHTML = "";
    vcetDatabase.transport.routes.forEach(route => {
        const card = document.createElement("div");
        card.className = "glass-card";
        card.style.borderLeft = "3px solid var(--accent-blue)";
        card.innerHTML = `
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.3rem;">
                <strong style="font-size:0.82rem; color:var(--text-primary);">${route.zone}</strong>
                <span style="color:#10b981; font-weight:700; font-size:0.8rem;">${route.fee}</span>
            </div>
            <p style="font-size:0.75rem; color:var(--text-secondary); line-height:1.4;">${route.points}</p>
        `;
        container.appendChild(card);
    });
}

function setupDirectorySearch() {
    document.getElementById("course-search").addEventListener("input", (e) => {
        renderCourses(e.target.value);
    });
    document.getElementById("staff-search").addEventListener("input", (e) => {
        renderStaff(e.target.value);
    });
}

/* ==========================================================================
   Tab Navigation & Drawer Controls
   ========================================================================== */
function setupDrawerControls() {
    const toggleBtn = document.getElementById("toggle-directory-btn");
    const closeBtn = document.getElementById("close-drawer-btn");
    const drawer = document.getElementById("directory-drawer");
    
    // Toggle drawer open/close
    toggleBtn.addEventListener("click", () => {
        drawer.classList.toggle("active");
    });

    closeBtn.addEventListener("click", () => {
        drawer.classList.remove("active");
    });

    // Drawer tab switching
    const tabButtons = document.querySelectorAll(".drawer-tab-btn");
    const tabContents = document.querySelectorAll(".drawer-tab-content");

    tabButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            tabButtons.forEach(b => b.classList.remove("active"));
            tabContents.forEach(c => c.classList.remove("active"));

            btn.classList.add("active");
            document.getElementById(`dtab-${btn.dataset.tab}`).classList.add("active");
        });
    });
}

function setupThemeToggle() {
    const btn = document.getElementById("theme-toggle");
    const html = document.documentElement;

    btn.addEventListener("click", () => {
        const theme = html.getAttribute("data-theme") === "dark" ? "light" : "dark";
        html.setAttribute("data-theme", theme);
        
        const icon = btn.querySelector("i");
        const label = btn.querySelector("span");
        if (theme === "light") {
            icon.className = "fa-solid fa-moon";
            label.innerText = "Toggle Dark Mode";
        } else {
            icon.className = "fa-solid fa-sun";
            label.innerText = "Toggle Light Mode";
        }
    });
}

/* ==========================================================================
   ChatGPT Style Session Engine
   ========================================================================== */
function loadChatSessionsFromStorage() {
    const stored = localStorage.getItem("vcet_chat_sessions");
    if (stored) {
        try {
            chatSessions = JSON.parse(stored);
        } catch (e) {
            chatSessions = {};
        }
    }
    renderSidebarSessions();
}

function saveChatSessionsToStorage() {
    localStorage.setItem("vcet_chat_sessions", JSON.stringify(chatSessions));
}

function renderSidebarSessions() {
    const list = document.getElementById("history-list");
    list.innerHTML = "";

    const sessionIds = Object.keys(chatSessions).reverse(); // Show recent first
    if (sessionIds.length === 0) {
        list.innerHTML = `<div style="text-align:center; padding:1rem; color:var(--text-muted); font-size:0.75rem;">No recent chats.</div>`;
        return;
    }

    sessionIds.forEach(id => {
        const item = document.createElement("div");
        item.className = `history-item ${id === currentSessionId ? 'active' : ''}`;
        item.dataset.id = id;
        item.innerHTML = `
            <span class="history-title-text"><i class="fa-regular fa-message" style="margin-right:0.4rem;"></i> ${escapeHTML(chatSessions[id].title)}</span>
            <button class="btn-delete-history" title="Delete conversation">
                <i class="fa-solid fa-trash-can"></i>
            </button>
        `;

        // Switch to session
        item.addEventListener("click", (e) => {
            if (e.target.closest(".btn-delete-history")) return; // ignore delete clicks
            selectChatSession(id);
        });

        // Delete session
        item.querySelector(".btn-delete-history").addEventListener("click", () => {
            deleteChatSession(id);
        });

        list.appendChild(item);
    });
}

function selectChatSession(id) {
    currentSessionId = id;
    renderSidebarSessions();
    
    // Hide welcome screen
    document.getElementById("welcome-screen").style.display = "none";
    
    // Render session messages
    const log = document.getElementById("messages-log");
    log.innerHTML = "";

    const session = chatSessions[id];
    if (session && session.messages) {
        session.messages.forEach(msg => {
            appendMessageHTML(msg.sender, msg.text);
        });
    }
    scrollToBottom();
}

function startNewChat() {
    currentSessionId = null;
    document.getElementById("welcome-screen").style.display = "flex";
    document.getElementById("messages-log").innerHTML = "";
    
    // Remove active highlights in sidebar
    document.querySelectorAll(".history-item").forEach(item => item.classList.remove("active"));
}

function deleteChatSession(id) {
    delete chatSessions[id];
    saveChatSessionsToStorage();
    renderSidebarSessions();

    if (currentSessionId === id) {
        startNewChat();
    }
}

/* ==========================================================================
   Chat Engine & API Interactions
   ========================================================================== */
function setupChatEngine() {
    const chatForm = document.getElementById("chat-form");
    const chatInput = document.getElementById("chat-input");
    const newChatBtn = document.getElementById("new-chat-btn");
    const clearHistoryBtn = document.getElementById("clear-chats-btn");
    
    // Suggestions card click handler
    document.querySelectorAll(".suggestion-card").forEach(card => {
        card.addEventListener("click", () => {
            submitUserMessage(card.dataset.query);
        });
    });

    // Form submit
    chatForm.addEventListener("submit", (e) => {
        e.preventDefault();
        const text = chatInput.value.trim();
        if (!text) return;

        submitUserMessage(text);
        chatInput.value = "";
    });

    newChatBtn.addEventListener("click", startNewChat);

    clearHistoryBtn.addEventListener("click", () => {
        if (confirm("Are you sure you want to clear all chat histories?")) {
            chatSessions = {};
            saveChatSessionsToStorage();
            startNewChat();
            renderSidebarSessions();
        }
    });

    // Start in fresh welcome state
    startNewChat();
}

async function submitUserMessage(text) {
    // Hide welcome panel
    document.getElementById("welcome-screen").style.display = "none";

    // 1. Initialize session if this is the first message
    if (!currentSessionId) {
        currentSessionId = "chat_" + Date.now();
        chatSessions[currentSessionId] = {
            title: text.length > 25 ? text.substring(0, 25) + "..." : text,
            messages: []
        };
    }

    // 2. Append user message locally
    chatSessions[currentSessionId].messages.push({ sender: "user", text: text });
    appendMessageHTML("user", text);
    scrollToBottom();
    
    // Update sidebar layout
    saveChatSessionsToStorage();
    renderSidebarSessions();

    // 3. Append typing indicator
    const typingWrap = appendMessageHTML("bot", "", true);
    scrollToBottom();

    // 4. Query Python API Backend
    const engineBadge = document.getElementById("engine-badge");
    try {
        const response = await fetch(`${API_BASE}/chat`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: text })
        });
        
        if (!response.ok) throw new Error("Backend response error");
        
        const data = await response.json();
        
        // Remove typing indicator & append bot reply
        typingWrap.remove();
        
        const replyText = data.response;
        chatSessions[currentSessionId].messages.push({ sender: "bot", text: replyText });
        appendMessageHTML("bot", replyText);
        scrollToBottom();
        
        // Update engine badge
        const engineName = data.engine || "Python Server";
        engineBadge.innerText = `Engine: ${engineName}`;
        engineBadge.style.color = "#10b981";
        
        saveChatSessionsToStorage();
    } catch (err) {
        console.error("API communications failed:", err);
        typingWrap.remove();
        
        const errorText = "**Communication Error:** Unable to reach the Python backend server. Please verify Flask is running on port 5000.";
        chatSessions[currentSessionId].messages.push({ sender: "bot", text: errorText });
        appendMessageHTML("bot", errorText);
        scrollToBottom();
        
        engineBadge.innerText = "Engine: Connection Lost";
        engineBadge.style.color = "#ef4444";
    }
}

// Helper to inject message items into log scroll
function appendMessageHTML(sender, text, isTyping = false) {
    const container = document.getElementById("messages-log");
    const msgWrap = document.createElement("div");
    
    msgWrap.className = `message-wrapper ${sender === 'user' ? 'user-msg-wrap' : 'bot-msg-wrap'}`;
    
    let avatarIcon = sender === 'user' ? '<i class="fa-regular fa-user"></i>' : '<i class="fa-solid fa-robot"></i>';
    
    let contentHTML = "";
    if (isTyping) {
        contentHTML = `
            <div class="typing-pulse">
                <span class="pulse-dot"></span>
                <span class="pulse-dot"></span>
                <span class="pulse-dot"></span>
            </div>
        `;
    } else {
        // Use marked.parse to render Markdown strings into structured HTML
        contentHTML = marked.parse(text);
    }

    msgWrap.innerHTML = `
        <div class="message-layout">
            <div class="message-avatar">
                ${avatarIcon}
            </div>
            <div class="message-content">
                ${contentHTML}
            </div>
        </div>
    `;

    container.appendChild(msgWrap);
    return msgWrap;
}

function scrollToBottom() {
    const container = document.getElementById("chat-messages-container");
    container.scrollTo({
        top: container.scrollHeight,
        behavior: 'smooth'
    });
}

function escapeHTML(str) {
    return str.replace(/[&<>'"]/g, 
        tag => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;' }[tag] || tag)
    );
}

// Global utility helper function triggered from clicking chatbot links
window.openDrawerTab = function(tabName) {
    // Open drawer first
    const drawer = document.getElementById("directory-drawer");
    drawer.classList.add("active");
    
    // Activate specific tab
    const tabButton = document.querySelector(`.drawer-tab-btn[data-tab="${tabName}"]`);
    if (tabButton) {
        tabButton.click();
    }
};
