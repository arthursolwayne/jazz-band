
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 1.0),    # Kick on 1
    (38, 0.5, 0.5),    # Snare on 2
    (42, 0.0, 1.0),    # Hihat on every 8th
    (42, 0.375, 0.375),
    (42, 0.75, 0.375),
    (42, 1.125, 0.375),
    (36, 1.5, 1.0),    # Kick on 3
    (38, 1.0, 0.5),    # Snare on 4
    (42, 1.5, 0.5)     # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Walking bass line in F
bass_notes = [
    # Bar 2
    (45, 1.5, 0.5),    # F
    (46, 2.0, 0.5),    # G
    (43, 2.5, 0.5),    # D
    (44, 3.0, 0.5),    # E
    # Bar 3
    (44, 3.5, 0.5),    # E
    (45, 4.0, 0.5),    # F
    (47, 4.5, 0.5),    # A
    (45, 5.0, 0.5),    # F
    # Bar 4
    (43, 5.5, 0.5),    # D
    (44, 6.0, 0.5)     # E
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane - 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (59, 2.0, 0.5),    # C7 (F7 root)
    (62, 2.0, 0.5),    # E
    (64, 2.0, 0.5),    # G
    (67, 2.0, 0.5),    # Bb
    (59, 3.0, 0.5),    # C7
    (62, 3.0, 0.5),    # E
    (64, 3.0, 0.5),    # G
    (67, 3.0, 0.5),    # Bb
    # Bar 3
    (59, 4.0, 0.5),    # C7
    (62, 4.0, 0.5),    # E
    (64, 4.0, 0.5),    # G
    (67, 4.0, 0.5),    # Bb
    (59, 5.0, 0.5),    # C7
    (62, 5.0, 0.5),    # E
    (64, 5.0, 0.5),    # G
    (67, 5.0, 0.5),    # Bb
    # Bar 4
    (59, 6.0, 0.5),    # C7
    (62, 6.0, 0.5),    # E
    (64, 6.0, 0.5),    # G
    (67, 6.0, 0.5)     # Bb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray - Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
drum_notes = [
    # Bar 2
    (36, 1.5, 1.0),    # Kick on 1
    (38, 2.0, 0.5),    # Snare on 2
    (42, 1.5, 1.0),    # Hihat
    (42, 1.875, 0.375),
    (42, 2.25, 0.375),
    (42, 2.625, 0.375),
    (36, 3.0, 1.0),    # Kick on 3
    (38, 3.5, 0.5),    # Snare on 4
    (42, 3.5, 0.5),    # Hihat on 4
    # Bar 3
    (36, 3.5, 1.0),    # Kick on 1
    (38, 4.0, 0.5),    # Snare on 2
    (42, 3.5, 1.0),    # Hihat
    (42, 3.875, 0.375),
    (42, 4.25, 0.375),
    (42, 4.625, 0.375),
    (36, 5.0, 1.0),    # Kick on 3
    (38, 5.5, 0.5),    # Snare on 4
    (42, 5.5, 0.5),    # Hihat on 4
    # Bar 4
    (36, 5.5, 1.0),    # Kick on 1
    (38, 6.0, 0.5),    # Snare on 2
    (42, 5.5, 1.0),    # Hihat
    (42, 5.875, 0.375),
    (42, 6.25, 0.375),
    (42, 6.625, 0.375),
    (36, 7.0, 1.0),    # Kick on 3
    (38, 7.5, 0.5),    # Snare on 4
    (42, 7.5, 0.5)     # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante - Sax solo (motif in F minor, starts on 1.5s)
sax_notes = [
    (62, 1.5, 0.5),    # A (F minor 3rd)
    (64, 2.0, 0.5),    # Bb (F minor 5th)
    (61, 2.5, 0.5),    # G (F minor 7th)
    (66, 3.0, 0.5),    # C (F minor 9th)
    (62, 3.5, 0.5),    # A (F minor 3rd)
    (64, 4.0, 0.5),    # Bb (F minor 5th)
    (61, 4.5, 0.5),    # G (F minor 7th)
    (66, 5.0, 0.5),    # C (F minor 9th)
    (62, 5.5, 0.5),    # A (F minor 3rd)
    (64, 6.0, 0.5)     # Bb (F minor 5th)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.save('wayne_intro.mid')
