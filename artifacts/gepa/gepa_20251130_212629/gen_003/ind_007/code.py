
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature to 4/4
pm.time_signature_changes[0].numerator = 4
pm.time_signature_changes[0].denominator = 4

# Set key to D minor
pm.key_signature_changes[0].key = pretty_midi.KeySignature.KeyType.minor
pm.key_signature_changes[0].key_number = pretty_midi.key_number_from_key_signature_key('D', 'minor')

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano')
drums_program = pretty_midi.instrument_name_to_program('Drum Kit')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# Tempo: 160 BPM → 0.375 seconds per beat
# 4 bars = 16 beats → 6.0 seconds total
# Bar length: 1.5 seconds

# Define the time at which we start
time = 0.0

# ------------------------------ DRUMS ------------------------------
# Bar 1: Only the drummer, setting the groove
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Define the kick notes and times
kick_notes = [36]  # C2
snare_notes = [38]  # D2
hihat_notes = [42]  # F#2

# Bar 1 (4 beats)
for i in range(4):
    time = i * 0.375
    if i % 2 == 0:
        # Kick on 1 and 3
        note = pretty_midi.Note(velocity=90, pitch=kick_notes[0], start=time, end=time + 0.1)
        drums.notes.append(note)
    else:
        # Snare on 2 and 4
        note = pretty_midi.Note(velocity=90, pitch=snare_notes[0], start=time, end=time + 0.1)
        drums.notes.append(note)
    # Hihat on every eighth
    for j in range(2):
        hihat_time = time + j * 0.1875
        note = pretty_midi.Note(velocity=60, pitch=hihat_notes[0], start=hihat_time, end=hihat_time + 0.05)
        drums.notes.append(note)

# ------------------------------ BASS ------------------------------
# Marcus: Walking line, chromatic approaches, never the same note twice
# Dm7 key: D, F, A, C
# Walking line in D Dorian (D, E, F, G, A, B, C)

# Bar 1: Root, 5th, 7th, 9th in chromatic walk
bass_notes = [50, 53, 55, 57]  # D, F, A, C (Dm7)
bass_times = [0.0, 0.375, 0.75, 1.125]  # Start of each beat
for i, pitch in enumerate(bass_notes):
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=bass_times[i], end=bass_times[i] + 0.125)
    bass.notes.append(note)

# Bar 2: Chromatic approach to D
bass_notes = [53, 52, 50, 50]  # F, E, D, D
bass_times = [1.5, 1.875, 2.25, 2.625]
for i, pitch in enumerate(bass_notes):
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=bass_times[i], end=bass_times[i] + 0.125)
    bass.notes.append(note)

# Bar 3: Chromatic approach to F (from E)
bass_notes = [52, 51, 50, 50]  # E, D#, D, D
bass_times = [3.0, 3.375, 3.75, 4.125]
for i, pitch in enumerate(bass_notes):
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=bass_times[i], end=bass_times[i] + 0.125)
    bass.notes.append(note)

# Bar 4: Chromatic approach to A (from G#)
bass_notes = [51, 50, 49, 50]  # D#, D, C#, D
bass_times = [4.5, 4.875, 5.25, 5.625]
for i, pitch in enumerate(bass_notes):
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=bass_times[i], end=bass_times[i] + 0.125)
    bass.notes.append(note)

# ------------------------------ PIANO ------------------------------
# Diane: 7th chords, comp on 2 and 4
# Dm7: D, F, A, C
# 7th chords: Dm7, G7, Cm7, F7

# Bar 2: Dm7 (comp on beat 2 and 4)
chord_notes = [50, 53, 57, 48]  # D, F, C, G (Dm7)
for beat in [1.875, 2.625]:
    note = pretty_midi.Note(velocity=70, pitch=chord_notes[0], start=beat, end=beat + 0.125)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=70, pitch=chord_notes[1], start=beat, end=beat + 0.125)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=70, pitch=chord_notes[2], start=beat, end=beat + 0.125)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=70, pitch=chord_notes[3], start=beat, end=beat + 0.125)
    piano.notes.append(note)

# Bar 3: G7 (comp on beat 2 and 4)
chord_notes = [62, 65, 67, 60]  # G, B, D, F (G7)
for beat in [3.375, 4.125]:
    note = pretty_midi.Note(velocity=70, pitch=chord_notes[0], start=beat, end=beat + 0.125)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=70, pitch=chord_notes[1], start=beat, end=beat + 0.125)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=70, pitch=chord_notes[2], start=beat, end=beat + 0.125)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=70, pitch=chord_notes[3], start=beat, end=beat + 0.125)
    piano.notes.append(note)

# Bar 4: Cm7 (comp on beat 2 and 4)
chord_notes = [55, 58, 50, 48]  # C, Eb, G, Bb (Cm7)
for beat in [3.375, 4.125]:
    note = pretty_midi.Note(velocity=70, pitch=chord_notes[0], start=beat, end=beat + 0.125)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=70, pitch=chord_notes[1], start=beat, end=beat + 0.125)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=70, pitch=chord_notes[2], start=beat, end=beat + 0.125)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=70, pitch=chord_notes[3], start=beat, end=beat + 0.125)
    piano.notes.append(note)

# ------------------------------ SAX ------------------------------
# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2: Motif starts
note = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75)
sax.notes.append(note)  # E (from D Dorian)

note = pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=1.9)
sax.notes.append(note)  # F

note = pretty_midi.Note(velocity=100, pitch=65, start=1.9, end=2.0)
sax.notes.append(note)  # F#

# Bar 3: Return to motif, but with a resolution to A
note = pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25)
sax.notes.append(note)  # E

note = pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.4)
sax.notes.append(note)  # F

note = pretty_midi.Note(velocity=100, pitch=69, start=3.4, end=3.6)
sax.notes.append(note)  # A

# Bar 4: Final resolution to D
note = pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.75)
sax.notes.append(note)  # D

note = pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0)
sax.notes.append(note)  # E

# Save the MIDI
pm.write('dante_intro.mid')
print("MIDI file written as 'dante_intro.mid'")
