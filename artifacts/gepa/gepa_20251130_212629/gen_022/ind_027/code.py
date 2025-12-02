
import pretty_midi
import numpy as np

# Create a Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
drums = pretty_midi.Instrument(program=10)
bass = pretty_midi.Instrument(program=33)
piano = pretty_midi.Instrument(program=0)
sax = pretty_midi.Instrument(program=64)

# Set up time (each bar is 1.5 seconds, 4 bars = 6 seconds)
# Each beat is 0.375 seconds (60 / 160 = 0.375)
# 1 bar = 4 beats = 1.5 seconds

# Define note durations and note values
note_length = 0.375  # quarter note at 160 BPM
eighth_note = note_length / 2
sixteenth_note = note_length / 4
trill = [sixteenth_note] * 4

# Define MIDI note numbers (Dm in C minor? Wait — Dm is D, F, A)
# Dm7 = D, F, A, C
# We'll use Dm7 for the chord, but the melody is in D dorian

# Drums (Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
# Bar 1 only
for i in range(4):
    time = i * eighth_note
    hihat = pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + sixteenth_note)
    drums.notes.append(hihat)

kick1 = pretty_midi.Note(velocity=100, pitch=36, start=0, end=note_length)
drums.notes.append(kick1)
snare1 = pretty_midi.Note(velocity=90, pitch=38, start=eighth_note, end=eighth_note + note_length)
drums.notes.append(snare1)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=note_length, end=note_length + note_length)
drums.notes.append(kick2)
snare2 = pretty_midi.Note(velocity=90, pitch=38, start=note_length + eighth_note, end=note_length + eighth_note + note_length)
drums.notes.append(snare2)

# Bass: Walking line in D minor, chromatic approaches
# Dm7 - F - A - C - D
# Walking bass line: C - D - F - E - A - G - Bb - A
# Start at bar 2
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=note_length, end=note_length + note_length),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=note_length + note_length, end=note_length + 2 * note_length),  # D
    pretty_midi.Note(velocity=80, pitch=65, start=note_length + 2 * note_length, end=note_length + 3 * note_length),  # F
    pretty_midi.Note(velocity=80, pitch=64, start=note_length + 3 * note_length, end=note_length + 4 * note_length),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=note_length + 4 * note_length, end=note_length + 5 * note_length),  # A
    pretty_midi.Note(velocity=80, pitch=65, start=note_length + 5 * note_length, end=note_length + 6 * note_length),  # G
    pretty_midi.Note(velocity=80, pitch=62, start=note_length + 6 * note_length, end=note_length + 7 * note_length),  # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=note_length + 7 * note_length, end=note_length + 8 * note_length),  # A
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# Dm7 = D, F, A, C
# Comp on 2 and 4 (bar 2 and bar 4 — 1.5s and 4.5s)
# Each chord is a 7th chord, played with a slight dynamic variation

# Dm7 on beat 2 of bar 2 and beat 2 of bar 4
piano_notes = [
    # Bar 2, beat 2
    pretty_midi.Note(velocity=80, pitch=50, start=note_length * 2, end=note_length * 2 + 0.1),  # D
    pretty_midi.Note(velocity=75, pitch=53, start=note_length * 2, end=note_length * 2 + 0.1),  # F
    pretty_midi.Note(velocity=85, pitch=57, start=note_length * 2, end=note_length * 2 + 0.1),  # A
    pretty_midi.Note(velocity=70, pitch=52, start=note_length * 2, end=note_length * 2 + 0.1),  # C
    # Bar 4, beat 2
    pretty_midi.Note(velocity=80, pitch=50, start=note_length * 5, end=note_length * 5 + 0.1),  # D
    pretty_midi.Note(velocity=75, pitch=53, start=note_length * 5, end=note_length * 5 + 0.1),  # F
    pretty_midi.Note(velocity=85, pitch=57, start=note_length * 5, end=note_length * 5 + 0.1),  # A
    pretty_midi.Note(velocity=70, pitch=52, start=note_length * 5, end=note_length * 5 + 0.1),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif in D dorian — start with a question, leave it hanging
# Motif: D (62) - F (65) - A (67) - Bb (62), then rest
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=note_length * 2, end=note_length * 2 + note_length),  # D
    pretty_midi.Note(velocity=105, pitch=65, start=note_length * 2 + note_length, end=note_length * 2 + 2 * note_length),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=note_length * 2 + 2 * note_length, end=note_length * 2 + 3 * note_length),  # A
    pretty_midi.Note(velocity=95, pitch=62, start=note_length * 2 + 3 * note_length, end=note_length * 2 + 4 * note_length),  # Bb
    # Leave it hanging — don't resolve
]

for note in sax_notes:
    sax.notes.append(note)

# Add instruments to the MIDI file
pm.instruments.append(drums)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(sax)

# Save the MIDI file
pm.write("dante_intro.mid")
