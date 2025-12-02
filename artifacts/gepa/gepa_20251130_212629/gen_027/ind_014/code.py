
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
    (36, 0.0, 0.375),     # Kick on 1
    (42, 0.0, 0.1875),    # Hihat on 1 &
    (42, 0.1875, 0.1875), # Hihat on 2
    (38, 0.375, 0.375),   # Snare on 2
    (42, 0.375, 0.1875),  # Hihat on 2 &
    (42, 0.5625, 0.1875), # Hihat on 3
    (36, 0.75, 0.375),    # Kick on 3
    (42, 0.75, 0.1875),   # Hihat on 3 &
    (42, 0.9375, 0.1875), # Hihat on 4
    (38, 1.125, 0.375),   # Snare on 4
    (42, 1.125, 0.1875),  # Hihat on 4 &
    (42, 1.3125, 0.1875)  # Hihat on &
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line for Marcus: walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    (39, 1.5, 1.625),     # F (root)
    (40, 1.625, 1.75),    # Gb (chromatic)
    (41, 1.75, 1.875),    # G (3rd)
    (42, 1.875, 2.0),     # Ab (flat 5)
    (41, 2.0, 2.125),     # G
    (40, 2.125, 2.25),    # Gb
    (39, 2.25, 2.375),    # F
    (44, 2.375, 2.5),     # Bb (7th)
    (43, 2.5, 2.625),     # A (chromatic)
    (44, 2.625, 2.75),    # Bb
    (45, 2.75, 2.875),    # B (chromatic)
    (44, 2.875, 3.0),     # Bb
    (43, 3.0, 3.125),     # A
    (42, 3.125, 3.25),    # Ab
    (41, 3.25, 3.375),    # G
    (40, 3.375, 3.5),     # Gb
    (39, 3.5, 3.625),     # F
    (38, 3.625, 3.75),    # Eb (root down)
    (37, 3.75, 3.875),    # D (chromatic)
    (38, 3.875, 4.0),     # Eb
    (42, 4.0, 4.125),     # Ab
    (43, 4.125, 4.25),    # A
    (44, 4.25, 4.375),    # Bb
    (43, 4.375, 4.5),     # A
    (42, 4.5, 4.625),     # Ab
    (41, 4.625, 4.75),    # G
    (40, 4.75, 4.875),    # Gb
    (39, 4.875, 5.0)      # F
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Piano: Diane on 2 and 4, 7th chords, comping with intensity
piano_notes = [
    # Bar 2 (1.5 - 2.0s)
    (44, 1.5, 1.75),      # Bb7
    (42, 1.5, 1.75),      # Ab
    (41, 1.5, 1.75),      # G
    (39, 1.5, 1.75),      # F
    # Bar 3 (2.5 - 3.0s)
    (44, 2.5, 2.75),      # Bb7
    (42, 2.5, 2.75),      # Ab
    (41, 2.5, 2.75),      # G
    (39, 2.5, 2.75),      # F
    # Bar 4 (3.5 - 4.0s)
    (44, 3.5, 3.75),      # Bb7
    (42, 3.5, 3.75),      # Ab
    (41, 3.5, 3.75),      # G
    (39, 3.5, 3.75),      # F
    # Bar 4 (4.5 - 5.0s)
    (44, 4.5, 4.75),      # Bb7
    (42, 4.5, 4.75),      # Ab
    (41, 4.5, 4.75),      # G
    (39, 4.5, 4.75)       # F
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=105, pitch=note[0], start=note[1], end=note[2]))

# Sax: Dante on the melody
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (41, 1.5, 1.75),      # G (start of motif)
    (43, 1.75, 1.9375),   # A (next note)
    (44, 1.9375, 2.0),    # Bb (end of first phrase)
    (41, 2.5, 2.75),      # G (reprise)
    (43, 2.75, 2.9375),   # A
    (44, 2.9375, 3.0),    # Bb (end of motif)
    (40, 3.5, 3.6875),    # Gb (new note)
    (42, 3.6875, 3.875),  # Ab
    (43, 3.875, 4.0),     # A
    (41, 4.5, 4.75),      # G (final phrase, ends with a question)
    (43, 4.75, 5.0)       # A (leaves it hanging, not a full resolution)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2]))

# Add instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
midi.write("dante_intro.mid")
