
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

# Bass line: D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25), # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=80, pitch=41, start=2.625, end=3.0),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=3.375, end=3.75), # F2
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125), # G2
    pretty_midi.Note(velocity=80, pitch=41, start=4.125, end=4.5),  # F#2
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=4.875, end=5.25), # F2
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625), # G2
    pretty_midi.Note(velocity=80, pitch=41, start=5.625, end=6.0),  # F#2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # C#4

    # Bar 3: G7 (G, B, D, F#)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # F#4

    # Bar 4: Cmaj7 (C, E, G, B)
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # C4
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # E4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # B4

    # Resolving chords
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # D4
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # E4
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # B4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F#4 - B4 - D5 (skip C# and A)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=1.6875, end=1.875), # F#4
    pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.0625), # B4
    pretty_midi.Note(velocity=110, pitch=74, start=2.0625, end=2.25),  # D5 (leave hanging)

    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=2.8125),  # D4 (come back)
    pretty_midi.Note(velocity=110, pitch=67, start=2.8125, end=3.0),   # F#4
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.1875),   # B4
    pretty_midi.Note(velocity=110, pitch=74, start=3.1875, end=3.375), # D5
]
sax.notes.extend(sax_notes)

# Drums continue for bars 2-4
# Bar 2
bar2_drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.1875),
]
drums.notes.extend(bar2_drum_notes)

# Bar 3
bar3_drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=2.8125),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0),
]
drums.notes.extend(bar3_drum_notes)

# Bar 4
bar4_drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5625),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
]
drums.notes.extend(bar4_drum_notes)

# Add fill at the end of bar 4
bar4_fill = [
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.9375),  # Snare
    pretty_midi.Note(velocity=100, pitch=36, start=3.9375, end=4.125),  # Kick
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
]
drums.notes.extend(bar4_fill)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
