
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 62),      # D4
    (1.875, 63),    # Eb4
    (2.25, 64),     # E4
    (2.625, 65),    # F4
    (3.0, 67),      # G4
    (3.375, 69),    # A4
    (3.75, 71),     # Bb4
    (4.125, 72),    # B4
    (4.5, 74),      # C5
    (4.875, 76),    # D5
    (5.25, 77),     # Eb5
    (5.625, 79),    # F5
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 (D, F#, A, C)
    (1.5, 62), (1.5, 67), (1.5, 74), (1.5, 76),
    # Bar 3: G7 (G, B, D, F)
    (3.0, 67), (3.0, 71), (3.0, 74), (3.0, 76),
    # Bar 4: C7 (C, E, G, B)
    (4.5, 60), (4.5, 64), (4.5, 74), (4.5, 76),
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Little Ray on drums: same pattern as bar 1, but with more intensity
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=110, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        hihat = pretty_midi.Note(velocity=85, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(hihat)

# Dante on sax: short motif, make it sing
# First bar: 4 notes (D, F#, Bb, D)
# Phrase: D (62) -> F# (67) -> Bb (71) -> D (62) - then leave it hanging
sax_notes = [
    (1.5, 62), (1.5, 67), (1.5, 71), (1.5, 62),
    (3.0, 62)  # Come back in bar 3 on the same note
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
