
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create an instrument for each player
tenor_sax = pretty_midi.Instrument(program=64)  # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Note()                    # Placeholder for piano
drums = pretty_midi.Instrument(program=0)     # Drums

# Set up time: 4 bars = 6 seconds at 160 BPM
bar_length = 1.5  # seconds per bar
note_length = 0.375  # quarter note

# Create a time signature of 4/4
midi.time_signature_changes.append(pretty_midi.TimeSignature(numerator=4, denominator=4, time=0))

# Define key: Dm (D Dorian or D minor)
# Scale: D (root), E (major 2), F (minor 3), G (perfect 4), A (perfect 5), Bb (diminished 6), C (minor 7)
# Use D Dorian for a more open, modal feel
# We'll map the Dorian scale as follows:
# D (0), E (2), F (3), G (5), A (7), Bb (8), C (10)

# Create a key to note mapping for D Dorian
key_to_pitch = {
    'D': 62,    # D4
    'E': 64,    # E4
    'F': 65,    # F4
    'G': 67,    # G4
    'A': 69,    # A4
    'Bb': 67,   # Bb4 (same as G4, but enharmonic)
    'C': 71,    # C5
}

# Define the tenor sax motif
tenor_notes = [
    key_to_pitch['D'],  # D4 (start with the root)
    key_to_pitch['F'],  # F4 (minor 3rd)
    key_to_pitch['G'],  # G4 (perfect 4th)
    key_to_pitch['A'],  # A4 (perfect 5th)
    key_to_pitch['Bb'], # Bb4 (diminished 6th)
    key_to_pitch['C'],  # C5 (minor 7th)
]

# Tenor sax: Play the first three notes of the motif
for note in tenor_notes[:3]:
    note_obj = pretty_midi.Note(
        velocity=100,
        pitch=note,
        start=0,
        end=note_length
    )
    tenor_sax.notes.append(note_obj)

# Bass line: Walking bass in Dm
# Dm7 chord: D, F, A, C
# Walking bass: D -> F -> G -> A -> Bb -> C -> D -> E -> F -> G -> A -> Bb -> C -> D
bass_notes = [62, 65, 67, 69, 67, 71, 62, 64, 65, 67, 69, 67, 71, 62]
for i, note in enumerate(bass_notes):
    start_time = i * note_length
    end_time = start_time + note_length
    note_obj = pretty_midi.Note(
        velocity=70,
        pitch=note,
        start=start_time,
        end=end_time
    )
    bass.notes.append(note_obj)

# Piano: 7th chords on 2 and 4 (comp)
# Dm7: D, F, A, C
# G7: G, B, D, F
# Dm7 on 2nd and 4th beat
# Time in seconds: bar_length = 1.5s
# bar 1: 0.0 - 1.5
# bar 2: 1.5 - 3.0
# bar 3: 3.0 - 4.5
# bar 4: 4.5 - 6.0

# Bar 2: Dm7 at 1.5s
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.5 + 0.125),
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.5 + 0.125),
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.5 + 0.125),
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.5 + 0.125),
]

# Bar 4: G7 at 4.5s
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.5 + 0.125),
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.5 + 0.125),
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.5 + 0.125),
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.5 + 0.125),
])

# Add piano notes to the piano instrument
for note in piano_notes:
    piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 1: 0.0 - 1.5s
# Beat 1: 0.0
# Beat 2: 0.75
# Beat 3: 1.5
# Beat 4: 2.25
# But we only have bar 1 (drums alone)
# So only beat 1 and 3 in bar 1 (0.0 and 1.5)
# Hihat every eighth: 0.0, 0.375, 0.75, 1.125, 1.5

# Kick on 1 and 3
kick_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.0 + 0.1),
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.5 + 0.1),
]

# Snare on 2 and 4 (but only in bar 1, so only beat 2)
snare_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.75 + 0.1),
]

# Hi-hats on every eighth
hihat_notes = []
for i in range(4):
    time = i * 0.375
    hihat_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.05))

# Add all drum notes
for note in kick_notes + snare_notes + hihat_notes:
    drums.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.append(tenor_sax)
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(drums)

# Save the MIDI file
midi.write("dante_intro.mid")
