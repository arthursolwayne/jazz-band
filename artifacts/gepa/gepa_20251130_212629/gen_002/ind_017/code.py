
import pretty_midi
import numpy as np

# Setup
midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = []
midi.key_signature_changes = []
midi.instruments = []

# Set tempo (160 BPM)
midi.tempo_changes = [pretty_midi.TempoChange(tempo=160, time=0)]

# Create instruments
bass = pretty_midi.Instrument(program=33)  # Acoustic Bass
piano = pretty_midi.Instrument(program=0)  # Acoustic Piano
drums = pretty_midi.Instrument(program=128)  # Drums
sax = pretty_midi.Instrument(program=64)  # Tenor Saxophone

# Function to convert time in seconds to MIDI ticks
def sec_to_ticks(seconds):
    return int(seconds * midi.time_signature_changes[0].tempo / 60 * pretty_midi.DEFAULT_TICKS_PER_BEAT)

# BPM = 160, 4/4 time, 6 seconds for 4 bars (1.5 seconds per bar)
# Each beat = 0.375 seconds
# Each bar = 6 beats = 1.5 seconds
# Each tick = 0.375 / (60 / 160) / pretty_midi.DEFAULT_TICKS_PER_BEAT
# This is precomputed for 160 BPM

# 1.5 seconds per bar
bar_duration = 1.5
beat_duration = bar_duration / 6  # 0.25 seconds per beat (but our tempo is 160 BPM = 4/4)

# D major key (key number 2)
midi.key_signature_changes = [pretty_midi.KeySignature(key_number=2, time=0)]

# Add instruments to MIDI
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(drums)
midi.instruments.append(sax)

# 1. DRUMS - Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
# Bar 1: 6 beats (1-6)
for beat in [0, 2, 4]:  # Kicks on 1, 3, 5
    kick_time = beat * beat_duration
    kick_tick = sec_to_ticks(kick_time)
    kick_note = pretty_midi.Note(velocity=100, pitch=36, start=kick_tick, end=kick_tick + 0.1)
    drums.notes.append(kick_note)

for beat in [1, 3, 5]:  # Snares on 2, 4, 6
    snare_time = beat * beat_duration
    snare_tick = sec_to_ticks(snare_time)
    snare_note = pretty_midi.Note(velocity=100, pitch=38, start=snare_tick, end=snare_tick + 0.1)
    drums.notes.append(snare_note)

for eight in range(0, 6, 1):  # Hihats every eighth note
    hihat_time = eight * (beat_duration / 2)
    hihat_tick = sec_to_ticks(hihat_time)
    hihat_note = pretty_midi.Note(velocity=80, pitch=42, start=hihat_tick, end=hihat_tick + 0.05)
    drums.notes.append(hihat_note)

# 2. BASS - Bar 1: Walking line, chromatic approach
# Start at D (D4 = 62), walk up chromatically to G (G4 = 67)
# Bar 1: D (62), Eb (63), E (64), F (65)
bass_notes = [62, 63, 64, 65]
for i, pitch in enumerate(bass_notes):
    start_time = i * beat_duration
    end_time = start_time + beat_duration / 4
    start_tick = sec_to_ticks(start_time)
    end_tick = sec_to_ticks(end_time)
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start_tick, end=end_tick)
    bass.notes.append(note)

# 3. PIANO - Bars 2-4: 7th chords on 2 and 4, aggressive left hand, sparse right
# Bar 2: D7 (D, F#, A, C) on beat 2 and 4
# Bar 3: G7 (G, B, D, F) on beat 2 and 4
# Bar 4: C7 (C, E, G, B) on beat 2 and 4
# Left hand: D (62) on beat 1, A (69) on beat 3, G (67) on beat 5, C (60) on beat 6

# Bar 2: D7 (beat 2) and G7 (beat 4)
for bar in [1, 2]:
    bar_start = bar * bar_duration
    chord_notes = [62, 67, 69, 71] if bar == 1 else [71, 76, 78, 80]
    for i, note in enumerate(chord_notes):
        start_time = bar_start + beat_duration * (2 + i)
        start_tick = sec_to_ticks(start_time)
        end_tick = start_tick + sec_to_ticks(0.25)
        piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start_tick, end=end_tick)
        piano.notes.append(piano_note)

# Left hand: D (62), A (69), G (67), C (60)
for i in [0, 2, 4, 5]:  # Beats 1, 3, 5, 6
    beat_start = i * beat_duration
    pitch = [62, 69, 67, 60][i // 2]
    start_tick = sec_to_ticks(beat_start)
    end_tick = start_tick + sec_to_ticks(0.25)
    piano_note = pretty_midi.Note(velocity=90, pitch=pitch, start=start_tick, end=end_tick)
    piano.notes.append(piano_note)

# 4. SAX - Bars 2-4: Motif
# Melody: D4 (62), F#4 (67), G4 (67), A4 (69) — simple, emotional, let it hang
# Play the motif once on bar 2, repeat it on bar 3, resolve on bar 4
# Let the first note hang and then resolve

# Bar 2: Start with D (62)
sax_notes = [62, 67, 67, 69]
for i, pitch in enumerate(sax_notes):
    start_time = bar_duration + i * beat_duration
    end_time = start_time + beat_duration / 2
    start_tick = sec_to_ticks(start_time)
    end_tick = sec_to_ticks(end_time)
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start_tick, end=end_tick)
    sax.notes.append(note)

# Bar 3: Repeat the motif
for i, pitch in enumerate(sax_notes):
    start_time = 2 * bar_duration + i * beat_duration
    end_time = start_time + beat_duration / 2
    start_tick = sec_to_ticks(start_time)
    end_tick = sec_to_ticks(end_time)
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start_tick, end=end_tick)
    sax.notes.append(note)

# Bar 4: Resolve on A (69)
start_time = 3 * bar_duration
end_time = start_time + beat_duration
start_tick = sec_to_ticks(start_time)
end_tick = sec_to_ticks(end_time)
note = pretty_midi.Note(velocity=100, pitch=69, start=start_tick, end=end_tick)
sax.notes.append(note)

# Save the MIDI file
midi.write("dante_intro.mid")
print("MIDI file created: 'dante_intro.mid'")
