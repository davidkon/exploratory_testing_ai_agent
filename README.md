#### AAOS Exploratory Testing AI Agent

# Overview
This project implements an AI-driven exploratory testing agent designed for an Android Automotive OS (AAOS) 14 device connected via ADB to a Windows PC. The target application is a recorder app that manages interior and exterior camera footage, USB storage, theft event recordings, and cloud uploads.

# Key Features
Parses structured app requirements from CSV to guide testing coverage.

Performs requirement-driven exploratory tests simulating user interactions like recording, playback, deletion, and validation.

Controls the AAOS device via ADB for app launch, UI manipulation, log retrieval, and file system inspection.

Logs test execution and coverage status, generating insightful reports.

Modular design supports incremental development and integration of additional testing capabilities.

User-like & Monkey Testing Behavior
While the initial design emphasizes structured, requirement-aligned testing, the AI agent is adaptable to behave more like a real user by incorporating:

Randomized "monkey testing" simulating random taps, swipes, and app switches to uncover edge cases.

Vehicle state simulations such as ignition on/off events to trigger app behaviors naturally.

Dynamic switching between scripted exploratory sequences and random input bursts for broader test coverage.

Potential integration of AI-driven behavioral strategies or reinforcement learning for optimized test exploration.

This allows the agent to emulate natural user interactions and more effectively discover unexpected issues beyond predefined scenarios.

# Project Structure
/src: Python source code files including the main agent, device controller, exploratory engine, and other modules.

/data: Contains requirements CSV files and other data resources.

/tests: Unit and integration test scripts.

/docs: Project documentation.

# Getting Started
Connect the rooted AAOS device to the Windows PC via ADB ethernet.

Install Python and required dependencies (pandas, Appium or UIAutomator clients, etc.).

Configure device connection parameters.

Prepare app_requirements.csv in /data.

Run the agent via python src/main_agent.py to execute exploratory test cycles.

# Future Enhancements
Extend exploratory engine with advanced AI-driven exploration and learning.

Implement vehicle ignition state control APIs.

Enhance monkey testing with adaptive random input strategies.

Integrate cloud upload validation and notification monitoring.