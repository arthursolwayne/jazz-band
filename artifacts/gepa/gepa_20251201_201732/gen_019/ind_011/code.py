
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a PrettyMIDI object with a tempo of 160 BPM
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the key: D minor (key number 29 for D minor)
# But let's use D major for the intro, with a minor feel through notes and phrasing

# Define the time signature: 4/4
pm.time_signature_changes.append(pretty_midi.TimeSignature(numerator=4, denominator=4, time=0))

# Define the instruments
# Drums (channel 9)
drums_instrument = Instrument(program=Program(9), is_drum=True, name='Drums')
pm.instruments.append(drums_instrument)

# Bass (channel 0)
bass_instrument = Instrument(program=Program(33), name='Bass')
pm.instruments.append(bass_instrument)

# Piano (channel 0 - but we'll use a different channel for clarity)
piano_instrument = Instrument(program=Program(0), name='Piano')
pm.instruments.append(piano_instrument)

# Tenor Sax (channel 6, Program 69 is tenor sax)
sax_instrument = Instrument(program=Program(69), name='Tenor Sax')
pm.instruments.append(sax_instrument)

# Define the beat duration in seconds (160 BPM = 60/160 = 0.375 seconds per beat)
beat = 0.375
bar = beat * 4  # 1.5 seconds per bar

def create_note(pitch, start, end, velocity):
    return Note(pitch=pitch, start=start, end=end, velocity=velocity)

# --- BAR 1: Little Ray on drums (snare on 2 and 4, kick on 1 and 3, hihat on every eighth)
# Bar 1 is 0 to 1.5 seconds

# Kick on 1 and 3
drums_instrument.notes.append(create_note(36, 0.0, 0.1, 100))  # Kick on 1
drums_instrument.notes.append(create_note(36, 0.75, 0.85, 100))  # Kick on 3

# Snare on 2 and 4
drums_instrument.notes.append(create_note(38, 0.375, 0.475, 90))  # Snare on 2
drums_instrument.notes.append(create_note(38, 1.125, 1.225, 90))  # Snare on 4

# Hi-hat on every eighth
drums_instrument.notes.append(create_note(42, 0.0, 0.075, 60))  # 1
drums_instrument.notes.append(create_note(42, 0.15, 0.225, 60))  # 2
drums_instrument.notes.append(create_note(42, 0.3, 0.375, 60))  # 3
drums_instrument.notes.append(create_note(42, 0.45, 0.525, 60))  # &
drums_instrument.notes.append(create_note(42, 0.6, 0.675, 60))  # 4
drums_instrument.notes.append(create_note(42, 0.75, 0.825, 60))  # &
drums_instrument.notes.append(create_note(42, 0.9, 0.975, 60))  # 1
drums_instrument.notes.append(create_note(42, 1.05, 1.125, 60))  # 2

# --- BAR 2: Marcus (bass) walks with roots and fifths, chromatic approaches
# D (D2), A (A2), chromatic approaches to Bb (Bb2), G (G2), etc.

# Time: 1.5 to 3.0 seconds

# Bass line (D2 - G2, roots and fifths with chromatic approaches)
# Bar 2: D2 → F#2 (chromatic approach to G2) → G2 → Bb2 (chromatic approach to A2)
bass_instrument.notes.append(create_note(38, 1.5, 1.55, 80))  # D2 (root)
bass_instrument.notes.append(create_note(41, 1.6, 1.65, 80))  # F#2 (chromatic approach to G2)
bass_instrument.notes.append(create_note(43, 1.7, 1.75, 80))  # G2 (fifth)
bass_instrument.notes.append(create_note(42, 1.8, 1.85, 80))  # Bb2 (chromatic approach to A2)

# --- BAR 3: Diane (piano) plays open voicings, resolving on the last bar

# Time: 3.0 to 4.5 seconds
# Bar 3: Dm7 (D, F, A, C) → Gm7 (G, Bb, D, F) → Am7 (A, C, E, G) → Dm7 (D, F, A, C)

# Dm7: D, F, A, C
piano_instrument.notes.append(create_note(62, 3.0, 3.05, 80))  # D4
piano_instrument.notes.append(create_note(65, 3.0, 3.05, 80))  # F4
piano_instrument.notes.append(create_note(67, 3.0, 3.05, 80))  # A4
piano_instrument.notes.append(create_note(69, 3.0, 3.05, 80))  # C5

# Gm7: G, Bb, D, F
piano_instrument.notes.append(create_note(67, 3.5, 3.55, 80))  # G4
piano_instrument.notes.append(create_note(69, 3.5, 3.55, 80))  # Bb4
piano_instrument.notes.append(create_note(71, 3.5, 3.55, 80))  # D5
piano_instrument.notes.append(create_note(74, 3.5, 3.55, 80))  # F5

# Am7: A, C, E, G
piano_instrument.notes.append(create_note(69, 4.0, 4.05, 80))  # A4
piano_instrument.notes.append(create_note(72, 4.0, 4.05, 80))  # C5
piano_instrument.notes.append(create_note(74, 4.0, 4.05, 80))  # E5
piano_instrument.notes.append(create_note(76, 4.0, 4.05, 80))  # G5

# --- BAR 4: You (tenor sax) take the melody — a short motif, sing it, leave it hanging

# Time: 4.5 to 6.0 seconds

# Tenor sax motif: D4 (beat 1) → F4 (beat 2) → G4 (beat 3), leave it hanging on beat 4

# D4 on beat 1 (4.5s)
sax_instrument.notes.append(create_note(62, 4.5, 4.6, 100))

# F4 on beat 2 (4.875s)
sax_instrument.notes.append(create_note(65, 4.875, 5.0, 100))

# G4 on beat 3 (5.25s)
sax_instrument.notes.append(create_note(67, 5.25, 5.35, 100))

# Leave it hanging on beat 4 — don't resolve yet
# No note on beat 4 — the silence is the punch

# Save the MIDI file
pm.write("dante_intro.mid")
