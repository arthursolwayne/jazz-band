
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

# Bass line - walking line with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root), chromatic approach to G2
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=2.125),
    pretty_midi.Note(velocity=90, pitch=43, start=2.125, end=2.5),
    # Bar 3: G2 (fifth), chromatic approach to A2
    pretty_midi.Note(velocity=90, pitch=43, start=2.5, end=2.875),
    pretty_midi.Note(velocity=90, pitch=44, start=2.875, end=3.125),
    pretty_midi.Note(velocity=90, pitch=45, start=3.125, end=3.5),
    # Bar 4: A2 (tonic), chromatic approach to D3
    pretty_midi.Note(velocity=90, pitch=45, start=3.5, end=3.875),
    pretty_midi.Note(velocity=90, pitch=46, start=3.875, end=4.125),
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano - open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: D7 (open voicing)
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),
    # Bar 3: G7 (open voicing)
    pretty_midi.Note(velocity=100, pitch=53, start=2.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=58, start=2.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=3.0),
    # Bar 4: A7 (open voicing)
    pretty_midi.Note(velocity=100, pitch=52, start=3.5, end=4.0),
    pretty_midi.Note(velocity=100, pitch=57, start=3.5, end=4.0),
    pretty_midi.Note(velocity=100, pitch=59, start=3.5, end=4.0),
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=4.0),
]
piano.notes.extend(piano_notes)

# Sax - one short motif, make it sing
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=2.0),
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=66, start=2.5, end=2.75),
    # Bar 4: Finish it
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75),
    pretty_midi.Note(velocity=110, pitch=66, start=3.75, end=4.0),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
