
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=40, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),   # G# (chromatic approach)
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.75),  # A#
    pretty_midi.Note(velocity=100, pitch=46, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=100, pitch=47, start=4.125, end=4.5),   # B# (chromatic approach)
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=49, start=4.875, end=5.25),  # C#
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=51, start=5.625, end=6.0),   # D# (chromatic approach)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=78, start=1.5, end=1.875),  # E
    # Bar 3: B7 (B, D#, F#, A)
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.375),  # D#
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.375),  # F#
    pretty_midi.Note(velocity=100, pitch=83, start=3.0, end=3.375),  # A
    # Bar 4: E7 (E, G#, B, D)
    pretty_midi.Note(velocity=100, pitch=78, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=4.875),  # G#
    pretty_midi.Note(velocity=100, pitch=83, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=85, start=4.5, end=4.875),  # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (71), Bb (73), G (76), E (78) — F to Bb to G to E
# Play it on beats 1 and 3 of bar 2, with a short rest in between

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=78, start=3.75, end=4.125),  # E
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
