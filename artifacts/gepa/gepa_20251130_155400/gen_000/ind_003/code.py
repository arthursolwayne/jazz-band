
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
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.1875), # Hihat on 1&
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2&
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3&
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4&
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (36, 1.5, 1.5),  # F
    (37, 1.5, 1.5),  # Gb
    (35, 1.5, 1.5),  # E
    (37, 1.5, 1.5),  # Gb
    (36, 2.0, 2.0),  # F
    (38, 2.0, 2.0),  # Ab
    (37, 2.0, 2.0),  # Gb
    (35, 2.0, 2.0),  # E
    (34, 2.5, 2.5),  # D
    (36, 2.5, 2.5),  # F
    (35, 2.5, 2.5),  # E
    (33, 2.5, 2.5),  # D
    (34, 3.0, 3.0),  # D
    (36, 3.0, 3.0),  # F
    (38, 3.0, 3.0),  # Ab
    (37, 3.0, 3.0),  # Gb
    (36, 3.5, 3.5),  # F
    (38, 3.5, 3.5),  # Ab
    (37, 3.5, 3.5),  # Gb
    (35, 3.5, 3.5)   # E
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, Eb)
    (64, 1.5, 1.5),  # F
    (69, 1.5, 1.5),  # A
    (67, 1.5, 1.5),  # C
    (66, 1.5, 1.5),  # Eb
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (62, 2.5, 2.5),  # Bb
    (67, 2.5, 2.5),  # D
    (64, 2.5, 2.5),  # F
    (66, 2.5, 2.5),  # Ab
    # Bar 4: Eb7 (Eb, G, Bb, Db)
    (66, 3.5, 3.5),  # Eb
    (71, 3.5, 3.5),  # G
    (62, 3.5, 3.5),  # Bb
    (64, 3.5, 3.5)   # Db
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax: Motif starting on F, bending into Bb
sax_notes = [
    (64, 1.5, 1.5),  # F
    (66, 1.5, 1.5),  # G
    (64, 1.5, 1.5),  # F
    (62, 1.5, 1.5),  # Eb
    (67, 2.0, 2.0),  # G
    (64, 2.0, 2.0),  # F
    (62, 2.0, 2.0),  # Eb
    (60, 2.0, 2.0),  # D
    (67, 2.5, 2.5),  # G
    (65, 2.5, 2.5),  # F#
    (64, 2.5, 2.5),  # F
    (62, 2.5, 2.5),  # Eb
    (67, 3.0, 3.0),  # G
    (64, 3.0, 3.0),  # F
    (62, 3.0, 3.0),  # Eb
    (60, 3.0, 3.0)   # D
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Drums in bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start_time = (bar - 1) * 1.5
    drum_notes = [
        (36, start_time, start_time + 0.375),  # Kick on 1
        (42, start_time, start_time + 0.1875), # Hihat on 1&
        (38, start_time + 0.375, start_time + 0.375),  # Snare on 2
        (42, start_time + 0.375, start_time + 0.1875), # Hihat on 2&
        (36, start_time + 0.75, start_time + 0.375),  # Kick on 3
        (42, start_time + 0.75, start_time + 0.1875), # Hihat on 3&
        (38, start_time + 1.125, start_time + 0.375), # Snare on 4
        (42, start_time + 1.125, start_time + 0.1875) # Hihat on 4&
    ]
    for note in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
