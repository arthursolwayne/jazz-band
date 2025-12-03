
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=2.125),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=40, start=2.125, end=2.5),  # G2
    pretty_midi.Note(velocity=90, pitch=43, start=2.5, end=2.875),  # C3 (fifth of F)
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # C3
    pretty_midi.Note(velocity=90, pitch=44, start=3.375, end=3.625),  # C#3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=45, start=3.625, end=4.0),  # D3
    pretty_midi.Note(velocity=90, pitch=38, start=4.0, end=4.375),  # F2
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=39, start=4.875, end=5.125),  # F#2
    pretty_midi.Note(velocity=90, pitch=40, start=5.125, end=5.5),  # G2
    pretty_midi.Note(velocity=90, pitch=43, start=5.5, end=5.875),  # C3
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 (1.5 - 3.0s): Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.0),  # G4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.0),  # E4
    # Bar 3 (3.0 - 4.5s): Bbmaj7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.5),  # Bb4
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.5),  # D4
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.5),  # C4
    pretty_midi.Note(velocity=90, pitch=59, start=3.0, end=3.5),  # Ab4
    # Bar 4 (4.5 - 6.0s): Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.0),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.0),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=5.0),  # G4
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=5.0),  # A4
]
piano.notes.extend(piano_notes)

# Saxophone (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s): Motif start
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75),  # G4
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=2.0),  # B4
    # Bar 3 (3.0 - 4.5s): Leave it hanging
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.25),  # G4 (reprise)
    # Bar 4 (4.5 - 6.0s): Finish the motif
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.75),  # B4
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0),  # A4
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4 (1.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3 for each bar
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875),
    pretty_midi.Note(velocity=100, pitch=36, start=4.625, end=4.875),
    # Snare on 2 and 4 for each bar
    pretty_midi.Note(velocity=110, pitch=38, start=2.0, end=2.125),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=110, pitch=38, start=4.0, end=4.125),
    pretty_midi.Note(velocity=110, pitch=38, start=5.0, end=5.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
