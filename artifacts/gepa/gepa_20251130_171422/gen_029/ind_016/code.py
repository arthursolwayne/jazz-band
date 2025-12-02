
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for i in range(4):
        time = bar * 1.5 + i * 0.375
        if i == 0 or i == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        if i == 1 or i == 3:
            note = pretty_midi.Note(velocity=80, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.0625)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
bass_notes = [48, 49, 50, 51, 52, 51, 50, 49, 48, 47, 46, 47, 48, 49, 50, 51]
for i, pitch in enumerate(bass_notes):
    time = 1.5 + i * 0.375
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = {
    2: [60, 64, 67, 71],
    4: [62, 65, 68, 72]
}
for bar in [2, 4]:
    for pitch in piano_notes[bar]:
        time = (bar - 1) * 1.5 + 0.75
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
        piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    for i in range(4):
        time = (bar - 1) * 1.5 + i * 0.375
        if i == 0 or i == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        if i == 1 or i == 3:
            note = pretty_midi.Note(velocity=80, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.0625)
        drums.notes.append(note)

# Dante: Melody (sparse, expressive, one motif)
sax_notes = [
    (62, 0.0),   # Start on 2nd beat of bar 2
    (64, 0.375), # Chromatic up
    (62, 0.75),  # Back down
    (60, 1.125), # Half note on 3rd beat
    (62, 1.5),   # Start of bar 3
    (67, 1.875), # Skip a few
    (62, 2.25),  # Back to the question
    (60, 2.625), # Half note again
    (62, 3.0),   # Start of bar 4
    (64, 3.375), # One last chromatic
    (62, 3.75),  # Back again
    (60, 4.125), # End with a half note
    (62, 4.5),   # Final pulse
    (60, 4.875), # End
]
for pitch, time in sax_notes:
    note = pretty_midi.Note(velocity=105, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
