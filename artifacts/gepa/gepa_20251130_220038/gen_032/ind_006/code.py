
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
    # Kick on 1 and 3
    (36, 0.0, 0.375),
    (36, 1.125, 0.375),
    # Snare on 2 and 4
    (38, 0.75, 0.375),
    (38, 1.875, 0.375),
    # Hi-hat on every eighth
    (42, 0.0, 0.1875),
    (42, 0.1875, 0.1875),
    (42, 0.375, 0.1875),
    (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875),
    (42, 0.9375, 0.1875),
    (42, 1.125, 0.1875),
    (42, 1.3125, 0.1875),
    (42, 1.5, 0.1875)
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line in Dm, chromatic approaches
bass_notes = [
    # Bar 2
    (62, 1.5, 1.5),       # D
    (63, 1.5, 1.5),       # Eb
    (60, 1.5, 1.5),       # C
    (62, 1.5, 1.5),       # D
    # Bar 3
    (64, 3.0, 3.0),       # F
    (63, 3.0, 3.0),       # Eb
    (62, 3.0, 3.0),       # D
    (60, 3.0, 3.0),       # C
    # Bar 4
    (62, 4.5, 4.5),       # D
    (63, 4.5, 4.5),       # Eb
    (60, 4.5, 4.5),       # C
    (62, 4.5, 4.5)        # D
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on 1 and 3
    (62, 1.5, 1.5),       # D
    (64, 1.5, 1.5),       # F
    (67, 1.5, 1.5),       # A
    (69, 1.5, 1.5),       # C
    # Bar 3: Dm7 on 2 and 4
    (62, 3.0, 3.0),       # D
    (64, 3.0, 3.0),       # F
    (67, 3.0, 3.0),       # A
    (69, 3.0, 3.0),       # C
    # Bar 4: Dm7 on 1 and 3
    (62, 4.5, 4.5),       # D
    (64, 4.5, 4.5),       # F
    (67, 4.5, 4.5),       # A
    (69, 4.5, 4.5)        # C
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax (Dante): short motif, make it sing
sax_notes = [
    # Bar 2: Start the motif
    (62, 1.5, 1.5),       # D
    (66, 1.5, 1.5),       # G
    (65, 1.5, 1.5),       # F
    # Bar 3: Let it hang
    (62, 3.0, 3.0),       # D
    # Bar 4: Come back and finish it
    (66, 4.5, 4.5),       # G
    (65, 4.5, 4.5),       # F
    (62, 4.5, 4.5)        # D
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
