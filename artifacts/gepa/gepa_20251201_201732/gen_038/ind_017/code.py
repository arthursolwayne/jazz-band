
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4 (1.5 - 6.0s)

# Bass: Marcus
# Walking line in Dm, roots and fifths with chromatic approaches
# Bar 2: D2 (D), F (fifth), E (chromatic approach), D2
# Bar 3: C (bass), G (fifth), Bb (chromatic), C
# Bar 4: A (bass), E (fifth), D (chromatic), A

bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # D2
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=40, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=36, start=4.125, end=4.5),  # C
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=40, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=47, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=45, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=40, start=5.625, end=6.0),  # A
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane
# Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, D, G), resolve on D
# Bar 3: Dm7 -> G7 (B, D, G, C), resolve on G
# Bar 4: Dm7 -> C7 (E, G, C, B), resolve on C

piano_notes = [
    # Bar 2: Dm7
    pretty_midi.Note(velocity=100, pitch=63, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # G
    # Bar 3: G7
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # C
    # Bar 4: C7
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # B
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D - G - F - D, spaced out with rests in between

sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.0625),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.4375),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=2.8125),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.6875),  # D
    pretty_midi.Note(velocity=110, pitch=71, start=4.875, end=5.0625),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.4375),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=5.8125),  # D
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
