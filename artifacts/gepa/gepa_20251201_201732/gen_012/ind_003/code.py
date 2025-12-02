
import numpy as np
import sounddevice as sd
import time

# Constants
SAMPLE_RATE = 44100
DURATION = 6.0  # 4 bars at 160 BPM
BPM = 160
BAR_DURATION = DURATION / 4
BEAT_DURATION = BAR_DURATION / 4
SAMPLES_PER_BAR = int(BAR_DURATION * SAMPLE_RATE)
SAMPLES_PER_BEAT = int(BEAT_DURATION * SAMPLE_RATE)
NOTES_PER_BAR = 4

# Frequencies for Dm chord (D, F, A, C)
D2_FREQ = 73.416  # D2
F2_FREQ = 87.307  # F2
A2_FREQ = 110.000  # A2
C3_FREQ = 130.813  # C3

# Rest and attack times
REST_TIME = 0.05  # seconds
ATTACK_TIME = 0.01  # seconds
DECAY_TIME = 0.03  # seconds

# Synthesize a simple sawtooth wave with ADSR
def sawtooth_wave(freq, duration, sample_rate):
    t = np.linspace(0, duration, int(duration * sample_rate), False)
    wave = 2 * (t * freq * 2 * np.pi) % (2 * np.pi) / np.pi - 1
    return wave

# ADSR envelope
def adsr_envelope(duration, attack, decay, release):
    t = np.linspace(0, duration, int(duration * SAMPLE_RATE), False)
    attack_mask = t < attack
    decay_mask = (t >= attack) & (t < attack + decay)
    release_mask = t >= attack + decay

    env = np.zeros_like(t)
    env[attack_mask] = t[attack_mask] / attack
    env[decay_mask] = 1 - (t[decay_mask] - attack) / decay
    env[release_mask] = 0

    return env

# Generate sound for a single note
def generate_note(freq, duration, attack, decay, release):
    wave = sawtooth_wave(freq, duration, SAMPLE_RATE)
    envelope = adsr_envelope(duration, attack, decay, release)
    return wave * envelope

# Generate a single bar of music
def generate_bar(bar_num, instrument):
    bar = np.zeros(SAMPLES_PER_BAR)
    if instrument == 'drums':
        # Kick on 1 and 3 (beat 1 and 3)
        kick_freq = 60.0  # KICK
        kick = generate_note(kick_freq, BEAT_DURATION, ATTACK_TIME, DECAY_TIME, RELEASE_TIME)
        bar[0:SAMPLES_PER_BEAT] += kick
        bar[2*SAMPLES_PER_BEAT:3*SAMPLES_PER_BEAT] += kick

        # Snare on 2 and 4
        snare_freq = 150.0  # SNARE
        snare = generate_note(snare_freq, BEAT_DURATION, ATTACK_TIME, DECAY_TIME, RELEASE_TIME)
        bar[1*SAMPLES_PER_BEAT:2*SAMPLES_PER_BEAT] += snare
        bar[3*SAMPLES_PER_BEAT:4*SAMPLES_PER_BEAT] += snare

        # Hihat on every eighth note
        hihat_freq = 1000.0  # HIHAT
        for i in range(0, 4):
            hihat = generate_note(hihat_freq, BEAT_DURATION / 2, ATTACK_TIME, DECAY_TIME, RELEASE_TIME)
            bar[i * SAMPLES_PER_BEAT // 2 : (i + 1) * SAMPLES_PER_BEAT // 2] += hihat

    elif instrument == 'bass':
        # Walking bass line in Dm
        # D2, F2, A2, C3 (roots and fifths with chromatic approaches)
        bass_notes = [D2_FREQ, F2_FREQ, A2_FREQ, C3_FREQ]
        for i, note in enumerate(bass_notes):
            note_length = BEAT_DURATION
            start = i * SAMPLES_PER_BEAT
            note_sound = generate_note(note, note_length, ATTACK_TIME, DECAY_TIME, RELEASE_TIME)
            bar[start:start + len(note_sound)] += note_sound

    elif instrument == 'piano':
        # Open voicings with different chords per bar
        chords = [
            [D2_FREQ, F2_FREQ, A2_FREQ],  # Dm
            [F2_FREQ, A2_FREQ, C3_FREQ],  # Fm
            [A2_FREQ, C3_FREQ, E3_FREQ],  # Am
            [C3_FREQ, E3_FREQ, G3_FREQ]   # Cm
        ]
        for i, chord in enumerate(chords):
            # Play on beats 2 and 4
            if i % 2 == 1:
                chord_duration = BEAT_DURATION * 2
                start = i * SAMPLES_PER_BEAT
                chord_sound = np.zeros(SAMPLES_PER_BAR)
                for note in chord:
                    note_sound = generate_note(note, chord_duration, ATTACK_TIME, DECAY_TIME, RELEASE_TIME)
                    chord_sound += note_sound
                bar[start:start + len(chord_sound)] += chord_sound

    elif instrument == 'sax':
        # Tenor sax motif: a short, questioning phrase in Dm
        # Dm -> F -> C -> D
        # Rest on beat 1, then play the motif on beat 2
        if bar_num == 0:
            # Rest on beat 1
            pass
        elif bar_num == 1:
            # Beat 2: Dm (D)
            sax_note = generate_note(D2_FREQ, BEAT_DURATION / 2, ATTACK_TIME, DECAY_TIME, RELEASE_TIME)
            bar[1 * SAMPLES_PER_BEAT // 2 : 1 * SAMPLES_PER_BEAT // 2 + len(sax_note)] += sax_note
        elif bar_num == 2:
            # Beat 2: F (F2)
            sax_note = generate_note(F2_FREQ, BEAT_DURATION / 2, ATTACK_TIME, DECAY_TIME, RELEASE_TIME)
            bar[1 * SAMPLES_PER_BEAT // 2 : 1 * SAMPLES_PER_BEAT // 2 + len(sax_note)] += sax_note
        elif bar_num == 3:
            # Beat 2: C (C3)
            sax_note = generate_note(C3_FREQ, BEAT_DURATION / 2, ATTACK_TIME, DECAY_TIME, RELEASE_TIME)
            bar[1 * SAMPLES_PER_BEAT // 2 : 1 * SAMPLES_PER_BEAT // 2 + len(sax_note)] += sax_note
            # Beat 3: D (D2)
            sax_note = generate_note(D2_FREQ, BEAT_DURATION / 2, ATTACK_TIME, DECAY_TIME, RELEASE_TIME)
            bar[2 * SAMPLES_PER_BEAT // 2 : 2 * SAMPLES_PER_BEAT // 2 + len(sax_note)] += sax_note

    return bar

# Generate the full 4-bar intro
def generate_intro():
    intro = np.zeros(int(DURATION * SAMPLE_RATE))
    for bar_num in range(4):
        if bar_num == 0:
            # Bar 1: Drums only
            intro[bar_num * SAMPLES_PER_BAR : (bar_num + 1) * SAMPLES_PER_BAR] += generate_bar(bar_num, 'drums')
        else:
            # Bars 2-4: All instruments
            intro[bar_num * SAMPLES_PER_BAR : (bar_num + 1) * SAMPLES_PER_BAR] += generate_bar(bar_num, 'drums')
            intro[bar_num * SAMPLES_PER_BAR : (bar_num + 1) * SAMPLES_PER_BAR] += generate_bar(bar_num, 'bass')
            intro[bar_num * SAMPLES_PER_BAR : (bar_num + 1) * SAMPLES_PER_BAR] += generate_bar(bar_num, 'piano')
            intro[bar_num * SAMPLES_PER_BAR : (bar_num + 1) * SAMPLES_PER_BAR] += generate_bar(bar_num, 'sax')
    return intro

# Play the intro
def play_intro():
    intro = generate_intro()
    sd.play(intro, SAMPLE_RATE)
    sd.wait()

# Run the intro
play_intro()
