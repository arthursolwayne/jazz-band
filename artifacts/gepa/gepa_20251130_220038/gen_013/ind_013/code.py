
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
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking, chromatic approaches
bass_notes = [
    (37, 1.5), (38, 1.875), (36, 2.25), (39, 2.625),
    (40, 3.0), (39, 3.375), (38, 3.75), (37, 4.125),
    (39, 4.5), (40, 4.875), (41, 5.25), (43, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, E♭)
    (71, 1.5), (74, 1.5), (76, 1.5), (70, 1.5),
    # Bar 3: B♭7 (B♭, D, F, A♭)
    (70, 3.0), (73, 3.0), (76, 3.0), (69, 3.0),
    # Bar 4: E7 (E, G#, B, D)
    (76, 4.5), (79, 4.5), (81, 4.5), (74, 4.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: The motif (F, G, D, E♭)
sax_notes = [
    (71, 1.5), (72, 1.75), (74, 2.0), (70, 2.25),
    (71, 3.0), (72, 3.25), (74, 3.5), (70, 3.75),
    (71, 4.5), (72, 4.75), (74, 5.0), (70, 5.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_introduction.mid")
