
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
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in F (F, G, Ab, A, Bb, B, C, Db)
bass_notes = [
    (78, 1.5), (79, 1.875), (80, 2.25), (81, 2.625),
    (82, 2.875), (83, 3.25), (84, 3.625), (85, 4.0),
    (78, 4.375), (79, 4.75), (80, 5.125), (81, 5.5)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords on 2 and 4 (F7, Bb7, F7, Bb7)
piano_notes = [
    # Bar 2: F7 (F, A, C, Eb)
    (78, 1.5), (82, 1.5), (84, 1.5), (87, 1.5),
    # Bar 2: Bb7 (Bb, D, F, Ab)
    (82, 2.25), (86, 2.25), (84, 2.25), (88, 2.25),
    # Bar 3: F7
    (78, 3.0), (82, 3.0), (84, 3.0), (87, 3.0),
    # Bar 3: Bb7
    (82, 3.75), (86, 3.75), (84, 3.75), (88, 3.75),
    # Bar 4: F7
    (78, 4.5), (82, 4.5), (84, 4.5), (87, 4.5),
    # Bar 4: Bb7
    (82, 5.25), (86, 5.25), (84, 5.25), (88, 5.25)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante: Tenor sax motif (F, Ab, Bb, C) - start on bar 2, leave it hanging, return on bar 4
sax_notes = [
    # Bar 2: F, Ab, Bb
    (78, 1.5), (81, 1.875), (82, 2.25),
    # Bar 3: (nothing)
    # Bar 4: C, Bb, Ab, F
    (84, 4.5), (82, 4.75), (81, 5.0), (78, 5.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("wayne_intro.mid")
