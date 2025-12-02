
import pretty_midi

midi = pretty_midi.PrettyMIDI()

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in [0, 1, 2, 3]:
    time = beat * 0.375
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
    drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)
# Bar 2 (1.5 - 3.0s)
# Bass: Walking line in C, chromatic approaches
bass_notes = [
    (1.5, 60), (1.75, 61), (2.0, 62), (2.25, 63),
    (2.5, 62), (2.75, 61), (3.0, 60), (3.25, 59)
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.75, 64), (1.75, 67), (1.75, 71), (1.75, 72),
    (2.25, 64), (2.25, 67), (2.25, 71), (2.25, 72),
    # Bar 3 (3.0 - 4.5s)
    (3.25, 64), (3.25, 67), (3.25, 71), (3.25, 72),
    (3.75, 64), (3.75, 67), (3.75, 71), (3.75, 72),
    # Bar 4 (4.5 - 6.0s)
    (4.75, 64), (4.75, 67), (4.75, 71), (4.75, 72),
    (5.25, 64), (5.25, 67), (5.25, 71), (5.25, 72)
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Drums: continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [2, 3, 4]:
    for beat in [0, 1, 2, 3]:
        time = 1.5 + bar * 1.5 + beat * 0.375
        if beat % 2 == 0:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        else:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Sax: short motif, make it sing
# Bar 2 (1.5 - 3.0s)
# C E D C
sax_notes = [
    (1.5, 60), (1.625, 64), (1.75, 62), (1.875, 60),
    (2.0, 60), (2.125, 64), (2.25, 62), (2.375, 60),
    (2.5, 60), (2.625, 64), (2.75, 62), (2.875, 60)
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
