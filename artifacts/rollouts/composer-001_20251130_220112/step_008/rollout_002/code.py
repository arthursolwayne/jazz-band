
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]
for start, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 46), (1.75, 47), (2.0, 48), (2.25, 49),
    # Bar 3 (3.0 - 4.5s)
    (3.0, 50), (3.25, 51), (3.5, 52), (3.75, 53),
    # Bar 4 (4.5 - 6.0s)
    (4.5, 54), (4.75, 55), (5.0, 56), (5.25, 57)
]
for start, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.25)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 (1.75 - 2.0s)
    (1.75, 53), (1.75, 61), (1.75, 67), (1.75, 71),  # F, Ab, C, Eb
    # Bar 3: Bb7 (3.25 - 3.5s)
    (3.25, 58), (3.25, 65), (3.25, 71), (3.25, 76),  # Bb, D, F, Ab
    # Bar 4: Eb7 (4.75 - 5.0s)
    (4.75, 55), (4.75, 63), (4.75, 69), (4.75, 74),  # Eb, G, Bb, D
]
for start, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.25)
    piano.notes.append(piano_note)

# Sax: Motif - start with a short phrase, leave it hanging, come back and finish it
# Fm scale: F, Gb, Ab, A, Bb, B, C, Db
sax_notes = [
    # Bar 2: Start of motif (1.5 - 2.0s)
    (1.5, 53), (1.75, 60), (2.0, 58),
    # Bar 3: Continue (3.0 - 3.5s)
    (3.0, 53), (3.25, 60), (3.5, 58),
    # Bar 4: Complete it (4.5 - 5.0s)
    (4.5, 53), (4.75, 60), (5.0, 58)
]
for start, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.25)
    sax.notes.append(sax_note)

# Drums: Fill the bar (1.5 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = 1.5 + (bar - 2) * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=bar_start, end=bar_start + 0.375)
    hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.375, end=bar_start + 0.75)
    hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125)
    hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5)
    # Add to drums
    drums.notes.extend([kick1, kick3, snare2, snare4, hihat1, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
