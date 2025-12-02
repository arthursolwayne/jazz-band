
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature of 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Create instruments
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')

sax = pretty_midi.Instrument(program=sax_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)

pm.instruments = [sax, bass, piano, drums]

# Time in seconds per bar (160 BPM = 60/160 = 0.375s per beat)
bpm = 160
beats_per_bar = 4
seconds_per_beat = 60.0 / bpm
seconds_per_bar = seconds_per_beat * beats_per_bar

# Time signature: 4/4, no key signature change
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define Dm7 chord (D, F, A, C)
Dm7_notes = [62, 65, 67, 71]  # D, F, A, C

# Define root movement for bass line (chromatic approach)
bass_line = [
    (62, 0.0),      # D (root)
    (63, 0.375),    # Eb (chromatic up)
    (61, 0.75),     # C (chromatic down)
    (62, 1.125),    # back to D
    (62, 1.5),      # D
    (63, 1.875),    # Eb
    (61, 2.25),     # C
    (62, 2.625),    # D
    (62, 3.0),      # D
    (63, 3.375),    # Eb
    (61, 3.75),     # C
    (62, 4.125),    # D
]

# Add bass notes
for note, time in bass_line:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=note, start=time, end=time + 0.375))

# Piano comp on 2 and 4
piano_notes = []
for bar in range(4):
    # Bar 1: only the kick on 1 and 3
    for beat in [0, 2]:
        time = bar * seconds_per_bar + beat * seconds_per_beat
        # Comp on 2 and 4
        if beat == 1 or beat == 3:
            for note in Dm7_notes:
                piano_notes.append((note, time, time + 0.25))
        # Otherwise, rest

# Add piano notes
for note, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=end))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every 8th
drum_notes = []
for bar in range(4):
    for beat in [0, 1, 2, 3]:
        time = bar * seconds_per_bar + beat * seconds_per_beat
        # Kick on 1 and 3
        if beat == 0 or beat == 2:
            drum_notes.append((36, time, time + 0.125))  # Kick
        # Snare on 2 and 4
        if beat == 1 or beat == 3:
            drum_notes.append((38, time, time + 0.125))  # Snare
        # Hi-hat on every 8th
        for eighth in [0, 1]:
            drum_notes.append((42, time + eighth * 0.1875, time + eighth * 0.1875 + 0.125))

# Add drum notes
for note, start, end in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Sax melody: short motif, singable, Dm key
sax_notes = [
    (62, 0.0, 0.75),      # D (start of motif)
    (67, 0.75, 1.5),      # A (suspense)
    (62, 1.5, 2.25),      # D (resolution)
    (64, 2.25, 3.0),      # Bb (extension)
    (62, 3.0, 3.75),      # D (repeat motif)
    (67, 3.75, 4.5),      # A (suspense)
    (62, 4.5, 5.25),      # D (resolution)
    (64, 5.25, 6.0),      # Bb (end)
]

# Add sax notes
for note, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Save the MIDI file
pm.write("dante_intro.mid")
