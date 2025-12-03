
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),  # Fm root (F)
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25), # D (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=80, pitch=45, start=2.625, end=3.0),  # Fm5 (C)

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=80, pitch=44, start=3.375, end=3.75), # B (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=80, pitch=48, start=4.125, end=4.5),  # F (octave)

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.875),  # F (octave)
    pretty_midi.Note(velocity=80, pitch=47, start=4.875, end=5.25), # E (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=48, start=5.25, end=5.625), # F (octave)
    pretty_midi.Note(velocity=80, pitch=51, start=5.625, end=6.0),  # Fm5 (C)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875),  # Ab

    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=46, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # Ab

    # Bar 4: Eb7 (Eb, G, Bb, Db)
    pretty_midi.Note(velocity=90, pitch=47, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=41, start=4.5, end=4.875),  # Db
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (Ab), G (Bb), C (D), F (Ab) — in 16th notes, staggered
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.6875),  # Ab
    pretty_midi.Note(velocity=100, pitch=46, start=1.6875, end=1.875), # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=2.25, end=2.4375),  # C
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=2.8125), # Ab
    pretty_midi.Note(velocity=100, pitch=46, start=2.8125, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=3.375, end=3.5625), # C
    pretty_midi.Note(velocity=100, pitch=43, start=3.9375, end=4.125), # Ab
    pretty_midi.Note(velocity=100, pitch=46, start=4.125, end=4.3125), # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=4.6875, end=4.875), # C
    pretty_midi.Note(velocity=100, pitch=43, start=5.0625, end=5.25), # Ab
    pretty_midi.Note(velocity=100, pitch=46, start=5.25, end=5.4375), # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=5.625, end=5.8125), # C
]
sax.notes.extend(sax_notes)

# Drums: Bar 2 (1.5 - 3.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar2_drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.8125),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),  # Snare
]
drums.notes.extend(bar2_drum_notes)

# Bar 3 (3.0 - 4.5s)
bar3_drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.3125),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),  # Snare
]
drums.notes.extend(bar3_drum_notes)

# Bar 4 (4.5 - 6.0s)
bar4_drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.8125),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),  # Snare
]
drums.notes.extend(bar4_drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
