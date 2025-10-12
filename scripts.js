// Audio Player Management
document.addEventListener('DOMContentLoaded', function() {
    initializeAudioPlayers();
    initializeCharts();
});

// Initialize Audio Players with simple HTML5 audio
function initializeAudioPlayers() {
    const audioIds = ['gepa-best', 'rlvr-best', 'gepa-worst', 'rlvr-worst'];
    const audioElements = {};

    audioIds.forEach(id => {
        const waveformDiv = document.getElementById(`waveform-${id}`);
        const audioElement = document.getElementById(`audio-${id}`);
        const playBtn = document.querySelector(`.play-btn[data-audio="${id}"]`);
        const timeDisplay = playBtn.parentElement.querySelector('.time');

        audioElements[id] = audioElement;

        // Create simple waveform visualization
        createSimpleWaveform(waveformDiv, id);

        // Play/Pause button
        playBtn.addEventListener('click', () => {
            if (audioElement.paused) {
                // Pause all other players
                Object.keys(audioElements).forEach(otherId => {
                    if (otherId !== id && !audioElements[otherId].paused) {
                        audioElements[otherId].pause();
                        const otherBtn = document.querySelector(`.play-btn[data-audio="${otherId}"]`);
                        otherBtn.textContent = '▶ Play';
                        otherBtn.classList.remove('playing');
                    }
                });

                audioElement.play().catch(err => {
                    console.error('Playback failed:', err);
                    alert('Could not play audio. Please check if the audio file exists.');
                });
                playBtn.textContent = '⏸ Pause';
                playBtn.classList.add('playing');
            } else {
                audioElement.pause();
                playBtn.textContent = '▶ Play';
                playBtn.classList.remove('playing');
            }
        });

        // Update time display
        audioElement.addEventListener('timeupdate', () => {
            const currentTime = formatTime(audioElement.currentTime);
            const duration = formatTime(audioElement.duration || 0);
            timeDisplay.textContent = `${currentTime} / ${duration}`;

            // Update waveform progress
            if (audioElement.duration) {
                const progress = (audioElement.currentTime / audioElement.duration) * 100;
                const progressBar = waveformDiv.querySelector('.waveform-progress');
                if (progressBar) {
                    progressBar.style.width = `${progress}%`;
                }
            }
        });

        // Reset button when finished
        audioElement.addEventListener('ended', () => {
            playBtn.textContent = '▶ Play';
            playBtn.classList.remove('playing');
            audioElement.currentTime = 0;
            const progressBar = waveformDiv.querySelector('.waveform-progress');
            if (progressBar) {
                progressBar.style.width = '0%';
            }
        });

        // Update time on metadata loaded
        audioElement.addEventListener('loadedmetadata', () => {
            const duration = formatTime(audioElement.duration);
            timeDisplay.textContent = `0:00 / ${duration}`;
        });
    });
}

// Create simple waveform visualization
function createSimpleWaveform(container, id) {
    container.innerHTML = '';
    container.style.position = 'relative';
    container.style.overflow = 'hidden';

    // Create bars
    const numBars = 100;
    const color = id.includes('rlvr') ? '#3b82f6' : '#10b981';

    for (let i = 0; i < numBars; i++) {
        const bar = document.createElement('div');
        bar.style.position = 'absolute';
        bar.style.bottom = '0';
        bar.style.left = `${(i / numBars) * 100}%`;
        bar.style.width = `${100 / numBars}%`;
        bar.style.backgroundColor = '#475569';
        bar.style.transition = 'background-color 0.3s';

        // Random height for visual variety
        const height = 20 + Math.random() * 60;
        bar.style.height = `${height}%`;
        bar.style.borderRadius = '2px';

        container.appendChild(bar);
    }

    // Create progress overlay
    const progress = document.createElement('div');
    progress.className = 'waveform-progress';
    progress.style.position = 'absolute';
    progress.style.top = '0';
    progress.style.left = '0';
    progress.style.width = '0%';
    progress.style.height = '100%';
    progress.style.backgroundColor = color;
    progress.style.opacity = '0.7';
    progress.style.transition = 'width 0.1s linear';
    progress.style.pointerEvents = 'none';

    container.appendChild(progress);
}

function formatTime(seconds) {
    const minutes = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${minutes}:${secs.toString().padStart(2, '0')}`;
}

// Initialize Charts
function initializeCharts() {
    initializeJudgeScoresChart();
    initializeDivergenceChart();
}

function initializeJudgeScoresChart() {
    const ctx = document.getElementById('judgeScoresChart').getContext('2d');

    // GEPA data (30 generations)
    const gepaSteps = Array.from({length: 30}, (_, i) => i);
    const gepaScores = [
        3.8, 3.6, 3.8, 3.6, 3.8, 3.8, 3.6, 3.6, 3.8, 3.6,
        3.8, 3.8, 4.0, 3.6, 4.0, 3.8, 4.0, 3.8, 3.6, 4.0,
        3.6, 3.8, 3.8, 3.8, 3.8, 3.8, 3.8, 3.8, 4.0, 3.8
    ];

    // RLVR data (30 steps)
    const rlvrSteps = Array.from({length: 30}, (_, i) => i);
    const rlvrScores = [
        4.60, 4.37, 4.43, 4.60, 4.47, 4.47, 4.50, 4.57, 4.40, 4.47,
        4.47, 4.43, 4.43, 4.40, 4.43, 4.60, 4.43, 4.47, 4.53, 4.53,
        4.57, 4.37, 4.60, 4.47, 4.47, 4.47, 4.50, 4.50, 4.47, 4.57
    ];

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: gepaSteps,
            datasets: [
                {
                    label: 'GEPA (Evolutionary)',
                    data: gepaScores,
                    borderColor: '#10b981',
                    backgroundColor: 'rgba(16, 185, 129, 0.1)',
                    borderWidth: 3,
                    tension: 0.3,
                    pointRadius: 4,
                    pointHoverRadius: 6,
                },
                {
                    label: 'RLVR (PPO)',
                    data: rlvrScores,
                    borderColor: '#3b82f6',
                    backgroundColor: 'rgba(59, 130, 246, 0.1)',
                    borderWidth: 3,
                    tension: 0.3,
                    pointRadius: 4,
                    pointHoverRadius: 6,
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    labels: {
                        color: '#cbd5e1',
                        font: {
                            size: 14,
                            weight: 'bold'
                        }
                    }
                },
                tooltip: {
                    backgroundColor: '#1e293b',
                    titleColor: '#f1f5f9',
                    bodyColor: '#cbd5e1',
                    borderColor: '#475569',
                    borderWidth: 1,
                    padding: 12,
                    displayColors: true,
                    callbacks: {
                        label: function(context) {
                            return `${context.dataset.label}: ${context.parsed.y.toFixed(2)}/10`;
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: false,
                    min: 3.0,
                    max: 5.0,
                    title: {
                        display: true,
                        text: 'Judge Score (out of 10)',
                        color: '#cbd5e1',
                        font: {
                            size: 14,
                            weight: 'bold'
                        }
                    },
                    ticks: {
                        color: '#cbd5e1'
                    },
                    grid: {
                        color: '#334155'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Training Step / Generation',
                        color: '#cbd5e1',
                        font: {
                            size: 14,
                            weight: 'bold'
                        }
                    },
                    ticks: {
                        color: '#cbd5e1'
                    },
                    grid: {
                        color: '#334155'
                    }
                }
            }
        }
    });
}

function initializeDivergenceChart() {
    const ctx = document.getElementById('divergenceChart').getContext('2d');

    // Sample data points: [reward, judge_score]
    // RLVR step 20 rollouts
    const rlvrData = [
        {x: 0.649, y: 4.4},
        {x: 0.654, y: 4.8},  // Best judge, low reward - THE DIVERGENCE POINT
        {x: 0.664, y: 4.5},
        {x: 0.666, y: 4.6},
        {x: 0.708, y: 4.6},  // Average reward
        {x: 0.965, y: 4.5},  // Highest reward
        // Other steps (sample)
        {x: 1.014, y: 4.6},
        {x: 1.005, y: 4.6},
        {x: 0.685, y: 4.3},
        {x: 0.638, y: 4.2},
        {x: 0.757, y: 4.4},
        {x: 0.747, y: 4.6},
    ];

    new Chart(ctx, {
        type: 'scatter',
        data: {
            datasets: [
                {
                    label: 'RLVR Rollouts',
                    data: rlvrData.filter((_, i) => i !== 1), // All except divergence point
                    backgroundColor: 'rgba(59, 130, 246, 0.6)',
                    borderColor: '#3b82f6',
                    borderWidth: 2,
                    pointRadius: 6,
                    pointHoverRadius: 8,
                },
                {
                    label: 'Best Judge (Divergence)',
                    data: [rlvrData[1]], // The divergence point
                    backgroundColor: 'rgba(239, 68, 68, 0.8)',
                    borderColor: '#ef4444',
                    borderWidth: 3,
                    pointRadius: 10,
                    pointHoverRadius: 12,
                    pointStyle: 'star',
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    labels: {
                        color: '#cbd5e1',
                        font: {
                            size: 14,
                            weight: 'bold'
                        }
                    }
                },
                tooltip: {
                    backgroundColor: '#1e293b',
                    titleColor: '#f1f5f9',
                    bodyColor: '#cbd5e1',
                    borderColor: '#475569',
                    borderWidth: 1,
                    padding: 12,
                    callbacks: {
                        label: function(context) {
                            return `Reward: ${context.parsed.x.toFixed(3)}, Judge: ${context.parsed.y.toFixed(1)}/10`;
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: false,
                    min: 4.0,
                    max: 5.0,
                    title: {
                        display: true,
                        text: 'Judge Score (out of 10)',
                        color: '#cbd5e1',
                        font: {
                            size: 14,
                            weight: 'bold'
                        }
                    },
                    ticks: {
                        color: '#cbd5e1'
                    },
                    grid: {
                        color: '#334155'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Reward Score',
                        color: '#cbd5e1',
                        font: {
                            size: 14,
                            weight: 'bold'
                        }
                    },
                    ticks: {
                        color: '#cbd5e1'
                    },
                    grid: {
                        color: '#334155'
                    }
                }
            }
        }
    });
}

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});
