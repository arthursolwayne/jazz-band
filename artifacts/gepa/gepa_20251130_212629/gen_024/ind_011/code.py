
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Key signature: F major (no sharps or flats)
pm.key_signature_changes = [pretty_midi.KeySignature(1, 0.0)]  # 1 = F major

# Define time in seconds per beat
BPM = 160
BEAT = 60.0 / BPM  # 0.375 seconds per beat
BAR = 4 * BEAT  # 1.5 seconds per bar

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano')
drums_program = pretty_midi.instrument_name_to_program('Drums')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

# -------------------------------
# Bar 1: Drums only — build tension
# -------------------------------
# Kick on 1 and 3
drum_notes = {
    'Kick': 36,
    'Snare': 38,
    'Hi-Hat': 42,
    'Ride': 48
}

# Bar 1 (0.0 - 1.5 seconds)
# Kick on beat 1 (0.0)
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.0 + 0.125))
# Hi-hat on every eighth (0.0, 0.375, 0.75, 1.125)
for t in [0.0, 0.375, 0.75, 1.125]:
    drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=t, end=t + 0.125))

# -------------------------------
# Bar 2: All instruments in
# -------------------------------
# Key: F major
# Tonic: C (F major scale: F, G, A, Bb, C, D, E)
# Tenor sax motif: start with a short phrase, then leave it hanging

# Tenor sax: F (C4), A (E4), Bb (F#4?), C (G4)
# Use F major scale, but with subtle rhythmic tension
# Play: F (0.0) -> A (0.375) -> Bb (0.75) -> C (1.125)
# Then rest for the end of the bar (1.5s)

sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=0.0, end=0.0 + 0.15))  # F (C4)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=0.375, end=0.375 + 0.15))  # A (E4)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=0.75, end=0.75 + 0.15))  # Bb (F#4)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.125, end=1.125 + 0.15))  # C (G4)

# Piano: 7th chords, comp on 2 and 4, avoid conflicting with sax
# Bar 2: F7 (F, A, C, Eb) on beat 2 and 4
# Note durations: 0.375s

# F7 on beat 2 (0.375s)
piano.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=0.375, end=0.375 + 0.375))  # F
piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=0.375, end=0.375 + 0.375))  # A
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=0.375, end=0.375 + 0.375))  # C
piano.notes.append(pretty_midi.Note(velocity=80, pitch=63, start=0.375, end=0.375 + 0.375))  # Eb

# F7 on beat 4 (1.5s)
piano.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=1.125, end=1.125 + 0.375))  # F
piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=1.125, end=1.125 + 0.375))  # A
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=1.125, end=1.125 + 0.375))  # C
piano.notes.append(pretty_midi.Note(velocity=80, pitch=63, start=1.125, end=1.125 + 0.375))  # Eb

# Bass: Walking line in F major, chromatic approaches
# F -> G -> A -> Bb -> C -> D -> E -> F
# Bar 2: F (0.0), G (0.375), A (0.75), Bb (1.125)

bass.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=0.0, end=0.0 + 0.25))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=0.375, end=0.375 + 0.25))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=0.75, end=0.75 + 0.25))  # A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=1.125, end=1.125 + 0.25))  # Bb

# Drums (Bar 2)
# Kick on beat 1 (0.0), beat 3 (0.75)
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.0 + 0.125))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=0.75, end=0.75 + 0.125))
# Snare on beat 2 (0.375), beat 4 (1.125)
drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=0.375, end=0.375 + 0.125))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=1.125, end=1.125 + 0.125))
# Hi-hat on every eighth again
for t in [0.0, 0.375, 0.75, 1.125]:
    drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=t, end=t + 0.125))

# -------------------------------
# Bar 3: No notes (rest)
# -------------------------------
# Let the silence breathe

# -------------------------------
# Bar 4: No notes (rest)
# -------------------------------
# But leave a question — sax ends on C (G4), unresolved

# Add instruments to the PrettyMIDI object
pm.instruments = [bass, piano, drums, sax]

# Write to a MIDI file
pm.write('jazz_intro.mid')
