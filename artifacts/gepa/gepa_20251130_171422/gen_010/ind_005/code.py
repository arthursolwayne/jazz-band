
import pretty_midi
import numpy as np

# Create a PrettyMIDI object at 160 BPM
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
drums = pretty_midi.Instrument(program=10)
bass = pretty_midi.Instrument(program=33)
piano = pretty_midi.Instrument(program=0)
sax = pretty_midi.Instrument(program=64)

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]

# Define note durations
beat = 60.0 / 160  # seconds per beat
bar = 4 * beat  # seconds per bar
note_duration = beat / 2  # eighth note
rest = beat / 4  # sixteenth note

# Bar 1: Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(4):
    time = i * beat
    if i % 2 == 0:
        # Kick on 1 and 3
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + rest))
        # Hihat on every eighth
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + rest))
    else:
        # Snare on 2 and 4
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + rest))
        # Hihat on every eighth
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + rest))

# Bar 2: All instruments in
# Bass: Walking line, chromatic approaches
bass_notes = [21, 22, 20, 19, 18, 17, 19, 21]
for i, note in enumerate(bass_notes):
    time = bar + (i * beat)
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + note_duration))

# Piano: 7th chords, comp on 2 and 4
chord_2 = [59, 64, 66, 67]  # F7
chord_4 = [59, 64, 66, 67]  # F7
for i, chord in enumerate([None, chord_2, None, chord_4]):
    if chord:
        for note in chord:
            time = bar + (i * beat)
            piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + note_duration))

# Sax: Motif - start it, leave it hanging
sax_notes = [62, 64, 65, 62, 60]  # Fm scale melody
for i, note in enumerate(sax_notes):
    time = bar + (i * beat)
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + note_duration))

# Add instruments to the PrettyMIDI object
pm.instruments = [drums, bass, piano, sax]

# Write to MIDI file
pm.write('fm_intro.mid')
