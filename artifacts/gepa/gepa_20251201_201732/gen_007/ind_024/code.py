
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet
# Bass: Walking line (F2-A2, MIDI 53-57), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.25),  # Ab2
    pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=2.625), # C3
    pretty_midi.Note(velocity=90, pitch=56, start=2.625, end=3.0),  # Bb2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # Eb (octave)
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),  # Ab
]
piano.notes.extend(piano_notes)

# Bar 3: Ab7 (Ab, C, Eb, Gb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=2.625),  # Gb (F#)
]
piano.notes.extend(piano_notes)

# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: Motif - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, B, C, Db
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=58, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=57, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=110, pitch=55, start=2.5, end=2.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=53, start=3.0, end=3.25),  # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('fm_intro.mid')
